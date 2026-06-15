"""Generate schema-valid stub pages.

The "template" for a new page is derived from ``schema.py`` (the same source of
truth the validator uses), so a freshly scaffolded page always passes structural
validation — only its content needs filling in. This keeps the template and the
schema from ever drifting apart.

Two entry points share that schema-driven core:

* ``stub_page`` — the *ingest* stub, carrying converted-source provenance
  (``source_markdown`` / ``extracted_with``); used by ``qappswiki ingest``.
* ``blank_page`` — the *authoring* stub with no source attached, used by
  ``qappswiki new`` so a contributor can start a page from nothing.
"""

from __future__ import annotations

import datetime as _dt

import yaml

from . import schema

# Conventional directory for each content page type. ``qappswiki new <type>
# <slug>`` places a bare slug here; a slug containing "/" or ending ".md" is
# treated as an explicit path instead.
TYPE_DIR = {
    "package": "packages",
    "concept": "concepts",
    "how-to": "how-to",
    "integration": "integrations",
    "workflow": "workflow",
    "qec-artifact": "qec-artifact",
    "benchmark": "benchmark",
    "source": "raw",
}

# Sensible placeholder for each required field, by name. List fields default to
# empty; scalar enum fields take a safe member; free-text fields get a TODO.
_SCALAR_DEFAULTS = {
    "status": "draft",
    "provenance_status": "needs-verification",
    "package_role": "library",
    "concept_kind": "other",
    "artifact_kind": "other",
    "benchmark_kind": "other",
    "source_type": "paper",
    "preferred_ingest_path": "raw/md",
    "validation_status": "unverified",
    "task": "TODO: describe the task",
    "version_scope": "TODO",
}

# Fields that are lists in the schema.
_LIST_FIELDS = {
    "capabilities", "hardware_targets", "interfaces", "packages", "inputs",
    "outputs", "artifacts", "metrics", "workflows", "formats", "producers",
    "consumers", "sources", "source_markdown", "domains",
}


def _humanize(slug: str) -> str:
    return slug.replace("-", " ").replace("_", " ").strip().title()


def _base_frontmatter(
    page_type: str,
    slug: str,
    title: str | None,
    sources: list[str],
    location: str = "",
) -> dict:
    """Build the required-field frontmatter for ``page_type`` from the schema.

    Every required field gets a safe placeholder so the page validates with no
    *missing*-field error (empty lists/strings remain incompleteness warnings to
    fill in). Provisional types are stamped ``status: provisional`` so they don't
    trip the provisional-status check.
    """
    today = _dt.date.today().isoformat()
    fm: dict = {}
    for field in schema.required_fields(page_type):
        if field == "type":
            fm["type"] = page_type
        elif field in ("name", "title"):
            fm[field] = title or _humanize(slug)
        elif field == "updated":
            fm["updated"] = today
        elif field == "location":
            fm["location"] = location
        elif field == "sources":
            fm["sources"] = list(sources)
        elif field in _LIST_FIELDS:
            fm[field] = []
        elif field in _SCALAR_DEFAULTS:
            fm[field] = _SCALAR_DEFAULTS[field]
        else:
            fm[field] = ""
    if page_type in schema.PROVISIONAL_TYPES:
        fm["status"] = "provisional"
    fm.setdefault("domains", [])
    return fm


def stub_frontmatter(
    page_type: str,
    slug: str,
    title: str | None,
    sources: list[str],
    source_markdown: list[str],
    converter: str,
    location: str = "",
) -> dict:
    fm = _base_frontmatter(page_type, slug, title, sources, location)
    # Ingest stubs always record where the markdown came from (provenance).
    fm["source_markdown"] = list(source_markdown)
    fm["extracted_with"] = converter
    return fm


def stub_page(
    page_type: str,
    slug: str,
    title: str | None,
    sources: list[str],
    source_markdown: list[str],
    converter: str,
    location: str = "",
) -> str:
    fm = stub_frontmatter(page_type, slug, title, sources, source_markdown, converter, location)
    fm_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    heading = fm.get("name") or fm.get("title") or _humanize(slug)
    md = source_markdown[0] if source_markdown else ""
    return f"""---
{fm_yaml}
---

# {heading}

> **Stub created by `qappswiki ingest`.** Compile claims from the converted
> source below, cite each non-obvious claim inline as `(source: {md})`, set
> `domains`, link related pages with `[[wikilinks]]`, then set
> `provenance_status` and run `qappswiki run`.

## Summary

TODO: one-paragraph synthesis grounded in the source.

## Source

Converted markdown: `{md}`

## Related

- TODO: `[[...]]`
"""


def blank_page(page_type: str, slug: str, title: str | None = None) -> str:
    """An authoring stub with no source attached (for ``qappswiki new``).

    Required fields are present (so the page validates with no missing-field
    error) but empty, and the body guides a contributor through filling it in —
    the "anyone can populate" entry point.
    """
    fm = _base_frontmatter(page_type, slug, title, sources=[])
    fm_yaml = yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip()
    heading = fm.get("name") or fm.get("title") or _humanize(slug)
    return f"""---
{fm_yaml}
---

# {heading}

> **New `{page_type}` stub created by `qappswiki new`.** The required frontmatter
> fields above are present but empty — fill them in, write the body, list every
> source in `sources:` and cite non-obvious claims inline as `(source: <path>)`,
> link related pages with `[[wikilinks]]`, set `domains`, then run
> `qappswiki run` (it must pass before the page is committed).

## Summary

TODO: one-paragraph summary grounded in your sources.

## Related

- TODO: `[[...]]`
"""
