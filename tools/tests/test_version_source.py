"""Form-only validation of version_source / version_built (offline)."""

from qappswiki import validate
from qappswiki.cli import run_pipeline

_HEADER = """---
type: package
name: Demo
status: active
updated: 2026-01-01
package_role: library
capabilities: [simulation]
hardware_targets: [local-cpu]
interfaces: [python-api]
domains: [quantum-software]
sources: [raw/md/demo.md]
provenance_status: source-backed
"""


def _pkg(tmp_wiki, name, extra):
    p = tmp_wiki / "packages" / f"{name}.md"
    p.write_text(_HEADER + extra + "---\n\n# Demo\n", encoding="utf-8")
    out = tmp_wiki / "wiki-out"
    pages, graph = run_pipeline(tmp_wiki, out, use_cache=False)
    findings = validate.validate(pages, graph, tmp_wiki)
    return {(f["level"], f["code"]) for f in findings if f["page"] == f"packages/{name}"}


def test_valid_version_source(tmp_wiki):
    codes = _pkg(tmp_wiki, "ok", 'version_source:\n  kind: pypi\n  id: qiskit\nversion_built: "1.2.0"\n')
    assert not any(c in {"invalid-version-source", "incomplete-version-source",
                         "invalid-version-built"} for _l, c in codes)


def test_invalid_kind_is_error(tmp_wiki):
    codes = _pkg(tmp_wiki, "badkind", "version_source:\n  kind: not-a-kind\n  id: qiskit\n")
    assert ("ERROR", "invalid-version-source") in codes


def test_version_source_not_mapping_is_error(tmp_wiki):
    codes = _pkg(tmp_wiki, "scalar", "version_source: just-a-string\n")
    assert ("ERROR", "invalid-version-source") in codes


def test_empty_id_is_warning(tmp_wiki):
    codes = _pkg(tmp_wiki, "noid", "version_source:\n  kind: pypi\n  id: \"\"\n")
    assert ("WARNING", "incomplete-version-source") in codes
    assert ("ERROR", "invalid-version-source") not in codes


def test_no_network_call(monkeypatch):
    # Guard the design invariant: validation must never open a socket.
    import socket

    def _boom(*a, **k):
        raise AssertionError("validation attempted a network connection")

    monkeypatch.setattr(socket.socket, "connect", _boom)
    findings = validate._validate_version_fields(
        "packages/x", {"version_source": {"kind": "pypi", "id": "qiskit"}, "version_built": "1.0"}
    )
    assert findings == []
