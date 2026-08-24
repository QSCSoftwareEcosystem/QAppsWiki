from qappswiki.search import Section, split_sections

PAGE = """---
type: concept
name: Steane code
domains:
- quantum-error-correction
sources:
- https://errorcorrectionzoo.org/c/steane
provenance_status: needs-verification
---

# Steane code

> Imported from the Error Correction Zoo. Text reused under CC-BY-SA.

## Description

The [[7,1,3]] CSS code built from the Hamming code.

## Protection

Corrects one arbitrary single-qubit error.
"""


def test_splits_on_h2_and_carries_frontmatter():
    secs = split_sections(PAGE, rel_path="concepts/qec/steane.md", node_id="concepts/qec/steane")
    headings = [s.heading for s in secs]
    assert headings == ["(intro)", "Description", "Protection"]
    body = {s.heading: s.text for s in secs}
    assert "CSS code built from the Hamming code" in body["Description"]
    assert "single-qubit error" in body["Protection"]
    for s in secs:
        assert s.title == "Steane code"
        assert s.provenance_status == "needs-verification"
        assert s.sources == ("https://errorcorrectionzoo.org/c/steane",)
        assert s.domains == ("quantum-error-correction",)
        assert s.node_id == "concepts/qec/steane"


def test_intro_section_dropped_when_only_a_title():
    secs = split_sections("---\nname: X\n---\n\n# X\n\n## Body\n\ntext\n", rel_path="a.md", node_id="a")
    assert [s.heading for s in secs] == ["Body"]


def test_page_without_frontmatter_still_splits():
    secs = split_sections("## Only\n\nbody text\n", rel_path="a.md", node_id="a")
    assert len(secs) == 1
    assert secs[0].title == "a"            # falls back to node_id
    assert secs[0].provenance_status == ""
    assert secs[0].sources == ()


def test_section_is_hashable_and_frozen():
    s = split_sections(PAGE, rel_path="p.md", node_id="p")[0]
    assert isinstance(s, Section)
    hash(s)  # tuples, not lists, so sections can go in sets
