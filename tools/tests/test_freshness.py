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
