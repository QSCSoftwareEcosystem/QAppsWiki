"""Stage 7: export the graph as JSON and a self-contained HTML visualization."""

from __future__ import annotations

import json
from collections import Counter

from . import cluster

_CYTOSCAPE_CDN = "https://unpkg.com/cytoscape@3.30.2/dist/cytoscape.min.js"

_TYPE_COLOR = {
    "package": "#2563eb",
    "concept": "#7c3aed",
    "how-to": "#059669",
    "integration": "#d97706",
    "workflow": "#0891b2",
    "qec-artifact": "#db2777",
    "benchmark": "#65a30d",
    "source": "#64748b",
    "external": "#94a3b8",
    "missing": "#dc2626",
}


def to_json(graph, generated: str = "") -> dict:
    clustering = cluster.detect(graph)
    assignment = clustering["assignment"]
    labels = {c["index"]: c["label"] for c in clustering["communities"]}

    nodes = []
    for nid, a in graph.nodes(data=True):
        node = {"id": nid, **{k: v for k, v in a.items()}}
        cid = assignment.get(nid)
        node["community"] = cid
        node["community_label"] = labels.get(cid) if cid is not None else None
        nodes.append(node)
    edges = [
        {"source": u, "target": v, "relation": d["relation"],
         "confidence": d["confidence"], "origin": d["origin"]}
        for u, v, d in graph.edges(data=True)
    ]
    by_type = Counter(a.get("type") for _n, a in graph.nodes(data=True))
    by_conf = Counter(e["confidence"] for e in edges)
    return {
        "schema_version": "qappswiki-graph-0",
        "generated": generated,
        "stats": {
            "nodes": graph.number_of_nodes(),
            "edges": len(edges),
            "by_type": dict(by_type),
            "by_confidence": dict(by_conf),
            "communities": clustering["count"],
            "modularity": clustering["modularity"],
        },
        "communities": clustering["communities"],
        "nodes": nodes,
        "edges": edges,
    }


def to_html(graph, generated: str = "") -> str:
    data = to_json(graph, generated)
    elements = []
    # Compound parent nodes group each community visually.
    for c in data["communities"]:
        elements.append({"data": {
            "id": f"comm:{c['index']}",
            "label": f"{c['label']} ({c['size']})",
            "iscommunity": "1",
        }})
    for n in data["nodes"]:
        d = {
            "id": n["id"],
            "label": n.get("title") or n["id"],
            "type": n.get("type") or "unknown",
            "domains": ", ".join(n.get("domains") or []),
            "provenance": n.get("provenance_status") or "",
            "community": n.get("community_label") or "",
        }
        if n.get("community") is not None:
            d["parent"] = f"comm:{n['community']}"
        elements.append({"data": d})
    for i, e in enumerate(data["edges"]):
        elements.append({"data": {
            "id": f"e{i}",
            "source": e["source"],
            "target": e["target"],
            "relation": e["relation"],
            "confidence": e["confidence"],
        }})

    color_map = json.dumps(_TYPE_COLOR)
    elements_json = json.dumps(elements)
    stats = data["stats"]
    legend = " · ".join(f"{k}: {v}" for k, v in sorted(stats["by_type"].items()) if k)
    comm_note = f"{stats.get('communities', 0)} communities (modularity {stats.get('modularity', 0)})"

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>QAppsWiki Graph</title>
<script src="{_CYTOSCAPE_CDN}"></script>
<style>
  body {{ margin:0; font-family: system-ui, sans-serif; }}
  #bar {{ padding:8px 12px; background:#0f172a; color:#e2e8f0; font-size:13px; }}
  #cy {{ position:absolute; top:38px; bottom:0; left:0; right:0; }}
  .hint {{ color:#94a3b8; }}
</style>
</head>
<body>
<div id="bar"><b>QAppsWiki</b> — {stats['nodes']} nodes, {stats['edges']} edges, {comm_note}
  <span class="hint">&nbsp;|&nbsp; {legend} &nbsp;|&nbsp; boxed = community, red node = missing page, dashed red edge = AMBIGUOUS</span>
</div>
<div id="cy"></div>
<script>
const TYPE_COLOR = {color_map};
const elements = {elements_json};
const cy = cytoscape({{
  container: document.getElementById('cy'),
  elements: elements,
  layout: {{ name: 'cose', animate: false, padding: 30, nodeRepulsion: 8000 }},
  style: [
    {{ selector: 'node', style: {{
        'background-color': ele => TYPE_COLOR[ele.data('type')] || '#475569',
        'label': 'data(label)', 'font-size': 9, 'color': '#0f172a',
        'text-wrap': 'wrap', 'text-max-width': 90, 'width': 18, 'height': 18 }} }},
    {{ selector: 'edge', style: {{
        'width': 1.2, 'line-color': '#cbd5e1', 'target-arrow-color': '#cbd5e1',
        'target-arrow-shape': 'triangle', 'curve-style': 'bezier',
        'label': 'data(relation)', 'font-size': 7, 'color': '#64748b',
        'text-rotation': 'autorotate' }} }},
    {{ selector: 'edge[confidence = "INFERRED"]', style: {{ 'line-style': 'dashed' }} }},
    {{ selector: 'edge[confidence = "AMBIGUOUS"]', style: {{
        'line-style': 'dashed', 'line-color': '#dc2626', 'target-arrow-color': '#dc2626' }} }},
    {{ selector: 'node[iscommunity = "1"]', style: {{
        'background-color': '#f1f5f9', 'background-opacity': 0.5, 'border-color': '#94a3b8',
        'border-width': 1, 'shape': 'round-rectangle', 'label': 'data(label)',
        'font-size': 11, 'font-weight': 'bold', 'color': '#475569',
        'text-valign': 'top', 'text-halign': 'center', 'padding': 12 }} }},
  ]
}});
cy.on('tap', 'node', e => {{
  const d = e.target.data();
  if (d.iscommunity) {{ return; }}
  alert(d.id + "\\ntype: " + d.type + "\\ncommunity: " + (d.community||'-') +
        "\\ndomains: " + (d.domains||'-') + "\\nprovenance: " + (d.provenance||'-'));
}});
</script>
</body>
</html>
"""
