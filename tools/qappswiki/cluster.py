"""Stage 4: detect communities (thematic clusters) in the knowledge graph.

This is the QAppsWiki analogue of graphify's Leiden pass: it groups the wiki into
the neighborhoods it naturally falls into, names each one, and points at its
local hub. Two differences, both deliberate:

* **No new dependency.** Community detection uses networkx's built-in Louvain
  modularity optimisation over the *content* subgraph (synthetic ``missing`` /
  ``external`` nodes and navigation pages are excluded, same as ``analyze``).
  Edges are weighted by confidence so authored ``EXTRACTED`` links pull harder
  than ``INFERRED`` / ``AMBIGUOUS`` ones.
* **Deterministic by default.** A fixed seed makes the partition reproducible so
  ``graph.json`` and ``GRAPH_REPORT.md`` are stable across runs and diffable in
  CI. (graphify's labels come from an LLM; here the *core* is deterministic and
  an optional namer can be layered on — the same offline/online split used by
  ``freshness``.)

Each community gets a deterministic label from its dominant ``domains`` and its
highest-degree member (its local god-node). ``apply_labels`` is the seam where a
later LLM namer can replace those heuristic labels without touching detection.
"""

from __future__ import annotations

from collections import Counter

import networkx as nx

from . import schema

# Reproducible partitions: same corpus -> same communities, so outputs diff
# cleanly in CI. Louvain is randomised in its tie-breaking; the seed pins it.
_SEED = 1789

# Authored links should bind a community more tightly than inferred guesses.
_CONF_WEIGHT = {"EXTRACTED": 3.0, "INFERRED": 2.0, "AMBIGUOUS": 1.0}


def _content_undirected(graph) -> nx.Graph:
    """Undirected, confidence-weighted projection over content nodes only.

    Parallel and bidirectional edges between the same pair collapse into one
    weighted edge (weights summed) so Louvain sees link *strength*, not count.
    """
    ug = nx.Graph()
    for nid, a in graph.nodes(data=True):
        if schema.is_content(a):
            ug.add_node(nid)
    for u, v, d in graph.edges(data=True):
        if u == v or u not in ug or v not in ug:
            continue
        w = _CONF_WEIGHT.get(d.get("confidence"), 1.0)
        if ug.has_edge(u, v):
            ug[u][v]["weight"] += w
        else:
            ug.add_edge(u, v, weight=w)
    return ug


def _full_degree(graph, nid) -> int:
    """Total degree in the *full* graph (matches ``analyze`` god-node ranking)."""
    return graph.in_degree(nid) + graph.out_degree(nid)


def _label(members, domains_by_node, god_title) -> str:
    """Deterministic community name: dominant domain(s), else its hub's title."""
    dom = Counter()
    for nid in members:
        for d in domains_by_node.get(nid) or []:
            dom[d] += 1
    if dom:
        top = max(dom.values())
        winners = sorted(d for d, c in dom.items() if c == top)
        return " / ".join(winners[:2])
    return god_title or "uncategorised"


def detect(graph, resolution: float = 1.0, seed: int = _SEED) -> dict:
    """Partition the content graph into communities.

    Returns a dict with:

    * ``assignment``  — ``{node_id: community_index}`` for content nodes.
    * ``communities`` — list (largest first) of per-community summaries:
      ``index, label, size, members, god_node, domains, internal_edges,
      external_edges, cohesion``.
    * ``modularity``  — partition quality in ``[-0.5, 1]`` (higher = cleaner).
    * ``count``       — number of communities.
    """
    ug = _content_undirected(graph)
    if ug.number_of_nodes() == 0:
        return {"assignment": {}, "communities": [], "modularity": 0.0, "count": 0}

    parts = nx.community.louvain_communities(ug, weight="weight", resolution=resolution, seed=seed)
    # Order communities largest-first, then by smallest member id, for stable
    # indices regardless of Louvain's internal ordering.
    parts = sorted(parts, key=lambda s: (-len(s), min(s)))

    try:
        modularity = nx.community.modularity(ug, parts, weight="weight")
    except (ZeroDivisionError, nx.NetworkXError):  # pragma: no cover - degenerate graphs
        modularity = 0.0

    domains_by_node = {nid: (a.get("domains") or []) for nid, a in graph.nodes(data=True)}
    titles = {nid: (a.get("title") or nid) for nid, a in graph.nodes(data=True)}

    assignment: dict[str, int] = {}
    for idx, members in enumerate(parts):
        for nid in members:
            assignment[nid] = idx

    communities = []
    for idx, members in enumerate(parts):
        members_sorted = sorted(members)
        god = max(members_sorted, key=lambda n: (_full_degree(graph, n), n)) if members_sorted else None
        internal = external = 0
        for u, v in ug.edges():
            iu, iv = u in members, v in members
            if iu and iv:
                internal += 1
            elif iu or iv:
                external += 1
        dom = Counter()
        for nid in members_sorted:
            for d in domains_by_node.get(nid) or []:
                dom[d] += 1
        communities.append({
            "index": idx,
            "label": _label(members_sorted, domains_by_node, titles.get(god)),
            "size": len(members_sorted),
            "members": members_sorted,
            "god_node": god,
            "domains": [d for d, _ in dom.most_common()],
            "internal_edges": internal,
            "external_edges": external,
            "cohesion": round(internal / (internal + external), 3) if (internal + external) else 0.0,
        })

    return {
        "assignment": assignment,
        "communities": communities,
        "modularity": round(modularity, 4),
        "count": len(parts),
    }


def summarize(graph, resolution: float = 1.0, seed: int = _SEED) -> dict:
    """Detection result without the per-node ``assignment`` map.

    This is what ``analyze`` embeds in its report payload; the assignment map is
    only needed by ``export`` to stamp nodes.
    """
    r = detect(graph, resolution=resolution, seed=seed)
    return {"communities": r["communities"], "modularity": r["modularity"], "count": r["count"]}


def apply_labels(result: dict, labels: dict) -> dict:
    """Override heuristic labels by community index (the LLM-namer seam).

    ``labels`` maps community ``index`` -> name. Unknown indices are ignored;
    missing ones keep their deterministic label. Mutates and returns ``result``.
    """
    for c in result.get("communities", []):
        if c["index"] in labels:
            c["label"] = labels[c["index"]]
    return result
