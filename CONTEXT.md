---
type: operating-manual
status: draft
updated: 2026-06-02
---

# QAppsWiki Context

This file tells an LLM how to maintain QAppsWiki. The human owns source
selection, direction, and judgment. The LLM owns extraction, synthesis,
cross-linking, and bookkeeping.

## Purpose

QAppsWiki is an LLM-maintained knowledge base for quantum computing
applications, software packages, and QSC workflows. It is the knowledge layer
that connects OpenQEvo, Quantum Wiki / ChatQEC planning, openQSE discovery, and
future agentic workflow composition. It compounds knowledge across three page
families:

- `packages/` — what exists: package/entity pages.
- `how-to/` — how to use packages for specific tasks.
- `integrations/` — how packages compose into working pipelines.

Treat OpenQEvo as the first internal package and integration testbed. When
OpenQEvo sources are ingested, update the relevant package, how-to, and
integration pages rather than leaving the information only in raw notes.

## QSC Integration Rules

- Align page metadata with Data Schema work whenever possible.
- Preserve provenance so AS agents and openQSE services can cite source-backed
  claims.
- Capture interfaces and adapters explicitly; integration pages should describe
  inputs, outputs, schemas, version assumptions, and failure modes.
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

When a PDF is available, convert it with MarkItDown before ingest:

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
extracted_with: markitdown
```

Read the original PDF only when the markdown extraction is missing content,
garbles equations/tables, omits figures needed for the claim, or when the human
explicitly asks for PDF-level verification. If extraction quality is poor, note
that explicitly in the derived page.

Use Marker or the MarkItDown Marker plugin for PDFs where layout, equations,
figures, or tables are central to the wiki claims. Record the conversion path in
frontmatter:

```yaml
extracted_with: markitdown
extraction_backend: marker
```

## Ingest Workflow

1. Read the markdown source in `raw/md/` first and treat it as the default
   ingest input.
2. Do not read the PDF by default. Check the corresponding original source in
   `raw/pdf/` only when extraction is incomplete, ambiguous, missing important
   figures/tables, or needs verification.
3. Create or update the relevant pages in `packages/`, `how-to/`, and
   `integrations/`.
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
