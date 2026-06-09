---
type: project-charter
status: active
created: 2026-04-24
updated: 2026-06-08
proposer: Vicente Leyton
integrates: [data-schema, agentic-software, software-engineering, hybrid-workflows, openqevo, openqse]
pattern: llm-wiki
visibility: private-mvp
---

# QAppsWiki

QAppsWiki is an LLM-maintained knowledge base for quantum computing. It spans
quantum information, quantum algorithms, quantum simulation (simulating quantum
systems on quantum computers), quantum software and programming languages, and
quantum implementation and hardware, together with the packages, integrations,
and workflows that realize them.

It is a maintained markdown wiki plus an emerging agent workflow, designed to
help users and downstream agents discover, understand, and compose quantum
computing knowledge and software. QAppsWiki is developed in the QSC Software
Thrust and driven first by OpenQEvo, openQSE, and Quantum Wiki / ChatQEC, but
the knowledge graph itself is general to quantum computing rather than scoped to
a single project.

The repository is private during MVP development:
`QSCSoftwareThrust/QAppsWiki`.

## Current Position

QAppsWiki is no longer only a proposal. As of 2026-06-08, it is a dedicated
repository seeded from the QSC Software Thrust workspace, with an initial
OpenQEvo slice and an AS-assigned intern path for the LLM-Wiki implementation.
Its first active drivers are three QSC Software Thrust needs:

- **OpenQEvo support**: turn OpenQEvo docs, papers, examples, and context files
  into catalogued package, how-to, and integration knowledge.
- **Quantum Wiki / ChatQEC support**: provide the reusable LLM-wiki pattern for
  AS knowledge-base and conversational workflows. The near-term implementation
  is a RAG-like Markdown compilation workflow: gather concepts from source
  markdown, synthesize maintained wiki pages, and create interlink connections
  across the corpus. It is not intended to be a conventional chunk-retrieval
  RAG system.
- **openQSE integration**: become the discovery and composition surface for
  quantum software packages, schemas, adapters, and QHPC workflows.

### Scope

QAppsWiki is general to quantum computing. The QSC drivers above set the first
ingest priorities, but package, concept, how-to, and integration pages may
cover any quantum computing topic, including:

- quantum information and foundations;
- quantum algorithms and quantum simulation;
- quantum software, SDKs, and programming languages / IRs;
- quantum implementation, hardware, and control;
- quantum error correction and fault tolerance;
- compilation, simulation, benchmarking, and quantum-HPC integration.

Each page declares its topic areas with a `domains` field, defined in
[`schema/frontmatter-v0.md`](schema/frontmatter-v0.md). A page about a general
quantum computing topic is in scope even when no QSC project uses it yet.

## Goals

QAppsWiki has four concrete goals for the current QSC cycle.

### 1. Build a Quantum Computing Knowledge Graph

Maintain an interlinked markdown graph describing quantum computing concepts,
packages, languages, hardware targets, algorithms, and simulation methods, and
the integration points between them — not only software packages.

Primary page families:

- `packages/`: what exists.
- `concepts/`: what ideas, capabilities, interfaces, and patterns recur.
- `how-to/`: how to install, configure, and use packages for specific tasks.
- `integrations/`: how packages compose into working pipelines.
- `schema/`: structured page metadata and controlled vocabularies.
- `raw/`: immutable source material and extracted markdown.

### 2. Make Source Ingest Reproducible

Use the MarkItDown + Marker workflow to convert papers, PDFs, reports, and
technical docs into markdown before LLM synthesis. The goal is not just text
conversion; it is a repeatable source-to-wiki path with provenance.

Expected source path:

```bash
mid raw/pdf/<source>.pdf -o raw/md/<source>.md
```

Pages derived from converted sources should preserve both source layers:

```yaml
sources:
  - raw/pdf/<source>.pdf
source_markdown:
  - raw/md/<source>.md
extracted_with: markitdown
```

Marker is the higher-quality PDF extraction option when equations, tables, or
layout-sensitive content matter. MarkItDown is the front-door conversion
interface; Marker improves the PDF leg of that workflow.

### 3. Align With QSC Data and Provenance

QAppsWiki should use Data Schema work instead of inventing a parallel metadata
model. The first schema target is a frontmatter v0 that extends or maps cleanly
to OpenQEvo context-schema ideas and QSC provenance needs.

Near-term schema entities:

- `package`
- `capability`
- `hardware-target`
- `interface`
- `how-to`
- `integration`
- `source`

This gives AS agents and future openQSE services a structured substrate for
querying the wiki without losing human-readable markdown.

### 4. Support Agentic Composition

QAppsWiki is the knowledge substrate for AS agents that answer questions,
perform wiki maintenance, and eventually compose workflows. The MVP keeps the
first loop manual but explicit:

1. Ingest source markdown.
2. Update package/how-to/integration pages.
3. Update `index.md` and `log.md`.
4. Answer user questions from wiki pages, not raw documents.
5. File useful answers back into the wiki when they become reusable knowledge.

The longer-term AS interface may be MCP, CLI, direct API, or a hybrid. The
important constraint is that QAppsWiki compounds knowledge instead of forcing
agents to re-synthesize from raw chunks on every query.

## Integration in QSC

QAppsWiki connects the Software Thrust projects around a shared artifact.

| Project | QAppsWiki role |
|---------|----------------|
| OpenQEvo | First internal package and integration testbed; source of examples, adapters, schema patterns, and release documentation. |
| Data Schema | Owns frontmatter schema, controlled vocabularies, provenance, and optional machine-readable export. |
| Agentic Software | Owns ingest, query, lint, and future orchestration workflows over the wiki. |
| Software Engineering | Owns repo hygiene, validation, CI, deployment/access paths, and packaging of tools. |
| Hybrid Workflows | Provides QHPC workflow targets, simulator/backend integration needs, and hardware/workflow constraints. |
| Compilation Tools | Provides compiler/IR and lowering interfaces that integration pages should capture when available. |
| openQSE | Consumes QAppsWiki as a package discovery, documentation, and workflow-composition surface. |

## Relationship to OpenQEvo

OpenQEvo remains a scoped software library. QAppsWiki is the knowledge and
integration layer around it.

Concretely:

- OpenQEvo becomes the first `packages/` entry.
- OpenQEvo installation, examples, adapters, and release notes become `how-to/`
  pages.
- OpenQEvo pipelines with Qiskit, PennyLane, TNQVM, Qrack, and QHPC execution
  targets become `integrations/` pages.
- OpenQEvo context-schema work seeds QAppsWiki frontmatter and provenance.
- The MarkItDown + Marker workflow helps convert OpenQEvo-related papers and
  technical sources into wiki-ready markdown.

## MVP Definition

The first useful version is complete when:

- Five seed packages have package pages: OpenQEvo, Qiskit, PennyLane, TNQVM,
  and Stim.
- Each seed package has at least one source in `raw/md/`.
- At least three how-to pages and two integration pages exist.
- `index.md`, `log.md`, and `schema/frontmatter-v0.md` are maintained.
- A user can ask a package-selection or workflow-composition question and get
  an answer grounded in wiki pages with provenance.

## Current Implementation Focus

The next implementation step is to make the Markdown compilation loop explicit
enough for AS to automate:

1. collect or convert source material into `raw/md/`;
2. extract concepts, packages, interfaces, capabilities, and source-backed
   claims;
3. update maintained pages in `packages/`, `concepts/`, `how-to/`, and
   `integrations/`;
4. create or repair wiki links between related concepts and pages;
5. update `index.md`, `log.md`, and provenance frontmatter.

This workflow should scale by compiling durable wiki pages from source markdown
instead of repeatedly answering from raw chunks.

## Tooling

The repository ships `qappswiki` (in [`tools/`](tools/)), a markdown-native
validator and knowledge-graph engine that turns this wiki's own schema and
`[[wikilinks]]` into an enforced, queryable graph — no LLM, no code parsing. It:

- **validates** every page against `schema/frontmatter-v0.md` (required fields,
  controlled vocabularies, broken links, orphans, dangling refs, provenance);
- **compiles** `[[wikilinks]]` + `related_*` + sources into a typed,
  confidence-labeled graph, exported as `graph.json` and an interactive
  `graph.html`, with an insight report (`GRAPH_REPORT.md`);
- **ingests** PDFs (`qappswiki ingest <pdf>`) via `markitdown-lightpdf`,
  archiving the source and scaffolding a schema-valid stub page;
- **serves** the graph over an MCP server so agents query it instead of
  re-reading raw markdown.

It runs locally and in CI (`.github/workflows/validate.yml`), and is the
validation gate the AS compilation workflow runs before writing pages. See
[`tools/README.md`](tools/README.md) for installation and usage.

## Operating Docs

- [`CONTEXT.md`](CONTEXT.md): operating manual for LLM maintenance.
- [`PLAN.md`](PLAN.md): current work plan and milestones.
- [`docs/qsc-integration.md`](docs/qsc-integration.md): QSC integration note.
- [`docs/llm-wiki-pattern.md`](docs/llm-wiki-pattern.md): pattern reference.
- [`docs/llm-wiki-structure.md`](docs/llm-wiki-structure.md): applied page
  families, graph model, and compilation rules.
- [`docs/as-intern-task-brief.md`](docs/as-intern-task-brief.md): first AS
  implementation brief for Markdown compilation.
- [`tools/README.md`](tools/README.md): the `qappswiki` validator + knowledge-graph
  engine — installation and usage.
