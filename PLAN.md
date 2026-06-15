---
type: project-plan
status: active
updated: 2026-06-15
---

# QAppsWiki Plan

QAppsWiki is now a dedicated QSCSoftwareThrust repository. The immediate goal
is to turn the current proposal material into a working MVP that supports
OpenQEvo, Quantum Wiki / ChatQEC planning, and openQSE discovery workflows.

**Status (2026-06-15):** the `qappswiki` engine and the page structure are
complete and merged to `main` (CI-validated), so the structural/software phase
is done — populating the wiki is now a fill-in-the-blanks job (see
`CONTRIBUTING.md`). The corpus is seeded at scale: the full quantum Error
Correction Zoo (~650 code pages) and all QEM Zoo techniques are imported into
`concepts/qec/` and `concepts/qem/`. The remaining work is content: verifying
the imported `needs-verification` pages and authoring the seed package pages
(M4–M7 below).

## Goal

Build a maintained markdown knowledge base for quantum computing that helps
users and agents answer five practical questions:

1. What quantum computing concepts, packages, and languages exist for a task?
2. How do we install, configure, and use the software correctly?
3. How do we compose tools into working quantum, QSC, and QHPC workflows?
4. How do quantum information, algorithms, simulation, and implementation ideas
   connect across sources?
5. What sources, schema fields, and provenance support each answer?

QAppsWiki is general to quantum computing — quantum information, algorithms,
simulation, software, languages, implementation, QEC, compilation, and
quantum-HPC. The QSC drivers (OpenQEvo, openQSE, ChatQEC) set ingest priority,
not scope.

## Operating Principles

- Markdown is the working substrate.
- The wiki is useful before automation; agents come after the manual workflow is
  stable.
- PDFs remain immutable raw sources, but extracted markdown is the default LLM
  input.
- `markitdown-lightpdf` is the PDF→markdown converter (no-OCR; math/table
  heuristics for born-digital papers), invoked via `qappswiki ingest`.
- Every synthesized claim should trace back to a source file.
- The wiki should compound: ingest once, then update linked package, how-to,
  and integration pages.
- QAppsWiki should reuse QSC Data Schema and OpenQEvo context-schema ideas
  instead of creating isolated metadata.
- The first AS implementation should be a RAG-like Markdown compilation
  workflow, not a conventional retrieval-only RAG system: extract concepts from
  source markdown, synthesize maintained pages, and add interlink connections.
- QAppsWiki is general to quantum computing; tag every page with `domains`, and
  prefer broadening a general concept page over creating a QSC-only duplicate.
- Provenance is two-level: page-level `sources:` frontmatter plus claim-level
  inline `(source: ...)` citations.
- New page types beyond the validated core (package, concept, how-to,
  integration, source) start as `provisional` and must be earned by real
  sources before becoming `active`.
- Structural validation is tooling-enforced: the `qappswiki` engine validates
  every page against `schema/frontmatter-v0.md` and compiles the corpus into a
  typed knowledge graph; automated page writes must pass `qappswiki run` first.

## Strategic Direction: a quantum-native GraphRAG engine

QAppsWiki's `qappswiki` engine is evolving into a **graphify-class knowledge-graph
engine, specialized for quantum computing and stronger where graphify is
structurally weak**. The goal is not to clone graphify (Leiden, tree-sitter, 36
language grammars are solved infrastructure) but to match its mechanics and beat
it on the four things a derive-from-anything tool cannot have.

### Where we already stand (parity, not a rebuild)

The engine already matches graphify on: typed `graph.json` + interactive
`graph.html`; `EXTRACTED` / `INFERRED` / `AMBIGUOUS` confidence-labeled edges;
a `GRAPH_REPORT.md` with god-nodes, orphans, and surprising cross-domain links;
and an MCP server (`query_graph` / `get_node` / `get_neighbors` /
`shortest_path` / `graph_stats` / `list_orphans`). It already **exceeds**
graphify on provenance (`cites` edges from `sources:` + inline citations),
freshness (a `check_freshness` MCP tool — graphify is fully time-blind), the
typed quantum schema, and the curated authored layer. The work below is two
missing modules plus hardening these edges — not a from-scratch clone.

### The two real gaps vs graphify

1. **No auto-extraction from raw input.** The derive side is empty: every node
   depends on a hand-authored page. graphify reads a raw PDF or codebase and
   *extracts* a candidate graph. We have `qappswiki ingest` (PDF→markdown) but
   nothing that turns `raw/md/` into candidate nodes/edges.
2. **No community detection.** No Leiden/Louvain clustering or auto-named
   communities; we surface centrality (god-nodes) but not clustered communities.

### The four differentiators ("graphify, but better")

These are core, not nice-to-have, and define the project's edge:

1. **Provenance to primary sources** — claim-level `(source: …)` tracing every
   assertion to the literature/code it came from. graphify tags *edge extraction
   confidence*; we trace *editorial sourcing*. Different axis, science-grade.
2. **Freshness / version-staleness** — `version_source` + `qappswiki freshness`
   + composite roll-up: staleness propagates up the graph from software through
   integrations to applications. graphify is time-blind.
3. **Curated authored layer** — compile-once maintained pages are the source of
   truth; the derived graph is reconciled *against* them, never overwriting them.
4. **Quantum domain specialization** — typed node/edge vocab and extraction
   priors (`implements`, `wraps`, `encodes-qec`, `validates-against`, hardware
   targets) yield a higher-precision graph than generic extraction.

### Design invariant (the thing graphify cannot do)

Extraction output is **never written directly into authored pages**. Extracted
nodes/edges land in a **staging area**, tagged `INFERRED` with provenance to the
source file, and enter a **review queue**. Curation promotes them into authored
frontmatter edges. graphify's `INFERRED` edges are dead-ends; ours are
candidates for durable, curated knowledge. This **discover → promote loop** is
the project's defining feature and is only possible because we keep an authored
layer of truth.

### Roadmap

**Phase 1 — Close the two gaps (reach graphify parity)**

- [x] **1A · `extract.py`** — extraction over `raw/md/` → `INFERRED` candidate
      concept nodes/edges, each carrying the source in its `sources` list and
      staged to `wiki-out/extract/` (never written to authored pages — the design
      invariant). Two paths, mirroring `freshness`'s offline/online split: a
      deterministic, CI-safe **quantum term lexicon + heading** core (no
      dependency), and an **optional injected LLM backend** whose output is
      validated against the schema vocab (`concept_kind` / `domains` / relations
      scrubbed to safe values). Candidates resolve against the existing graph
      (`exists` flag) and merge across the corpus by id, ranked by source support.
      Exposed via `qappswiki extract` + an `EXTRACT_REPORT.md`. 12 tests; the
      18-paper corpus yields 141 candidates, top-ranked exactly right (Trotter
      Decomposition 17×, Suzuki-Trotter / Time Evolution 14×). *Tree-sitter code
      extraction and richer typed edges remain for a later pass.*
- [x] **1B · `cluster.py`** — Louvain community detection over the
      confidence-weighted content graph (networkx built-in, no new dependency,
      deterministic via fixed seed). Each community gets a heuristic label
      (dominant `domains` + local god-node) with an `apply_labels` seam for a
      later LLM namer. Surfaced in `GRAPH_REPORT.md` (Communities section),
      stamped onto `graph.json` nodes and drawn as compound groups in
      `graph.html`, exposed via a `qappswiki cluster` command and a
      `list_communities` MCP tool. 13 tests; corpus yields 3 clean communities
      (concepts / OpenQEvo / source-inventory). *LLM community naming deferred to
      Phase 1A's extraction layer.*

**Phase 2 — Make the four edges first-class (the "better")**

- [x] **Provenance:** added a coverage metric (`analyze` → `GRAPH_REPORT.md`) +
      a `cite` CLI subcommand and MCP tool returning the source(s) behind any
      node, split page- vs claim-level; and promoted "every inline `(source:)` ∈
      `sources:`" to a hard ERROR for content pages in `qappswiki validate`.
- [x] **Freshness:** `freshness.stamp_graph` stamps last-known staleness onto
      package nodes at build time (offline, from a `wiki-out/freshness.json`
      cache the online `freshness` command writes) and rolls the worst status up
      the graph through `composes-with`/`uses`/… edges to integrations and
      applications (the composite roll-up from
      [[concepts/self-refreshing-context]]); surfaced in `GRAPH_REPORT.md` and
      `graph.json`. A nightly `freshness` Action
      (`.github/workflows/freshness.yml`) reports staleness out-of-band (job
      summary + artifact), never blocking a build.
- [x] **Curated layer:** implemented the **discover → promote loop** —
      `qappswiki promote` turns a reviewed candidate from the staged queue
      (`wiki-out/extract/candidates.json`) into an authored, schema-valid
      `concepts/` page carrying the extractor's source provenance, as a
      `status: draft` / `needs-verification` stub awaiting authoring. Frontmatter
      is built from `schema.required_fields` so it always validates;
      `concept_kind`/`domains` are scrubbed to the vocab. Single (`promote
      <id|slug|title>`) or batch (`--all --min-sources N [--kind ...]`), with
      `--dry-run` and `--force`. Promotion is the *only* path from staging into
      the authored layer — extraction writes nothing. 12 tests including a
      round-trip that a promoted page validates with 0 errors and links into the
      graph; verified on the real corpus (Trotterization → a 9-source page).
      *Edge-level promotion (typed `related_*`) folds into the next pass.*
- [x] **Domain specialization:** expanded the typed edge vocabulary with the
      quantum relations `wraps`, `encodes-qec`, and `validates-against` (the last
      auto-derived for `benchmark` pages; the first two authored / LLM-extracted
      to keep the derived graph high-precision), broadened the deterministic
      extraction lexicon beyond the time-evolution seed corpus (QEC codes, error
      mitigation, tensor networks, transpilation, QASM, …), and the LLM
      extraction prompt now ships these relations as priors. *Further relations
      added as real sources validate them.*

**Phase 3 — Prove it on the time-evolution corpus (acceptance test)**

- [ ] Run the full pipeline over the ~18 papers already in `raw/md/`: extract →
      cluster → promote → produce `concepts/` pages (time evolution,
      Trotterization, randomized compilation, …) with provenance and freshness.
      The long-deferred first compilation pass becomes the engine's acceptance
      test and the schema's validation.

### Positioning

> graphify *derives* a graph and stops. QAppsWiki *derives, then curates* —
> freshness-aware, quantum-typed, source-provenanced, with a discover → promote
> loop that turns extraction into durable curated knowledge.

## Workstreams

### 1. Wiki Structure

Owner: Vicente initially; review with DS / AS / SE leads.

Deliverables:

- `CONTEXT.md` operating manual.
- `README.md` project charter.
- `index.md` content catalog.
- `log.md` append-only activity log.
- Directory conventions for `packages/`, `concepts/`, `how-to/`,
  `integrations/`, `raw/`, `schema/`, and `docs/`.

Current status:

- Dedicated GitHub repo created and pushed: `QSCSoftwareThrust/QAppsWiki`.
- `README.md`, `PLAN.md`, `CONTEXT.md`, and `docs/llm-wiki-pattern.md` exist.
- `index.md`, `log.md`, `schema/frontmatter-v0.md`, the first OpenQEvo
  package/how-to/integration pages, and the first concept page exist.
- The next structure task is to broaden from the OpenQEvo slice to the five
  seed package pages and the first source markdown inventory.

### 2. Source Ingest

Owner: Vicente initially; AS later automates.

Deliverables:

- Source workflow using `markitdown-lightpdf` for PDF→markdown extraction.
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
  *(Delivered: the `qappswiki` engine exports `graph.json` + interactive
  `graph.html`, and adds an optional typed `edges:` extension to the schema.)*

First schema entities:

- `package`
- `concept`
- `how-to`
- `integration`
- `source`
- `capability`
- `hardware-target`
- `interface`

### 4. Agent Workflow

Owner: AS lead after review.

Current status:

- AS has assigned an intern to work on the LLM-Wiki / QAppsWiki effort.
- The first implementation target is a RAG-like Markdown compilation workflow:
  gather concepts from source markdown, synthesize durable wiki pages, preserve
  provenance, and create interlink connections across the corpus.

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

Current status:

- Delivered `tools/qappswiki`, a markdown-native validator + knowledge-graph
  engine providing frontmatter + link validation, a typed graph
  (`graph.json` / `graph.html`), an insight report, a `qappswiki ingest` PDF
  conversion command, and an MCP server (see workstream 7).
- CI gate `.github/workflows/validate.yml` runs the test suite +
  `qappswiki validate` on pushes and PRs.

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

### 7. Knowledge-Graph Tooling (`qappswiki`)

Owner: SE / Vicente.

Delivered (2026-06) as `tools/qappswiki`, an installable Python CLI that turns
the schema into an enforced, queryable engine. Started markdown-native — no code
parsing, no LLM, reading only the wiki's own frontmatter, `[[wikilinks]]`, and
provenance — and is now evolving into a full quantum-native GraphRAG engine (see
**Strategic Direction** above): the deterministic authored-graph core stays, and
an LLM/AST **extraction** layer plus **community detection** are added on top,
feeding the curated layer through a discover → promote loop.

Delivered:

- **Validate** — checks every page against `schema/frontmatter-v0.md` (required
  fields, controlled vocabulary, broken `[[wikilinks]]`, orphans, dangling
  `related_*` / `packages:` refs, under-linked packages, and the two-level
  provenance rule: every inline `(source:)` must be declared in `sources:` —
  a hard ERROR on content pages).
- **New** — `qappswiki new <type> <slug>` scaffolds a blank, schema-valid page
  of any type (required fields present, ready to fill), built from the same
  `schema.py` source of truth the validator uses. The contributor entry point:
  populating the wiki is fill-in-the-blanks (see `CONTRIBUTING.md`).
- **Graph** — compiles `[[wikilinks]]` + `related_*` + sources into a typed,
  confidence-labeled (`EXTRACTED` / `INFERRED` / `AMBIGUOUS`) graph; exports
  `graph.json` + interactive `graph.html`.
- **Report** — god-nodes, orphans, under-linked pages, surprising cross-domain
  edges, AMBIGUOUS edges, and provenance gaps in `GRAPH_REPORT.md`.
- **Ingest** — `qappswiki ingest <pdf>` converts a PDF to `raw/md/` via
  `markitdown-lightpdf` (configurable), archives the PDF, and scaffolds a
  schema-valid stub page.
- **Import-zoo** — `qappswiki import-zoo {eczoo,qemzoo}` ingests two curated
  community catalogs into schema-valid `concept` pages: the Error Correction
  Zoo (error-correcting *codes*, CC-BY-SA YAML) and the QEM Zoo (error
  *mitigation/suppression* techniques, public-domain JSON). Pages render with
  provenance to the registered source page + upstream entry URL and are linked
  from `index.md`; they land `needs-verification` for a human pass. Rendering is
  offline-pure (network confined to fetch), so `run` stays deterministic. Seeded
  11 flagship ECZ codes + all 39 QEM techniques; `--all` imports the full
  ~1100-code ECZ catalog.
- **Serve** — MCP stdio server (`query` / `path` / `explain` / `list_orphans` /
  …) so agents query the graph instead of re-reading raw markdown.
- **Freshness** — `version_source` / `version_built` / `version_scope` package
  fields (with an offline form-validator) plus `qappswiki freshness`, an online
  command that fetches the latest upstream version (PyPI / GitHub / npm / conda /
  crates) and flags stale contexts. Verdicts are cached to
  `wiki-out/freshness.json`; the next build **stamps** staleness onto package
  nodes and **rolls it up** the graph to the integrations/applications that
  compose stale software (the composite roll-up). Surfaced in `GRAPH_REPORT.md`
  and `graph.json`; exposed to agents via a `check_freshness` MCP tool. A nightly
  Action reports staleness out-of-band. Network is isolated and kept out of the
  CI gate.
- **Schema extension** — optional typed `edges:` block and the `version_source`
  freshness fields in `frontmatter-v0`.
- **CI** — `.github/workflows/validate.yml` (tests + non-strict validate).
- 120 unit tests; the corpus currently validates with 0 errors.

This realizes the first tier of the
[[concepts/self-refreshing-context]] design (version-stamped, demand-fresh
context units — "Context7 for quantum") for software packages.

Next: see the **Strategic Direction** roadmap above (Phase 1 `extract.py` +
`cluster.py`; Phase 2 the four edges; Phase 3 the time-evolution acceptance
pass). Carried-over near-term items folded into that roadmap:

- Wire `qappswiki run --strict` into the AS compilation workflow as the
  pre-write gate; promote CI to `--strict` once outstanding warnings clear.
- Build the auto-refresh tier (pull current docs on a stale flag → recompile →
  commit) and application roll-up freshness; add a nightly `freshness` Action.

## Cross-Project Milestones

| Milestone | Target | Lead project | Deliverable |
|-----------|--------|--------------|-------------|
| M0: Repo live | 2026-06 | SE / Vicente | Private GitHub repo created, initial charter and plan pushed — ✓ delivered |
| M1: MVP scaffold | 2026-06 | SE / Vicente | `index.md`, `log.md`, `schema/frontmatter-v0.md`, and seed directories — ✓ delivered |
| M2: OpenQEvo slice | 2026-06 | DS / AS / SE | OpenQEvo package page, first concept page, first how-to, first integration page — ✓ delivered |
| M3: Source workflow | 2026-06 | AS / SE | PDF→markdown conversion documented + demonstrated — ✓ delivered as `qappswiki ingest` (markitdown-lightpdf) |
| M4: Seed corpus | 2026-07 | DS / AS | Five seed package pages grounded in source markdown |
| M5: Query loop | 2026-07 | AS | Manual query workflow answers from wiki pages with provenance |
| M6: Repo checks | 2026-08 | SE | Required-file, link, and frontmatter validation — ✓ delivered early (2026-06) via `qappswiki validate` + CI |
| M7: MVP review | 2026-08 | DS / AS / SE / HW | Demo QAppsWiki answering package-selection and workflow-composition questions |

## Project Action Items

### Data Schema

- [x] Name a DS DRI for QAppsWiki: Thomas Naughton. Vicente will define tasks
      and execute locally if collaboration does not materialize.
- [x] Draft `schema/frontmatter-v0.md`. *(Drafted and now `status: active`;
      mirrored machine-readably in `tools/qappswiki/schema.py`, the validator's
      single source of truth.)*
- [x] Define required fields for `package`, `how-to`, `integration`, and
      `source` pages. *(All defined in `frontmatter-v0` + `schema.py`;
      tooling-enforced by `qappswiki validate` and used to scaffold pages.)*
- [x] Define required fields for `concept` pages and graph edges. *(Concept
      required fields in `frontmatter-v0`; typed `edges:` extension added,
      including the quantum relations `wraps` / `encodes-qec` /
      `validates-against`.)*
- [x] Define required fields for QEC artifact, workflow, and benchmark pages.
      *(Defined as `provisional` types — fields are hypotheses to validate
      against real sources during the Phase-3 compilation pass.)*
- [x] Define controlled vocabularies for capabilities, hardware targets,
      package maturity, source type, interface type, and provenance status.
      *(All in `frontmatter-v0` "Controlled Vocabularies" + `schema.py`;
      membership enforced by `qappswiki validate`.)*
- [ ] Map frontmatter v0 to OpenQEvo context-schema concepts.
- [ ] Review the first five seed package pages for schema completeness.
- [x] Define whether a machine-readable export is needed for openQSE or AS
      workflows. *(Yes — `qappswiki` emits `graph.json`; typed `edges:` added.)*

### Agentic Software

- [x] Name an AS DRI for QAppsWiki: Tirthankar Ghosal. Vicente will define
      tasks and execute locally if collaboration does not materialize.
- [ ] Convert `CONTEXT.md` into explicit ingest, query, and lint workflows.
- [ ] Define the first ingest prompt/workflow for source markdown in `raw/md/`.
- [ ] Define the query workflow: read `index.md`, select relevant wiki pages,
      answer from wiki pages, and cite sources.
- [~] Define the lint workflow: stale pages, missing provenance, broken links,
      contradictions, orphan pages, and missing package/how-to/integration
      pages. *(Structural lint delivered in `qappswiki validate`: broken links,
      missing/uncited provenance, orphans, dangling refs, under-linked packages.
      Semantic lint — stale claims, contradictions — still open.)*
- [x] Evaluate whether the first automated interface should be MCP, direct API,
      CLI, or hybrid. *(CLI-first with an MCP server, delivered in `qappswiki`.)*
- [ ] Align QAppsWiki workflow with Quantum Wiki / ChatQEC planning.
- [ ] Define intern-ready implementation tasks for concept extraction,
      Markdown page compilation, link suggestion, provenance preservation, and
      scaling behavior.
- [ ] Define when the workflow should create a new concept page versus only
      adding a link or tag to an existing page.

### Software Engineering

- [x] Name an SE DRI for QAppsWiki: Seth Johnson. Vicente will define tasks
      and execute locally if collaboration does not materialize.
- [ ] Confirm repo layout and branch/review conventions.
- [ ] Add basic validation for required files: `CONTEXT.md`, `PLAN.md`,
      `README.md`, `index.md`, `log.md`, and `schema/frontmatter-v0.md`.
- [x] Add frontmatter validation once DS schema v0 exists. *(`qappswiki validate`.)*
- [x] Add link validation for internal wiki links and source file references.
      *(`qappswiki validate`.)*
- [x] Decide first access path: markdown repo, static site, CLI, REST endpoint,
      MCP server, or staged combination. *(Markdown repo + `qappswiki` CLI +
      MCP server.)*
- [ ] Define how QAppsWiki reuses or extends OpenQEvo packaging/CI work.
- [x] Support the MVP demo with a repeatable local command or documented
      workflow. *(`qappswiki run`.)*
- [x] Define repository checks needed before automated page updates are
      allowed: frontmatter validation, link validation, and source provenance
      checks. *(All three in `qappswiki validate`; CI gate added.)*

### Hybrid Workflows / Compilation Tools

- [x] Name an HW DRI for QAppsWiki: Samuel Stein. Vicente will define tasks and
      execute locally if collaboration does not materialize.
- [ ] Identify the first QHPC-relevant integration target for OpenQEvo.
- [ ] Identify hardware/backend metadata that should appear on package and
      integration pages.
- [ ] Capture compiler/IR interface assumptions when an integration crosses CT
      or HW boundaries.

### Vicente / Coordination

- [ ] Convert the June 2026 QAppsWiki direction into intern-ready work
      packages.
- [ ] Decide which seed package pages AS should implement first after
      OpenQEvo.
- [ ] Coordinate with Data Schema on the minimum viable frontmatter fields
      required by the Markdown compilation workflow.
- [ ] Coordinate with Software Engineering on validation before automated page
      updates are allowed.

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
- At least five `concepts/` pages exist, including concepts that connect more
  than one package or workflow.
- `index.md` and `log.md` are maintained.
- `schema/frontmatter-v0.md` defines the first usable page schema.
- A human can ask a package-selection or workflow-composition question and get
  an answer grounded in wiki pages, not raw PDFs.

## Immediate Next Actions

- [x] Create `index.md` and `log.md`.
- [x] Create `schema/frontmatter-v0.md`.
- [x] Create starter package page: `packages/openqevo.md`.
- [x] Draft first `how-to/` page from OpenQEvo install or adapter usage.
- [x] Draft first `integrations/` page: Qiskit to OpenQEvo.
- [x] Pick the first source for each seed package.
- [ ] Convert seed-package PDFs before ingest — now via `qappswiki ingest <pdf>`
      (markitdown-lightpdf). *(Command delivered; no source PDFs ingested into
      pages yet.)*
- [x] File companion page in `thrust-wiki/themes/qapps-wiki.md` after the name
      is stable.
- [x] Draft the AS intern task brief for the Markdown compilation workflow.
- [x] Add the first concept page: `concepts/markdown-compilation.md`.
- [ ] Add package pages for Qiskit, PennyLane, TNQVM, and Stim.
- [ ] Add concept pages for time evolution, Trotterization, adapter pattern,
      provenance, QEC-aware compilation, and quantum-HPC/QEC LLM-wiki
      structure.
- [x] Create a first lint checklist for missing links, missing provenance, and
      stale package status. *(Automated as `qappswiki validate`.)*
- [x] Broaden QAppsWiki scope to general quantum computing and add the `domains`
      controlled vocabulary.
- [x] Add the inline (claim-level) provenance convention to `CONTEXT.md` and
      `schema/frontmatter-v0.md`.
- [x] Mark the QEC-artifact, benchmark, and workflow page types `provisional`
      until a compilation pass validates them.

## Open Decisions

- [x] Name: keep `QAppsWiki`.
- [x] Audience / hosting: keep private until DOE copyright release.
- [x] Agent stack: hybrid interface.
- [x] DRIs: Thomas Naughton for DS, Tirthankar Ghosal for AS, Seth Johnson for
      SE, Samuel Stein for HW. Vicente will define tasks and execute locally if
      needed.
- [x] PDF converter: standardized on `markitdown-lightpdf` (`lightpdf` / `mid`),
      invoked by `qappswiki ingest`; configurable via `--converter` /
      `$QAPPSWIKI_CONVERTER`.
- [x] Machine-readable export + access path: the `qappswiki` graph
      (`graph.json` / `graph.html`) plus a CLI and an MCP server.
