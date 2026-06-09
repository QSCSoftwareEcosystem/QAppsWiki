import json

from qappswiki import analyze, export, report, serve


def test_analyze_metrics(pipeline):
    a = analyze.analyze(pipeline["graph"])
    assert a["stats"]["nodes"] > 0
    # lonely-pkg has no content edges -> orphan
    assert "packages/lonely-pkg" in a["orphans"]
    # one AMBIGUOUS edge (Ghost) at least
    assert any(e["target"] == "packages/ghost" for e in a["ambiguous"])
    assert "AMBIGUOUS" in a["stats"]["by_confidence"]


def test_report_sections(pipeline):
    a = analyze.analyze(pipeline["graph"])
    md = report.render_graph_report(a, "2026-01-01")
    for header in ["God nodes", "Orphans", "AMBIGUOUS edges", "Provenance gaps"]:
        assert header in md


def test_validation_report_renders(pipeline):
    from qappswiki import validate
    findings = validate.validate(pipeline["pages"], pipeline["graph"], pipeline["root"])
    md = report.render_validation_report(findings, "2026-01-01")
    assert "ERRORS" in md and "WARNINGS" in md


def test_export_json_roundtrip(pipeline, tmp_path):
    data = export.to_json(pipeline["graph"], "2026-01-01")
    assert data["schema_version"] == "qappswiki-graph-0"
    assert data["stats"]["nodes"] == pipeline["graph"].number_of_nodes()
    p = tmp_path / "graph.json"
    p.write_text(json.dumps(data))
    g2 = serve.load_graph(p)
    assert g2.number_of_nodes() == pipeline["graph"].number_of_nodes()
    assert g2.number_of_edges() == pipeline["graph"].number_of_edges()


def test_export_html_self_contained(pipeline):
    html = export.to_html(pipeline["graph"], "2026-01-01")
    assert "cytoscape" in html
    assert "const elements =" in html


def test_serve_query_functions(pipeline, tmp_path):
    p = tmp_path / "graph.json"
    p.write_text(json.dumps(export.to_json(pipeline["graph"])))
    g = serve.load_graph(p)
    assert any(n["id"] == "packages/widget" for n in serve.q_query(g, "widget"))
    node = serve.q_get_node(g, "packages/widget")
    assert node and node["type"] == "package" and node["out_edges"]
    path = serve.q_shortest_path(g, "packages/widget", "concepts/idea")
    assert path["found"] and path["length"] >= 1
    assert "packages/lonely-pkg" in serve.q_list_orphans(g)
    assert isinstance(serve.q_graph_stats(g)["by_type"], dict)
