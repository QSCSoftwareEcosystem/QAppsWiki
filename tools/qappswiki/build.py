"""Stage 3b: assemble nodes + edges into a ``networkx.MultiDiGraph``.

A MultiDiGraph lets two pages carry several differently-typed edges (e.g. both
``uses`` and ``cites``) without collision; the edge key is the relation.
Synthetic ``missing``/``external`` targets are added so every edge resolves.
"""

from __future__ import annotations

import networkx as nx


def build_graph(node_dicts: list[dict], edge_dicts: list[dict], synthetic: dict[str, str] | None = None) -> nx.MultiDiGraph:
    g = nx.MultiDiGraph()

    for node in node_dicts:
        attrs = {k: v for k, v in node.items() if k != "id"}
        attrs.setdefault("synthetic", False)
        g.add_node(node["id"], **attrs)

    for node_id, kind in (synthetic or {}).items():
        if g.has_node(node_id):
            continue
        g.add_node(
            node_id,
            type=kind,  # "missing" or "external"
            title=node_id.split("/")[-1].replace("ext:", ""),
            domains=[],
            status=None,
            provenance_status=None,
            rel_path=None,
            synthetic=True,
        )

    for e in edge_dicts:
        g.add_edge(
            e["source"],
            e["target"],
            key=e["relation"],
            relation=e["relation"],
            confidence=e["confidence"],
            origin=e["origin"],
        )

    return g
