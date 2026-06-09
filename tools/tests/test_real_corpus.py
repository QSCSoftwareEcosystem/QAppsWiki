"""Read-only smoke test against the actual QAppsWiki corpus.

Skipped automatically when run outside the repo (e.g. the package installed
standalone). Asserts the pipeline runs and the known Qiskit gap is reported.
"""

from pathlib import Path

import pytest

from qappswiki import cli, validate

# tools/tests/ -> tools/ -> wiki root
REAL_ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.skipif(
    not (REAL_ROOT / "schema" / "frontmatter-v0.md").exists(),
    reason="not running inside the QAppsWiki repo",
)
def test_real_corpus_runs_and_flags_qiskit(tmp_path):
    pages, graph = cli.run_pipeline(REAL_ROOT, tmp_path / "out", use_cache=False)
    assert len(pages) > 5
    findings = validate.validate(pages, graph, REAL_ROOT)
    qiskit = [f for f in findings if "qiskit" in f["page"].lower() or "qiskit" in f["message"].lower()]
    assert any(f["code"] == "dangling-package-ref" for f in qiskit), \
        "expected the Qiskit package reference with no page to be flagged"
