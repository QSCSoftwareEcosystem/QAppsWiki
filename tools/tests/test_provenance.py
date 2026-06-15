import json

from qappswiki import analyze, export, report, serve


def test_cite_marks_inline_source_claim_level(pipeline):
    # packages/widget cites raw/md/widget-docs.md inline (a specific claim),
    # so that source is claim-level (the stronger signal wins over frontmatter).
    r = serve.q_cite(pipeline["graph"], "packages/widget")
    assert r is not None
    assert any("widget-docs" in s for s in r["sources"])
    assert any("widget-docs" in s for s in r["claim_level"])
    assert "inline-citation" in {c["origin"] for c in r["cites"]}


def test_cite_unknown_node(pipeline):
    assert serve.q_cite(pipeline["graph"], "concepts/nope") is None


def test_cite_frontmatter_only_is_page_level(pipeline):
    # concepts/idea declares a source but never cites it inline -> page-level only
    r = serve.q_cite(pipeline["graph"], "concepts/idea")
    assert r["page_level"]
    assert r["claim_level"] == []
    # page_level + claim_level partition the full source set
    assert set(r["sources"]) == set(r["page_level"]) | set(r["claim_level"])


def test_cite_roundtrips_through_graph_json(pipeline, tmp_path):
    p = tmp_path / "graph.json"
    p.write_text(json.dumps(export.to_json(pipeline["graph"])))
    g = serve.load_graph(p)
    r = serve.q_cite(g, "packages/widget")
    # origin survives the json round-trip
    assert "inline-citation" in {c["origin"] for c in r["cites"]}


def test_coverage_metric_shape(pipeline):
    cov = analyze.analyze(pipeline["graph"])["provenance"]["coverage"]
    assert cov["content_pages"] >= 1
    assert 0.0 <= cov["source_coverage"] <= 1.0
    assert 0.0 <= cov["claim_coverage"] <= 1.0
    assert "by_status" in cov
    # widget has an inline citation -> at least one claim-level page
    assert cov["with_inline_citations"] >= 1


def test_coverage_counts_widget_sourced(pipeline):
    cov = analyze.analyze(pipeline["graph"])["provenance"]["coverage"]
    # widget cites a source, so it is not unsourced
    assert "packages/widget" not in cov["unsourced"]


def test_report_renders_coverage(pipeline):
    a = analyze.analyze(pipeline["graph"])
    md = report.render_graph_report(a, "2026-01-01")
    assert "Provenance coverage" in md
    assert "sourceable pages cite a source" in md
