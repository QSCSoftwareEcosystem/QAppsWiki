"""Stage 8: MCP stdio server exposing read-only queries over graph.json.

The query functions (``q_*``) are pure and importable without the ``mcp``
package, so tests exercise them directly. ``start_server`` wires them to an MCP
stdio server (requires ``pip install 'qappswiki[mcp]'``).
"""

from __future__ import annotations

import json
from pathlib import Path

import networkx as nx

from . import analyze as _analyze


def load_graph(path) -> nx.MultiDiGraph:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    g = nx.MultiDiGraph()
    for n in data["nodes"]:
        nid = n["id"]
        g.add_node(nid, **{k: v for k, v in n.items() if k != "id"})
    for e in data["edges"]:
        g.add_edge(e["source"], e["target"], key=e["relation"],
                   relation=e["relation"], confidence=e["confidence"], origin=e["origin"])
    return g


# --------------------------------------------------------------------------- #
# pure query functions
# --------------------------------------------------------------------------- #

def q_query(g, term, type=None, domain=None) -> list[dict]:
    term = (term or "").lower()
    out = []
    for nid, a in g.nodes(data=True):
        if type and a.get("type") != type:
            continue
        if domain and domain not in (a.get("domains") or []):
            continue
        hay = " ".join([nid, str(a.get("title") or ""), " ".join(a.get("domains") or [])]).lower()
        if not term or term in hay:
            out.append({"id": nid, "type": a.get("type"), "title": a.get("title"),
                        "domains": a.get("domains") or []})
    return out


def q_get_node(g, node_id) -> dict | None:
    if node_id not in g:
        return None
    a = g.nodes[node_id]
    out_edges = [{"target": v, "relation": d["relation"], "confidence": d["confidence"]}
                 for _u, v, d in g.out_edges(node_id, data=True)]
    in_edges = [{"source": u, "relation": d["relation"], "confidence": d["confidence"]}
                for u, _v, d in g.in_edges(node_id, data=True)]
    return {"id": node_id, **{k: v for k, v in a.items()},
            "out_edges": out_edges, "in_edges": in_edges}


def q_get_neighbors(g, node_id, relation=None, confidence=None) -> list[dict]:
    if node_id not in g:
        return []
    out = []
    for _u, v, d in g.out_edges(node_id, data=True):
        if relation and d["relation"] != relation:
            continue
        if confidence and d["confidence"] != confidence:
            continue
        out.append({"id": v, "direction": "out", "relation": d["relation"], "confidence": d["confidence"]})
    for u, _v, d in g.in_edges(node_id, data=True):
        if relation and d["relation"] != relation:
            continue
        if confidence and d["confidence"] != confidence:
            continue
        out.append({"id": u, "direction": "in", "relation": d["relation"], "confidence": d["confidence"]})
    return out


def q_shortest_path(g, source, target) -> dict:
    ug = g.to_undirected()
    try:
        nodes = nx.shortest_path(ug, source, target)
    except (nx.NetworkXNoPath, nx.NodeNotFound) as exc:
        return {"found": False, "reason": str(exc), "path": []}
    return {"found": True, "path": nodes, "length": len(nodes) - 1}


def q_list_orphans(g) -> list[str]:
    return _analyze.analyze(g)["orphans"]


def q_graph_stats(g) -> dict:
    return _analyze.analyze(g)["stats"]


def q_list_ambiguous(g) -> list[dict]:
    return _analyze.analyze(g)["ambiguous"]


def q_check_freshness(g, node_id, timeout=10.0, fetch=None) -> dict:
    """Online freshness verdict for one package node (uses graph version fields)."""
    from . import freshness as _freshness
    if node_id not in g:
        return {"page": node_id, "status": "untracked", "detail": "no such node"}
    a = g.nodes[node_id]
    fm = {"version_source": a.get("version_source"), "version_built": a.get("version_built"),
          "version_scope": a.get("version_scope")}
    return _freshness.check_package({"id": node_id, "type": a.get("type")}, fm, timeout, fetch)


# --------------------------------------------------------------------------- #
# MCP wiring
# --------------------------------------------------------------------------- #

def start_server(graph_path):  # pragma: no cover - requires mcp + stdio
    try:
        import asyncio

        from mcp.server import Server
        from mcp.server.stdio import stdio_server
        from mcp.types import TextContent, Tool
    except ImportError as exc:
        raise SystemExit(
            "MCP server needs the 'mcp' package. Install with: pip install 'qappswiki[mcp]'"
        ) from exc

    g = load_graph(graph_path)
    server = Server("qappswiki")

    tools = [
        Tool(name="query_graph", description="Search nodes by term/type/domain",
             inputSchema={"type": "object", "properties": {
                 "term": {"type": "string"}, "type": {"type": "string"}, "domain": {"type": "string"}}}),
        Tool(name="get_node", description="Full node + its edges",
             inputSchema={"type": "object", "properties": {"id": {"type": "string"}}, "required": ["id"]}),
        Tool(name="get_neighbors", description="Adjacent nodes, optionally filtered",
             inputSchema={"type": "object", "properties": {
                 "id": {"type": "string"}, "relation": {"type": "string"}, "confidence": {"type": "string"}},
                 "required": ["id"]}),
        Tool(name="shortest_path", description="Shortest path between two pages",
             inputSchema={"type": "object", "properties": {
                 "source": {"type": "string"}, "target": {"type": "string"}},
                 "required": ["source", "target"]}),
        Tool(name="list_orphans", description="Content pages with no content links",
             inputSchema={"type": "object", "properties": {}}),
        Tool(name="graph_stats", description="Node/edge counts and breakdowns",
             inputSchema={"type": "object", "properties": {}}),
        Tool(name="list_ambiguous", description="AMBIGUOUS edges needing review",
             inputSchema={"type": "object", "properties": {}}),
        Tool(name="check_freshness", description="Online: is a package context current vs upstream?",
             inputSchema={"type": "object", "properties": {"id": {"type": "string"}}, "required": ["id"]}),
    ]

    dispatch = {
        "query_graph": lambda a: q_query(g, a.get("term", ""), a.get("type"), a.get("domain")),
        "get_node": lambda a: q_get_node(g, a["id"]),
        "get_neighbors": lambda a: q_get_neighbors(g, a["id"], a.get("relation"), a.get("confidence")),
        "shortest_path": lambda a: q_shortest_path(g, a["source"], a["target"]),
        "list_orphans": lambda a: q_list_orphans(g),
        "graph_stats": lambda a: q_graph_stats(g),
        "list_ambiguous": lambda a: q_list_ambiguous(g),
        "check_freshness": lambda a: q_check_freshness(g, a["id"]),
    }

    @server.list_tools()
    async def list_tools():
        return tools

    @server.call_tool()
    async def call_tool(name, arguments):
        result = dispatch[name](arguments or {})
        return [TextContent(type="text", text=json.dumps(result, indent=2))]

    async def _run():
        async with stdio_server() as (r, w):
            await server.run(r, w, server.create_initialization_options())

    asyncio.run(_run())
