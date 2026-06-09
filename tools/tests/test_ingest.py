"""Ingest: PDF conversion (via a fake converter) + schema-valid stub scaffolding."""

import os
import stat

import pytest

from qappswiki import ingest, scaffold, validate
from qappswiki.cli import run_pipeline


def _fake_converter(tmp_path):
    """A stand-in for lightpdf: writes a markdown file at the -o target."""
    script = tmp_path / "fakeconv.sh"
    script.write_text(
        "#!/usr/bin/env bash\n"
        'out=""\n'
        'while [ $# -gt 0 ]; do if [ "$1" = "-o" ]; then out="$2"; shift; fi; shift; done\n'
        'printf "# converted source\\n\\nbody\\n" > "$out"\n'
    )
    script.chmod(script.stat().st_mode | stat.S_IEXEC)
    return script


def test_slugify():
    assert ingest.slugify("OpenQEvo Trotter 2025.pdf") == "openqevo-trotter-2025.pdf"
    assert ingest.slugify("  weird//name  ") == "weird-name"


def test_resolve_converter_missing(monkeypatch):
    monkeypatch.delenv("QAPPSWIKI_CONVERTER", raising=False)
    monkeypatch.setattr(ingest.shutil, "which", lambda c: None)
    with pytest.raises(ingest.IngestError):
        ingest.resolve_converter("definitely-not-real-xyz")


@pytest.mark.parametrize("ptype", ["concept", "package", "how-to", "integration", "source"])
def test_stub_is_structurally_valid(tmp_wiki, ptype):
    # A scaffolded stub must not produce missing-required-field ERRORs.
    text = scaffold.stub_page(ptype, "demo-paper", "Demo Paper",
                              ["raw/pdf/demo-paper.pdf"], ["raw/md/demo-paper.md"], "lightpdf")
    target = {"concept": "concepts", "package": "packages", "how-to": "how-to",
              "integration": "integrations", "source": "raw"}[ptype]
    p = tmp_wiki / target / "demo-paper.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text, encoding="utf-8")
    out = tmp_wiki / "wiki-out"
    pages, graph = run_pipeline(tmp_wiki, out, use_cache=False)
    findings = validate.validate(pages, graph, tmp_wiki)
    errs = [f for f in findings if f["page"] == f"{target}/demo-paper"
            and f["code"] == "missing-required-field"]
    assert not errs, errs


def test_ingest_end_to_end(tmp_wiki, tmp_path):
    conv = _fake_converter(tmp_path)
    pdf = tmp_path / "paper.pdf"
    pdf.write_bytes(b"%PDF-1.4 fake")
    result = ingest.ingest(pdf, tmp_wiki, page_type="concept", converter=str(conv))
    assert (tmp_wiki / result["markdown"]).exists()
    assert (tmp_wiki / result["pdf"]).exists()
    page = tmp_wiki / result["page"]
    assert page.exists()
    # The converted markdown is referenced from the stub frontmatter.
    assert result["markdown"] in page.read_text()
    # Re-ingest without --force refuses to clobber.
    with pytest.raises(ingest.IngestError):
        ingest.ingest(pdf, tmp_wiki, page_type="concept", converter=str(conv))
