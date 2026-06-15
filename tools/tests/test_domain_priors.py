"""Quantum-domain specialization: typed-edge vocabulary + extraction priors."""

from qappswiki import edges, extract, schema, validate
from qappswiki.parse import parse_page


def _page(tmp_path, rel, text):
    p = tmp_path / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    node, meta = parse_page(
        {"path": str(p), "rel_path": rel, "node_id": rel[:-3]}, tmp_path, cache=None
    )
    return {"node": node, "meta": meta}


def test_quantum_relations_in_vocabulary():
    for rel in ("wraps", "encodes-qec", "validates-against"):
        assert rel in schema.EDGE_RELATIONS


def test_authored_quantum_relation_validates(tmp_path):
    # An authored edges: block using a new quantum relation must NOT be flagged
    # invalid-edge-relation.
    a = _page(tmp_path, "packages/a.md", """---
type: package
name: A
status: active
updated: 2026-01-01
package_role: library
capabilities: [simulation]
hardware_targets: [local-cpu]
interfaces: [python-api]
domains: [quantum-software]
sources: []
provenance_status: source-backed
edges:
  - target: packages/b
    relation: wraps
---
# A
""")
    from qappswiki import build
    edge_list, synth = edges.derive_edges([a], tmp_path)
    graph = build.build_graph([a["node"]], edge_list, synth)
    findings = validate.validate([a], graph, tmp_path)
    assert not any(f["code"] == "invalid-edge-relation" for f in findings)
    assert any(e["relation"] == "wraps" for e in edge_list)


def test_benchmark_link_derives_validates_against(tmp_path):
    bench = _page(tmp_path, "benchmark/speed.md", """---
type: benchmark
status: provisional
updated: 2026-01-01
benchmark_kind: performance-dataset
packages: []
workflows: []
metrics: []
hardware_targets: [local-cpu]
sources: []
provenance_status: source-backed
---
# Speed
Measures [[packages/sim]].
""")
    sim = _page(tmp_path, "packages/sim.md", """---
type: package
name: Sim
status: active
updated: 2026-01-01
package_role: simulator
capabilities: [simulation]
hardware_targets: [local-cpu]
interfaces: [python-api]
domains: [quantum-software]
sources: []
provenance_status: source-backed
---
# Sim
""")
    edge_list, _ = edges.derive_edges([bench, sim], tmp_path)
    assert any(e["source"] == "benchmark/speed" and e["target"] == "packages/sim"
               and e["relation"] == "validates-against" for e in edge_list)


def test_lexicon_priors_extended_beyond_time_evolution():
    text = ("# Paper\nWe study lattice surgery and magic state distillation on a "
            "surface code, with randomized benchmarking and tensor network methods.")
    result = extract.extract_source("raw/md/p.md", text)
    titles = {n["title"] for n in result["candidates"]["nodes"]}
    assert {"Lattice Surgery", "Magic State Distillation", "Randomized Benchmarking",
            "Tensor Network Methods"} <= titles


def test_llm_prompt_ships_quantum_relations():
    prompt = extract.build_prompt("raw/md/p.md", "text")
    assert "validates-against" in prompt and "encodes-qec" in prompt
