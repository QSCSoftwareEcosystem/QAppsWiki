"""Stage 3a: derive typed, confidence-labeled edges from parsed pages.

Edges come from four origins:

1. Body ``[[wikilinks]]``        -> EXTRACTED, relation inferred from type pair.
2. ``related_*`` / ``packages:`` -> EXTRACTED (authored) / INFERRED (named),
   unresolved target -> AMBIGUOUS edge to a ``missing`` node.
3. ``sources:`` + inline cites   -> ``cites`` edges, EXTRACTED, target is a
   ``source`` page or an ``external`` node.
4. Explicit ``edges:`` frontmatter -> as authored (schema extension).

Returns ``(edges, synthetic_nodes)`` where ``synthetic_nodes`` maps the ids of
``missing``/``external`` targets to their node type so ``build`` can add them.
"""

from __future__ import annotations

from pathlib import Path

from . import schema
from .paths import classify_wikilink, is_url, resolve_source

_CONF_RANK = {"AMBIGUOUS": 0, "INFERRED": 1, "EXTRACTED": 2}

# Directory each related_* field / named-list prefers when resolving names.
_PREFER_DIR = {
    "related_packages": "packages",
    "related_concepts": "concepts",
    "related_integrations": "integrations",
    "related_how_to": "how-to",
    "related_workflows": "workflow",
    "related_artifacts": "qec-artifact",
    "packages": "packages",
}

_NAV = schema.NAV_TYPES


def _slug(value: str) -> str:
    return str(value).strip().lower().replace(" ", "-")


def _relation_for(src_type, tgt_type) -> str:
    """Heuristic relation for an explicit wikilink between two pages.

    Only high-precision, type-determined relations are inferred here; quantum
    relations that need editorial judgement (``wraps`` / ``encodes-qec``) are
    left to authored ``edges:`` so the derived graph stays high-precision.
    """
    if tgt_type in _NAV or tgt_type is None:
        return "related"
    # A benchmark page links the thing it measures -> validates-against (the
    # benchmark→subject relation is fixed by the source type, so it's safe here).
    if src_type == "benchmark" and tgt_type in ("package", "workflow", "concept", "integration"):
        return "validates-against"
    if src_type == "integration" and tgt_type == "package":
        return "integrates"
    if {src_type, tgt_type} == {"package", "how-to"}:
        return "has-how-to"
    if tgt_type == "concept":
        return "implements" if src_type == "package" else "related"
    if tgt_type == "integration":
        return "integrates"
    return "uses"


class _Resolver:
    """Resolve human names / slugs to node ids."""

    def __init__(self, node_ids: set[str]):
        self.ids = node_ids
        self.by_slug: dict[str, list[str]] = {}
        for nid in node_ids:
            base = nid.rsplit("/", 1)[-1]
            self.by_slug.setdefault(_slug(base), []).append(nid)

    def resolve(self, value: str, prefer_dir: str | None = None) -> str | None:
        if value in self.ids:
            return value
        cands = self.by_slug.get(_slug(value), [])
        if prefer_dir:
            pref = [c for c in cands if c.startswith(prefer_dir + "/")]
            if len(pref) == 1:
                return pref[0]
        return cands[0] if len(cands) == 1 else None


def derive_edges(pages: list[dict], root) -> tuple[list[dict], dict[str, str]]:
    root = Path(root).resolve()
    nodes = {p["node"]["id"]: p["node"] for p in pages}
    node_ids = set(nodes)
    resolver = _Resolver(node_ids)
    synthetic: dict[str, str] = {}
    edges: list[dict] = []

    def emit(src, tgt, relation, confidence, origin):
        edges.append(
            {
                "source": src,
                "target": tgt,
                "relation": relation,
                "confidence": confidence,
                "origin": origin,
            }
        )

    def add_missing(node_id, kind):
        # Real pages win; only register a synthetic node if id is unknown.
        if node_id not in node_ids:
            synthetic.setdefault(node_id, kind)

    for page in pages:
        node = page["node"]
        meta = page["meta"]
        src = node["id"]
        src_type = node["type"]
        fm = meta["frontmatter"]

        # 1. body wikilinks
        for raw in meta["body_links"]:
            cls = classify_wikilink(raw, node_ids)
            tgt = cls["node_id"]
            if cls["kind"] == "page":
                rel = _relation_for(src_type, nodes[tgt]["type"])
                emit(src, tgt, rel, "EXTRACTED", "wikilink")
            elif cls["kind"] == "external":
                add_missing(tgt, "external")
                emit(src, tgt, "related", "EXTRACTED", "wikilink")
            else:  # missing
                add_missing(tgt, "missing")
                emit(src, tgt, _relation_for(src_type, None), "EXTRACTED", "wikilink")

        # 2. related_* fields + named packages: list
        for field, relation in schema.RELATED_FIELDS.items():
            for value in _as_list(fm.get(field)):
                tgt = resolver.resolve(value, _PREFER_DIR.get(field))
                if tgt:
                    emit(src, tgt, relation, "EXTRACTED", f"frontmatter:{field}")
                else:
                    mid = f"{_PREFER_DIR.get(field, 'unknown')}/{_slug(value)}"
                    add_missing(mid, "missing")
                    emit(src, mid, relation, "AMBIGUOUS", f"frontmatter:{field}")

        if src_type in ("integration", "how-to", "benchmark", "workflow"):
            for value in _as_list(fm.get("packages")):
                tgt = resolver.resolve(value, "packages")
                if tgt:
                    emit(src, tgt, "composes-with", "INFERRED", "frontmatter:packages")
                else:
                    mid = f"packages/{_slug(value)}"
                    add_missing(mid, "missing")
                    emit(src, mid, "composes-with", "AMBIGUOUS", "frontmatter:packages")

        # 3. provenance: sources / source_markdown frontmatter + inline citations.
        # A path cited inline is claim-level (stronger) and wins over a path that
        # only appears in frontmatter; merging here keeps one cites edge per
        # source with the most-informative origin (instead of two that dedupe
        # would silently collapse, losing the inline signal).
        cited: dict[str, str] = {}
        for field in ("sources", "source_markdown"):
            for p in _as_list(fm.get(field)):
                cited.setdefault(p, "sources")
        for c in meta["citations"]:
            for p in c.get("paths", []):
                cited[p] = "inline-citation"
        for ref, origin in cited.items():
            info = resolve_source(ref, meta["rel_path"], root, node_ids)
            if info["node_id"]:
                emit(src, info["node_id"], "cites", "EXTRACTED", origin)
            else:
                ext_id = ref if is_url(ref) else f"ext:{ref}"
                add_missing(ext_id, "external")
                emit(src, ext_id, "cites", "EXTRACTED", origin)

        # 4. explicit edges: frontmatter
        for e in meta["explicit_edges"]:
            if not isinstance(e, dict) or not e.get("target"):
                continue
            target = str(e["target"]).strip()
            relation = e.get("relation", "related")
            confidence = e.get("confidence", "EXTRACTED")
            tgt = resolver.resolve(target) or (target if target in node_ids else None)
            if tgt is None:
                if is_url(target) or target.startswith("../"):
                    add_missing(target, "external")
                    tgt = target
                else:
                    add_missing(target, "missing")
                    tgt = target
                    confidence = "AMBIGUOUS"
            emit(src, tgt, relation, confidence, "explicit-edges")

    return _dedupe(edges), synthetic


def _dedupe(edges: list[dict]) -> list[dict]:
    """Collapse duplicate (source, target, relation); keep highest confidence."""
    best: dict[tuple, dict] = {}
    for e in edges:
        if e["source"] == e["target"]:
            continue
        key = (e["source"], e["target"], e["relation"])
        cur = best.get(key)
        if cur is None or _CONF_RANK[e["confidence"]] > _CONF_RANK[cur["confidence"]]:
            best[key] = e
    return list(best.values())


def _as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value] if value.strip() else []
    if isinstance(value, (list, tuple)):
        return [str(v) for v in value if str(v).strip()]
    return [str(value)]
