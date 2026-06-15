"""Stage 4: validate parsed pages + graph against frontmatter-v0.

Returns a list of ``Finding`` dicts ``{level, code, page, message}`` where level
is ``ERROR`` or ``WARNING``. Field-level checks read ``parse_meta``; link/edge
checks read the built graph (so a single source of truth for resolution).
"""

from __future__ import annotations

from pathlib import Path

from . import schema
from .paths import resolve_source

# Content types subject to orphan / domains checks.
_ORPHAN_TYPES = schema.CONTENT_TYPES - {"source"}


def _f(level, code, page, message):
    return {"level": level, "code": code, "page": page, "message": message}


def _as_list(value):
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, (list, tuple)):
        return [str(v) for v in value if str(v).strip()]
    return [str(value)]


def _index_targets(pages: list[dict]) -> set[str]:
    """Node ids reachable from index.md body wikilinks."""
    from .paths import strip_link

    for p in pages:
        if p["node"]["id"] == "index":
            return {strip_link(t) for t in p["meta"]["body_links"]}
    return set()


def validate(pages: list[dict], graph, root) -> list[dict]:
    root = Path(root).resolve()
    findings: list[dict] = []
    index_targets = _index_targets(pages)

    for page in pages:
        findings += _validate_page(page, root, index_targets)

    findings += _validate_graph(graph)
    return _dedupe(findings)


def _validate_page(page: dict, root: Path, index_targets: set[str]) -> list[dict]:
    node = page["node"]
    meta = page["meta"]
    pid = node["id"]
    fm = meta["frontmatter"]
    out: list[dict] = []

    if meta["parse_error"]:
        out.append(_f("ERROR", "malformed-frontmatter", pid, meta["parse_error"]))
        if not fm:
            return out

    ptype = node["type"]
    is_content = ptype in schema.CONTENT_TYPES
    is_provisional = ptype in schema.PROVISIONAL_TYPES

    # Unknown type
    if ptype is None:
        out.append(_f("ERROR", "missing-required-field", pid, "missing required field: type"))
    elif ptype not in schema.KNOWN_TYPES:
        out.append(_f("WARNING", "unknown-type", pid, f"type '{ptype}' is not in the known taxonomy"))

    # Required fields. Absent/None is a hard miss; present-but-empty (e.g. a
    # freshly scaffolded `capabilities: []`) is an incompleteness warning.
    required = schema.required_fields(ptype) if ptype else schema.COMMON_REQUIRED
    miss_level = "WARNING" if (is_provisional or not is_content) else "ERROR"
    for field in required:
        if field == "type":
            continue
        val = fm.get(field)
        if val is None:
            out.append(_f(miss_level, "missing-required-field", pid, f"missing required field: {field}"))
        elif isinstance(val, (list, str)) and len(val) == 0:
            out.append(_f("WARNING", "empty-required-field", pid, f"required field is empty: {field}"))

    # Provisional pages should be marked provisional
    if is_provisional and fm.get("status") != "provisional":
        out.append(_f("WARNING", "provisional-status", pid, f"provisional type '{ptype}' should have status: provisional"))

    # domains presence (content pages; source catalog entries are exempt)
    if is_content and ptype != "source" and not node["domains"]:
        out.append(_f("WARNING", "missing-domains", pid, "content page has no domains tag"))

    # Closed-enum membership
    for field, vocab in schema.CLOSED_ENUM_FIELDS.items():
        for v in _as_list(fm.get(field)):
            if v not in vocab:
                out.append(_f("ERROR", "invalid-enum-value", pid, f"{field}: '{v}' not in controlled vocabulary"))

    # Open-list membership (warnings)
    for field, vocab in schema.OPEN_LIST_FIELDS.items():
        for v in _as_list(fm.get(field)):
            if v not in vocab:
                out.append(_f("WARNING", "unknown-tag", pid, f"{field}: '{v}' not in initial vocabulary (typo or new tag?)"))

    # provenance_status: needs-verification surfaced
    if fm.get("provenance_status") == "needs-verification":
        out.append(_f("WARNING", "needs-verification", pid, "provenance_status is needs-verification"))

    # Explicit edges validity
    for e in meta["explicit_edges"]:
        if not isinstance(e, dict):
            continue
        rel = e.get("relation")
        if rel is not None and rel not in schema.EDGE_RELATIONS:
            out.append(_f("ERROR", "invalid-edge-relation", pid, f"edges: relation '{rel}' not in vocabulary"))
        conf = e.get("confidence")
        if conf is not None and conf not in schema.EDGE_CONFIDENCE:
            out.append(_f("ERROR", "invalid-edge-confidence", pid, f"edges: confidence '{conf}' not in {{EXTRACTED,INFERRED,AMBIGUOUS}}"))

    # Source-path existence + inline-citation coverage
    fm_sources = set(_as_list(fm.get("sources")) + _as_list(fm.get("source_markdown")))
    for ref in fm_sources:
        info = resolve_source(ref, meta["rel_path"], root, set())
        if info["kind"] in ("internal", "external") and not info["exists"]:
            out.append(_f("WARNING", "missing-source-file", pid, f"source not found: {ref}"))
    # Every path cited inline must also be declared in sources:/source_markdown:
    # (the schema's two-level provenance rule). On a content page this is a hard
    # ERROR — a claim attributing itself to an undeclared source is a provenance
    # break the strict gate must stop; on nav/doc pages it stays a WARNING.
    inline_level = "ERROR" if is_content else "WARNING"
    for c in meta["citations"]:
        for ref in c.get("paths", []):
            if ref not in fm_sources:
                out.append(_f(inline_level, "uncited-inline-source", pid, f"inline source '{ref}' not listed in sources:"))

    # Orphan: content page not linked from index
    if ptype in _ORPHAN_TYPES and pid not in index_targets:
        out.append(_f("WARNING", "orphan-not-in-index", pid, "page is not linked from index.md"))

    # Versioning & freshness fields (form only — no network; staleness is a
    # separate online concern handled by the serving layer / `freshness`).
    out += _validate_version_fields(pid, fm)

    return out


def _validate_version_fields(pid: str, fm: dict) -> list[dict]:
    """Validate the *form* of version_source / version_built (never the network)."""
    out: list[dict] = []
    vs = fm.get("version_source")
    if vs is not None:
        if not isinstance(vs, dict):
            out.append(_f("ERROR", "invalid-version-source", pid,
                          "version_source must be a mapping with `kind` and `id`"))
        else:
            kind = vs.get("kind")
            if kind not in schema.VERSION_SOURCE_KIND:
                out.append(_f("ERROR", "invalid-version-source", pid,
                              f"version_source.kind '{kind}' not in vocabulary"))
            if not vs.get("id"):
                out.append(_f("WARNING", "incomplete-version-source", pid,
                              "version_source.id is empty"))
    vb = fm.get("version_built")
    if vb is not None and not isinstance(vb, (str, int, float)):
        out.append(_f("WARNING", "invalid-version-built", pid,
                      "version_built should be a version string (e.g. \"1.2.0\")"))
    return out


def _validate_graph(graph) -> list[dict]:
    out: list[dict] = []

    # Broken / dangling targets
    for u, v, _k, data in graph.edges(keys=True, data=True):
        tnode = graph.nodes[v]
        if not (tnode.get("synthetic") and tnode.get("type") == "missing"):
            continue
        origin = data.get("origin", "")
        if origin == "wikilink":
            out.append(_f("ERROR", "broken-wikilink", u, f"[[{v}]] does not resolve to a page"))
        elif origin.startswith("frontmatter:related"):
            out.append(_f("WARNING", "dangling-related-ref", u, f"related reference '{v}' has no page"))
        elif origin == "frontmatter:packages":
            out.append(_f("WARNING", "dangling-package-ref", u, f"packages reference '{v}' has no page"))
        elif origin == "explicit-edges":
            out.append(_f("WARNING", "ambiguous-edge", u, f"explicit edge target '{v}' has no page"))

    # Under-linked package pages
    for nid, attrs in graph.nodes(data=True):
        if attrs.get("type") != "package":
            continue
        neighbor_types = set()
        for _u, v in graph.out_edges(nid):
            neighbor_types.add(graph.nodes[v].get("type"))
        for u, _v in graph.in_edges(nid):
            neighbor_types.add(graph.nodes[u].get("type"))
        if not neighbor_types & {"concept", "how-to", "integration"}:
            out.append(_f("WARNING", "package-underlinked", nid, "package page links to no concept/how-to/integration"))

    return out


def _dedupe(findings: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for f in findings:
        key = (f["level"], f["code"], f["page"], f["message"])
        if key not in seen:
            seen.add(key)
            out.append(f)
    order = {"ERROR": 0, "WARNING": 1}
    out.sort(key=lambda f: (order.get(f["level"], 2), f["page"], f["code"]))
    return out


def has_errors(findings: list[dict]) -> bool:
    return any(f["level"] == "ERROR" for f in findings)
