"""Stage 1.5: extract *candidate* nodes/edges from raw sources.

This is the derive side graphify is built around — but bound by QAppsWiki's
defining invariant: **extraction never writes authored pages.** Everything it
produces is a *candidate*, tagged ``INFERRED``, carrying provenance back to the
raw source, written to a **staging area** (``wiki-out/extract/``). A separate
promote step (Phase 2) turns reviewed candidates into authored frontmatter; the
authored layer stays the source of truth.

Two extraction paths, mirroring the offline/online split used by ``freshness``:

* **deterministic core** (default, no dependency, CI-safe) — a curated quantum
  term lexicon plus section headings propose ``concept`` candidates, each with a
  ``concept_kind``/``domains`` guess and the source in its ``sources`` list.
* **optional LLM backend** (injected callable) — richer, typed semantic
  extraction. The backend is passed in (never imported), so tests and CI run the
  deterministic path and the LLM is opt-in, exactly like freshness's network.

Candidates resolve against the *existing* graph: a proposal that already has an
authored page is marked ``exists`` (a link/strengthen opportunity, not a new
page); novel ones are new-page candidates. Across the corpus, candidates merge
by id so one concept accumulates every source that supports it.
"""

from __future__ import annotations

import json
import re

from . import schema

# --------------------------------------------------------------------------- #
# Deterministic quantum term lexicon
# --------------------------------------------------------------------------- #
# (pattern, canonical title, concept_kind, domains). Patterns are matched
# case-insensitively on word boundaries. Kept focused on the time-evolution seed
# corpus plus broad quantum-computing anchors; extend as real sources validate
# each term. This is the deterministic counterpart to an LLM's entity list.
_TERMS: list[tuple[str, str, str, list[str]]] = [
    (r"trotteriz\w+", "Trotterization", "algorithm", ["quantum-simulation"]),
    (r"trotter(?:['’]s)?[ -]?(?:formula|decomposition|step|error)?", "Trotter Decomposition", "algorithm", ["quantum-simulation"]),
    (r"suzuki(?:[ -]trotter)?", "Suzuki-Trotter Decomposition", "algorithm", ["quantum-simulation"]),
    (r"product[ -]formula", "Product Formula", "algorithm", ["quantum-simulation"]),
    (r"q[ -]?drift", "qDRIFT", "algorithm", ["quantum-simulation"]),
    (r"randomized? compil\w+", "Randomized Compilation", "algorithm", ["quantum-simulation", "compilation"]),
    (r"hamiltonian simulation", "Hamiltonian Simulation", "algorithm", ["quantum-simulation"]),
    (r"(?:real[ -]?)?time[ -]evolution", "Time Evolution", "algorithm", ["quantum-simulation"]),
    (r"time[ -]dependent hamiltonian", "Time-Dependent Hamiltonian Simulation", "algorithm", ["quantum-simulation"]),
    (r"interaction picture", "Interaction-Picture Simulation", "algorithm", ["quantum-simulation"]),
    (r"linear combination of unitaries|\blcu\b", "Linear Combination of Unitaries", "algorithm", ["quantum-simulation"]),
    (r"qubitiz\w+", "Qubitization", "algorithm", ["quantum-simulation"]),
    (r"quantum signal processing|\bqsp\b", "Quantum Signal Processing", "algorithm", ["quantum-simulation"]),
    (r"quantum phase estimation|\bqpe\b", "Quantum Phase Estimation", "algorithm", ["quantum-algorithms"]),
    (r"variational quantum eigensolver|\bvqe\b", "Variational Quantum Eigensolver", "algorithm", ["quantum-algorithms"]),
    (r"\bqaoa\b", "QAOA", "algorithm", ["quantum-algorithms"]),
    (r"adiabatic|quantum annealing", "Quantum Annealing", "algorithm", ["quantum-algorithms"]),
    (r"stabilizer (?:code|simulation|formalism)", "Stabilizer Formalism", "capability", ["quantum-error-correction"]),
    (r"(?:quantum )?error correction|\bqec\b", "Quantum Error Correction", "qec", ["quantum-error-correction"]),
    (r"surface code", "Surface Code", "qec", ["quantum-error-correction"]),
    (r"fault[ -]toleran\w+", "Fault Tolerance", "qec", ["quantum-error-correction"]),
    (r"resource estimation", "Resource Estimation", "capability", ["benchmarking-validation"]),
    (r"gate (?:count|complexity)|circuit depth", "Gate Complexity", "capability", ["benchmarking-validation"]),
]

_COMPILED_TERMS = [(re.compile(rf"\b{pat}\b", re.IGNORECASE), title, kind, doms)
                   for pat, title, kind, doms in _TERMS]

# Headings that never name a concept.
_HEADING_STOP = {
    "abstract", "introduction", "conclusion", "conclusions", "discussion",
    "references", "bibliography", "acknowledgments", "acknowledgements",
    "appendix", "methods", "results", "summary", "background", "related work",
    "contents", "notation", "preliminaries", "overview",
}

_H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
_HEADING_RE = re.compile(r"^#{2,4}\s+(.+?)\s*$", re.MULTILINE)
_ARXIV_RE = re.compile(r"arxiv[:/ ]\s*(\d{4}\.\d{4,5})", re.IGNORECASE)
_DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+", re.IGNORECASE)

EXTRACT_SCHEMA_VERSION = "qappswiki-extract-0"


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #

def _slug(title: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s


def _clean_heading(text: str) -> str:
    # Drop leading section markers: "3.", "2.1", roman "I.", or letter "A."
    # (the alpha/roman forms require a trailing period so "A New Method" is safe).
    text = re.sub(r"^(\d+(\.\d+)*\.?|[IVXLCDM]+\.|[A-Z]\.)\s+", "", text).strip()
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    return text.strip()


def source_title(text: str, fallback: str) -> str:
    m = _H1_RE.search(text)
    return _clean_heading(m.group(1)) if m else fallback


# --------------------------------------------------------------------------- #
# deterministic extraction
# --------------------------------------------------------------------------- #

def _candidate_node(title, kind, domains, source_id, evidence, existing_ids) -> dict:
    nid = f"concepts/{_slug(title)}"
    return {
        "id": nid,
        "type": "concept",
        "title": title,
        "concept_kind": kind,
        "domains": sorted(set(domains)),
        "status": "provisional",
        "provenance_status": "needs-verification",
        "sources": [source_id],
        "confidence": "INFERRED",
        "origin": "extracted:heuristic",
        "evidence": evidence,
        "exists": nid in (existing_ids or set()),
    }


def extract_source(source_id: str, text: str, existing_ids: set[str] | None = None,
                   backend=None, max_headings: int = 12) -> dict:
    """Extract candidate nodes/edges from one raw source's markdown ``text``.

    ``source_id`` is the source's repo-relative path (e.g. ``raw/md/x.md``),
    stored in each candidate's ``sources`` so promotion writes real provenance.
    ``existing_ids`` is the set of authored node ids (to flag ``exists``).
    ``backend`` is an optional ``callable(prompt) -> json-string`` LLM hook; when
    given, its candidates are merged on top of the deterministic ones.
    """
    existing_ids = existing_ids or set()
    title = source_title(text, source_id.rsplit("/", 1)[-1])
    nodes: dict[str, dict] = {}

    # 1. Lexicon hits -> concept candidates (counted for evidence strength).
    for rx, cterm, kind, doms in _COMPILED_TERMS:
        hits = rx.findall(text)
        if not hits:
            continue
        node = _candidate_node(cterm, kind, doms, source_id,
                               f"term '{cterm}' matched {len(hits)}×", existing_ids)
        nodes.setdefault(node["id"], node)

    # 2. Section headings -> weaker concept candidates (only multiword, non-stop).
    for h in _HEADING_RE.findall(text)[:max_headings]:
        hc = _clean_heading(h)
        low = hc.lower()
        if low in _HEADING_STOP or len(hc) < 4 or len(hc.split()) > 8 or len(hc.split()) < 2:
            continue
        nid = f"concepts/{_slug(hc)}"
        if nid in nodes:
            continue
        nodes[nid] = _candidate_node(hc, "other", [], source_id,
                                     f"section heading '{hc}'", existing_ids)
        nodes[nid]["confidence"] = "AMBIGUOUS"  # headings are noisier than lexicon

    # 3. External references -> cites edges from this source's strongest candidate.
    refs = sorted(set(_ARXIV_RE.findall(text)))[:20]
    dois = sorted(set(m.group(0) for m in _DOI_RE.finditer(text)))[:20]

    # 4. Edges: relate new candidates to existing graph nodes they co-mention.
    edges: list[dict] = []
    new_concepts = [n for n in nodes.values() if not n["exists"]]
    for n in new_concepts:
        for eid in existing_ids:
            base = eid.rsplit("/", 1)[-1]
            if len(base) >= 4 and re.search(rf"\b{re.escape(base.replace('-', ' '))}\b", text, re.IGNORECASE):
                edges.append({
                    "source": n["id"], "target": eid, "relation": "related",
                    "confidence": "INFERRED", "origin": "extracted:heuristic",
                    "provenance": source_id, "evidence": f"co-mentioned in {source_id}",
                })

    result = {
        "schema_version": EXTRACT_SCHEMA_VERSION,
        "source": source_id,
        "title": title,
        "backend": "heuristic",
        "references": {"arxiv": refs, "doi": dois},
        "candidates": {"nodes": list(nodes.values()), "edges": edges},
    }

    if backend is not None:
        _merge_llm(result, text, existing_ids, backend)

    result["stats"] = _stats(result)
    return result


# --------------------------------------------------------------------------- #
# optional LLM backend
# --------------------------------------------------------------------------- #

def build_prompt(source_id: str, text: str) -> str:
    """Schema-grounded extraction prompt (the quantum domain priors)."""
    return (
        "You extract a knowledge graph from a quantum-computing source. "
        "Return ONLY JSON: {\"nodes\":[{\"title\",\"concept_kind\",\"domains\",\"evidence\"}],"
        "\"edges\":[{\"source_title\",\"target_title\",\"relation\",\"evidence\"}]}.\n"
        f"Allowed concept_kind: {sorted(schema.CONCEPT_KIND)}.\n"
        f"Allowed domains: {sorted(schema.DOMAINS)}.\n"
        f"Allowed relation: {sorted(schema.EDGE_RELATIONS)}.\n"
        "Only assert what the text supports; prefer fewer, well-grounded nodes.\n"
        f"SOURCE {source_id}:\n{text[:12000]}"
    )


def _merge_llm(result: dict, text: str, existing_ids: set[str], backend) -> None:
    """Call the injected backend, validate against the schema, merge candidates."""
    source_id = result["source"]
    try:
        raw = backend(build_prompt(source_id, text))
        data = json.loads(raw) if isinstance(raw, str) else raw
    except (ValueError, TypeError, KeyError):
        result.setdefault("backend_error", "llm output was not valid JSON")
        return
    result["backend"] = "heuristic+llm"
    by_id = {n["id"]: n for n in result["candidates"]["nodes"]}
    title_to_id: dict[str, str] = {n["title"].lower(): n["id"] for n in by_id.values()}

    for n in data.get("nodes", []):
        title = (n.get("title") or "").strip()
        if not title:
            continue
        kind = n.get("concept_kind") if n.get("concept_kind") in schema.CONCEPT_KIND else "other"
        doms = sorted({d for d in (n.get("domains") or []) if d in schema.DOMAINS})
        nid = f"concepts/{_slug(title)}"
        title_to_id[title.lower()] = nid
        if nid in by_id:  # strengthen an existing candidate
            by_id[nid]["origin"] = "extracted:heuristic+llm"
            continue
        node = _candidate_node(title, kind, doms, source_id,
                               (n.get("evidence") or "llm-extracted")[:200], existing_ids)
        node["origin"] = "extracted:llm"
        by_id[nid] = node

    for e in data.get("edges", []):
        rel = e.get("relation") if e.get("relation") in schema.EDGE_RELATIONS else "related"
        s = title_to_id.get((e.get("source_title") or "").lower())
        t = title_to_id.get((e.get("target_title") or "").lower())
        if not s or not t or s == t:
            continue
        result["candidates"]["edges"].append({
            "source": s, "target": t, "relation": rel, "confidence": "INFERRED",
            "origin": "extracted:llm", "provenance": source_id,
            "evidence": (e.get("evidence") or "llm-extracted")[:200],
        })

    result["candidates"]["nodes"] = list(by_id.values())


# --------------------------------------------------------------------------- #
# corpus-level merge + staging
# --------------------------------------------------------------------------- #

def _stats(result: dict) -> dict:
    nodes = result["candidates"]["nodes"]
    return {
        "candidate_nodes": len(nodes),
        "new": sum(1 for n in nodes if not n["exists"]),
        "existing": sum(1 for n in nodes if n["exists"]),
        "candidate_edges": len(result["candidates"]["edges"]),
    }


def merge_corpus(results: list[dict]) -> dict:
    """Dedup candidate nodes across sources by id; accumulate their sources.

    A concept supported by many papers ends up with many ``sources`` — the
    review signal for which candidates are worth promoting first.
    """
    nodes: dict[str, dict] = {}
    related: dict[str, list[str]] = {}
    for r in results:
        for n in r["candidates"]["nodes"]:
            cur = nodes.get(n["id"])
            if cur is None:
                nodes[n["id"]] = {**n, "sources": list(n["sources"])}
            else:
                for s in n["sources"]:
                    if s not in cur["sources"]:
                        cur["sources"].append(s)
                # keep the strongest confidence (INFERRED beats AMBIGUOUS)
                if n["confidence"] == "INFERRED":
                    cur["confidence"] = "INFERRED"
        # accumulate each candidate's related targets (links into the graph)
        for e in r["candidates"]["edges"]:
            bucket = related.setdefault(e["source"], [])
            if e["target"] not in bucket:
                bucket.append(e["target"])
    for nid, n in nodes.items():
        n["related"] = sorted(related.get(nid, []))
    ranked = sorted(nodes.values(), key=lambda n: (-len(n["sources"]), n["id"]))
    return {
        "schema_version": EXTRACT_SCHEMA_VERSION,
        "candidate_nodes": ranked,
        "stats": {
            "candidates": len(ranked),
            "new": sum(1 for n in ranked if not n["exists"]),
            "multi_source": sum(1 for n in ranked if len(n["sources"]) > 1),
        },
    }


def render_extract_report(results: list[dict], merged: dict, generated: str = "") -> str:
    L = ["# QAppsWiki Extraction Report", ""]
    if generated:
        L += [f"_Generated: {generated}_", ""]
    s = merged["stats"]
    L.append(f"**{len(results)} sources → {s['candidates']} distinct candidate concepts** "
             f"({s['new']} new, {s['multi_source']} supported by >1 source).")
    L += ["", "> Candidates are `INFERRED`, staged for review — not authored pages.", ""]
    L.append("## Top candidates (by source support)")
    L += ["| candidate | kind | sources | status |", "|---|---|---|---|"]
    for n in merged["candidate_nodes"][:30]:
        tag = "exists" if n["exists"] else "**new**"
        L.append(f"| {n['title']} | {n['concept_kind']} | {len(n['sources'])} | {tag} |")
    L.append("")
    return "\n".join(L)


def stage(result: dict, out_dir) -> "Path":  # noqa: F821 - Path imported by caller
    from pathlib import Path
    d = Path(out_dir) / "extract"
    d.mkdir(parents=True, exist_ok=True)
    stem = result["source"].rsplit("/", 1)[-1].rsplit(".", 1)[0]
    path = d / f"{stem}.json"
    path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return path


def extract_corpus(root, raw_dir: str = "raw/md", existing_ids=None, backend=None) -> list[dict]:
    """Extract every ``*.md`` under ``raw_dir`` (skips dotfiles/placeholders)."""
    from pathlib import Path
    root = Path(root)
    base = root / raw_dir
    results = []
    if not base.exists():
        return results
    for p in sorted(base.glob("*.md")):
        if p.name.startswith("."):
            continue
        text = p.read_text(encoding="utf-8")
        source_id = p.relative_to(root).as_posix()  # keep .md (the sources: convention)
        results.append(extract_source(source_id, text, existing_ids, backend))
    return results
