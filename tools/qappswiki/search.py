"""Stage 9: section-level full-text search over the wiki corpus.

The graph tools answer "what exists and how is it connected". This answers
"which passage says it", which is what a RAG client needs to ground and cite an
answer. Sections rather than whole pages so a hit points at the paragraph that
matched.

Pure stdlib: BM25 is ~40 lines and hand-writing it keeps the package on
pyyaml + networkx.
"""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import yaml

from . import collect
from .cache import Cache
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


_TOKEN = re.compile(r"[a-z0-9]+")
_K1 = 1.5
_B = 0.75


def tokenize(text: str) -> list[str]:
    """Lowercase alphanumeric tokens, dropping single characters."""
    return [t for t in _TOKEN.findall(text.lower()) if len(t) > 1]


@dataclass(frozen=True)
class Hit:
    section: Section
    score: float


class Bm25Index:
    """Okapi BM25 over section text. Built in memory, queried per request."""

    def __init__(self, sections: list[Section]) -> None:
        self.sections = list(sections)
        # Heading and title are part of the searchable text: a query naming a code
        # should match its page even when the body phrases things differently.
        self._docs = [
            Counter(tokenize(f"{s.title} {s.heading} {s.text}")) for s in self.sections
        ]
        self._lengths = [sum(d.values()) for d in self._docs]
        n = len(self._docs)
        self._avglen = (sum(self._lengths) / n) if n else 0.0
        df: Counter[str] = Counter()
        for d in self._docs:
            df.update(d.keys())
        self._idf = {
            term: math.log(1 + (n - freq + 0.5) / (freq + 0.5)) for term, freq in df.items()
        }

    def search(self, query: str, k: int = 8, domain: str | None = None) -> list[Hit]:
        terms = tokenize(query)
        if not terms or not self._docs:
            return []
        scored: list[Hit] = []
        for i, doc in enumerate(self._docs):
            section = self.sections[i]
            if domain and domain not in section.domains:
                continue
            length = self._lengths[i]
            total = 0.0
            for term in terms:
                freq = doc.get(term, 0)
                if not freq:
                    continue
                denom = freq + _K1 * (1 - _B + _B * length / (self._avglen or 1.0))
                total += self._idf.get(term, 0.0) * freq * (_K1 + 1) / denom
            if total > 0:
                scored.append(Hit(section=section, score=total))
        scored.sort(key=lambda h: (-h.score, h.section.node_id, h.section.heading))
        return scored[:k]


def _section_to_dict(s: Section) -> dict:
    return {
        "rel_path": s.rel_path,
        "node_id": s.node_id,
        "title": s.title,
        "heading": s.heading,
        "text": s.text,
        "provenance_status": s.provenance_status,
        "sources": list(s.sources),
        "domains": list(s.domains),
    }


def _section_from_dict(d: dict) -> Section:
    return Section(
        rel_path=d["rel_path"],
        node_id=d["node_id"],
        title=d["title"],
        heading=d["heading"],
        text=d["text"],
        provenance_status=d.get("provenance_status", ""),
        sources=tuple(d.get("sources") or ()),
        domains=tuple(d.get("domains") or ()),
    )


def build_index(root, *, out_dir=None, use_cache: bool = True) -> Bm25Index:
    """Split every corpus page into sections and build a BM25 index.

    `collect_pages` already drops `raw/md`, `raw/pdf`, `tools/`, and the rest of
    `paths.IGNORED_DIRS`, so exclusions live in one place.

    The cache root is `<out_dir>/search`, NOT `<out_dir>`: `Cache` keys entries on
    the file digest alone, so sharing a root with the parse cache would make the
    two overwrite each other for the same page.
    """
    root = Path(root).resolve()
    cache = None
    if use_cache and out_dir is not None:
        cache = Cache(Path(out_dir) / "search", enabled=True)

    sections: list[Section] = []
    for ref in collect.collect_pages(root):
        path = Path(ref["path"])
        digest = Cache.file_hash(path) if cache else None
        payload = cache.load(digest) if cache else None
        if payload is None:
            text = path.read_text(encoding="utf-8", errors="replace")
            page_sections = split_sections(
                text, rel_path=ref["rel_path"], node_id=ref["node_id"]
            )
            if cache:
                cache.save(digest, [_section_to_dict(s) for s in page_sections])
        else:
            page_sections = [_section_from_dict(d) for d in payload]
        sections.extend(page_sections)
    return Bm25Index(sections)
