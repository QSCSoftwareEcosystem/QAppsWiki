"""Stage 5: derive insight metrics from the graph.

Surfaces what the wiki can't see by eye: central pages, orphans, under-linked
pages, surprising cross-domain links, ambiguous edges to review, and provenance
gaps. Navigation hubs (README/index/schema/…) and synthetic nodes are excluded
from centrality/orphan metrics so they don't dominate.
"""

from __future__ import annotations

from collections import Counter

from . import cluster, schema

# Shared with cluster so metrics and communities agree on which nodes count.
_is_content = schema.is_content


def analyze(graph) -> dict:
    nodes = dict(graph.nodes(data=True))

    by_type = Counter(a.get("type") for a in nodes.values())
    by_domain: Counter = Counter()
    for a in nodes.values():
        if _is_content(a):
            for d in a.get("domains") or []:
                by_domain[d] += 1
    by_conf = Counter(d["confidence"] for _u, _v, d in graph.edges(data=True))

    # God nodes by total degree (content only)
    degree = []
    for nid, a in nodes.items():
        if _is_content(a):
            deg = graph.in_degree(nid) + graph.out_degree(nid)
            degree.append((nid, deg))
    degree.sort(key=lambda x: (-x[1], x[0]))
    god_nodes = [{"id": n, "degree": d} for n, d in degree[:10] if d > 0]

    # Orphans: content nodes with no edge to another content node
    orphans = []
    for nid, a in nodes.items():
        if not _is_content(a):
            continue
        linked = False
        for _u, v in graph.out_edges(nid):
            if _is_content(nodes[v]):
                linked = True
                break
        if not linked:
            for u, _v in graph.in_edges(nid):
                if _is_content(nodes[u]):
                    linked = True
                    break
        if not linked:
            orphans.append(nid)

    # Under-linked packages
    under_linked = []
    for nid, a in nodes.items():
        if a.get("type") != "package":
            continue
        ntypes = set()
        for _u, v in graph.out_edges(nid):
            ntypes.add(nodes[v].get("type"))
        for u, _v in graph.in_edges(nid):
            ntypes.add(nodes[u].get("type"))
        if not ntypes & {"concept", "how-to", "integration"}:
            under_linked.append(nid)

    # Surprising cross-domain edges
    cross_domain = []
    for u, v, d in graph.edges(data=True):
        au, av = nodes[u], nodes[v]
        if not (_is_content(au) and _is_content(av)):
            continue
        du, dv = set(au.get("domains") or []), set(av.get("domains") or [])
        if du and dv and not (du & dv):
            cross_domain.append(
                {"source": u, "target": v, "relation": d["relation"],
                 "source_domains": sorted(du), "target_domains": sorted(dv)}
            )

    # Ambiguous edges
    ambiguous = [
        {"source": u, "target": v, "relation": d["relation"], "origin": d["origin"]}
        for u, v, d in graph.edges(data=True)
        if d["confidence"] == "AMBIGUOUS"
    ]

    # Provenance gaps
    needs_verification = sorted(
        nid for nid, a in nodes.items()
        if a.get("provenance_status") == "needs-verification"
    )
    external_cites = sum(
        1 for _u, v, d in graph.edges(data=True)
        if d["relation"] == "cites" and nodes[v].get("type") == "external"
    )

    # Provenance coverage: of the content pages that should carry sources
    # (everything but the source catalog), how many actually cite at least one?
    sourced = set()
    claim_level = set()
    for u, _v, d in graph.edges(data=True):
        if d["relation"] != "cites":
            continue
        sourced.add(u)
        if d.get("origin") == "inline-citation":
            claim_level.add(u)
    by_status: Counter = Counter()
    sourceable = []
    for nid, a in nodes.items():
        if not _is_content(a) or a.get("type") == "source":
            continue
        sourceable.append(nid)
        by_status[a.get("provenance_status") or "none"] += 1
    n_total = len(sourceable)
    n_sourced = sum(1 for nid in sourceable if nid in sourced)
    n_claim = sum(1 for nid in sourceable if nid in claim_level)
    unsourced = sorted(nid for nid in sourceable if nid not in sourced)
    coverage = {
        "content_pages": n_total,
        "with_sources": n_sourced,
        "with_inline_citations": n_claim,
        "source_coverage": round(n_sourced / n_total, 3) if n_total else 0.0,
        "claim_coverage": round(n_claim / n_total, 3) if n_total else 0.0,
        "by_status": dict(by_status),
        "unsourced": unsourced,
    }

    return {
        "stats": {
            "nodes": graph.number_of_nodes(),
            "edges": graph.number_of_edges(),
            "by_type": dict(by_type),
            "by_confidence": dict(by_conf),
            "by_domain": dict(by_domain),
        },
        "god_nodes": god_nodes,
        "communities": cluster.summarize(graph),
        "orphans": sorted(orphans),
        "under_linked": sorted(under_linked),
        "cross_domain": cross_domain,
        "ambiguous": ambiguous,
        "provenance": {
            "needs_verification": needs_verification,
            "external_cites": external_cites,
            "coverage": coverage,
        },
    }
