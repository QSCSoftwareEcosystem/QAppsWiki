"""Online freshness check for package contexts.

The counterpart to ``validate``: ``validate`` checks the *form* of
``version_source`` offline (CI-safe); ``freshness`` performs the *online*
comparison — fetch the latest upstream version, test it against ``version_scope``,
and classify each package as fresh / stale / unknown / manual / untracked /
error. It is read-only on the wiki (writes only to ``wiki-out/``) and never
fails a build; staleness is reported, not enforced.

HTTP uses the standard library (``urllib``); version comparison uses ``packaging``
when available. The network call is isolated in ``_http_json`` so tests inject a
fake fetcher and never touch the network.
"""

from __future__ import annotations

import json
import urllib.request
from urllib.parse import quote

from . import schema

_DETERMINISTIC = {"pypi", "npm", "github-releases", "github-tags", "conda", "crates"}
_USER_AGENT = "qappswiki-freshness"


def _http_json(url: str, timeout: float = 10.0):
    req = urllib.request.Request(url, headers={"User-Agent": _USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 (https only)
        return json.loads(resp.read().decode("utf-8"))


def _max_semver(names):
    try:
        from packaging.version import InvalidVersion, Version
    except ImportError:
        return sorted(names)[-1] if names else None
    best = best_raw = None
    for n in names:
        try:
            v = Version(str(n).lstrip("v"))
        except InvalidVersion:
            continue
        if best is None or v > best:
            best, best_raw = v, str(n).lstrip("v")
    return best_raw


def latest_version(kind: str, sid: str, timeout: float = 10.0, fetch=None):
    """Resolve the latest upstream version for a deterministic ``kind``.

    Returns the version string, or ``None`` for non-deterministic kinds.
    Raises on network/parse failure (caller classifies as ``error``).
    """
    fetch = fetch or _http_json
    if kind == "pypi":
        return fetch(f"https://pypi.org/pypi/{quote(sid)}/json", timeout)["info"]["version"]
    if kind == "npm":
        return fetch(f"https://registry.npmjs.org/{quote(sid, safe='@/')}/latest", timeout)["version"]
    if kind == "github-releases":
        tag = fetch(f"https://api.github.com/repos/{sid}/releases/latest", timeout).get("tag_name", "")
        return tag.lstrip("v")
    if kind == "github-tags":
        tags = fetch(f"https://api.github.com/repos/{sid}/tags", timeout)
        return _max_semver([t.get("name", "") for t in tags])
    if kind == "crates":
        return fetch(f"https://crates.io/api/v1/crates/{quote(sid)}", timeout)["crate"]["max_stable_version"]
    if kind == "conda":
        channel, _, pkg = sid.partition("/")
        return fetch(f"https://api.anaconda.org/package/{channel}/{pkg}", timeout)["latest_version"]
    return None


def compare(latest, scope) -> tuple[str, str]:
    """Classify ``latest`` against a ``version_scope`` specifier."""
    if not scope:
        return "unknown", "no version_scope to compare against"
    try:
        from packaging.specifiers import SpecifierSet
        from packaging.version import Version
    except ImportError:
        return "unknown", "install 'packaging' to compare versions"
    try:
        spec = SpecifierSet(str(scope))
        in_scope = spec.contains(Version(str(latest)), prereleases=True)
    except Exception as exc:  # invalid specifier or version
        return "unknown", f"cannot parse version/scope ({exc})"
    if in_scope:
        return "fresh", f"latest {latest} within scope {scope}"
    return "stale", f"latest {latest} outside scope {scope}"


def check_package(node: dict, fm: dict, timeout: float = 10.0, fetch=None) -> dict:
    """Freshness verdict for one package page."""
    res = {"page": node["id"], "built": fm.get("version_built"),
           "scope": fm.get("version_scope"), "kind": None, "id": None,
           "latest": None, "status": None, "detail": ""}
    vs = fm.get("version_source")
    if not isinstance(vs, dict) or not vs.get("kind"):
        res["status"], res["detail"] = "untracked", "no version_source"
        return res
    kind, sid = vs.get("kind"), vs.get("id")
    res["kind"], res["id"] = kind, sid
    if kind not in _DETERMINISTIC:
        res["status"], res["detail"] = "manual", f"{kind}: no version endpoint — check by hand/LLM"
        return res
    if not sid:
        res["status"], res["detail"] = "unknown", "version_source.id is empty"
        return res
    try:
        latest = latest_version(kind, sid, timeout, fetch)
    except Exception as exc:  # network/parse/HTTP error — never fatal
        res["status"], res["detail"] = "error", f"fetch failed: {exc}"
        return res
    res["latest"] = latest
    res["status"], res["detail"] = compare(latest, res["scope"])
    return res


def run_freshness(pages: list[dict], timeout: float = 10.0, fetch=None,
                  only: str | None = None) -> list[dict]:
    """Check every package page (optionally a single ``only`` id)."""
    out = []
    for p in pages:
        node = p["node"]
        if node.get("type") != "package":
            continue
        if only and node["id"] != only and node["id"].rsplit("/", 1)[-1] != only:
            continue
        out.append(check_package(node, p["meta"]["frontmatter"], timeout, fetch))
    return out
