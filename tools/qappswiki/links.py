"""Extract Obsidian wikilinks and inline provenance citations from page body.

Wikilinks:   ``[[packages/openqevo]]``, ``[[target|display]]``, ``[[target#anchor]]``
Citations:   ``(source: path)``, ``(synthesis: pathA, pathB)``,
             ``(inferred)``, ``(needs-verification)``
"""

from __future__ import annotations

import re

_WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
_SOURCE_RE = re.compile(r"\((source|synthesis):\s*([^)]+)\)", re.IGNORECASE)
_MARKER_RE = re.compile(r"\((inferred|needs-verification)\)", re.IGNORECASE)
_FENCED_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`]*`")


def strip_code(body: str) -> str:
    """Remove fenced blocks and inline code so example snippets (e.g. a
    ``(source: <path>)`` placeholder shown in prose) aren't mistaken for real
    links or citations."""
    body = _FENCED_RE.sub("", body)
    return _INLINE_CODE_RE.sub("", body)


def extract_links(body: str) -> list[str]:
    """Return raw wikilink bodies in document order (duplicates preserved)."""
    return [m.group(1).strip() for m in _WIKILINK_RE.finditer(strip_code(body))]


def extract_citations(body: str) -> list[dict]:
    """Return inline citations.

    Each entry is ``{"kind": "source"|"synthesis", "paths": [...]}`` for
    ``(source:/synthesis:)`` forms, or ``{"kind": "inferred"|"needs-verification",
    "paths": []}`` for bare markers.
    """
    body = strip_code(body)
    out: list[dict] = []
    for m in _SOURCE_RE.finditer(body):
        kind = m.group(1).lower()
        paths = [p.strip() for p in m.group(2).split(",") if p.strip()]
        out.append({"kind": kind, "paths": paths})
    for m in _MARKER_RE.finditer(body):
        out.append({"kind": m.group(1).lower(), "paths": []})
    return out
