"""Command-line interface and pipeline orchestration.

Subcommands:
  validate   collect -> parse -> build -> validate; write VALIDATION_REPORT.md
  build      ... -> export; write graph.json + graph.html
  report     ... -> analyze; write GRAPH_REPORT.md
  new        scaffold a blank schema-valid page of a given type (fill-in-the-blanks)
  extract    derive INFERRED candidate concepts from raw sources (staged, not authored)
  promote    turn a reviewed candidate into an authored concepts/ page (discover→promote)
  import-zoo import a community catalog (Error Correction Zoo / QEM Zoo) into concept pages
  cluster    detect + name thematic communities (Louvain)
  run        validate + build + report in one parse (the AS/CI entry point)
  serve      MCP stdio server over graph.json
  query/path/explain/cite   read-only graph queries (cite = provenance behind a node)
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import sys
from pathlib import Path

from . import analyze as _analyze
from . import build as _build
from . import cluster as _cluster
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
    # Stamp last-known freshness (offline: reads wiki-out/freshness.json if the
    # online `freshness` command has run; otherwise everything stays untracked).
    from . import freshness as _freshness
    _freshness.stamp_graph(graph, _freshness.load_cache(out))
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


def cmd_cluster(args):
    graph = _load_graph(args)
    result = _cluster.detect(graph, resolution=args.resolution)
    if args.format == "json":
        print(json.dumps(result, indent=2))
        return 0
    print(f"{result['count']} communities · modularity {result['modularity']}\n")
    for c in result["communities"]:
        doms = ", ".join(c["domains"]) or "—"
        print(f"  [{c['size']:>2}] {c['label']}  (hub: {c['god_node']}, cohesion {c['cohesion']})")
        print(f"       domains: {doms}")
        for m in c["members"]:
            print(f"         - {m}")
    return 0


def cmd_extract(args):
    from . import extract as _extract
    root = Path(args.root).resolve()
    out = _out_dir(args, root)
    _, graph = run_pipeline(root, out, not args.no_cache)
    # Resolve/relate candidates only against real *content* pages, so common
    # words in nav docs (CONTEXT, index, …) don't become spurious related links.
    from . import schema as _schema
    existing_ids = {n for n, a in graph.nodes(data=True) if _schema.is_content(a)}

    if args.source:
        src = Path(args.source)
        text = src.read_text(encoding="utf-8")
        source_id = src.resolve().relative_to(root).as_posix() if src.is_absolute() else args.source
        results = [_extract.extract_source(source_id, text, existing_ids)]
    else:
        results = _extract.extract_corpus(root, existing_ids=existing_ids)

    if not results:
        print("no raw sources found under raw/md/")
        return 0

    for r in results:
        _extract.stage(r, out)
    merged = _extract.merge_corpus(results)
    _write(out / "EXTRACT_REPORT.md", _extract.render_extract_report(results, merged, _today()))
    _write(out / "extract" / "candidates.json", json.dumps(merged, indent=2))

    if args.format == "json":
        print(json.dumps(merged, indent=2))
    else:
        s = merged["stats"]
        print(f"{len(results)} sources → {s['candidates']} distinct candidate concepts "
              f"({s['new']} new, {s['multi_source']} multi-source)")
        print(f"staged to {out}/extract/  ·  report: {out}/EXTRACT_REPORT.md")
        print("\ntop candidates by source support:")
        for n in merged["candidate_nodes"][:10]:
            tag = "exists" if n["exists"] else "NEW"
            print(f"  [{len(n['sources'])}x] {n['title']:<42} {n['concept_kind']:<14} {tag}")
    return 0


def cmd_promote(args):
    from . import promote as _promote
    root = Path(args.root).resolve()
    out = _out_dir(args, root)
    try:
        queue = _promote.load_queue(out)
    except _promote.PromoteError as exc:
        print(f"promote failed: {exc}")
        return 1

    if args.all:
        cands = _promote.select_batch(queue, min_sources=args.min_sources,
                                      kind=args.kind, include_existing=args.force)
        if not cands:
            print(f"no candidates with >= {args.min_sources} sources"
                  + (f" of kind '{args.kind}'" if args.kind else ""))
            return 0
    else:
        if not args.candidate:
            print("promote: give a candidate id/title, or use --all")
            return 1
        c = _promote.find_candidate(queue, args.candidate)
        if c is None:
            print(f"no candidate matches '{args.candidate}' "
                  f"(run `qappswiki extract` and check EXTRACT_REPORT.md)")
            return 1
        cands = [c]

    written, skipped = [], []
    for c in cands:
        try:
            written.append(_promote.promote_one(root, c, force=args.force, dry_run=args.dry_run))
        except _promote.PromoteError as exc:
            skipped.append((c["id"], str(exc)))

    verb = "would promote" if args.dry_run else "promoted"
    for r in written:
        print(f"  {verb}: {r['path']}  ({r['sources']} sources)")
    for cid, why in skipped:
        print(f"  skipped: {cid} — {why}")
    if written and not args.dry_run:
        print(f"\n{len(written)} page(s) written. Author the stubs, then run `qappswiki run`.")
    return 0


def cmd_new(args):
    from . import scaffold
    from . import schema as _schema
    root = Path(args.root).resolve()
    page_type = args.type
    if page_type not in _schema.CONTENT_TYPES:
        print(f"unknown page type: '{page_type}' — choose one of "
              f"{', '.join(sorted(_schema.CONTENT_TYPES))}")
        return 1
    # Bare slug -> conventional directory for the type; a path (has '/' or .md)
    # is used as given.
    target = args.target
    if target.endswith(".md") or "/" in target:
        rel = target if target.endswith(".md") else target + ".md"
    else:
        rel = f"{scaffold.TYPE_DIR.get(page_type, page_type)}/{target}.md"
    path = root / rel
    if path.exists() and not args.force:
        print(f"refusing to overwrite existing page {rel} (use --force)")
        return 1
    content = scaffold.blank_page(page_type, path.stem, args.title)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"created {page_type} stub: {rel}")
    print("\nnext: fill in the frontmatter + body, then run `qappswiki run`.")
    return 0


def cmd_ingest(args):
    from . import ingest as _ingest
    root = Path(args.root).resolve()
    try:
        result = _ingest.ingest(
            args.pdf, root, page_type=args.type, name=args.name, title=args.title,
            converter=args.converter, keep_pdf=not args.no_keep_pdf, force=args.force,
        )
    except _ingest.IngestError as exc:
        print(f"ingest failed: {exc}")
        return 1
    print(f"converted with {result['converter']}:")
    print(f"  markdown : {result['markdown']}")
    if result["pdf"]:
        print(f"  archived : {result['pdf']}")
    print(f"  stub page: {result['page']}")
    print("\nnext: compile claims into the stub, then run `qappswiki run`.")
    print("source-inventory row to paste into raw/source-inventory.md:")
    print(f"  {result['inventory_row']}")
    return 0


def cmd_import_zoo(args):
    """Import a community catalog (Error Correction Zoo / QEM Zoo) into pages."""
    from . import import_zoo as _iz
    root = Path(args.root).resolve()
    source = args.source
    today = _today()
    cache = str(root / _iz.DEFAULT_CACHE)       # clone lives under the wiki root
    try:
        if source == "eczoo":
            # explicit ids > flagship set > whole catalog (--all)
            ids = args.ids or (None if args.all else list(_iz.ECZ_FLAGSHIP))
            entries = _iz.fetch_eczoo(ids, cache, refresh=args.refresh)
            batch = frozenset(_iz._slug(e["code_id"]) for e in entries)
            rendered = [(*_iz.eczoo_page(e, today, batch), _iz.tex_to_md(e.get("name") or e["code_id"]))
                        for e in entries]
        else:  # qemzoo
            ids = args.ids or None                          # default: all techniques
            entries, refs = _iz.fetch_qemzoo(ids, cache, refresh=args.refresh)
            batch = frozenset(_iz._slug(e["id"]) for e in entries)
            rendered = [(*_iz.qemzoo_page(e, refs, today, batch), e.get("name") or e["id"])
                        for e in entries]
    except _iz.ImportError_ as exc:
        print(f"import failed: {exc}")
        return 1

    if args.dry_run:
        for rel_path, _md, title in rendered:
            print(f"  would write {rel_path}  ({title})")
        print(f"\n{len(rendered)} page(s) from {source} (dry run; nothing written)")
        return 0

    results = _iz.write_pages(root, source, [(rp, md, t) for rp, md, t in rendered],
                              force=args.force)
    titles = [(rp[:-3], t) for rp, _md, t in rendered]      # node id = path without .md
    _iz.update_index(root, source, titles)
    print(f"imported {len(results)} page(s) from {source} into "
          f"{_iz.OUT_DIR[source]}/ and linked them from index.md")
    print(f"attribution: {_iz.ATTRIBUTION[source]}")
    print("\nnext: run `qappswiki run` to validate, then verify/enrich the "
          "`needs-verification` pages.")
    return 0


def cmd_freshness(args):
    from . import freshness as _freshness
    root = Path(args.root).resolve()
    out = _out_dir(args, root)
    pages, _ = run_pipeline(root, out, not args.no_cache)
    results = _freshness.run_freshness(pages, timeout=args.timeout, only=args.package)
    _write(out / "FRESHNESS_REPORT.md", _report.render_freshness_report(results, _today()))
    # Persist verdicts so the next build can stamp them onto the graph (and roll
    # software staleness up to integrations/applications). A single-package run
    # merges into the existing cache rather than dropping the others.
    if not args.package:
        _freshness.save_cache(out, results)
    else:
        merged = dict(_freshness.load_cache(out))
        for r in results:
            merged[r["page"]] = {"status": r["status"], "latest": r["latest"],
                                 "built": r["built"], "detail": r["detail"]}
        _freshness.save_cache(out, [{"page": k, **v} for k, v in merged.items()])
    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            src = f"{r['kind']}:{r['id']}" if r["kind"] else "-"
            print(f"  {r['status']:>9}  {r['page']:<32} built={r['built'] or '-':<8} "
                  f"latest={r['latest'] or '-':<8} {src}")
        n_stale = sum(r["status"] == "stale" for r in results)
        print(f"\n{len(results)} package contexts checked; {n_stale} stale")
    if args.fail_on_stale and any(r["status"] == "stale" for r in results):
        return 1
    return 0


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


def cmd_cite(args):
    from . import serve
    graph = _load_graph(args)
    result = serve.q_cite(graph, args.node)
    if result is None:
        print(f"unknown node: {args.node}")
        return 1
    if args.format == "json":
        print(json.dumps(result, indent=2))
        return 0
    print(f"# {result['id']}  ({result.get('title')})")
    print(f"provenance_status: {result.get('provenance_status')}")
    print(f"\npage-level sources ({len(result['page_level'])}):")
    for s in result["page_level"]:
        print(f"  - {s}")
    print(f"claim-level inline citations ({len(result['claim_level'])}):")
    for s in result["claim_level"]:
        print(f"  - {s}")
    if not result["cites"]:
        print("  (no sources cited — provenance gap)")
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

    px = sub.add_parser("extract", help="extract INFERRED candidate concepts from raw sources (staged for review)")
    _add_common(px)
    px.add_argument("source", nargs="?", default=None,
                    help="a single raw source file (default: all of raw/md/)")
    px.add_argument("--format", choices=["text", "json"], default="text")
    px.set_defaults(func=cmd_extract)

    pmp = sub.add_parser("promote", help="promote a reviewed candidate into an authored concepts/ page")
    _add_common(pmp)
    pmp.add_argument("candidate", nargs="?", default=None, help="candidate id, slug, or title")
    pmp.add_argument("--all", action="store_true", help="promote every candidate above --min-sources")
    pmp.add_argument("--min-sources", type=int, default=2, help="min supporting sources for --all (default 2)")
    pmp.add_argument("--kind", default=None, help="restrict --all to one concept_kind")
    pmp.add_argument("--force", action="store_true", help="overwrite an existing page")
    pmp.add_argument("--dry-run", action="store_true", help="show what would be written, write nothing")
    pmp.set_defaults(func=cmd_promote)

    pc = sub.add_parser("cluster", help="detect + name thematic communities")
    _add_common(pc)
    pc.add_argument("--resolution", type=float, default=1.0,
                    help="Louvain resolution; >1 = more, smaller communities")
    pc.add_argument("--format", choices=["text", "json"], default="text")
    pc.set_defaults(func=cmd_cluster)

    pnew = sub.add_parser("new", help="scaffold a blank schema-valid page to fill in")
    pnew.add_argument("--root", default=str(_default_root()), help="wiki root (default: parent of tools/)")
    pnew.add_argument("type", help="page type (package|concept|how-to|integration|workflow|qec-artifact|benchmark|source)")
    pnew.add_argument("target", help="slug (placed in the type's dir) or an explicit path like packages/qiskit.md")
    pnew.add_argument("--title", default=None, help="page title (default: humanized slug)")
    pnew.add_argument("--force", action="store_true", help="overwrite an existing page")
    pnew.set_defaults(func=cmd_new)

    pi = sub.add_parser("ingest", help="convert a PDF and scaffold a stub page")
    _add_common(pi)
    pi.add_argument("pdf", help="path to the source PDF")
    pi.add_argument("--type", default="concept",
                    help="stub page type (package|concept|how-to|integration|source|...)")
    pi.add_argument("--name", default=None, help="slug override (default: PDF stem)")
    pi.add_argument("--title", default=None, help="page title")
    pi.add_argument("--converter", default=None,
                    help="converter command (default: $QAPPSWIKI_CONVERTER, lightpdf, mid)")
    pi.add_argument("--no-keep-pdf", action="store_true", help="don't archive the PDF to raw/pdf/")
    pi.add_argument("--force", action="store_true", help="overwrite an existing stub")
    pi.set_defaults(func=cmd_ingest)

    piz = sub.add_parser("import-zoo",
                         help="import a community catalog (Error Correction Zoo / QEM Zoo) into concept pages")
    piz.add_argument("--root", default=str(_default_root()), help="wiki root (default: parent of tools/)")
    piz.add_argument("source", choices=["eczoo", "qemzoo"], help="which catalog to import")
    piz.add_argument("ids", nargs="*", help="specific entry ids (default: eczoo=flagship set, qemzoo=all)")
    piz.add_argument("--all", action="store_true", help="eczoo: import the entire ~1100-code catalog")
    piz.add_argument("--refresh", action="store_true", help="git pull the local zoo clone before importing")
    piz.add_argument("--dry-run", action="store_true", help="show what would be written, write nothing")
    piz.add_argument("--force", action="store_true", help="overwrite existing imported pages")
    piz.set_defaults(func=cmd_import_zoo)

    pf = sub.add_parser("freshness", help="online: check package contexts against upstream versions")
    _add_common(pf)
    pf.add_argument("--package", default=None, help="check only this package (id or basename)")
    pf.add_argument("--format", choices=["text", "json"], default="text")
    pf.add_argument("--timeout", type=float, default=10.0, help="per-request timeout (seconds)")
    pf.add_argument("--fail-on-stale", action="store_true", help="exit non-zero if any package is stale")
    pf.set_defaults(func=cmd_freshness)

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

    pct = sub.add_parser("cite", help="show the sources behind a node (page- and claim-level)")
    _add_common(pct)
    pct.add_argument("node")
    pct.add_argument("--format", choices=["text", "json"], default="text")
    pct.set_defaults(func=cmd_cite)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
