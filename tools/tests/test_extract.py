import json

from qappswiki import extract

_PAPER = """# Generalized Trotter Formula and Systematic Approximants

**Abstract.** We study Trotterization and product-formula approximants for
Hamiltonian simulation and real-time evolution. See also arXiv:1811.08017.

### 1. Introduction
Background only.

### 2. Suzuki-Trotter Decomposition of Exponential Operators
The Suzuki decomposition generalizes Trotter's formula.

### 3. References
[1] doi:10.1007/BF01609348
"""


def test_extract_finds_lexicon_concepts():
    r = extract.extract_source("raw/md/suzuki.md", _PAPER)
    titles = {n["title"] for n in r["candidates"]["nodes"]}
    assert "Trotterization" in titles
    assert "Hamiltonian Simulation" in titles
    assert "Product Formula" in titles


def test_candidates_are_inferred_and_provenanced():
    r = extract.extract_source("raw/md/suzuki.md", _PAPER)
    for n in r["candidates"]["nodes"]:
        assert n["confidence"] in {"INFERRED", "AMBIGUOUS"}
        assert n["status"] == "provisional"
        assert n["provenance_status"] == "needs-verification"
        assert n["sources"] == ["raw/md/suzuki.md"]
        assert n["id"].startswith("concepts/")
        assert n["origin"].startswith("extracted")


def test_stop_headings_excluded():
    r = extract.extract_source("raw/md/suzuki.md", _PAPER)
    titles = {n["title"].lower() for n in r["candidates"]["nodes"]}
    assert "introduction" not in titles
    assert "references" not in titles


def test_extracts_references():
    r = extract.extract_source("raw/md/suzuki.md", _PAPER)
    assert "1811.08017" in r["references"]["arxiv"]
    assert any("BF01609348" in d for d in r["references"]["doi"])


def test_exists_flag_against_graph():
    # an authored concept already covering Trotterization
    existing = {"concepts/trotterization"}
    r = extract.extract_source("raw/md/suzuki.md", _PAPER, existing_ids=existing)
    trot = next(n for n in r["candidates"]["nodes"] if n["id"] == "concepts/trotterization")
    assert trot["exists"] is True
    other = next(n for n in r["candidates"]["nodes"] if n["id"] == "concepts/hamiltonian-simulation")
    assert other["exists"] is False


def test_title_from_h1():
    r = extract.extract_source("raw/md/suzuki.md", _PAPER)
    assert r["title"].startswith("Generalized Trotter Formula")


def test_deterministic_core_is_stable():
    a = extract.extract_source("raw/md/suzuki.md", _PAPER)
    b = extract.extract_source("raw/md/suzuki.md", _PAPER)
    assert a["candidates"]["nodes"] == b["candidates"]["nodes"]


def test_merge_corpus_accumulates_sources():
    r1 = extract.extract_source("raw/md/a.md", _PAPER)
    r2 = extract.extract_source("raw/md/b.md", _PAPER)
    merged = extract.merge_corpus([r1, r2])
    trot = next(n for n in merged["candidate_nodes"] if n["id"] == "concepts/trotterization")
    assert sorted(trot["sources"]) == ["raw/md/a.md", "raw/md/b.md"]
    assert merged["stats"]["multi_source"] >= 1
    # ranked by support, descending
    counts = [len(n["sources"]) for n in merged["candidate_nodes"]]
    assert counts == sorted(counts, reverse=True)


def test_llm_backend_merges_and_validates():
    def fake_backend(prompt):
        # asserts the schema priors are in the prompt
        assert "Allowed concept_kind" in prompt and "quantum-simulation" in prompt
        return json.dumps({
            "nodes": [
                {"title": "Qubitization", "concept_kind": "algorithm",
                 "domains": ["quantum-simulation"], "evidence": "discussed"},
                {"title": "Bogus", "concept_kind": "not-a-kind",
                 "domains": ["not-a-domain"], "evidence": "x"},
            ],
            "edges": [
                {"source_title": "Qubitization", "target_title": "Trotterization",
                 "relation": "related", "evidence": "compared"},
                {"source_title": "Qubitization", "target_title": "Trotterization",
                 "relation": "not-a-relation", "evidence": "still kept as related"},
            ],
        })

    r = extract.extract_source("raw/md/suzuki.md", _PAPER, backend=fake_backend)
    assert r["backend"] == "heuristic+llm"
    nodes = {n["id"]: n for n in r["candidates"]["nodes"]}
    assert "concepts/qubitization" in nodes
    # invalid concept_kind/domains scrubbed to safe defaults
    bogus = nodes["concepts/bogus"]
    assert bogus["concept_kind"] == "other" and bogus["domains"] == []
    # edges: invalid relation coerced to 'related'
    rels = {e["relation"] for e in r["candidates"]["edges"]
            if e["origin"] == "extracted:llm"}
    assert rels == {"related"}


def test_llm_bad_json_is_safe():
    r = extract.extract_source("raw/md/suzuki.md", _PAPER, backend=lambda p: "not json{")
    assert "backend_error" in r
    # deterministic candidates survive
    assert any(n["title"] == "Trotterization" for n in r["candidates"]["nodes"])


def test_extract_corpus_and_stage(tmp_path):
    raw = tmp_path / "raw" / "md"
    raw.mkdir(parents=True)
    (raw / "suzuki.md").write_text(_PAPER, encoding="utf-8")
    (raw / ".gitkeep").write_text("", encoding="utf-8")
    results = extract.extract_corpus(tmp_path)
    assert len(results) == 1
    assert results[0]["source"] == "raw/md/suzuki.md"
    p = extract.stage(results[0], tmp_path / "wiki-out")
    assert p.exists()
    data = json.loads(p.read_text())
    assert data["schema_version"] == extract.EXTRACT_SCHEMA_VERSION


def test_report_renders():
    r = extract.extract_source("raw/md/suzuki.md", _PAPER)
    merged = extract.merge_corpus([r])
    md = extract.render_extract_report([r], merged, "2026-01-01")
    assert "Extraction Report" in md and "candidate concepts" in md
