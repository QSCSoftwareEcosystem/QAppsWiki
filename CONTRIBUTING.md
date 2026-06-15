---
type: operating-manual
status: active
updated: 2026-06-15
owner: Vicente Leyton
tags: [contributing, authoring, tooling]
---

# Contributing to QAppsWiki

QAppsWiki is a maintained Markdown knowledge base for quantum computing. The
structure and the tooling are designed so that **populating it is a
fill-in-the-blanks job**: scaffold a schema-valid page, fill it in, and let the
`qappswiki` engine check it. You should never have to hand-craft frontmatter or
guess what fields a page needs.

This guide covers the everyday authoring loop. For the *why* and the deeper
conventions, see [`CONTEXT.md`](CONTEXT.md) (operating manual),
[`schema/frontmatter-v0.md`](schema/frontmatter-v0.md) (the page schema), and
[`PLAN.md`](PLAN.md) (direction).

## Setup (once)

```bash
uv venv && uv pip install -e "tools[dev]"     # or: python -m venv .venv && pip install -e "tools[dev]"
```

This installs the `qappswiki` CLI. Run everything inside the project venv.

## The authoring loop

```
qappswiki new <type> <slug>   →   fill in the page   →   qappswiki run   →   commit
```

### 1. Scaffold a page

Pick a page type and scaffold a blank, schema-valid stub:

```bash
qappswiki new package qiskit          # -> packages/qiskit.md
qappswiki new concept time-evolution  # -> concepts/time-evolution.md
qappswiki new how-to install-stim     # -> how-to/install-stim.md
qappswiki new integration qiskit-to-openqevo
```

Page types: `package`, `concept`, `how-to`, `integration`, `source`, and the
provisional `workflow` / `qec-artifact` / `benchmark`. A bare slug lands in the
type's conventional directory; pass an explicit path (`packages/qiskit.md`) to
override. The stub already contains every required frontmatter field — empty,
ready to fill. (To start from a PDF instead, use `qappswiki ingest <pdf>`.)

### 2. Fill it in

- Complete the frontmatter (the required fields are present but empty).
- Write the body.
- **Provenance is required.** List every source in `sources:`, and cite
  non-obvious claims inline as `(source: <path>)`. Every inline `(source:)` path
  **must** also appear in `sources:` — the validator enforces this as an error.
- Tag `domains:` from the controlled vocabulary.
- Link related pages with `[[wikilinks]]` and `related_*` fields so the page
  isn't an orphan, and link it from `index.md`.

### 3. Validate

```bash
qappswiki run            # validate + build graph + report
qappswiki run --strict   # also fail on warnings (the pre-commit/CI bar)
```

`qappswiki run` must pass with **0 errors** before a page is committed. It writes
`wiki-out/VALIDATION_REPORT.md`, `wiki-out/GRAPH_REPORT.md`, and the graph
(`graph.json` / `graph.html`). Fix every error; clear warnings where you can.

## Adding sources in bulk (discover → promote)

When you drop new converted sources under `raw/md/`, the engine can propose
candidate concept pages for you:

```bash
qappswiki extract                       # stage INFERRED candidates from raw/md/
qappswiki promote <id|title>            # turn a reviewed candidate into a concepts/ page
qappswiki promote --all --min-sources 2 # batch-promote well-supported candidates
```

Extraction never writes authored pages — it only stages candidates. Promotion is
the single path into the authored layer, and it produces a `needs-verification`
draft you then fill in and validate like any other page.

## Freshness (software pages)

Package pages can declare a `version_source` (PyPI / GitHub / …) and a
`version_scope`. `qappswiki freshness` checks them against upstream (online) and
caches the result; the next `qappswiki run` stamps staleness onto the graph and
rolls it up to the integrations and applications that build on stale software. A
nightly GitHub Action reports staleness out-of-band — it never blocks a build.

## Querying the wiki

```bash
qappswiki query <term>            # find nodes
qappswiki explain <node-id>       # a node and its edges
qappswiki cite <node-id>          # the sources behind a node (page- + claim-level)
qappswiki path <a> <b>            # shortest path between two pages
qappswiki serve                   # MCP server, so agents query the graph
```

## Checklist before you commit

- [ ] `qappswiki run` passes with 0 errors.
- [ ] Every inline `(source:)` is also in `sources:`.
- [ ] `domains:` set; the page is linked (`[[...]]`) and listed in `index.md`.
- [ ] `provenance_status` reflects reality (`needs-verification` until checked).
- [ ] A line added to `log.md`.
