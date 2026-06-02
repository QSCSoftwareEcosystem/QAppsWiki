---
type: project-plan
status: active
updated: 2026-06-02
---

# QAppsWiki Plan

QAppsWiki is now a dedicated QSCSoftwareThrust repository. The immediate goal
is to turn the current proposal material into a working MVP that supports
OpenQEvo, Quantum Wiki / ChatQEC planning, and openQSE discovery workflows.

## Goal

Build a maintained markdown knowledge base that helps QSC users and agents
answer four practical questions:

1. What quantum software packages exist for a task?
2. How do we install, configure, and use them correctly?
3. How do we compose them into working QSC and QHPC workflows?
4. What sources, schema fields, and provenance support each answer?

## Operating Principles

- Markdown is the working substrate.
- The wiki is useful before automation; agents come after the manual workflow is
  stable.
- PDFs remain immutable raw sources, but extracted markdown is the default LLM
  input.
- MarkItDown is the front-door conversion workflow; Marker is used for
  higher-quality PDF extraction when equations, tables, or layout matter.
- Every synthesized claim should trace back to a source file.
- The wiki should compound: ingest once, then update linked package, how-to,
  and integration pages.
- QAppsWiki should reuse QSC Data Schema and OpenQEvo context-schema ideas
  instead of creating isolated metadata.

## Workstreams

### 1. Wiki Structure

Owner: Vicente initially; review with DS / AS / SE leads.

Deliverables:

- `CONTEXT.md` operating manual.
- `README.md` project charter.
- `index.md` content catalog.
- `log.md` append-only activity log.
- Directory conventions for `packages/`, `how-to/`, `integrations/`, `raw/`,
  `schema/`, and `docs/`.

Current status:

- Dedicated GitHub repo created and pushed: `QSCSoftwareThrust/QAppsWiki`.
- `README.md`, `PLAN.md`, `CONTEXT.md`, and `docs/llm-wiki-pattern.md` exist.
- `index.md`, `log.md`, `schema/`, and starter wiki pages still need to be
  created.

### 2. Source Ingest

Owner: Vicente initially; AS later automates.

Deliverables:

- Source workflow using MarkItDown and Marker-backed PDF extraction.
- Source provenance frontmatter convention.
- First source set for OpenQEvo and the remaining seed packages.
- First conversion examples that demonstrate PDF/report/doc-to-wiki flow.

Initial source priority:

- OpenQEvo README, docs, examples, adapter notes, context files, release notes,
  and relevant issues.
- Official package documentation for Qiskit, PennyLane, TNQVM, Stim, and any
  QHPC/QSC backends in the first integration pages.
- Relevant papers only when they clarify algorithms, capabilities, or
  integration assumptions.
- Quantum Wiki / ChatQEC planning sources when they define reusable AS needs.

### 3. Schema

Owner: DS lead after review.

Deliverables:

- `schema/frontmatter-v0.md`.
- Controlled vocabularies for capabilities, hardware targets, package maturity,
  interface types, source types, and provenance status.
- A mapping to OpenQEvo context-schema fields where possible.
- Optional projection path for Dataview, JSON, LinkML, or graph export.

First schema entities:

- `package`
- `how-to`
- `integration`
- `source`
- `capability`
- `hardware-target`
- `interface`

### 4. Agent Workflow

Owner: AS lead after review.

Deliverables:

- Manual ingest workflow encoded in `CONTEXT.md`.
- Query workflow that answers from wiki pages and cites provenance.
- Lint workflow for stale claims, broken links, missing provenance, and
  contradictions.
- Decision on first implementation interface: MCP, direct model API, CLI, or
  hybrid.
- Reusable workflow pattern for Quantum Wiki / ChatQEC knowledge-base work.

MVP rule:

The first version can be manual LLM operation following `CONTEXT.md`.
Automation comes after the source and page conventions are stable.

### 5. Infrastructure

Owner: SE lead after review.

Deliverables:

- Repo hygiene and branch/review conventions.
- Basic validation for required files.
- Link/frontmatter validation.
- Packaging path for ingest/query/lint tools once they exist.
- Access path for users and agents: plain markdown repo first, then static
  site, CLI, MCP server, REST endpoint, or staged combination.

MVP rule:

Do not block the wiki on a service. A useful markdown repo comes first.

### 6. QSC Integration

Owner: Vicente coordinates; DS / AS / SE / HW provide inputs.

Deliverables:

- OpenQEvo package page.
- OpenQEvo how-to page for first-run or adapter usage.
- First integration page: Qiskit to OpenQEvo.
- A short QSC integration note that explains how QAppsWiki feeds openQSE,
  Quantum Wiki / ChatQEC, and QHPC workflow discovery.
- Companion entry in `thrust-wiki/` once the naming and MVP scope are stable.

## Cross-Project Milestones

| Milestone | Target | Lead project | Deliverable |
|-----------|--------|--------------|-------------|
| M0: Repo live | 2026-06 | SE / Vicente | Private GitHub repo created, initial charter and plan pushed |
| M1: MVP scaffold | 2026-06 | SE / Vicente | `index.md`, `log.md`, `schema/frontmatter-v0.md`, and seed directories |
| M2: OpenQEvo slice | 2026-06 | DS / AS / SE | OpenQEvo package page, first how-to, first integration page |
| M3: Source workflow | 2026-06 | AS / SE | MarkItDown + Marker conversion workflow documented and demonstrated |
| M4: Seed corpus | 2026-07 | DS / AS | Five seed package pages grounded in source markdown |
| M5: Query loop | 2026-07 | AS | Manual query workflow answers from wiki pages with provenance |
| M6: Repo checks | 2026-08 | SE | Required-file, link, and frontmatter validation |
| M7: MVP review | 2026-08 | DS / AS / SE / HW | Demo QAppsWiki answering package-selection and workflow-composition questions |

## Project Action Items

### Data Schema

- [ ] Name a DS DRI for QAppsWiki.
- [ ] Draft `schema/frontmatter-v0.md`.
- [ ] Define required fields for `package`, `how-to`, `integration`, and
      `source` pages.
- [ ] Define controlled vocabularies for capabilities, hardware targets,
      package maturity, source type, interface type, and provenance status.
- [ ] Map frontmatter v0 to OpenQEvo context-schema concepts.
- [ ] Review the first five seed package pages for schema completeness.
- [ ] Define whether a machine-readable export is needed for openQSE or AS
      workflows.

### Agentic Software

- [ ] Name an AS DRI for QAppsWiki.
- [ ] Convert `CONTEXT.md` into explicit ingest, query, and lint workflows.
- [ ] Define the first ingest prompt/workflow for source markdown in `raw/md/`.
- [ ] Define the query workflow: read `index.md`, select relevant wiki pages,
      answer from wiki pages, and cite sources.
- [ ] Define the lint workflow: stale pages, missing provenance, broken links,
      contradictions, orphan pages, and missing package/how-to/integration
      pages.
- [ ] Evaluate whether the first automated interface should be MCP, direct API,
      CLI, or hybrid.
- [ ] Align QAppsWiki workflow with Quantum Wiki / ChatQEC planning.

### Software Engineering

- [ ] Confirm repo layout and branch/review conventions.
- [ ] Add basic validation for required files: `CONTEXT.md`, `PLAN.md`,
      `README.md`, `index.md`, `log.md`, and `schema/frontmatter-v0.md`.
- [ ] Add frontmatter validation once DS schema v0 exists.
- [ ] Add link validation for internal wiki links and source file references.
- [ ] Decide first access path: markdown repo, static site, CLI, REST endpoint,
      MCP server, or staged combination.
- [ ] Define how QAppsWiki reuses or extends OpenQEvo packaging/CI work.
- [ ] Support the MVP demo with a repeatable local command or documented
      workflow.

### Hybrid Workflows / Compilation Tools

- [ ] Identify the first QHPC-relevant integration target for OpenQEvo.
- [ ] Identify hardware/backend metadata that should appear on package and
      integration pages.
- [ ] Capture compiler/IR interface assumptions when an integration crosses CT
      or HW boundaries.

## Seed Corpus

Start with five packages, because they cover internal application code,
frameworks, simulator targets, and integration roles.

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
- [ ] Create starter package page: `packages/openqevo.md`.
- [ ] Draft first `how-to/` page from OpenQEvo install or adapter usage.
- [ ] Draft first `integrations/` page: Qiskit to OpenQEvo.
- [ ] Pick the first source for each seed package.
- [ ] Convert any PDFs with MarkItDown / Marker before ingest.
- [ ] File companion page in `thrust-wiki/themes/qapps-wiki.md` after the name
      is stable.

## Open Decisions

- Name: keep `QAppsWiki` or align with openQSE branding?
- Audience: QSC internal first or external community from day one?
- Hosting: private until MVP or public early?
- Agent stack: MCP, direct API, CLI, or hybrid?
- DRIs: who signs off for DS, AS, SE, and HW?
- Marker integration: use Marker directly, through MarkItDown plugin support,
  or as a fallback conversion path for high-value PDFs?
