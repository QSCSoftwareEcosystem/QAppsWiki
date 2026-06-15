"""`qappswiki new` — the fill-in-the-blanks scaffold command."""

from pathlib import Path

import pytest

from qappswiki import cli, scaffold, schema, validate

# Every content type a contributor can scaffold, with the dir it lands in.
_TYPES = sorted(schema.CONTENT_TYPES)


@pytest.mark.parametrize("ptype", _TYPES)
def test_blank_page_has_no_missing_required_field(tmp_path, ptype):
    # A freshly scaffolded page must validate with no *missing*-field error;
    # empty required lists/strings are incompleteness warnings, not errors.
    (tmp_path / "raw" / "md").mkdir(parents=True)
    rel = f"{scaffold.TYPE_DIR[ptype]}/sample.md"
    path = tmp_path / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(scaffold.blank_page(ptype, "sample"), encoding="utf-8")

    pages, graph = cli.run_pipeline(tmp_path, tmp_path / "out", use_cache=False)
    findings = validate.validate(pages, graph, tmp_path)
    missing = [f for f in findings
               if f["code"] == "missing-required-field" and f["page"].endswith("sample")]
    assert missing == [], missing


def test_provisional_type_gets_provisional_status():
    fm_text = scaffold.blank_page("benchmark", "my-bench")
    assert "status: provisional" in fm_text


def test_new_infers_conventional_dir(tmp_path):
    rc = cli.main(["new", "package", "qiskit", "--root", str(tmp_path)])
    assert rc == 0
    assert (tmp_path / "packages" / "qiskit.md").exists()


def test_new_accepts_explicit_path(tmp_path):
    rc = cli.main(["new", "concept", "concepts/time-evolution.md", "--root", str(tmp_path)])
    assert rc == 0
    assert (tmp_path / "concepts" / "time-evolution.md").exists()


def test_new_refuses_overwrite_without_force(tmp_path):
    assert cli.main(["new", "package", "qiskit", "--root", str(tmp_path)]) == 0
    before = (tmp_path / "packages" / "qiskit.md").read_text()
    # second call without --force must not clobber
    assert cli.main(["new", "package", "qiskit", "--root", str(tmp_path)]) == 1
    assert (tmp_path / "packages" / "qiskit.md").read_text() == before
    # with --force it overwrites (and still returns 0)
    assert cli.main(["new", "package", "qiskit", "--force", "--root", str(tmp_path)]) == 0


def test_new_rejects_unknown_type(tmp_path):
    assert cli.main(["new", "bogus", "thing", "--root", str(tmp_path)]) == 1
