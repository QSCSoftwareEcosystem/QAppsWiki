def _edges(graph):
    return [(u, v, d["relation"], d["confidence"], d["origin"])
            for u, v, d in graph.edges(data=True)]


def test_wikilink_edge_extracted(pipeline):
    e = _edges(pipeline["graph"])
    assert ("packages/widget", "concepts/idea", "implements", "EXTRACTED", "wikilink") in e


def test_related_field_edge(pipeline):
    e = _edges(pipeline["graph"])
    # related_concepts: [idea] resolves to concepts/idea
    assert any(s == "packages/widget" and t == "concepts/idea" and o == "frontmatter:related_concepts"
               for s, t, _r, _c, o in e)


def test_packages_named_inferred_and_ambiguous(pipeline):
    e = _edges(pipeline["graph"])
    # Widget resolves -> INFERRED; Ghost does not -> AMBIGUOUS to missing node
    assert ("integrations/widget-to-thing", "packages/widget", "composes-with", "INFERRED", "frontmatter:packages") in e
    assert any(t == "packages/ghost" and c == "AMBIGUOUS" for _s, t, _r, c, _o in e)


def test_cites_edge_to_internal_source(pipeline):
    e = _edges(pipeline["graph"])
    assert any(r == "cites" for _s, _t, r, _c, _o in e)


def test_missing_and_external_synthetic_nodes(pipeline):
    g = pipeline["graph"]
    assert g.nodes["packages/ghost"]["type"] == "missing"
    assert g.nodes["packages/ghost"]["synthetic"] is True


def test_multigraph_parallel_relations(pipeline):
    # widget -> idea exists via both wikilink(implements) and related(related)
    g = pipeline["graph"]
    rels = {d["relation"] for _u, _v, d in g.out_edges("packages/widget", data=True)
            if _v == "concepts/idea"}
    assert {"implements", "related"} <= rels
