"""Stage 9: section-level full-text search over the wiki corpus.

The graph tools answer "what exists and how is it connected". This answers
"which passage says it", which is what a RAG client needs to ground and cite an
answer. Sections rather than whole pages so a hit points at the paragraph that
matched.

Pure stdlib: BM25 is ~40 lines and hand-writing it keeps the package on
pyyaml + networkx.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

import yaml

from .parse import split_frontmatter

_H2 = re.compile(r"^##\s+(.*?)\s*$", re.M)
_H1 = re.compile(r"^#\s+.*$", re.M)

INTRO_HEADING = "(intro)"


@dataclass(frozen=True)
class Section:
    """One `##` block of a page, carrying its page's frontmatter."""

    rel_path: str
    node_id: str
    title: str
    heading: str
    text: str
    provenance_status: str
    sources: tuple[str, ...]
    domains: tuple[str, ...]


def _as_tuple(value) -> tuple[str, ...]:
    if isinstance(value, str):
        return (value,)
    if isinstance(value, list):
        return tuple(str(v) for v in value)
    return ()


def split_sections(text: str, *, rel_path: str, node_id: str) -> list[Section]:
    """Split one page into `##` sections, each carrying the page's frontmatter."""
    raw_fm, body = split_frontmatter(text)
    fm: dict = {}
    if raw_fm:
        try:
            loaded = yaml.safe_load(raw_fm)
            if isinstance(loaded, dict):
                fm = loaded
        except yaml.YAMLError:
            fm = {}

    title = str(fm.get("name") or node_id)
    provenance = str(fm.get("provenance_status") or "")
    sources = _as_tuple(fm.get("sources"))
    domains = _as_tuple(fm.get("domains"))

    def make(heading: str, chunk: str) -> Section:
        return Section(
            rel_path=rel_path,
            node_id=node_id,
            title=title,
            heading=heading,
            text=chunk.strip(),
            provenance_status=provenance,
            sources=sources,
            domains=domains,
        )

    out: list[Section] = []
    matches = list(_H2.finditer(body))

    intro = body[: matches[0].start()] if matches else body
    intro = _H1.sub("", intro).strip()
    if intro:
        out.append(make(INTRO_HEADING, intro))

    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        chunk = body[m.end() : end]
        if chunk.strip():
            out.append(make(m.group(1), chunk))
    return out
