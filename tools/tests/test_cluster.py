import json

from qappswiki import analyze, cluster, export, report, serve


def test_detect_basic_shape(pipeline):
    r = cluster.detect(pipeline["graph"])
    assert r["count"] == len(r["communities"]) >= 1
    # every content node is assigned exactly one community
    assert all(isinstance(v, int) for v in r["assignment"].values())
    # the connected widget cluster lands together
    a = r["assignment"]
    assert a["packages/widget"] == a["concepts/idea"] == a["how-to/use-widget"]


def test_synthetic_nodes_excluded(pipeline):
    r = cluster.detect(pipeline["graph"])
    # ghost is a synthetic missing node -> never clustered
    assert "packages/ghost" not in r["assignment"]


def test_orphan_is_its_own_community(pipeline):
    r = cluster.detect(pipeline["graph"])
    a = r["assignment"]
    assert a["packages/lonely-pkg"] != a["packages/widget"]


def test_deterministic(pipeline):
    a = cluster.detect(pipeline["graph"])
    b = cluster.detect(pipeline["graph"])
    assert a["assignment"] == b["assignment"]
    assert a["modularity"] == b["modularity"]


def test_community_fields(pipeline):
    r = cluster.detect(pipeline["graph"])
    c = r["communities"][0]
    assert c["size"] == len(c["members"]) >= 1
    assert c["god_node"] in c["members"]
    assert 0.0 <= c["cohesion"] <= 1.0
    assert isinstance(c["label"], str) and c["label"]


def test_label_uses_dominant_domain(pipeline):
    r = cluster.detect(pipeline["graph"])
    widget_idx = r["assignment"]["packages/widget"]
    widget_comm = next(c for c in r["communities"] if c["index"] == widget_idx)
    # all those pages carry domains: [quantum-software]
    assert "quantum-software" in widget_comm["label"]


def test_apply_labels_seam(pipeline):
    r = cluster.detect(pipeline["graph"])
    cluster.apply_labels(r, {0: "Custom Name"})
    assert next(c for c in r["communities"] if c["index"] == 0)["label"] == "Custom Name"


def test_empty_graph():
    import networkx as nx
    r = cluster.detect(nx.MultiDiGraph())
    assert r == {"assignment": {}, "communities": [], "modularity": 0.0, "count": 0}


def test_analyze_embeds_communities(pipeline):
    a = analyze.analyze(pipeline["graph"])
    assert "communities" in a
    assert a["communities"]["count"] >= 1
    assert "modularity" in a["communities"]


def test_report_has_communities_section(pipeline):
    a = analyze.analyze(pipeline["graph"])
    md = report.render_graph_report(a, "2026-01-01")
    assert "Communities" in md


def test_export_stamps_community(pipeline):
    data = export.to_json(pipeline["graph"])
    assert data["stats"]["communities"] >= 1
    assert "communities" in data
    widget = next(n for n in data["nodes"] if n["id"] == "packages/widget")
    assert widget["community"] is not None
    assert widget["community_label"]
    # synthetic node carries no community
    ghost = next(n for n in data["nodes"] if n["id"] == "packages/ghost")
    assert ghost["community"] is None


def test_export_html_has_compound_communities(pipeline):
    html = export.to_html(pipeline["graph"], "2026-01-01")
    assert "iscommunity" in html
    assert "communities (modularity" in html


def test_serve_list_communities(pipeline, tmp_path):
    p = tmp_path / "graph.json"
    p.write_text(json.dumps(export.to_json(pipeline["graph"])))
    g = serve.load_graph(p)
    comms = serve.q_list_communities(g)
    assert comms and all("god_node" in c and "members" in c for c in comms)
    # widget cluster present
    assert any("packages/widget" in c["members"] for c in comms)
