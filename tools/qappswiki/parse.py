"""Stage 2: parse one page into a graph node dict + parse metadata.

``parse_page`` returns ``(node_dict, parse_meta)``:

* ``node_dict``  — graph node attributes (id, type, title, domains, status,
  provenance_status, rel_path). Stored on the graph.
* ``parse_meta`` — everything validation/edges need but the graph doesn't store
  (raw frontmatter, body wikilinks, citations, explicit edges, a parse-error
  flag). Not stored on the graph.

Both are JSON-safe (dates are stringified) so they can be cached verbatim.
"""

from __future__ import annotations

import datetime as _dt
import re
from pathlib import Path

import yaml

from . import links
from .cache import Cache
from .paths import to_node_id

_H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


def _jsonsafe(value):
    """Recursively convert dates/datetimes to ISO strings for cache/JSON parity."""
    if isinstance(value, (_dt.date, _dt.datetime)):
        return value.isoformat()
    if isinstance(value, dict):
        return {k: _jsonsafe(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [_jsonsafe(v) for v in value]
    return value


def split_frontmatter(text: str) -> tuple[str | None, str]:
    """Return ``(frontmatter_str_or_None, body)``.

    Recognizes a leading ``---`` fenced YAML block. Tolerates a leading BOM and
    blank lines before the fence.
    """
    stripped = text.lstrip("﻿")
    if not stripped.startswith("---"):
        return None, text
    # Match the first fenced block: --- ... \n---
    m = re.match(r"^---\s*\n(.*?)\n---\s*(?:\n|$)", stripped, re.DOTALL)
    if not m:
        return None, text
    return m.group(1), stripped[m.end():]


def _title(frontmatter: dict, body: str, node_id: str) -> str:
    for key in ("name", "title"):
        val = frontmatter.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip()
    m = _H1_RE.search(body)
    if m:
        return m.group(1).strip()
    return node_id.rsplit("/", 1)[-1]


def _as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, str):
        return [value]
    if isinstance(value, (list, tuple)):
        return [str(v) for v in value]
    return [str(value)]


def _parse_text(text: str, rel_path: str) -> tuple[dict, dict]:
    node_id = to_node_id(rel_path)
    fm_str, body = split_frontmatter(text)
    parse_error = None
    frontmatter: dict = {}
    if fm_str is not None:
        try:
            loaded = yaml.safe_load(fm_str)
            if isinstance(loaded, dict):
                frontmatter = _jsonsafe(loaded)
            elif loaded is not None:
                parse_error = "frontmatter is not a mapping"
        except yaml.YAMLError as exc:
            parse_error = f"YAML error: {exc}"
    else:
        parse_error = "missing frontmatter block"

    page_type = frontmatter.get("type")
    node_dict = {
        "id": node_id,
        "type": page_type if isinstance(page_type, str) else None,
        "title": _title(frontmatter, body, node_id),
        "domains": _as_list(frontmatter.get("domains")),
        "status": frontmatter.get("status"),
        "provenance_status": frontmatter.get("provenance_status"),
        "rel_path": rel_path,
        # freshness metadata (used by the serving layer / `freshness`)
        "version_built": frontmatter.get("version_built"),
        "version_scope": frontmatter.get("version_scope"),
        "version_source": frontmatter.get("version_source"),
    }

    explicit = frontmatter.get("edges") or []
    if not isinstance(explicit, list):
        explicit = []

    parse_meta = {
        "node_id": node_id,
        "rel_path": rel_path,
        "frontmatter": frontmatter,
        "body_links": links.extract_links(body),
        "citations": links.extract_citations(body),
        "explicit_edges": _jsonsafe(explicit),
        "parse_error": parse_error,
    }
    return node_dict, parse_meta


def parse_page(page_ref: dict, root, cache: Cache | None = None) -> tuple[dict, dict]:
    """Parse a ``PageRef`` into ``(node_dict, parse_meta)``, using the cache."""
    path = Path(page_ref["path"])
    rel_path = page_ref["rel_path"]
    digest = None
    if cache is not None and cache.enabled:
        digest = Cache.file_hash(path)
        cached = cache.load(digest)
        if cached is not None:
            return cached["node"], cached["meta"]

    text = path.read_text(encoding="utf-8")
    node_dict, parse_meta = _parse_text(text, rel_path)

    if cache is not None and cache.enabled and digest is not None:
        cache.save(digest, {"node": node_dict, "meta": parse_meta})
    return node_dict, parse_meta
