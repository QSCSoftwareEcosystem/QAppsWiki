"""Offline tests for the zoo importer (rendering is pure; no network)."""

from qappswiki import build, edges, import_zoo, validate
from qappswiki.parse import parse_page


def _validate_markdown(tmp_path, rel_path, markdown):
    """Write rendered markdown and run it through parse + validate."""
    p = tmp_path / rel_path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(markdown, encoding="utf-8")
    node, meta = parse_page(
        {"path": str(p), "rel_path": rel_path, "node_id": rel_path[:-3]},
        tmp_path, cache=None)
    return {"node": node, "meta": meta}


ECZ_ENTRY = {
    "code_id": "surface",
    "name": "Surface code",
    "alternative_names": ["Kitaev surface code", r"\(\mathbb{Z}_2\) surface code"],
    "description": (
        "A family of stabilizer codes defined on a 2D lattice "
        r"\cite{arxiv:quant-ph/9707021,doi:10.1063/1.1499754}. See the "
        r"\href{https://example.org/x}{tutorial} for details."),
    "protection": "Distance is the shortest non-contractible cycle.",
    "features": {"decoders": ["MWPM decoder.", "Union-find decoder."]},
    "realizations": ["Demonstrated on superconducting qubits."],
    "relations": {"parents": [{"code_id": "css"}],
                  "cousins": [{"code_id": "color", "detail": "related by unfolding"}]},
    "notes": ["A note."],
}

QEM_ENTRY = {
    "id": "zne", "name": "Zero-Noise Extrapolation", "abbreviation": "ZNE",
    "aliases": ["digital ZNE"], "category": "mitigation",
    "summary": "Run the circuit at amplified noise, then extrapolate to zero noise.",
    "properties": {"Bias": "Depends on the extrapolation model",
                   "Sampling overhead": "Moderate"},
    "references": ["giurgica2020", "missingkey"],
    "related": [{"id": "pec", "reason": "both reduce noise bias"},
                {"id": "cdr", "reason": "vnCDR combines the two"}],
}

QEM_REFS = {
    "giurgica2020": {"authors": "T. Giurgica-Tiron et al.",
                     "title": "Digital Zero Noise Extrapolation",
                     "journal": "QCE", "year": 2020, "arxiv": "2005.10921",
                     "doi": "10.1109/X"},
}


def test_tex_to_md_converts_cite_href_and_math():
    out = import_zoo.tex_to_md(
        r"State \(|\psi\rangle\) \cite{arxiv:2005.10921} \href{http://a.b}{link}")
    assert "$|\\psi\\rangle$" in out
    assert "[arXiv:2005.10921](https://arxiv.org/abs/2005.10921)" in out
    assert "[link](http://a.b)" in out
    assert "\\cite" not in out and "\\href" not in out


def test_tex_to_md_handles_cite_note_hyperref_and_figure():
    out = import_zoo.tex_to_md(
        r"A \cite[Fig. 3]{arxiv:1234.5678} code; see the "
        r"\hyperref[topic:clifford]{Clifford group}."
        r"\begin{figure}\includegraphics{x}\end{figure}")
    assert "[arXiv:1234.5678](https://arxiv.org/abs/1234.5678)" in out
    assert "Clifford group" in out and "\\hyperref" not in out
    assert "\\begin{figure}" not in out and "includegraphics" not in out


def test_tex_to_md_guards_stabilizer_bracket_against_wikilink():
    # \([[7,1,3]]\) must not survive as a [[wikilink]] (would be a broken link)
    out = import_zoo.tex_to_md(r"The \([[7,1,3]]\) Steane code")
    assert "[[" not in out and "]]" not in out
    assert "⟦7,1,3⟧" in out


def test_eczoo_page_renders_valid_concept(tmp_path):
    rel_path, md = import_zoo.eczoo_page(ECZ_ENTRY, "2026-06-15")
    assert rel_path == "concepts/qec/surface.md"
    assert "concept_kind: qec" in md
    assert "imported_from: error-correction-zoo" in md
    assert "CC-BY-SA" in md
    # cousin not in batch -> external link; no broken wikilink
    assert "errorcorrectionzoo.org/c/color" in md
    assert "[[" not in md  # nothing in batch -> no internal wikilinks

    # the rendered description cites the source page, which must be declared
    (tmp_path / import_zoo.SOURCE_PAGE["eczoo"]).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / import_zoo.SOURCE_PAGE["eczoo"]).write_text("x", encoding="utf-8")
    page = _validate_markdown(tmp_path, rel_path, md)
    edge_list, synth = edges.derive_edges([page], tmp_path)
    graph = build.build_graph([page["node"]], edge_list, synth)
    findings = validate.validate([page], graph, tmp_path)
    errors = [f for f in findings if f["level"] == "ERROR"]
    assert not errors, errors


def test_eczoo_batch_wikilinks_resolve(tmp_path):
    # css is in the batch -> the parent relation becomes an internal wikilink
    batch = frozenset({"surface", "css"})
    _rel, md = import_zoo.eczoo_page(ECZ_ENTRY, "2026-06-15", batch)
    assert "[[concepts/qec/css]]" in md
    assert "concepts/qec/css" in md  # also in related_concepts frontmatter


def test_qemzoo_page_renders_valid_concept(tmp_path):
    rel_path, md = import_zoo.qemzoo_page(QEM_ENTRY, QEM_REFS, "2026-06-15")
    assert rel_path == "concepts/qem/zne.md"
    assert "imported_from: qem-zoo" in md
    assert "The Unlicense" in md
    assert "| Bias |" in md                      # properties table
    assert "[arXiv:2005.10921]" in md            # resolved reference
    assert "reference not found" in md           # missing key handled gracefully
    assert "qemzoo.com/technique.html?id=pec" in md  # related, not in batch

    (tmp_path / import_zoo.SOURCE_PAGE["qemzoo"]).parent.mkdir(parents=True, exist_ok=True)
    (tmp_path / import_zoo.SOURCE_PAGE["qemzoo"]).write_text("x", encoding="utf-8")
    page = _validate_markdown(tmp_path, rel_path, md)
    edge_list, synth = edges.derive_edges([page], tmp_path)
    graph = build.build_graph([page["node"]], edge_list, synth)
    findings = validate.validate([page], graph, tmp_path)
    errors = [f for f in findings if f["level"] == "ERROR"]
    assert not errors, errors


def test_update_index_is_idempotent(tmp_path):
    (tmp_path / "index.md").write_text(
        "---\ntype: index\nstatus: active\nupdated: 2026-06-15\n---\n\n# Index\n",
        encoding="utf-8")
    import_zoo.update_index(tmp_path, "qemzoo", [("concepts/qem/zne", "ZNE")])
    once = (tmp_path / "index.md").read_text(encoding="utf-8")
    import_zoo.update_index(tmp_path, "qemzoo", [("concepts/qem/zne", "ZNE")])
    twice = (tmp_path / "index.md").read_text(encoding="utf-8")
    assert once == twice                          # managed block replaced, not duplicated
    assert twice.count("[[concepts/qem/zne]]") == 1


def test_update_index_handles_latex_titles(tmp_path):
    # Titles carry LaTeX (e.g. \mathbb) — these must not be parsed as regex
    # replacement escapes when the managed block is rewritten in place.
    idx = tmp_path / "index.md"
    idx.write_text("# Index\n", encoding="utf-8")
    titles = [("concepts/qec/qudit-surface", r"$\mathbb{Z}_q$ surface code")]
    import_zoo.update_index(tmp_path, "eczoo", titles)
    import_zoo.update_index(tmp_path, "eczoo", titles)   # second pass = the in-place rewrite
    out = idx.read_text(encoding="utf-8")
    assert r"$\mathbb{Z}_q$ surface code" in out
    assert out.count("[[concepts/qec/qudit-surface]]") == 1
