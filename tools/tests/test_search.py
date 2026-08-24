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


from qappswiki.search import Bm25Index, Hit, tokenize


def _sec(node_id, heading, text, domains=("quantum-error-correction",)):
    return Section(
        rel_path=f"{node_id}.md",
        node_id=node_id,
        title=node_id,
        heading=heading,
        text=text,
        provenance_status="needs-verification",
        sources=(),
        domains=domains,
    )


def test_tokenize_lowercases_and_drops_punctuation_and_single_chars():
    assert tokenize("Surface-code THRESHOLD, p=0.01!") == ["surface", "code", "threshold", "01"]


def test_ranks_the_section_that_is_actually_about_the_query_first():
    idx = Bm25Index([
        _sec("a", "Description", "The surface code is a topological stabilizer code."),
        _sec("b", "Description", "The repetition code protects against bit flips only."),
        _sec("c", "Protection", "Surface code threshold under depolarizing noise is about 1%."),
    ])
    hits = idx.search("surface code threshold", k=3)
    assert [h.section.node_id for h in hits][0] == "c"
    assert all(isinstance(h, Hit) for h in hits)
    assert hits[0].score > hits[-1].score


def test_k_limits_results_and_zero_score_hits_are_dropped():
    idx = Bm25Index([_sec("a", "D", "alpha beta"), _sec("b", "D", "gamma delta")])
    assert len(idx.search("alpha", k=5)) == 1        # only one section matches at all
    assert idx.search("nonexistent term", k=5) == []


def test_domain_filter_excludes_other_domains():
    idx = Bm25Index([
        _sec("a", "D", "mitigation of noise", domains=("quantum-error-mitigation",)),
        _sec("b", "D", "mitigation of noise", domains=("quantum-error-correction",)),
    ])
    hits = idx.search("mitigation noise", k=5, domain="quantum-error-correction")
    assert [h.section.node_id for h in hits] == ["b"]


def test_empty_index_and_empty_query_are_safe():
    assert Bm25Index([]).search("anything", k=5) == []
    idx = Bm25Index([_sec("a", "D", "text here")])
    assert idx.search("", k=5) == []


from pathlib import Path

from qappswiki.search import build_index

_PAGE_TMPL = """---
type: concept
name: {name}
domains:
- quantum-error-correction
sources: []
provenance_status: needs-verification
---

# {name}

## Description

{body}
"""


def _wiki(tmp_path: Path) -> Path:
    (tmp_path / "concepts" / "qec").mkdir(parents=True)
    (tmp_path / "concepts" / "qec" / "steane.md").write_text(
        _PAGE_TMPL.format(name="Steane code", body="A CSS code with distance three."),
        encoding="utf-8",
    )
    (tmp_path / "raw" / "md").mkdir(parents=True)
    (tmp_path / "raw" / "md" / "paper.md").write_text(
        _PAGE_TMPL.format(name="Some Paper", body="A CSS code with distance three."),
        encoding="utf-8",
    )
    return tmp_path


def test_build_index_reads_the_corpus_and_skips_raw_md(tmp_path):
    idx = build_index(_wiki(tmp_path), use_cache=False)
    hits = idx.search("CSS code distance", k=10)
    ids = {h.section.node_id for h in hits}
    assert "concepts/qec/steane" in ids
    assert not any(i.startswith("raw/md/") for i in ids)


def test_cache_round_trip_produces_identical_results(tmp_path):
    root = _wiki(tmp_path)
    out = tmp_path / "wiki-out"
    first = build_index(root, out_dir=out, use_cache=True)
    second = build_index(root, out_dir=out, use_cache=True)   # served from cache
    assert [(h.section.node_id, round(h.score, 6)) for h in first.search("CSS code", k=5)] == [
        (h.section.node_id, round(h.score, 6)) for h in second.search("CSS code", k=5)
    ]
    assert (out / "search" / "cache").is_dir()


def test_edited_page_invalidates_its_cache_entry(tmp_path):
    root = _wiki(tmp_path)
    out = tmp_path / "wiki-out"
    build_index(root, out_dir=out, use_cache=True)
    (root / "concepts" / "qec" / "steane.md").write_text(
        _PAGE_TMPL.format(name="Steane code", body="Now mentions toric lattices instead."),
        encoding="utf-8",
    )
    idx = build_index(root, out_dir=out, use_cache=True)
    assert idx.search("toric lattices", k=5)
    assert idx.search("distance three", k=5) == []


from qappswiki.serve import q_search_pages


def test_q_search_pages_returns_the_client_payload(tmp_path):
    idx = build_index(_wiki(tmp_path), use_cache=False)
    rows = q_search_pages(idx, "CSS code distance", k=3)
    assert rows, "expected at least one hit"
    row = rows[0]
    assert set(row) == {
        "path", "node_id", "title", "heading", "text",
        "score", "provenance_status", "sources", "url",
    }
    assert row["node_id"] == "concepts/qec/steane"
    assert row["url"] == (
        "https://github.com/QSCSoftwareEcosystem/QAppsWiki/blob/main/concepts/qec/steane.md"
    )
    assert isinstance(row["score"], float)
    assert isinstance(row["sources"], list)


def test_q_search_pages_is_json_serializable(tmp_path):
    import json
    idx = build_index(_wiki(tmp_path), use_cache=False)
    json.dumps(q_search_pages(idx, "CSS", k=2))  # must not raise


def test_q_search_pages_empty_query_returns_empty(tmp_path):
    idx = build_index(_wiki(tmp_path), use_cache=False)
    assert q_search_pages(idx, "", k=3) == []
