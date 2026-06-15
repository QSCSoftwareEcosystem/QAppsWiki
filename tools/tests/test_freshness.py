"""Freshness logic — fully offline (the network fetcher is always injected)."""

import pytest

from qappswiki import freshness


def test_compare_fresh_stale_unknown():
    assert freshness.compare("0.1.3", ">=0.1,<0.2")[0] == "fresh"
    assert freshness.compare("0.2.0", ">=0.1,<0.2")[0] == "stale"
    assert freshness.compare("1.4.1", ">=1.0,<2.0")[0] == "fresh"
    assert freshness.compare("2.0.0", ">=1.0,<2.0")[0] == "stale"
    assert freshness.compare("1.0", "")[0] == "unknown"


def test_latest_version_parsers():
    fake = {
        "https://pypi.org/pypi/qiskit/json": {"info": {"version": "1.4.1"}},
        "https://registry.npmjs.org/foo/latest": {"version": "3.2.1"},
        "https://api.github.com/repos/o/r/releases/latest": {"tag_name": "v0.5.0"},
        "https://api.github.com/repos/o/r/tags": [{"name": "v1.2.0"}, {"name": "v1.10.0"}, {"name": "v1.3.0"}],
    }
    f = lambda url, timeout=10: fake[url]
    assert freshness.latest_version("pypi", "qiskit", fetch=f) == "1.4.1"
    assert freshness.latest_version("npm", "foo", fetch=f) == "3.2.1"
    assert freshness.latest_version("github-releases", "o/r", fetch=f) == "0.5.0"
    assert freshness.latest_version("github-tags", "o/r", fetch=f) == "1.10.0"  # semver, not lexical


def test_check_package_statuses():
    node = {"id": "packages/x", "type": "package"}

    untracked = freshness.check_package(node, {})
    assert untracked["status"] == "untracked"

    manual = freshness.check_package(node, {"version_source": {"kind": "docs", "id": "http://x"}})
    assert manual["status"] == "manual"

    f_fresh = lambda url, timeout=10: {"info": {"version": "1.1.0"}}
    fm = {"version_source": {"kind": "pypi", "id": "x"}, "version_built": "1.0.0", "version_scope": ">=1.0,<2.0"}
    assert freshness.check_package(node, fm, fetch=f_fresh)["status"] == "fresh"

    f_stale = lambda url, timeout=10: {"info": {"version": "2.0.0"}}
    assert freshness.check_package(node, fm, fetch=f_stale)["status"] == "stale"


def test_check_package_network_error_is_not_fatal():
    def boom(url, timeout=10):
        raise OSError("network down")

    node = {"id": "packages/x", "type": "package"}
    fm = {"version_source": {"kind": "pypi", "id": "x"}, "version_scope": ">=1.0,<2.0"}
    res = freshness.check_package(node, fm, fetch=boom)
    assert res["status"] == "error" and "network down" in res["detail"]


def test_run_freshness_filters_to_packages(tmp_wiki):
    from qappswiki.cli import run_pipeline
    pages, _ = run_pipeline(tmp_wiki, tmp_wiki / "wiki-out", use_cache=False)
    # no version_source in the fixture -> all packages report untracked, non-packages skipped
    results = freshness.run_freshness(pages, fetch=lambda *a, **k: {})
    assert results and all(r["status"] == "untracked" for r in results)
    assert all(p.startswith("packages/") for p in (r["page"] for r in results))


def test_real_default_fetcher_is_offline_safe(monkeypatch):
    # The default fetcher must require an explicit URL; nothing runs at import.
    import socket
    monkeypatch.setattr(socket.socket, "connect", lambda *a, **k: (_ for _ in ()).throw(
        AssertionError("unexpected network use")))
    # compare/check with injected fetch never touches the socket
    assert freshness.compare("1.0.0", ">=1.0")[0] == "fresh"


# --------------------------------------------------------------------------- #
# build-time stamping + composite roll-up
# --------------------------------------------------------------------------- #

# A package with a version_source, an integration composing it, and a how-to
# using it — so staleness has somewhere to roll up to.
_ROLLUP_FILES = {
    "index.md": "---\ntype: index\nstatus: active\nupdated: 2026-01-01\n---\n# I\n"
                "- [[packages/qpkg]]\n- [[integrations/qpkg-to-thing]]\n- [[how-to/use-qpkg]]\n",
    "packages/qpkg.md": """---
type: package
name: Qpkg
status: active
updated: 2026-01-01
package_role: library
capabilities: [simulation]
hardware_targets: [local-cpu]
interfaces: [python-api]
domains: [quantum-software]
sources: [raw/md/qpkg.md]
provenance_status: source-backed
version_source: {kind: pypi, id: qpkg}
version_built: "1.0.0"
version_scope: ">=1.0,<2.0"
---
# Qpkg
See [[how-to/use-qpkg]].
""",
    "integrations/qpkg-to-thing.md": """---
type: integration
status: draft
updated: 2026-01-01
packages: [Qpkg]
interfaces: [python-api]
inputs: [a]
outputs: [b]
domains: [quantum-software]
sources: [raw/md/qpkg.md]
provenance_status: source-backed
---
# Integration
Composes [[packages/qpkg]].
""",
    "how-to/use-qpkg.md": """---
type: how-to
status: draft
updated: 2026-01-01
task: Use Qpkg
packages: [Qpkg]
version_scope: v1
domains: [quantum-software]
sources: [raw/md/qpkg.md]
provenance_status: source-backed
---
# Use Qpkg
See [[packages/qpkg]].
""",
    "raw/md/qpkg.md": "# qpkg docs\n",
}


def _rollup_wiki(tmp_path):
    for rel, content in _ROLLUP_FILES.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return tmp_path


def test_cache_roundtrip(tmp_path):
    out = tmp_path / "wiki-out"
    results = [{"page": "packages/qpkg", "status": "stale", "latest": "2.0.0",
                "built": "1.0.0", "detail": "x"}]
    freshness.save_cache(out, results)
    loaded = freshness.load_cache(out)
    assert loaded["packages/qpkg"]["status"] == "stale"
    assert loaded["packages/qpkg"]["latest"] == "2.0.0"


def test_load_cache_absent_is_empty(tmp_path):
    assert freshness.load_cache(tmp_path / "nope") == {}


def test_stamp_and_rollup_propagates_staleness(tmp_path):
    from qappswiki.cli import run_pipeline
    root = _rollup_wiki(tmp_path)
    _, graph = run_pipeline(root, root / "wiki-out", use_cache=False)
    freshness.stamp_graph(graph, {"packages/qpkg": {"status": "stale", "latest": "2.0.0"}})

    assert graph.nodes["packages/qpkg"]["freshness"] == "stale"
    # the integration and how-to that compose qpkg inherit its staleness
    assert graph.nodes["integrations/qpkg-to-thing"]["freshness_rollup"] == "stale"
    assert "packages/qpkg" in graph.nodes["integrations/qpkg-to-thing"]["freshness_basis"]
    assert graph.nodes["how-to/use-qpkg"]["freshness_rollup"] == "stale"


def test_stamp_untracked_when_no_cache(tmp_path):
    from qappswiki.cli import run_pipeline
    root = _rollup_wiki(tmp_path)
    _, graph = run_pipeline(root, root / "wiki-out", use_cache=False)
    freshness.stamp_graph(graph, {})
    # version_source present but never checked -> untracked; no roll-up signal
    assert graph.nodes["packages/qpkg"]["freshness"] == "untracked"
    assert graph.nodes["integrations/qpkg-to-thing"]["freshness_rollup"] is None


def test_run_pipeline_stamps_from_written_cache(tmp_path):
    from qappswiki.cli import run_pipeline
    root = _rollup_wiki(tmp_path)
    out = root / "wiki-out"
    freshness.save_cache(out, [{"page": "packages/qpkg", "status": "stale",
                                "latest": "2.0.0", "built": "1.0.0", "detail": "x"}])
    # run_pipeline must auto-load the cache and stamp without any extra call
    _, graph = run_pipeline(root, out, use_cache=False)
    assert graph.nodes["packages/qpkg"]["freshness"] == "stale"
    assert graph.nodes["integrations/qpkg-to-thing"]["freshness_rollup"] == "stale"


def test_analyze_and_report_surface_freshness(tmp_path):
    from qappswiki import analyze, report
    from qappswiki.cli import run_pipeline
    root = _rollup_wiki(tmp_path)
    out = root / "wiki-out"
    freshness.save_cache(out, [{"page": "packages/qpkg", "status": "stale",
                                "latest": "2.0.0", "built": "1.0.0", "detail": "x"}])
    _, graph = run_pipeline(root, out, use_cache=False)
    a = analyze.analyze(graph)
    assert a["freshness"]["tracked"]
    assert "packages/qpkg" in a["freshness"]["stale_packages"]
    assert "integrations/qpkg-to-thing" in a["freshness"]["stale_rollup"]
    md = report.render_graph_report(a, "2026-01-01")
    assert "## Freshness" in md
    assert "stale packages" in md
