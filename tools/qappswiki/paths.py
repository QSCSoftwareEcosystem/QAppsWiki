"""Path normalization and link/source target classification.

Node ids are POSIX-style relative paths without the ``.md`` suffix
(``packages/openqevo``, ``schema/frontmatter-v0``, root files as ``README``).
Wikilinks and source references are classified against the set of known node
ids and the filesystem so the rest of the pipeline can tell a real page from a
missing one from an external (sibling-repo / URL) reference.
"""

from __future__ import annotations

import os
from pathlib import Path

# Directories never treated as part of the wiki corpus.
IGNORED_DIRS = {"node_modules", ".git", ".github", "wiki-out", "tools", "__pycache__"}
# raw/ holds the evidence layer: raw/md extracted source markdown, raw/pdf
# binaries, raw/assets attachments. These are sources, not maintained wiki pages
# (raw/source-inventory.md at the raw/ root IS a page and stays included).
IGNORED_REL_PREFIXES = ("raw/md/", "raw/pdf/", "raw/assets/")


def is_url(value: str) -> bool:
    return value.startswith(("http://", "https://"))


def to_node_id(rel_path: str | os.PathLike) -> str:
    """``packages/openqevo.md`` -> ``packages/openqevo`` (POSIX separators)."""
    rel = Path(rel_path).as_posix()
    if rel.endswith(".md"):
        rel = rel[:-3]
    return rel


def strip_link(target: str) -> str:
    """Normalize a raw wikilink body: drop alias, anchor, ./ and .md."""
    t = target.strip()
    if "|" in t:  # [[target|display]]
        t = t.split("|", 1)[0].strip()
    if "#" in t:  # [[target#heading]]
        t = t.split("#", 1)[0].strip()
    if t.startswith("./"):
        t = t[2:]
    if t.endswith(".md"):
        t = t[:-3]
    return t


def classify_wikilink(target: str, known_ids: set[str]) -> dict:
    """Classify a ``[[target]]`` body link.

    Returns ``{"raw", "node_id", "kind"}`` where kind is one of
    ``page`` (resolves to a known node), ``external`` (URL or escapes root),
    or ``missing`` (looks internal but no backing page exists).
    """
    raw = target.strip()
    norm = strip_link(target)
    if is_url(norm) or norm.startswith("../"):
        return {"raw": raw, "node_id": norm, "kind": "external"}
    if norm in known_ids:
        return {"raw": raw, "node_id": norm, "kind": "page"}
    return {"raw": raw, "node_id": norm, "kind": "missing"}


def resolve_source(ref: str, page_rel: str, root: Path, known_ids: set[str]) -> dict:
    """Classify a ``sources:`` / inline ``(source:)`` reference.

    ``page_rel`` is the page's path relative to root (e.g. ``packages/openqevo.md``);
    source refs are written relative to the page's directory. Returns
    ``{"raw", "kind", "exists", "node_id"}`` where kind is ``url``, ``external``
    (escapes the wiki root, e.g. ``../OpenQEvo/README.md``), or ``internal``.
    ``node_id`` is set when the ref is an internal ``.md`` page.
    """
    raw = ref.strip()
    if is_url(raw):
        return {"raw": raw, "kind": "url", "exists": True, "node_id": None}

    root = root.resolve()
    page_dir = (root / page_rel).parent
    # The corpus mixes page-dir-relative (``../OpenQEvo/README.md``) and
    # root-relative (``raw/md/x.md``) source paths. Try both bases; prefer the
    # candidate that exists, else fall back to the page-relative resolution.
    candidates = [(page_dir / raw).resolve(), (root / raw).resolve()]
    resolved = next((c for c in candidates if c.exists()), candidates[0])

    try:
        rel = resolved.relative_to(root)
    except ValueError:
        # Escapes the wiki root -> sibling repo / external file.
        return {"raw": raw, "kind": "external", "exists": resolved.exists(), "node_id": None}

    rel_posix = rel.as_posix()
    node_id = to_node_id(rel_posix) if rel_posix.endswith(".md") else None
    if node_id is not None and node_id not in known_ids:
        node_id = None  # internal path but not a maintained page (e.g. raw/md file)
    return {
        "raw": raw,
        "kind": "internal",
        "exists": resolved.exists(),
        "node_id": node_id,
    }


def is_ignored(rel_path: str) -> bool:
    parts = Path(rel_path).parts
    if parts and parts[0] in IGNORED_DIRS:
        return True
    posix = Path(rel_path).as_posix()
    return posix.startswith(IGNORED_REL_PREFIXES)
