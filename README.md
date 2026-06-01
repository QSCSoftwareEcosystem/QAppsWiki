---
type: project-proposal
status: draft
created: 2026-04-24
updated: 2026-04-24
proposer: Vicente Leyton
integrates: [data-schema, agentic-software, software-engineering]
subsumes: [openqevo]
pattern: llm-wiki
---

# QAppsWiki — an LLM-maintained knowledge base for quantum computing applications

> **Status:** Draft proposal, 2026-04-24. Name is a placeholder.
> **Scope:** A cross-project integration initiative that **supersets** OpenQEvo and spans Data Schema (DS), Agentic Software (AS), and Software Engineering (SE).
> **Design pattern:** LLM Wiki (see [`docs/llm-wiki-pattern.md`](docs/llm-wiki-pattern.md)).
> **Work plan:** See [`PLAN.md`](PLAN.md).

## 1. Motivation

Quantum software is fragmented across dozens of packages (Qiskit, PennyLane, Cirq, TKET, TNQVM, Stim, OpenQEvo, …), each with its own docs, conventions, interfaces, and gotchas. Users — and agents acting on their behalf — spend disproportionate effort on:

- **Discovery** — what exists for a given task, at what maturity, on what hardware.
- **Usage** — how to install, configure, and drive each package correctly.
- **Composition** — how to wire packages together into end-to-end workflows.

Most existing approaches (qBraid, ecosystem lists, RAG over docs) either flatten the ecosystem to a registry or rediscover knowledge from scratch on every query. **QAppsWiki takes a different approach: an LLM-maintained, compounding knowledge base** where every new source strengthens an evolving, interlinked synthesis — the LLM Wiki pattern.

## 2. Why the LLM Wiki pattern

The classical RAG approach (retrieve raw chunks at query time, let the model re-synthesize) has a known ceiling: **nothing is built up**. A subtle question that requires connecting five packages forces the model to re-derive the connection every time.

The LLM Wiki pattern inverts this:

- Sources are ingested **once**; the LLM writes summary and entity pages into a persistent markdown wiki, and updates cross-references across the existing wiki when new sources contradict, extend, or refine prior pages.
- Queries read the **wiki**, not the raw sources. The synthesis is already there.
- The wiki **compounds** — richer with every source, every question, every lint pass.

Existence proof: the `thrust-wiki/` adjacent to this folder is already an LLM Wiki (for Software Thrust project management). Same pattern, different domain. QAppsWiki applies it to the quantum-software ecosystem.

Full pattern spec: [`docs/llm-wiki-pattern.md`](docs/llm-wiki-pattern.md).

## 3. The three pillars (the shape of the wiki)

The wiki's content is organized around three pillars. They are **not** three separate systems — they are three kinds of pages in one interlinked wiki.

### Pillar 1 — **What** (software catalog)
Entity pages, one per quantum software package:
- Versions, licenses, maintainers, activity signals.
- Capabilities (simulation, compilation, error mitigation, device control, …).
- Hardware targets.

### Pillar 2 — **How** (usage knowledge)
How-to pages, one per (package, task) pair:
- Installation + environment recipes (spack / conda / pip).
- Canonical examples, common patterns, gotchas.
- Version-specific quirks.
- Benchmarks and resource expectations.

### Pillar 3 — **Integration** (composition)
Integration pages, one per (package-A, package-B, …) pipeline:
- Interface contracts, I/O schemas, type mappings.
- Known working pipelines (e.g., Qiskit → OpenQEvo → TNQVM).
- Shim / adapter patterns.
- Failure modes at the seams.

All three pillars live in the same markdown graph. A `Qiskit` entity page links to how-to pages for Qiskit, which link to integration pages where Qiskit composes with other packages, which link back to those other packages' entity pages. **The graph is the value.**

## 4. Architecture — three LLM-Wiki layers × three thrust projects

The LLM Wiki pattern has three layers: **raw sources**, **the wiki**, and **the schema**. Each maps cleanly onto one thrust project's scope.

```
┌─────────────────────────────────────────────────────────────────┐
│  Consumers: QSC scientists, external users, downstream agents   │
└─────────────────────────────────────────────────────────────────┘
                              │
                       queries & composes
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  THE WIKI (markdown graph)            ← AS runs ingest/query/lint│
│  ─ entity / how-to / integration pages                          │
│  ─ index.md, log.md                                             │
│  ─ structured YAML frontmatter on every page                    │
└─────────────────────────────────────────────────────────────────┘
             ▲                                      ▲
             │ structures                           │ maintains
             │                                      │
┌─────────────────────────┐            ┌────────────────────────────┐
│  THE SCHEMA (DS-owned)  │            │  AGENTS (AS-owned)         │
│  ─ frontmatter fields   │            │  ─ ingest agent            │
│  ─ entity types         │            │  ─ query agent             │
│  ─ DB projection        │            │  ─ lint agent              │
│                         │            │  ─ orchestrator (Phase 2)  │
└─────────────────────────┘            └────────────────────────────┘
                       ▲                                ▲
                       └──────── read from ─────────────┘
                                      │
┌─────────────────────────────────────────────────────────────────┐
│  RAW SOURCES (immutable)                                        │
│  docs, repos, release notes, papers, release benchmarks, issues │
└─────────────────────────────────────────────────────────────────┘
                              │
                   INFRA layer (SE-owned)
          repo, git, CI/CD, hosting, packaging, search
┌─────────────────────────────────────────────────────────────────┐
│  SE: makes all of the above runnable, deployable, installable   │
└─────────────────────────────────────────────────────────────────┘
```

### DS — the schema layer
DS owns the **structured fields** that every wiki page carries (YAML frontmatter) plus an optional projection to a queryable DB. This is the natural extension of DS's OpenQEvo context-schema work (PR #5, merged 2026-04-02).

- Defines entity types: `QApp`, `Capability`, `Interface`, `HardwareTarget`, `Example`, `Integration`, `Source`.
- Defines required fields per type (provenance, version, last-updated, source links).
- Defines vocabularies / controlled tags.
- Optionally: a build step that reads all markdown frontmatter and emits a graph DB (or Dataview-style projection) for programmatic queries.

This is **data schema**, distinct from the wiki-maintenance `CONTEXT.md` (below).

### AS — the agent layer
AS owns the LLM agents that implement the three LLM-Wiki operations plus, later, orchestration.

- **Ingest agent** — reads a raw source, drafts or updates summary pages, updates entity/how-to/integration pages, appends to `log.md`, keeps `index.md` current.
- **Query agent** — answers user questions using the wiki (not the raw sources), with citations back to wiki pages. Good answers are filed back as new wiki pages so the exploration compounds.
- **Lint agent** — periodic health-check: contradictions, stale claims, orphan pages, missing entities, broken links.
- **Orchestrator agent (Phase 2)** — given a user task, reads the integration pillar and composes q-apps into a runnable pipeline or callable API.

The agent stack (MCP / direct model API / RAG as a sub-component / local vs. hosted) is an **implementation choice, not part of the pattern**. Phase 0 picks it after surveying options.

### SE — the infra layer
SE owns everything that makes the wiki + agents real software.

- The wiki is a git repo of markdown; SE owns the repo hygiene, CI, branch protection.
- Ingest/query/lint agents packaged and runnable locally and as a service.
- Hosting: a search + query endpoint consumers can hit (CLI, REST, MCP server, whichever we pick in Phase 0).
- Reuses / extends SE's in-flight OpenQEvo CI/packaging work (issue #1).

### The wiki-maintenance schema
A `CONTEXT.md` at the root of the wiki tells the LLM *how* to maintain it — ingest workflow, page templates, cross-referencing conventions, lint checklist. This is the QAppsWiki operating manual, separate from the DS-owned frontmatter/schema specification. Not owned by a single project — drafted collaboratively, iterated over time.

### PDF source extraction
PDFs remain immutable raw sources, but the LLM should prioritize the markdown extracted from them because it is cheaper, cleaner, and more token-efficient than reading PDFs directly. Use MarkItDown:

```bash
mid raw/pdf/<source>.pdf -o raw/md/<source>.md
```

Any wiki page derived from a PDF should link both the original PDF and the extracted markdown representation in frontmatter, with the markdown listed as the preferred LLM-readable source:

```yaml
sources:
  - raw/pdf/<source>.pdf
source_markdown:
  - raw/md/<source>.md
extracted_with: markitdown
```

Read the original PDF only when the markdown extraction is incomplete, ambiguous, missing important figures/tables, or needs verification.

## 5. Relationship to OpenQEvo, openQSE, external registries

### OpenQEvo (**decided: QAppsWiki supersets OpenQEvo**)
OpenQEvo is a single quantum application (Trotterization library) and the thrust's current integration testbed. **QAppsWiki subsumes OpenQEvo's integration scope**: OpenQEvo becomes one catalogued entry in the What pillar, with its how-tos and integrations filed under Pillars 2 and 3.

Per-project implications:
- DS's OpenQEvo context-schema work becomes the **seed** for QAppsWiki's frontmatter spec.
- AS's MCP-over-RAG recommendation for OpenQEvo #3 becomes a candidate implementation for QAppsWiki's agent stack (to be decided in Phase 0).
- SE's OpenQEvo CI/packaging scope (issue #1) extends to QAppsWiki — one CI pipeline, one package pattern, covering both.
- OpenQEvo v0.1.0 (2026-06-15) still ships as scoped; QAppsWiki is how it gets *discovered and composed* going forward.

### openQSE
openQSE is the thrust's target unified quantum–HPC ecosystem. QAppsWiki is a strong candidate for the **discovery and composition surface** of openQSE.

### External registries
Phase-0 deliverable: survey qBraid, Qiskit ecosystem registry, PennyLane plugins, Unitary Fund ecosystem lists. Questions: what can we wrap or federate rather than rebuild? Do any expose structured data we can ingest directly?

## 6. Phased plan (rough)

**Phase 0 — Align (now → 2026-05)**
- Confirm scope with DS / AS / SE leads.
- External-registry survey (1-page findings).
- Draft wiki-maintenance `CONTEXT.md`.
- Pick Phase-1 seed corpus (5 q-apps — candidates: Qiskit, PennyLane, OpenQEvo, TNQVM, Stim).
- Named DRI per thrust.

**Phase 1 — LLM Wiki MVP (2026-05 → 2026-08)**
- DS: frontmatter schema v0, extending OpenQEvo context schema.
- AS: ingest + query agents working end-to-end on one source at a time.
- SE: repo + CI + basic deployable query service.
- 5 seed q-apps fully catalogued (What + How + at least one Integration page each).

**Phase 2 — Orchestrator (2026-09 → 2026-12)**
- First orchestrator agent composes a real pipeline from a user task spec (candidate: something that discovers and drives OpenQEvo).
- Catalog grows to ~20 packages.
- First external-user trial.

**Phase 3 — Scale (2027)**
- Open contributions.
- Measure impact (time-to-first-run, discovery quality) on real QSC workflows.
- Hand-off / integration with openQSE umbrella.

## 7. Open questions

1. ~~**Scope vs. OpenQEvo** — superset or sibling?~~ **Resolved 2026-04-24: superset.** OpenQEvo becomes a catalogued entry; its integration scope folds into QAppsWiki.
2. **Name** — `QAppsWiki` is a placeholder. Tie into `openQSE` branding?
3. **Audience** — QSC internal first, or external community from day one?
4. **Hosting** — public GitHub repo? Private until MVP?
5. **External registry alignment** (Phase-0 deliverable) — wrap / federate qBraid / Qiskit ecosystem / PennyLane plugins, or build fresh? Do any expose structured, ingestable data?
6. **Agent stack** — MCP as primary interface? Direct model API? Something else? Decided in Phase 0 after the registry survey.
7. **Leads** — named DRI from each of DS, AS, SE.
8. **Wiki-maintenance `CONTEXT.md`** — who drafts the first version? (Suggestion: Vicente drafts, leads review, agent iterates it live during Phase 1.)

## 8. Next steps

- [ ] Vicente — walk Seth / Thomas / Tirthankar through this doc at the next 1:1; close Q2, Q6, Q7.
- [ ] External-registry survey → `docs/external-registries.md` (1-page).
- [ ] DS (Thomas) — propose frontmatter schema v0 extending OpenQEvo context schema.
- [ ] AS (Tirthankar / Sharmin) — evaluate agent stack options (MCP / direct API / hybrid) given the LLM Wiki pattern's non-RAG framing.
- [ ] SE (Seth) — outline CI + packaging; reuse OpenQEvo work.
- [ ] Pick Phase-1 seed corpus (5 q-apps).
- [ ] Draft wiki-maintenance `CONTEXT.md` (page templates, ingest/query/lint workflows).
- [ ] File companion page in `thrust-wiki/themes/qapps-wiki.md` once name is fixed.

## 9. Repo layout (current)

```
QAppsWiki/
├── CONTEXT.md                      # LLM operating manual
├── PLAN.md                         # project work plan
├── README.md                       # this file
└── docs/
    └── llm-wiki-pattern.md         # reference: the LLM Wiki pattern spec
```

Intentionally minimal. No code yet — design-stage.
