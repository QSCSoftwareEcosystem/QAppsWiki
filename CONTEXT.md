---
type: operating-manual
status: draft
updated: 2026-06-08
---

# QAppsWiki Context

This file tells an LLM how to maintain QAppsWiki. The human owns source
selection, direction, and judgment. The LLM owns extraction, synthesis,
cross-linking, and bookkeeping.

## Purpose

QAppsWiki is an LLM-maintained knowledge base for quantum computing. Its scope
is general — quantum information, quantum algorithms, quantum simulation,
quantum software and programming languages, quantum implementation and hardware,
quantum error correction, compilation, and quantum-HPC integration. It is
developed in the QSC Software Thrust and connects OpenQEvo, Quantum Wiki /
ChatQEC planning, openQSE discovery, and future agentic workflow composition,
but the knowledge graph is not limited to those projects. It compounds knowledge
across four page families:

- `packages/` — what exists: package/entity pages.
- `concepts/` — what ideas recur: concepts, capabilities, interfaces,
  algorithms, patterns, schemas, provenance topics, and failure modes.
- `how-to/` — how to use packages for specific tasks.
- `integrations/` — how packages compose into working pipelines.
- workflow, QEC artifact, and benchmark pages — created when a source describes
  quantum-HPC/QEC artifact flow, validation cases, or benchmark structure.

Treat OpenQEvo as the first internal package and integration testbed. When
OpenQEvo sources are ingested, update the relevant package, how-to, and
integration pages rather than leaving the information only in raw notes.

## Scope and Domains

QAppsWiki covers quantum computing broadly. Tag every maintained page with one
or more `domains` values so the graph stays navigable as topics multiply:

- `quantum-information`, `quantum-algorithms`, `quantum-simulation`
- `quantum-software`, `quantum-languages`, `quantum-implementation`
- `quantum-error-correction`, `quantum-hpc`, `compilation`
- `benchmarking-validation`, `wiki-infrastructure`

QSC drivers (OpenQEvo, openQSE, ChatQEC) set ingest priority, not scope. A page
about a general quantum computing topic is in scope even when no QSC project
uses it yet. Prefer broadening an existing concept page over creating a
QSC-only duplicate of a general idea.

## Current AS Implementation Direction

The first AS implementation should be a RAG-like Markdown compilation workflow,
not a conventional retrieval-only RAG system. The goal is to compile durable,
linked wiki pages from source markdown:

1. read source markdown from `raw/md/` or local markdown sources;
2. extract concepts, packages, capabilities, interfaces, adapters, and
   source-backed claims;
3. map extracted concepts to existing wiki pages or propose new pages;
4. update maintained pages in `packages/`, `how-to/`, and `integrations/`;
5. create or update concept pages in `concepts/` when concepts recur across
   sources, packages, or workflows;
6. create or repair wiki links between related pages;
7. preserve provenance in frontmatter and page text;
8. update `index.md` and append one entry to `log.md`.

The workflow should scale by reducing repeated synthesis from raw chunks.
Source markdown remains the evidence layer; maintained wiki pages become the
compiled knowledge layer.

## QSC Integration Rules

- Align page metadata with Data Schema work whenever possible.
- Preserve provenance so AS agents and openQSE services can cite source-backed
  claims.
- Capture interfaces and adapters explicitly; integration pages should describe
  inputs, outputs, schemas, version assumptions, and failure modes.
- For QEC and quantum-HPC content, capture artifacts explicitly: protocol
  packages, circuit families, compiler outputs, IR/lowering outputs, benchmark
  inputs, metadata bundles, and validation status.
- Track hardware and execution targets explicitly: simulator, local CPU/GPU,
  HPC, vendor QPU, and QHPC operating environment.
- Prefer QSC-relevant workflows over generic package summaries when choosing
  what to synthesize first.
- Mark claims as uncertain when source extraction, version drift, or package
  behavior is not verified.

## Source Layers

- `raw/pdf/` — original PDFs. Immutable source of truth, used for verification
  and recovery when extraction is incomplete.
- `raw/md/` — markdown extracted from PDFs or other source formats. This is
  the preferred LLM-readable source layer.
- `raw/assets/` — extracted images, tables, or attachments when needed.

When a PDF is available, convert it with `markitdown-lightpdf` before ingest:

```bash
mid raw/pdf/<source>.pdf -o raw/md/<source>.md
```

The LLM should prioritize the markdown extraction because it is cheaper,
cleaner, and more token-efficient than reading PDFs directly. Preserve a link to
the original PDF for provenance. Pages derived from PDFs should include:

```yaml
sources:
  - raw/pdf/<source>.pdf
source_markdown:
  - raw/md/<source>.md
extracted_with: markitdown-lightpdf
```

Read the original PDF only when the markdown extraction is missing content,
garbles equations/tables, omits figures needed for the claim, or when the human
explicitly asks for PDF-level verification. If extraction quality is poor, note
that explicitly in the derived page.

`markitdown-lightpdf` handles inline/display math and tables for born-digital
PDFs directly; tune extraction with its flags (e.g. `--columns`, `--no-math`,
`--min-math-score`) when a paper's layout needs it. If a PDF is scanned (no text
layer), `markitdown-lightpdf` cannot extract it — note that on the derived page
and fall back to a manual transcription or another OCR tool.

## Ingest Workflow

1. Read the markdown source in `raw/md/` first and treat it as the default
   ingest input.
2. Do not read the PDF by default. Check the corresponding original source in
   `raw/pdf/` only when extraction is incomplete, ambiguous, missing important
   figures/tables, or needs verification.
3. Create or update the relevant pages in `packages/`, `concepts/`, `how-to/`,
   and `integrations/`.
4. Update `index.md` with any new pages.
5. Append one entry to `log.md`:
   `## [YYYY-MM-DD] ingest | <source title> | touched: <files>`.
6. Report what changed and flag uncertain claims.

For OpenQEvo ingest, prioritize:

1. Package identity and release status.
2. Installation and first-run usage.
3. Adapter paths: Qiskit, PennyLane, Qrack, TNQVM, or other active targets.
4. Context-schema/provenance fields that should inform `schema/frontmatter-v0.md`.
5. Integration pages that connect OpenQEvo to QSC workflows.

## Markdown Compilation Workflow

Use this workflow when turning a source or source set into maintained wiki
knowledge.

1. Identify the source set and record it in `raw/source-inventory.md` if it is
   not already listed.
2. Read existing pages first: `index.md`, relevant `packages/`, relevant
   `concepts/`, relevant `how-to/`, relevant `integrations/`, and
   `schema/frontmatter-v0.md`.
3. Extract a concept list from the source set. For each concept, classify it as
   one of: package, capability, interface, adapter, hardware target, workflow,
   QEC artifact, compiler artifact, benchmark, source, failure mode, or open
   question.
4. Decide whether each concept belongs on an existing page or needs a new page.
5. Update pages with source-backed claims only. If a claim is inferred, mark it
   as inferred or `needs-verification`.
6. Add links using Obsidian-style wiki links where the target page exists or
   should exist.
7. Update frontmatter fields: `updated`, `sources`, `source_markdown`,
   `provenance_status`, `capabilities`, `interfaces`, and `hardware_targets`
   where applicable.
8. Update `index.md` for any new maintained page.
9. Append to `log.md` using the standard format.

Do not allow automated compilation to overwrite pages without validation once
repo checks exist. Until then, keep changes reviewable and narrowly scoped.

## Query Workflow

When answering a question from QAppsWiki:

1. Read `index.md` first.
2. Read the relevant maintained wiki pages before raw sources.
3. Answer from maintained pages and cite the page names used.
4. If the maintained pages are insufficient, say which source needs ingest or
   verification.
5. If the answer becomes reusable, offer to file it as a package, how-to,
   integration, or note page.

## Lint Workflow

Periodic lint should report, not silently fix:

- pages missing required frontmatter fields;
- pages with `provenance_status: needs-verification`;
- broken wiki links;
- source references that do not exist locally;
- reusable concepts that appear in multiple pages but do not have a concept
  page;
- package pages without at least one concept, how-to, or integration link;
- stale package status, especially when external package versions or local
  adapters have changed;
- claims that mention support for an adapter or backend without tests, source,
  or local verification.

## Provenance Convention

QAppsWiki uses two levels of provenance.

Page-level provenance lists every source a page draws on, in frontmatter:

```yaml
sources:
  - raw/md/openqevo-trotter-suzuki-1976-10.1007-BF01609348.md
provenance_status: source-backed | partially-source-backed | needs-verification
provenance_granularity: page | section | claim
```

Claim-level provenance cites the specific source inline, next to the claim:

- Cite a non-obvious factual claim inline with `(source: <path>)`. Example:
  second-order Trotter error scales as O(t^3/n^2)
  `(source: raw/md/openqevo-trotter-suzuki-1976-10.1007-BF01609348.md)`.
- When a whole paragraph or table comes from one source, cite once at the
  paragraph or section level instead of per sentence.
- Mark a claim that combines sources as `(synthesis: <pathA>, <pathB>)`.
- Mark an inferred claim as `(inferred)` and an unverified one as
  `(needs-verification)`.
- Every path cited inline must also appear in the page's `sources:` frontmatter.
  Frontmatter is the index of sources; inline citations say which claim came
  from which source.

Page-level frontmatter alone is too coarse for an agent to cite a specific
sentence. Inline citations make each claim independently traceable and are the
default for synthesized package, concept, how-to, and integration pages. Record
the chosen level in `provenance_granularity`.

## Page Conventions

- Use markdown files with YAML frontmatter.
- Use Obsidian-style wiki links for internal links: `[[packages/qiskit]]`.
- Use ISO dates: `YYYY-MM-DD`.
- Preserve provenance. Claims should trace back to source markdown and, when
  applicable, the original PDF.
- Use QSC-facing language: explain why a package or workflow matters for QSC,
  openQSE, OpenQEvo, QHPC, validation, or agentic composition.
- Keep package summaries factual and version-aware. Do not imply current
  support for an integration unless a source or local verification supports it.
