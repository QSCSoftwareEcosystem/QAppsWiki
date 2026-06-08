---
type: note
status: draft
updated: 2026-06-08
owner: Agentic Software
tags: [agentic-software, markdown-compilation, llm-wiki, qappswiki]
sources:
  - ../README.md
  - ../PLAN.md
  - ../CONTEXT.md
provenance_status: source-backed
---

# AS Intern Task Brief

The first AS implementation for QAppsWiki should build a Markdown compilation
workflow. This is RAG-like because it uses source material to support answers,
but the main output is not ephemeral retrieval. The output is a maintained,
interlinked wiki that compounds over time.

## Objective

Build a workflow that reads source markdown, extracts structured concepts, and
updates QAppsWiki pages with source-backed claims and wiki links.

## Inputs

- `index.md`
- `schema/frontmatter-v0.md`
- existing pages in `packages/`, `how-to/`, and `integrations/`
- existing concept pages in `concepts/`
- source markdown in `raw/md/` or local markdown sources listed in
  `raw/source-inventory.md`

## Outputs

- proposed updates to package, how-to, and integration pages;
- proposed updates to concept pages;
- suggested new wiki links;
- provenance updates in YAML frontmatter;
- `index.md` updates for new pages;
- `log.md` entry describing the compilation pass.

## Minimum Workflow

1. Read `index.md` and `schema/frontmatter-v0.md`.
2. Read the selected source markdown.
3. Extract concepts and classify them as package, capability, interface,
   adapter, hardware target, workflow, source, failure mode, or open question.
4. Match concepts to existing wiki pages.
5. Create a new concept page only when the concept is reusable across more
   than one source, package, or workflow.
6. Propose page updates with source-backed claims only.
7. Add or suggest Obsidian-style links to related pages.
8. Update provenance fields.
9. Emit a concise change summary.

## First Package Targets

OpenQEvo is the current slice. The next seed package pages should be:

- Qiskit
- PennyLane
- TNQVM
- Stim

Each package page should start small: identity, QSC relevance, core
capabilities, interfaces, source links, and known uncertainty.

## First Concept Targets

- Markdown compilation
- Time evolution
- Trotterization
- Adapter pattern
- Provenance
- QEC-aware compilation

## Guardrails

- Do not invent support for integrations that are not source-backed.
- Mark version-sensitive claims as `needs-verification` unless locally checked.
- Prefer maintained wiki pages over raw chunks for answering user questions.
- Keep generated changes reviewable; avoid broad rewrites until validation
  checks exist.

## Open Questions

- Should the first interface be CLI, MCP, direct API, or a hybrid?
- Which package should be compiled first after OpenQEvo?
- What validation must pass before automated page updates can be accepted?
- Should QAppsWiki export a machine-readable graph for AS or openQSE services?
