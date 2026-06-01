---
type: project-plan
status: draft
updated: 2026-04-29
---

# QAppsWiki Plan

This page organizes what we are going to do in QAppsWiki. The goal is to move
from a proposal to a working, LLM-maintained knowledge base for quantum
software applications.

## Goal

Build a maintained markdown wiki that helps QSC users and agents answer three
questions:

1. What quantum software packages exist for a task?
2. How do we install, configure, and use them correctly?
3. How do we compose them into working workflows?

## Operating Principles

- Markdown is the working substrate.
- PDFs remain immutable raw sources, but extracted markdown is the default LLM
  input.
- Every synthesized claim should trace back to a source file.
- The wiki should compound: ingest once, then update linked package, how-to,
  and integration pages.
- Start narrow with a seed corpus before building infrastructure.

## Workstreams

### 1. Wiki Structure

Owner: Vicente initially; review with DS / AS / SE leads.

Deliverables:
- `CONTEXT.md` operating manual.
- `index.md` content catalog.
- `log.md` append-only activity log.
- Directory conventions for `packages/`, `how-to/`, `integrations/`, `raw/`,
  `schema/`, and `docs/`.

Status:
- `CONTEXT.md` exists in draft.
- Core directories are being scaffolded.

### 2. Source Ingest

Owner: Vicente initially; AS later automates.

Deliverables:
- Source workflow using MarkItDown:
  `mid raw/pdf/<source>.pdf -o raw/md/<source>.md`.
- Source provenance frontmatter convention.
- First source set for the seed packages.

Initial source priority:
- Official package documentation.
- Release notes / changelogs.
- Installation guides.
- Relevant papers only when they clarify capabilities or algorithms.
- Existing OpenQEvo repo docs and issues.

### 3. Schema

Owner: DS lead after review.

Deliverables:
- Frontmatter schema v0.
- Controlled vocabularies for capabilities, hardware targets, package maturity,
  and source types.
- Optional projection path for Dataview, JSON, or graph database export.

First schema entities:
- `package`
- `how-to`
- `integration`
- `source`
- `capability`
- `hardware-target`

### 4. Agent Workflow

Owner: AS lead after review.

Deliverables:
- Ingest workflow.
- Query workflow.
- Lint workflow.
- Decision on implementation interface: MCP, direct model API, local CLI, or
  hybrid.

MVP rule:
The first version can be manual LLM operation following `CONTEXT.md`. Automation
comes after the workflow is stable.

### 5. Infrastructure

Owner: SE lead after review.

Deliverables:
- Repo hygiene and CI checks.
- Link/frontmatter validation.
- Optional static site or searchable endpoint.
- Packaging path for ingest/query/lint tools once they exist.

MVP rule:
Do not block the wiki on a service. A useful markdown repo comes first.

## Cross-Project Milestones

These milestones organize DS, AS, and SE participation around concrete
deliverables. Dates are draft targets for discussion with the project leads.

| Milestone | Target | Lead project | Deliverable |
|-----------|--------|--------------|-------------|
| M0: Alignment | 2026-05 | DS / AS / SE | Confirm scope, DRI, seed corpus, and MVP definition |
| M1: Schema v0 | 2026-05 | DS | Frontmatter schema and controlled vocabularies for the first wiki pages |
| M2: Manual ingest loop | 2026-06 | AS | Documented ingest/query/lint workflows using `CONTEXT.md` |
| M3: Repo checks | 2026-06 | SE | Basic validation for links, frontmatter, and required files |
| M4: Seed corpus catalogued | 2026-07 | DS / AS | Five seed package pages grounded in source markdown |
| M5: First integrations | 2026-08 | AS / SE | At least two integration pages and a runnable/queryable access path |
| M6: MVP review | 2026-08 | DS / AS / SE | Demo query over the wiki and decide Phase 2 automation scope |

## Project Action Items

### Data Schema

DS owns the structure of the information represented in wiki pages.

- [ ] Name a DS DRI for QAppsWiki.
- [ ] Draft `schema/frontmatter-v0.md`.
- [ ] Define required fields for `package`, `how-to`, `integration`, and
      `source` pages.
- [ ] Define controlled vocabularies for capabilities, hardware targets,
      package maturity, source type, and provenance status.
- [ ] Decide whether the schema should extend the OpenQEvo context schema
      directly or map to it through a separate projection.
- [ ] Review the first five seed package pages for schema completeness.
- [ ] Define what a machine-readable export should look like, if needed:
      Dataview, JSON, graph DB, or another projection.

### Agentic Software

AS owns the LLM workflows that maintain and query the wiki.

- [ ] Name an AS DRI for QAppsWiki.
- [ ] Convert the manual process in `CONTEXT.md` into explicit ingest, query,
      and lint workflows.
- [ ] Define the first ingest prompt/workflow for source markdown in `raw/md/`.
- [ ] Define the query workflow: read `index.md`, select relevant wiki pages,
      answer from wiki pages, and cite sources.
- [ ] Define the lint workflow: stale pages, missing provenance, broken links,
      contradictions, orphan pages, and missing package/how-to/integration
      pages.
- [ ] Evaluate whether the first automated interface should be MCP, direct API,
      CLI, or hybrid.
- [ ] Produce one end-to-end demo: ingest a source markdown file and update at
      least one package page plus `index.md` and `log.md`.

### Software Engineering

SE owns the repository, validation, and deployable access path.

- [ ] Name an SE DRI for QAppsWiki.
- [ ] Confirm repo layout and branch/review conventions.
- [ ] Add basic validation for required files: `CONTEXT.md`, `PLAN.md`,
      `index.md`, `log.md`, and `schema/frontmatter-v0.md`.
- [ ] Add frontmatter validation once DS schema v0 exists.
- [ ] Add link validation for internal wiki links and source file references.
- [ ] Decide the first access path: plain markdown repo, static site, CLI,
      REST endpoint, MCP server, or staged combination.
- [ ] Define how QAppsWiki reuses or extends OpenQEvo packaging/CI work.
- [ ] Support the MVP demo with a repeatable local command or documented
      workflow.

## Seed Corpus

Start with five packages, because the proposal already names them and they give
good coverage across application, framework, simulator, and integration roles.

| Package | Reason |
|---------|--------|
| OpenQEvo | Internal integration testbed and first catalogued QApp |
| Qiskit | Common circuit framework and OpenQEvo adapter target |
| PennyLane | Differentiable quantum programming and OpenQEvo adapter target |
| TNQVM | QSC/HPC-relevant simulator target |
| Stim | Focused high-performance stabilizer simulator |

## MVP Definition

Phase-1 MVP is complete when:

- The five seed packages each have one `packages/` page.
- Each seed package has at least one source in `raw/md/`.
- At least three `how-to/` pages exist.
- At least two `integrations/` pages exist.
- `index.md` and `log.md` are maintained.
- `schema/frontmatter-v0.md` defines the first usable page schema.
- A human can ask a package-selection or workflow-composition question and get
  an answer grounded in wiki pages, not raw PDFs.

## Immediate Next Actions

- [ ] Create `index.md` and `log.md`.
- [ ] Create `schema/frontmatter-v0.md`.
- [ ] Create starter package pages for the seed corpus.
- [ ] Pick the first source for each seed package.
- [ ] Convert any PDFs with MarkItDown before ingest.
- [ ] Draft first `how-to/` page from OpenQEvo or Qiskit.
- [ ] Draft first `integrations/` page: Qiskit to OpenQEvo.
- [ ] File companion page in `thrust-wiki/themes/qapps-wiki.md` after the name
      is stable.

## Open Decisions

- Name: keep `QAppsWiki` or align with openQSE branding?
- Audience: QSC internal first or external community from day one?
- Hosting: private until MVP or public early?
- Agent stack: MCP, direct API, CLI, or hybrid?
- DRI: who signs off for DS, AS, and SE?
