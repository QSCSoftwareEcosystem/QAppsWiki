"""Importer: turn external *zoo* catalogs into schema-valid `concept` pages.

Two community catalogs are first-class ingest sources for QAppsWiki's
quantum-error-correction coverage (registered as `source` pages under `raw/`):

- **Error Correction Zoo** (errorcorrectionzoo.org) — error-correcting *codes*,
  stored as one YAML file per code in ``errorcorrectionzoo/eczoo_data``.
  Licensed **CC-BY-SA**; attribute on reuse.
- **QEM Zoo** (qemzoo.com) — quantum error *mitigation/suppression* techniques,
  stored as JSON in ``vprusso/qemzoo`` under ``data/``. **The Unlicense**
  (public domain).

This module is an *authoring* tool, not part of ``qappswiki run``: it reaches
the network (GitHub) to fetch upstream data, then renders schema-valid
`concept` pages with full provenance back to the zoo source page and the
upstream entry URL. Imported pages are written as ``status: provisional`` /
``provenance_status: needs-verification`` — they carry the catalog's own prose
verbatim and a human/agent is expected to verify and enrich them. Rendering is
kept pure (no network) so it is unit-tested offline; only ``fetch_*`` touches
the wire.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from . import schema

# --- upstream coordinates ---------------------------------------------------

SOURCE_PAGE = {
    "eczoo": "raw/error-correction-zoo.md",
    "qemzoo": "raw/qem-zoo.md",
}
ENTRY_URL = {
    "eczoo": lambda cid: f"https://errorcorrectionzoo.org/c/{cid}",
    "qemzoo": lambda cid: f"https://qemzoo.com/technique.html?id={cid}",
}
OUT_DIR = {"eczoo": "concepts/qec", "qemzoo": "concepts/qem"}
ATTRIBUTION = {
    "eczoo": "Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA",
    "qemzoo": "QEM Zoo (qemzoo.com), public domain (The Unlicense)",
}

# A bounded, recognizable starter set of code families spanning the main
# branches of the quantum kingdom (stabilizer / topological / qLDPC /
# small-distance). `--all` imports the whole catalog instead.
ECZ_FLAGSHIP = (
    "stabilizer", "css", "surface", "toric", "triangular_color", "qldpc",
    "hypergraph_product", "bacon_shor", "steane", "shor_nine", "stab_5_1_3",
)


class ImportError_(Exception):
    """Raised for fetch/parse failures or refused overwrites."""


# --- LaTeX-ish prose -> markdown -------------------------------------------

def _render_cite(m: re.Match) -> str:
    """``\\cite{arxiv:ID,doi:X}`` -> ``([arXiv:ID](url), [doi:X](url))``."""
    links = []
    for tok in (t.strip() for t in m.group(1).split(",")):
        low = tok.lower()
        if low.startswith("arxiv:"):
            aid = tok.split(":", 1)[1]
            links.append(f"[arXiv:{aid}](https://arxiv.org/abs/{aid})")
        elif low.startswith("doi:"):
            doi = tok.split(":", 1)[1]
            links.append(f"[doi:{doi}](https://doi.org/{doi})")
        # `manual:{...}` and unknown kinds are dropped (no stable URL).
    return f" ({', '.join(links)})" if links else ""


def tex_to_md(text: str) -> str:
    """Convert the Zoo's LaTeX-flavored prose to wiki-friendly markdown.

    Handles the constructs that actually appear in entries: ``\\href``,
    ``\\cite`` (-> arXiv/doi links), light text styling, and inline/display
    math delimiters (``\\( \\)`` -> ``$ $``). Math *content* is left intact.
    """
    if not text:
        return ""
    # Drop figure environments — they \includegraphics zoo images we don't host.
    text = re.sub(r"\\begin\{figure\}.*?\\end\{figure\}", "", text, flags=re.DOTALL)
    text = re.sub(r"manual:\{[^{}]*\}", "", text)        # drop manual cite bodies
    text = re.sub(r"\\href\{([^}]*)\}\{([^}]*)\}", r"[\2](\1)", text)
    text = re.sub(r"\\hyperref\[[^\]]*\]\{([^}]*)\}", r"\1", text)   # cross-ref -> plain text
    # ``\cite{...}`` and ``\cite[Fig. 3]{...}`` (optional note dropped).
    text = re.sub(r"\\cite(?:\[[^\]]*\])?\{([^}]*)\}", _render_cite, text)
    text = re.sub(r"\\(?:textit|emph)\{([^}]*)\}", r"*\1*", text)
    text = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", text)
    text = text.replace(r"\(", "$").replace(r"\)", "$")
    text = text.replace(r"\[", "$$").replace(r"\]", "$$")
    # The Zoo writes stabilizer-code parameters as ``[[n,k,d]]`` (and ``[[n,k]]``)
    # inside math. That double-bracket collides with wiki ``[[link]]`` syntax and
    # would be parsed as a broken wikilink, so render it as the proper double
    # bracket symbol it actually denotes. (Zoo prose never uses wiki links.)
    text = text.replace("[[", "⟦").replace("]]", "⟧")
    return text.strip()


def _slug(value: str, sep_from: str = "_") -> str:
    return value.strip().replace(sep_from, "-").replace("/", "-")


def _fm_yaml(fm: dict) -> str:
    return yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()


# --- rendering: Error Correction Zoo ---------------------------------------

def _render_block(value) -> str:
    """A YAML field that is a string, a list of strings, or a list of dicts."""
    if isinstance(value, str):
        return tex_to_md(value)
    if isinstance(value, list):
        out = []
        for item in value:
            if isinstance(item, str):
                out.append(f"- {tex_to_md(item)}")
            elif isinstance(item, dict):
                label = item.get("code_id") or item.get("name") or ""
                detail = tex_to_md(item.get("detail", ""))
                out.append(f"- `{label}`" + (f" — {detail}" if detail else ""))
        return "\n".join(out)
    return ""


def eczoo_page(entry: dict, today: str, batch_slugs: frozenset = frozenset()) -> tuple[str, str]:
    """Render one ECZ code entry -> (rel_path, markdown). Pure / offline."""
    cid = entry["code_id"]
    slug = _slug(cid)
    rel_path = f"{OUT_DIR['eczoo']}/{slug}.md"
    name = tex_to_md(entry.get("name") or cid)
    aliases = [tex_to_md(a) for a in (entry.get("alternative_names") or [])]

    related_ids = []
    for kind in ("parents", "cousins"):
        for rel in (entry.get("relations") or {}).get(kind, []) or []:
            rid = rel.get("code_id")
            if rid and _slug(rid) in batch_slugs:
                related_ids.append(f"{OUT_DIR['eczoo']}/{_slug(rid)}")

    fm = {
        "type": "concept",
        "name": name,
        "status": "provisional",
        "updated": today,
        "concept_kind": "qec",
        "aliases": aliases,
        "domains": ["quantum-error-correction"],
        "related_concepts": sorted(set(related_ids)),
        "sources": [SOURCE_PAGE["eczoo"], ENTRY_URL["eczoo"](cid)],
        "provenance_status": "needs-verification",
        "imported_from": "error-correction-zoo",
        "imported_id": cid,
    }

    parts = [f"---\n{_fm_yaml(fm)}\n---\n", f"# {name}\n"]
    parts.append(
        f"> **Imported by `qappswiki import-zoo eczoo`** from the "
        f"[Error Correction Zoo]({ENTRY_URL['eczoo'](cid)}) "
        f"(`code_id: {cid}`). Text is reused under **CC-BY-SA**; attribute the "
        f"{ATTRIBUTION['eczoo']}. This is a `needs-verification` page — confirm "
        f"the claims against the cited primary sources before relying on it.\n"
    )
    desc = tex_to_md(entry.get("description", ""))
    if desc:
        parts.append("## Description\n\n"
                     f"{desc}\n\n(source: {SOURCE_PAGE['eczoo']})\n")
    if entry.get("protection"):
        parts.append(f"## Protection\n\n{_render_block(entry['protection'])}\n")
    for key, value in (entry.get("features") or {}).items():
        title = key.replace("_", " ").capitalize()
        body = _render_block(value)
        if body:
            parts.append(f"## {title}\n\n{body}\n")
    if entry.get("realizations"):
        parts.append(f"## Realizations\n\n{_render_block(entry['realizations'])}\n")
    rel = entry.get("relations") or {}
    rel_lines = []
    for kind in ("parents", "cousins"):
        for r in rel.get(kind, []) or []:
            rid = r.get("code_id")
            if not rid:
                continue
            if _slug(rid) in batch_slugs:
                link = f"[[{OUT_DIR['eczoo']}/{_slug(rid)}]]"
            else:
                link = f"[`{rid}`]({ENTRY_URL['eczoo'](rid)})"
            detail = tex_to_md(r.get("detail", ""))
            rel_lines.append(f"- _{kind[:-1]}_: {link}" + (f" — {detail}" if detail else ""))
    if rel_lines:
        parts.append("## Relations\n\n" + "\n".join(rel_lines) + "\n")
    if entry.get("notes"):
        parts.append(f"## Notes\n\n{_render_block(entry['notes'])}\n")
    return rel_path, "\n".join(parts)


# --- rendering: QEM Zoo -----------------------------------------------------

def _qem_reference(key: str, refs: dict) -> str:
    r = refs.get(key)
    if not r:
        return f"- `{key}` _(reference not found in QEM Zoo references.json)_"
    bits = [r.get("authors", ""), f"*{r.get('title', key)}*"]
    venue = ", ".join(str(x) for x in (r.get("journal"), r.get("year")) if x)
    if venue:
        bits.append(venue)
    line = "- " + ". ".join(b for b in bits if b)
    if r.get("arxiv"):
        line += f" [arXiv:{r['arxiv']}](https://arxiv.org/abs/{r['arxiv']})"
    if r.get("doi"):
        line += f" [doi](https://doi.org/{r['doi']})"
    return line


def qemzoo_page(entry: dict, refs: dict, today: str,
                batch_slugs: frozenset = frozenset()) -> tuple[str, str]:
    """Render one QEM technique -> (rel_path, markdown). Pure / offline."""
    tid = entry["id"]
    slug = _slug(tid)
    rel_path = f"{OUT_DIR['qemzoo']}/{slug}.md"
    name = entry.get("name") or tid
    aliases = list(entry.get("aliases") or [])
    if entry.get("abbreviation"):
        aliases = [entry["abbreviation"], *aliases]

    related_ids = [f"{OUT_DIR['qemzoo']}/{_slug(r['id'])}"
                   for r in (entry.get("related") or [])
                   if r.get("id") and _slug(r["id"]) in batch_slugs]

    fm = {
        "type": "concept",
        "name": name,
        "status": "provisional",
        "updated": today,
        "concept_kind": "qec",
        "aliases": aliases,
        "domains": ["quantum-error-correction"],
        "related_concepts": sorted(set(related_ids)),
        "sources": [SOURCE_PAGE["qemzoo"], ENTRY_URL["qemzoo"](tid)],
        "provenance_status": "needs-verification",
        "imported_from": "qem-zoo",
        "imported_id": tid,
    }

    category = entry.get("category", "")
    parts = [f"---\n{_fm_yaml(fm)}\n---\n", f"# {name}\n"]
    parts.append(
        f"> **Imported by `qappswiki import-zoo qemzoo`** from the "
        f"[QEM Zoo]({ENTRY_URL['qemzoo'](tid)}) (`id: {tid}`"
        + (f", category: {category}" if category else "") + "). Public domain "
        f"(The Unlicense); cited as the {ATTRIBUTION['qemzoo']}. This is a "
        f"`needs-verification` page — confirm against the references below.\n"
    )
    if entry.get("summary"):
        parts.append("## Summary\n\n"
                     f"{tex_to_md(entry['summary'])}\n\n(source: {SOURCE_PAGE['qemzoo']})\n")
    props = entry.get("properties") or {}
    if props:
        rows = "\n".join(f"| {k} | {v} |" for k, v in props.items())
        parts.append("## Properties\n\n| Property | Value |\n|---|---|\n" + rows + "\n")
    related = entry.get("related") or []
    if related:
        lines = []
        for r in related:
            rid = r.get("id", "")
            if _slug(rid) in batch_slugs:
                link = f"[[{OUT_DIR['qemzoo']}/{_slug(rid)}]]"
            else:
                link = f"[`{rid}`]({ENTRY_URL['qemzoo'](rid)})"
            lines.append(f"- {link} — {r.get('reason', '')}".rstrip(" —"))
        parts.append("## Related techniques\n\n" + "\n".join(lines) + "\n")
    cited = entry.get("references") or []
    if cited:
        parts.append("## References\n\n"
                     + "\n".join(_qem_reference(k, refs) for k in cited) + "\n")
    return rel_path, "\n".join(parts)


# --- local data: clone once, then read everything off disk -----------------
#
# The whole point: we *gather once* (a single shallow ``git clone`` of each
# zoo's data repo into a gitignored cache) and then process the entire catalog
# locally — no per-code API calls, no token, no rate limit. After the clone,
# import/render/validate never touch the network. ``--refresh`` re-syncs.

DEFAULT_CACHE = ".zoo-cache"
REPO_URL = {
    "eczoo": "https://github.com/errorcorrectionzoo/eczoo_data",
    "qemzoo": "https://github.com/vprusso/qemzoo",
}
REPO_DIR = {"eczoo": "eczoo_data", "qemzoo": "qemzoo"}


def repo_path(source: str, cache_dir: str = DEFAULT_CACHE) -> Path:
    return Path(cache_dir) / REPO_DIR[source]


def sync(source: str, cache_dir: str = DEFAULT_CACHE, refresh: bool = False) -> Path:
    """Ensure a local clone of the zoo's data repo exists; return its path.

    This is the *only* networked step, and it runs at most once per import
    (shallow clone on first use; ``refresh=True`` pulls the latest). Everything
    downstream reads from the returned local directory.
    """
    import subprocess
    dest = repo_path(source, cache_dir)
    if dest.exists():
        if refresh:
            try:
                subprocess.run(["git", "-C", str(dest), "pull", "--ff-only"],
                               check=True, capture_output=True, text=True)
            except (OSError, subprocess.CalledProcessError) as exc:
                raise ImportError_(f"failed to refresh {dest}: {exc}")
        return dest
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(["git", "clone", "--depth", "1", REPO_URL[source], str(dest)],
                       check=True, capture_output=True, text=True)
    except (OSError, subprocess.CalledProcessError) as exc:
        detail = getattr(exc, "stderr", "") or exc
        raise ImportError_(f"failed to clone {REPO_URL[source]} -> {dest}: {detail}")
    return dest


def _ecz_pathmap(repo_dir: Path) -> dict:
    """Map every ECZ ``code_id`` to its local YAML path (one file per code)."""
    return {p.stem: p for p in (Path(repo_dir) / "codes").rglob("*.yml")}


# The catalog mixes ~630 quantum codes with ~450 purely-classical ones. A
# quantum wiki tags everything ``quantum-error-correction``, so the bulk import
# defaults to the quantum subtrees and treats classical codes as opt-in.
_QUANTUM_SUBTREES = ("quantum", "classical_into_quantum")


def _is_quantum(path: Path, repo_dir: Path) -> bool:
    rel = path.relative_to(Path(repo_dir) / "codes").parts
    return bool(rel) and rel[0] in _QUANTUM_SUBTREES


def fetch_eczoo(code_ids=None, cache_dir: str = DEFAULT_CACHE,
                refresh: bool = False, include_classical: bool = False) -> list[dict]:
    """Read + YAML-parse ECZ code entries from the local clone.

    ``code_ids=None`` reads the whole catalog; by default that is scoped to the
    ~630 quantum codes (set ``include_classical=True`` for all ~1100). Explicit
    ``code_ids`` are always honored regardless of subtree.
    """
    repo_dir = sync("eczoo", cache_dir, refresh)
    pathmap = _ecz_pathmap(repo_dir)
    if code_ids is None:
        ids = sorted(cid for cid, p in pathmap.items()
                     if include_classical or _is_quantum(p, repo_dir))
    else:
        ids = list(code_ids)
    entries = []
    for cid in ids:
        path = pathmap.get(cid)
        if not path:
            raise ImportError_(f"unknown ECZ code_id: {cid}")
        entry = yaml.safe_load(path.read_text(encoding="utf-8"))
        entry.setdefault("code_id", cid)
        entries.append(entry)
    return entries


def fetch_qemzoo(ids=None, cache_dir: str = DEFAULT_CACHE,
                 refresh: bool = False) -> tuple[list[dict], dict]:
    """Read QEM techniques + the references index from the local clone."""
    repo_dir = sync("qemzoo", cache_dir, refresh)
    data = repo_dir / "data"
    techniques = json.loads((data / "techniques.json").read_text(encoding="utf-8"))
    refs = json.loads((data / "references.json").read_text(encoding="utf-8"))
    if ids is not None:
        wanted = set(ids)
        techniques = [t for t in techniques if t["id"] in wanted]
    return techniques, refs


# --- index.md registration (idempotent managed blocks) ---------------------

def update_index(root, source: str, node_titles: list[tuple[str, str]]) -> None:
    """Insert/replace a managed ``index.md`` section linking imported pages.

    Keeps imported catalog pages out of the orphan warning set without hand
    edits. The block is delimited by HTML-comment markers so re-imports just
    rewrite it in place.
    """
    index = Path(root) / "index.md"
    text = index.read_text(encoding="utf-8")
    begin, end = f"<!-- BEGIN imported:{source} -->", f"<!-- END imported:{source} -->"
    heading = {"eczoo": "## QEC Codes (imported from the Error Correction Zoo)",
               "qemzoo": "## QEM Techniques (imported from the QEM Zoo)"}[source]
    body = "\n".join(f"- [[{nid}]]: {title}." for nid, title in sorted(node_titles))
    block = f"{begin}\n{heading}\n\n{body}\n{end}"
    if begin in text and end in text:
        # Function replacement: ``block`` carries LaTeX titles (e.g. ``\mathbb``)
        # that would be mis-parsed as escapes in a string replacement template.
        text = re.sub(re.escape(begin) + r".*?" + re.escape(end),
                      lambda _m: block, text, flags=re.DOTALL)
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    index.write_text(text, encoding="utf-8")


def write_pages(root, source: str, rendered: list[tuple[str, str, str]],
                force: bool = False) -> list[dict]:
    """Write rendered (rel_path, markdown, title) pages under ``root``."""
    results = []
    for rel_path, markdown, _title in rendered:
        path = Path(root) / rel_path
        if path.exists() and not force:
            raise ImportError_(f"{rel_path} already exists (use --force to overwrite)")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8")
        results.append({"path": rel_path})
    return results
