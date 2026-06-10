"""Stage 6: render markdown reports from analysis + validation findings."""

from __future__ import annotations


def _kv_table(counter: dict, col: str) -> list[str]:
    if not counter:
        return ["_none_", ""]
    rows = ["| " + col + " | count |", "|---|---|"]
    for k, v in sorted(counter.items(), key=lambda x: (-x[1], str(x[0]))):
        rows.append(f"| {k} | {v} |")
    rows.append("")
    return rows


def render_graph_report(analysis: dict, generated: str = "") -> str:
    s = analysis["stats"]
    L: list[str] = []
    L.append("# QAppsWiki Graph Report")
    L.append("")
    if generated:
        L.append(f"_Generated: {generated}_")
        L.append("")
    L.append(
        f"**{s['nodes']} nodes · {s['edges']} edges.** "
        f"Confidence: " + ", ".join(f"{k}={v}" for k, v in sorted(s["by_confidence"].items()))
    )
    L.append("")

    L.append("## Nodes by type")
    L += _kv_table(s["by_type"], "type")
    L.append("## Pages by domain")
    L += _kv_table(s["by_domain"], "domain")

    L.append("## God nodes (most-connected pages)")
    if analysis["god_nodes"]:
        L.append("| page | degree |")
        L.append("|---|---|")
        for g in analysis["god_nodes"]:
            L.append(f"| [[{g['id']}]] | {g['degree']} |")
    else:
        L.append("_none_")
    L.append("")

    L.append("## Orphans (no link to/from another content page)")
    L += _bullets(f"[[{o}]]" for o in analysis["orphans"]) or ["_none_", ""]

    L.append("## Under-linked package pages")
    L += _bullets(f"[[{o}]]" for o in analysis["under_linked"]) or ["_none_", ""]

    L.append("## Surprising cross-domain edges")
    if analysis["cross_domain"]:
        for e in analysis["cross_domain"]:
            L.append(
                f"- [[{e['source']}]] —{e['relation']}→ [[{e['target']}]] "
                f"({'/'.join(e['source_domains'])} ✗ {'/'.join(e['target_domains'])})"
            )
        L.append("")
    else:
        L += ["_none_", ""]

    L.append("## AMBIGUOUS edges needing review")
    if analysis["ambiguous"]:
        for e in analysis["ambiguous"]:
            L.append(f"- [[{e['source']}]] —{e['relation']}→ `{e['target']}`  _(origin: {e['origin']})_")
        L.append("")
    else:
        L += ["_none_", ""]

    prov = analysis["provenance"]
    L.append("## Provenance gaps")
    L.append(f"- pages flagged `needs-verification`: {len(prov['needs_verification'])}")
    for n in prov["needs_verification"]:
        L.append(f"  - [[{n}]]")
    L.append(f"- `cites` edges to external (sibling-repo/URL) sources: {prov['external_cites']}")
    L.append("")
    return "\n".join(L)


def render_validation_report(findings: list[dict], generated: str = "") -> str:
    errors = [f for f in findings if f["level"] == "ERROR"]
    warnings = [f for f in findings if f["level"] == "WARNING"]
    L: list[str] = ["# QAppsWiki Validation Report", ""]
    if generated:
        L.append(f"_Generated: {generated}_")
        L.append("")
    L.append(f"**{len(errors)} errors · {len(warnings)} warnings.**")
    L.append("")
    for level, items in (("ERROR", errors), ("WARNING", warnings)):
        L.append(f"## {level}S ({len(items)})")
        if not items:
            L.append("_none_")
            L.append("")
            continue
        for f in items:
            L.append(f"- `{f['code']}` **[[{f['page']}]]** — {f['message']}")
        L.append("")
    return "\n".join(L)


_FRESH_ORDER = {"stale": 0, "error": 1, "unknown": 2, "manual": 3, "untracked": 4, "fresh": 5}


def render_freshness_report(results: list[dict], generated: str = "") -> str:
    from collections import Counter

    counts = Counter(r["status"] for r in results)
    L: list[str] = ["# QAppsWiki Freshness Report", ""]
    if generated:
        L.append(f"_Generated: {generated}_")
        L.append("")
    L.append(" · ".join(f"{k}: {v}" for k, v in sorted(counts.items())) or "_no package contexts_")
    L.append("")
    L.append("| package | built | scope | source | latest | status |")
    L.append("|---|---|---|---|---|---|")
    for r in sorted(results, key=lambda r: (_FRESH_ORDER.get(r["status"], 9), r["page"])):
        src = f"{r['kind']}:{r['id']}" if r["kind"] else "—"
        L.append(
            f"| [[{r['page']}]] | {r['built'] or '—'} | {r['scope'] or '—'} | "
            f"{src} | {r['latest'] or '—'} | **{r['status']}** |"
        )
    L.append("")
    stale = [r for r in results if r["status"] == "stale"]
    if stale:
        L.append("## Stale — flag an update")
        for r in stale:
            L.append(f"- [[{r['page']}]] — {r['detail']}")
        L.append("")
    return "\n".join(L)


def _bullets(items) -> list[str]:
    items = list(items)
    if not items:
        return []
    return [f"- {i}" for i in items] + [""]
