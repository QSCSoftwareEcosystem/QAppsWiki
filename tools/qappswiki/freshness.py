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
from pathlib import Path
from urllib.parse import quote

from . import schema

_DETERMINISTIC = {"pypi", "npm", "github-releases", "github-tags", "conda", "crates"}
_USER_AGENT = "qappswiki-freshness"

# Severity ordering for rolling "the worst freshness among the software a page
# builds on" up the graph. ``untracked`` / ``None`` carry no signal and are
# skipped in a roll-up (the page just has no software-freshness basis).
STATUS_SEVERITY = {"fresh": 0, "manual": 1, "unknown": 2, "error": 2, "stale": 3}

# Relations along which software staleness propagates *up* to the pages that
# build on it. A page that composes / uses / depends on a package inherits its
# staleness; `cites` (provenance) and `related` (loose) deliberately do not.
_ROLLUP_RELATIONS = {
    "composes-with", "uses", "depends-on", "integrates", "implements", "has-how-to",
}

FRESHNESS_CACHE_VERSION = "qappswiki-freshness-0"


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


# --------------------------------------------------------------------------- #
# Build-time stamping: last-known freshness onto the graph + composite roll-up
# --------------------------------------------------------------------------- #
#
# Freshness itself is online; the *build* must stay offline and deterministic.
# The bridge is a small cache (``wiki-out/freshness.json``) written by the
# online ``freshness`` command and read at build time. With no cache, packages
# stamp ``untracked`` and roll-ups are ``None`` — so CI (which never has the
# cache) is unaffected. This realizes "check on read, update out-of-band" from
# the self-refreshing-context design.

def cache_path(out) -> Path:
    return Path(out) / "freshness.json"


def save_cache(out, results: list[dict]) -> Path:
    """Persist per-package verdicts so the next build can stamp the graph."""
    p = cache_path(out)
    p.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": FRESHNESS_CACHE_VERSION,
        "packages": {
            r["page"]: {"status": r["status"], "latest": r["latest"],
                        "built": r["built"], "detail": r["detail"]}
            for r in results
        },
    }
    p.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    return p


def load_cache(out) -> dict:
    """Read ``{package_id: {status, latest, ...}}`` from the cache, or ``{}``."""
    p = cache_path(out)
    if not p.exists():
        return {}
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except (ValueError, OSError):
        return {}
    return data.get("packages", {}) if isinstance(data, dict) else {}


def _reachable_packages(graph, start, max_depth: int = 2) -> set[str]:
    """Package nodes reachable from ``start`` via roll-up relations (≤max_depth)."""
    pkgs: set[str] = set()
    seen = {start}
    frontier = [(start, 0)]
    while frontier:
        node, depth = frontier.pop()
        if depth >= max_depth:
            continue
        for _u, v, d in graph.out_edges(node, data=True):
            if d.get("relation") not in _ROLLUP_RELATIONS:
                continue
            if graph.nodes[v].get("type") == "package":
                pkgs.add(v)
            if v not in seen:
                seen.add(v)
                frontier.append((v, depth + 1))
    return pkgs


def stamp_graph(graph, cached: dict | None) -> None:
    """Stamp last-known freshness onto the graph (mutates node attrs in place).

    Packages get ``freshness`` (+ ``freshness_latest``) from ``cached``; every
    other content page gets a composite ``freshness_rollup`` — the worst
    freshness among the packages it composes (with ``freshness_basis`` listing
    them) — so software staleness propagates up to integrations and applications.
    Pure/offline given ``cached``; an empty cache leaves everything untracked.
    """
    cached = cached or {}
    for nid, a in graph.nodes(data=True):
        if a.get("type") != "package":
            continue
        info = cached.get(nid)
        if info:
            a["freshness"] = info.get("status")
            a["freshness_latest"] = info.get("latest")
        elif a.get("version_source"):
            a["freshness"] = "untracked"   # configured to track, but never checked
        else:
            a["freshness"] = None          # no freshness model at all

    for nid, a in graph.nodes(data=True):
        t = a.get("type")
        if t not in schema.CONTENT_TYPES or t in ("package", "source"):
            continue
        worst = None
        basis = []
        for pkg in _reachable_packages(graph, nid):
            st = graph.nodes[pkg].get("freshness")
            if st in STATUS_SEVERITY:
                basis.append(pkg)
                if worst is None or STATUS_SEVERITY[st] > STATUS_SEVERITY[worst]:
                    worst = st
        a["freshness_rollup"] = worst
        a["freshness_basis"] = sorted(basis)
