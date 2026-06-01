---
type: operating-manual
status: draft
updated: 2026-04-28
---

# QAppsWiki Context

This file tells an LLM how to maintain QAppsWiki. The human owns source
selection, direction, and judgment. The LLM owns extraction, synthesis,
cross-linking, and bookkeeping.

## Purpose

QAppsWiki is an LLM-maintained knowledge base for quantum computing
applications and software packages. It compounds knowledge across three page
families:

- `packages/` — what exists: package/entity pages.
- `how-to/` — how to use packages for specific tasks.
- `integrations/` — how packages compose into working pipelines.

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

## Page Conventions

- Use markdown files with YAML frontmatter.
- Use Obsidian-style wiki links for internal links: `[[packages/qiskit]]`.
- Use ISO dates: `YYYY-MM-DD`.
- Preserve provenance. Claims should trace back to source markdown and, when
  applicable, the original PDF.
