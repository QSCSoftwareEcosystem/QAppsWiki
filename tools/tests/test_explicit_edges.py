"""The optional `edges:` frontmatter extension (schema/frontmatter-v0.md)."""

from qappswiki import build, edges, validate
from qappswiki.parse import parse_page


def _page(tmp_path, rel, text):
    p = tmp_path / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    node, meta = parse_page(
        {"path": str(p), "rel_path": rel, "node_id": rel[:-3]}, tmp_path, cache=None
    )
    return {"node": node, "meta": meta}


def test_explicit_edge_is_emitted(tmp_path):
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
    relation: supersedes
    confidence: EXTRACTED
---
# A
""")
    b = _page(tmp_path, "packages/b.md", """---
type: package
name: B
status: active
updated: 2026-01-01
package_role: library
capabilities: [simulation]
hardware_targets: [local-cpu]
interfaces: [python-api]
domains: [quantum-software]
sources: []
provenance_status: source-backed
---
# B
""")
    pages = [a, b]
    edge_list, synth = edges.derive_edges(pages, tmp_path)
    assert any(e["source"] == "packages/a" and e["target"] == "packages/b"
               and e["relation"] == "supersedes" and e["origin"] == "explicit-edges"
               for e in edge_list)


def test_explicit_edge_bad_relation_flagged(tmp_path):
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
    relation: not-a-real-relation
---
# A
""")
    edge_list, synth = edges.derive_edges([a], tmp_path)
    graph = build.build_graph([a["node"]], edge_list, synth)
    findings = validate.validate([a], graph, tmp_path)
    assert any(f["code"] == "invalid-edge-relation" for f in findings)
