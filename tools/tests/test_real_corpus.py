"""Read-only smoke test against the actual QAppsWiki corpus.

Skipped automatically when run outside the repo (e.g. the package installed
standalone). Asserts the pipeline runs and the corpus stays error-free (the
CI deploy gate is "0 errors").
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
def test_real_corpus_runs_clean(tmp_path):
    pages, graph = cli.run_pipeline(REAL_ROOT, tmp_path / "out", use_cache=False)
    assert len(pages) > 5
    findings = validate.validate(pages, graph, REAL_ROOT)
    errors = [f for f in findings if f["level"] == "ERROR"]
    assert not errors, f"corpus has validation errors: {errors[:5]}"
    # The seed package pages now all exist, so nothing should be flagged as a
    # dangling package reference.
    assert not any(f["code"] == "dangling-package-ref" for f in findings)
