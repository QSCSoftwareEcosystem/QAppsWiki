"""Stage 1.6: promote a reviewed candidate into an authored page.

This closes the **discover → promote loop** — the project's defining feature and
the thing graphify structurally cannot do. ``extract`` stages `INFERRED`
candidates without ever touching authored pages; ``promote`` is the *curated*
action that turns a reviewed candidate into a real, schema-valid ``concepts/``
page carrying the source provenance the extractor found.

The split matters: extraction is automatic and never writes pages; promotion is
deliberate and the only path from staging into the authored layer. A promoted
page is a **stub awaiting authoring** (`status: draft`,
`provenance_status: needs-verification`) — the human/agent then writes the
grounded synthesis. The candidate supplies the skeleton (type, concept_kind,
domains, sources, related links); the curator supplies the knowledge.

Frontmatter is built from ``schema.required_fields`` (the same source of truth
the validator uses), so a promoted page always passes structural validation.
"""

from __future__ import annotations

import datetime as _dt
import json
from pathlib import Path

import yaml

from . import schema


class PromoteError(Exception):
    """Raised for unresolved candidates, missing queue, or refused overwrites."""


def load_queue(out_dir) -> dict:
    """Load the merged candidate queue written by ``qappswiki extract``."""
    path = Path(out_dir) / "extract" / "candidates.json"
    if not path.exists():
        raise PromoteError(
            f"no candidate queue at {path}; run `qappswiki extract` first")
    return json.loads(path.read_text(encoding="utf-8"))


def _slugify(value: str) -> str:
    import re
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def find_candidate(queue: dict, ref: str) -> dict | None:
    """Resolve a candidate by node id, ``concepts/`` slug, or title (ci)."""
    nodes = queue.get("candidate_nodes", [])
    ref_l = ref.lower()
    cand_id = ref if ref.startswith("concepts/") else f"concepts/{_slugify(ref)}"
    for n in nodes:
        if n["id"] == ref or n["id"] == cand_id:
            return n
    for n in nodes:
        if (n.get("title") or "").lower() == ref_l:
            return n
    return None


def page_path(root, candidate: dict) -> Path:
    return Path(root) / f"{candidate['id']}.md"


def build_frontmatter(candidate: dict, today: str | None = None) -> dict:
    """Schema-valid `concept` frontmatter seeded from the candidate."""
    today = today or _dt.date.today().isoformat()
    title = candidate.get("title") or candidate["id"].rsplit("/", 1)[-1]
    fm: dict = {}
    for field in schema.required_fields("concept"):
        if field == "type":
            fm["type"] = "concept"
        elif field == "name":
            fm["name"] = title
        elif field == "status":
            fm["status"] = "draft"           # a stub awaiting authoring
        elif field == "updated":
            fm["updated"] = today
        elif field == "concept_kind":
            ck = candidate.get("concept_kind")
            fm["concept_kind"] = ck if ck in schema.CONCEPT_KIND else "other"
        elif field == "sources":
            fm["sources"] = list(candidate.get("sources") or [])
        elif field == "provenance_status":
            fm["provenance_status"] = "needs-verification"
        else:
            fm[field] = ""
    fm.setdefault("domains", sorted({d for d in (candidate.get("domains") or [])
                                     if d in schema.DOMAINS}))
    return fm


def build_page(candidate: dict, today: str | None = None) -> str:
    """Render the full markdown for a promoted, schema-valid concept stub."""
    fm = build_frontmatter(candidate, today)
    fm_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    title = fm["name"]
    sources = fm["sources"]
    related = candidate.get("related") or []

    src_lines = "\n".join(f"- `{s}`" for s in sources) or "- _(none recorded)_"
    if related:
        rel_lines = "\n".join(f"- [[{r}]]" for r in related)
        rel_note = ""
    else:
        rel_lines = "- TODO: link related pages with `[[wikilinks]]`"
        rel_note = ""

    return f"""---
{fm_yaml}
---

# {title}

> **Promoted from extraction (`qappswiki promote`).** Built from {len(sources)}
> staged source(s); this is a stub that needs authoring. Write the summary
> grounded in the sources, cite each non-obvious claim inline as
> `(source: <path>)`, confirm the related links, then set `provenance_status`
> and run `qappswiki run`.

## Summary

TODO: one-paragraph synthesis grounded in the sources below.

## Supporting sources

{src_lines}

## Related
{rel_note}
{rel_lines}
"""


def promote_one(root, candidate: dict, today: str | None = None,
                force: bool = False, dry_run: bool = False) -> dict:
    """Write one candidate to ``concepts/<slug>.md``. Returns a result dict."""
    if candidate.get("exists") and not force:
        raise PromoteError(
            f"{candidate['id']} already has an authored page (use --force to overwrite)")
    path = page_path(root, candidate)
    if path.exists() and not force:
        raise PromoteError(f"{path} already exists (use --force to overwrite)")

    page = build_page(candidate, today)
    if not dry_run:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page, encoding="utf-8")
    return {
        "id": candidate["id"],
        "path": str(path.relative_to(Path(root))),
        "sources": len(candidate.get("sources") or []),
        "written": not dry_run,
    }


def select_batch(queue: dict, min_sources: int = 2, kind: str | None = None,
                 include_existing: bool = False) -> list[dict]:
    """Candidates worth bulk-promoting: well-supported, novel, optional kind."""
    out = []
    for n in queue.get("candidate_nodes", []):
        if not include_existing and n.get("exists"):
            continue
        if len(n.get("sources") or []) < min_sources:
            continue
        if kind and n.get("concept_kind") != kind:
            continue
        out.append(n)
    return sorted(out, key=lambda n: (-len(n.get("sources") or []), n["id"]))
