"""Command-line interface and pipeline orchestration.

Subcommands:
  validate   collect -> parse -> build -> validate; write VALIDATION_REPORT.md
  build      ... -> export; write graph.json + graph.html
  report     ... -> analyze; write GRAPH_REPORT.md
  run        validate + build + report in one parse (the AS/CI entry point)
  serve      MCP stdio server over graph.json
  query/path/explain   read-only graph queries
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path

from . import analyze as _analyze
from . import build as _build
from . import collect as _collect
from . import edges as _edges
from . import export as _export
from . import parse as _parse
from . import report as _report
from . import validate as _validate
from .cache import Cache


def _today() -> str:
    return _dt.date.today().isoformat()


def _default_root() -> Path:
    # Installed at <wiki>/tools/qappswiki/cli.py -> wiki root is parents[2].
    here = Path(__file__).resolve()
    return here.parents[2]


def _out_dir(args, root: Path) -> Path:
    out = Path(args.out) if args.out else root / "wiki-out"
    out.mkdir(parents=True, exist_ok=True)
    return out


def run_pipeline(root: Path, out: Path, use_cache: bool, dirs=None):
    """collect -> parse -> edges -> build. Returns (pages, graph)."""
    cache = Cache(out, enabled=use_cache)
    refs = _collect.collect_pages(root, dirs)
    pages = []
    for ref in refs:
        node, meta = _parse.parse_page(ref, root, cache)
        pages.append({"node": node, "meta": meta})
    edge_list, synthetic = _edges.derive_edges(pages, root)
    graph = _build.build_graph([p["node"] for p in pages], edge_list, synthetic)
    return pages, graph


def _write(path: Path, text: str):
    path.write_text(text, encoding="utf-8")


def _export_graph(graph, out: Path):
    _write(out / "graph.json", json.dumps(_export.to_json(graph, _today()), indent=2))
    _write(out / "graph.html", _export.to_html(graph, _today()))


def _emit_findings(findings, fmt):
    if fmt == "json":
        print(json.dumps(findings, indent=2))
    else:
        errs = sum(f["level"] == "ERROR" for f in findings)
        warns = sum(f["level"] == "WARNING" for f in findings)
        for f in findings:
            print(f"  [{f['level']}] {f['code']}  {f['page']} — {f['message']}")
        print(f"\n{errs} errors, {warns} warnings")


def _exit_code(findings, strict: bool) -> int:
    if _validate.has_errors(findings):
        return 1
    if strict and any(f["level"] == "WARNING" for f in findings):
        return 1
    return 0


# --------------------------------------------------------------------------- #
# commands
# --------------------------------------------------------------------------- #

def cmd_validate(args):
    root = Path(args.root).resolve()
    out = _out_dir(args, root)
    dirs = args.dirs.split(",") if args.dirs else None
    pages, graph = run_pipeline(root, out, not args.no_cache, dirs)
    findings = _validate.validate(pages, graph, root)
    _write(out / "VALIDATION_REPORT.md", _report.render_validation_report(findings, _today()))
    _emit_findings(findings, args.format)
    return _exit_code(findings, args.strict)


def cmd_build(args):
    root = Path(args.root).resolve()
    out = _out_dir(args, root)
    _, graph = run_pipeline(root, out, not args.no_cache)
    _export_graph(graph, out)
    print(f"wrote {out/'graph.json'} ({graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges)")
    return 0


def cmd_report(args):
    root = Path(args.root).resolve()
    out = _out_dir(args, root)
    _, graph = run_pipeline(root, out, not args.no_cache)
    analysis = _analyze.analyze(graph)
    _write(out / "GRAPH_REPORT.md", _report.render_graph_report(analysis, _today()))
    print(f"wrote {out/'GRAPH_REPORT.md'} — {len(analysis['orphans'])} orphans, "
          f"{len(analysis['ambiguous'])} ambiguous edges")
    return 0


def cmd_run(args):
    root = Path(args.root).resolve()
    out = _out_dir(args, root)
    pages, graph = run_pipeline(root, out, not args.no_cache)
    findings = _validate.validate(pages, graph, root)
    analysis = _analyze.analyze(graph)
    _write(out / "VALIDATION_REPORT.md", _report.render_validation_report(findings, _today()))
    _write(out / "GRAPH_REPORT.md", _report.render_graph_report(analysis, _today()))
    if not args.no_html:
        _export_graph(graph, out)
    errs = sum(f["level"] == "ERROR" for f in findings)
    warns = sum(f["level"] == "WARNING" for f in findings)
    print(f"validated {len(pages)} pages: {errs} errors, {warns} warnings")
    print(f"graph: {graph.number_of_nodes()} nodes, {graph.number_of_edges()} edges "
          f"({len(analysis['orphans'])} orphans, {len(analysis['ambiguous'])} ambiguous)")
    print(f"outputs in {out}/")
    if args.log:
        touched = "wiki-out/graph.json, wiki-out/GRAPH_REPORT.md, wiki-out/VALIDATION_REPORT.md"
        print("\n--- log.md entry ---")
        print(f"## {_today()} tooling | validate+graph build | touched: {touched}")
        print(f"\n{errs} errors, {warns} warnings; {len(analysis['orphans'])} orphans; "
              f"{len(analysis['ambiguous'])} ambiguous edges flagged.")
    return _exit_code(findings, args.strict)


def cmd_serve(args):
    from . import serve
    root = Path(args.root).resolve()
    out = _out_dir(args, root)
    graph_path = Path(args.graph) if args.graph else out / "graph.json"
    if not graph_path.exists():
        _, graph = run_pipeline(root, out, not args.no_cache)
        _export_graph(graph, out)
    serve.start_server(graph_path)
    return 0


def _load_graph(args):
    root = Path(args.root).resolve()
    out = _out_dir(args, root)
    _, graph = run_pipeline(root, out, not args.no_cache)
    return graph


def cmd_query(args):
    graph = _load_graph(args)
    term = args.term.lower()
    for nid, a in graph.nodes(data=True):
        hay = " ".join([nid, str(a.get("title") or ""), " ".join(a.get("domains") or [])]).lower()
        if term in hay:
            print(f"  {nid}  [{a.get('type')}]  {a.get('title')}")
    return 0


def cmd_path(args):
    import networkx as nx
    graph = _load_graph(args)
    ug = graph.to_undirected()
    try:
        nodes = nx.shortest_path(ug, args.source, args.target)
    except (nx.NetworkXNoPath, nx.NodeNotFound) as exc:
        print(f"no path: {exc}")
        return 1
    print(" -> ".join(nodes))
    return 0


def cmd_explain(args):
    graph = _load_graph(args)
    nid = args.node
    if nid not in graph:
        print(f"unknown node: {nid}")
        return 1
    a = graph.nodes[nid]
    print(f"# {nid}\ntype: {a.get('type')}\ntitle: {a.get('title')}\n"
          f"domains: {', '.join(a.get('domains') or [])}\nprovenance: {a.get('provenance_status')}")
    print("\noutgoing:")
    for _u, v, d in graph.out_edges(nid, data=True):
        print(f"  —{d['relation']}({d['confidence']})→ {v}")
    print("incoming:")
    for u, _v, d in graph.in_edges(nid, data=True):
        print(f"  {u} —{d['relation']}({d['confidence']})→")
    return 0


def _add_common(p):
    p.add_argument("--root", default=str(_default_root()), help="wiki root (default: parent of tools/)")
    p.add_argument("--out", default=None, help="output dir (default: <root>/wiki-out)")
    p.add_argument("--no-cache", action="store_true", help="bypass the parse cache")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="qappswiki", description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)

    pv = sub.add_parser("validate", help="validate pages against frontmatter-v0")
    _add_common(pv)
    pv.add_argument("--strict", action="store_true", help="treat warnings as failures")
    pv.add_argument("--format", choices=["text", "json"], default="text")
    pv.add_argument("--dirs", default=None, help="comma-separated top-level dirs to scan")
    pv.set_defaults(func=cmd_validate)

    pb = sub.add_parser("build", help="build graph.json + graph.html")
    _add_common(pb)
    pb.set_defaults(func=cmd_build)

    pr = sub.add_parser("report", help="write GRAPH_REPORT.md")
    _add_common(pr)
    pr.set_defaults(func=cmd_report)

    pn = sub.add_parser("run", help="validate + build + report (combined)")
    _add_common(pn)
    pn.add_argument("--strict", action="store_true")
    pn.add_argument("--no-html", action="store_true")
    pn.add_argument("--log", action="store_true", help="print a log.md entry line")
    pn.set_defaults(func=cmd_run)

    ps = sub.add_parser("serve", help="MCP stdio server over graph.json")
    _add_common(ps)
    ps.add_argument("--graph", default=None, help="path to graph.json")
    ps.set_defaults(func=cmd_serve)

    pq = sub.add_parser("query", help="find nodes matching a term")
    _add_common(pq)
    pq.add_argument("term")
    pq.set_defaults(func=cmd_query)

    pp = sub.add_parser("path", help="shortest path between two pages")
    _add_common(pp)
    pp.add_argument("source")
    pp.add_argument("target")
    pp.set_defaults(func=cmd_path)

    pe = sub.add_parser("explain", help="describe a node and its edges")
    _add_common(pe)
    pe.add_argument("node")
    pe.set_defaults(func=cmd_explain)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
