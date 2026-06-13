import json

import pytest
import yaml

from qappswiki import cli, extract, promote, validate


def _candidate(**over):
    base = {
        "id": "concepts/trotterization",
        "type": "concept",
        "title": "Trotterization",
        "concept_kind": "algorithm",
        "domains": ["quantum-simulation"],
        "status": "provisional",
        "provenance_status": "needs-verification",
        "sources": ["raw/md/a.md", "raw/md/b.md"],
        "confidence": "INFERRED",
        "origin": "extracted:heuristic",
        "evidence": "term matched",
        "exists": False,
        "related": ["concepts/idea"],
    }
    base.update(over)
    return base


def test_build_frontmatter_is_schema_complete():
    fm = promote.build_frontmatter(_candidate(), today="2026-06-13")
    from qappswiki import schema
    for field in schema.required_fields("concept"):
        assert field in fm
    assert fm["type"] == "concept"
    assert fm["status"] == "draft"
    assert fm["provenance_status"] == "needs-verification"
    assert fm["sources"] == ["raw/md/a.md", "raw/md/b.md"]
    assert fm["concept_kind"] == "algorithm"


def test_build_frontmatter_scrubs_bad_vocab():
    fm = promote.build_frontmatter(_candidate(concept_kind="nope", domains=["bad", "quantum-simulation"]))
    assert fm["concept_kind"] == "other"
    assert fm["domains"] == ["quantum-simulation"]


def test_build_page_has_frontmatter_and_sources():
    page = promote.build_page(_candidate(), today="2026-06-13")
    assert page.startswith("---\n")
    fm = yaml.safe_load(page.split("---")[1])
    assert fm["name"] == "Trotterization"
    assert "raw/md/a.md" in page and "raw/md/b.md" in page
    assert "[[concepts/idea]]" in page  # related link


def test_find_candidate_by_id_slug_title():
    queue = {"candidate_nodes": [_candidate()]}
    assert promote.find_candidate(queue, "concepts/trotterization")
    assert promote.find_candidate(queue, "trotterization")
    assert promote.find_candidate(queue, "Trotterization")
    assert promote.find_candidate(queue, "no-such") is None


def test_load_queue_missing(tmp_path):
    with pytest.raises(promote.PromoteError):
        promote.load_queue(tmp_path / "wiki-out")


def test_promote_one_writes_file(tmp_path):
    res = promote.promote_one(tmp_path, _candidate(), today="2026-06-13")
    assert res["written"] is True
    f = tmp_path / "concepts" / "trotterization.md"
    assert f.exists()
    assert res["path"] == "concepts/trotterization.md"


def test_promote_dry_run_writes_nothing(tmp_path):
    res = promote.promote_one(tmp_path, _candidate(), dry_run=True)
    assert res["written"] is False
    assert not (tmp_path / "concepts" / "trotterization.md").exists()


def test_promote_refuses_existing(tmp_path):
    promote.promote_one(tmp_path, _candidate())
    with pytest.raises(promote.PromoteError):
        promote.promote_one(tmp_path, _candidate())
    # force overwrites
    promote.promote_one(tmp_path, _candidate(), force=True)


def test_promote_refuses_when_candidate_exists(tmp_path):
    with pytest.raises(promote.PromoteError):
        promote.promote_one(tmp_path, _candidate(exists=True))


def test_select_batch_filters():
    queue = {"candidate_nodes": [
        _candidate(id="concepts/a", title="A", sources=["raw/md/1.md", "raw/md/2.md", "raw/md/3.md"]),
        _candidate(id="concepts/b", title="B", sources=["raw/md/1.md"]),  # too few
        _candidate(id="concepts/c", title="C", concept_kind="capability",
                   sources=["raw/md/1.md", "raw/md/2.md"]),
        _candidate(id="concepts/d", title="D", exists=True,
                   sources=["raw/md/1.md", "raw/md/2.md"]),  # already authored
    ]}
    picked = promote.select_batch(queue, min_sources=2)
    ids = [n["id"] for n in picked]
    assert ids == ["concepts/a", "concepts/c"]  # b too few, d exists; ranked by support
    # kind filter
    assert [n["id"] for n in promote.select_batch(queue, min_sources=2, kind="capability")] == ["concepts/c"]


def test_promoted_page_passes_validation(tmp_wiki):
    """The crucial round-trip: a promoted stub is structurally valid (no errors)."""
    cand = _candidate(id="concepts/trotterization", title="Trotterization",
                      sources=["raw/md/widget-docs.md"], related=["packages/widget"])
    promote.promote_one(tmp_wiki, cand, today="2026-06-13")
    out = tmp_wiki / "wiki-out"
    pages, graph = cli.run_pipeline(tmp_wiki, out, use_cache=False)
    findings = validate.validate(pages, graph, tmp_wiki)
    errors = [f for f in findings if f["level"] == "ERROR"
              and f["page"] == "concepts/trotterization"]
    assert errors == []
    # and it is now a real node in the graph, linked (not an orphan)
    assert "concepts/trotterization" in graph
    assert graph.degree("concepts/trotterization") > 0


def test_end_to_end_extract_then_promote(tmp_path):
    """extract → stage candidates.json → promote from the queue."""
    raw = tmp_path / "raw" / "md"
    raw.mkdir(parents=True)
    (raw / "paper.md").write_text(
        "# Trotter paper\nWe study Trotterization and Hamiltonian simulation.\n",
        encoding="utf-8")
    results = extract.extract_corpus(tmp_path)
    merged = extract.merge_corpus(results)
    out = tmp_path / "wiki-out" / "extract"
    out.mkdir(parents=True)
    (out / "candidates.json").write_text(json.dumps(merged), encoding="utf-8")

    queue = promote.load_queue(tmp_path / "wiki-out")
    cand = promote.find_candidate(queue, "Trotterization")
    assert cand is not None
    res = promote.promote_one(tmp_path, cand, today="2026-06-13")
    assert res["written"]
    page = (tmp_path / "concepts" / "trotterization.md").read_text()
    assert "raw/md/paper.md" in page  # provenance carried through
