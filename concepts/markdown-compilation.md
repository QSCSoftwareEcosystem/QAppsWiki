---
type: concept
name: Markdown compilation
status: active
updated: 2026-06-08
owner: Agentic Software
concept_kind: workflow-pattern
aliases: [llm-wiki compilation, durable synthesis, wiki compilation]
related_concepts: []
related_packages: []
related_integrations: []
qsc_projects: [agentic-software, data-schema, software-engineering, openqse]
sources:
  - ../docs/llm-wiki-pattern.md
  - ../CONTEXT.md
  - ../docs/as-intern-task-brief.md
provenance_status: source-backed
---

# Markdown Compilation

Markdown compilation is the core QAppsWiki workflow. It turns source markdown
into maintained, interlinked wiki pages. It is RAG-like because it uses source
material as evidence, but it is not a conventional retrieval-only RAG workflow:
the durable output is the wiki itself.

## Role in QAppsWiki

Markdown compilation should:

- extract reusable concepts from source markdown;
- update package, concept, how-to, and integration pages;
- create links between related pages;
- preserve provenance for source-backed claims;
- flag missing evidence, version drift, and contradictions.

## Why It Matters

The value of QAppsWiki comes from compounding. Once the wiki has compiled a
concept, package, or interface, future queries should start from that maintained
page rather than rediscovering the same relationship from raw chunks.

## Compilation Inputs

- source markdown from `raw/md/`;
- local markdown sources listed in `raw/source-inventory.md`;
- existing maintained wiki pages;
- `schema/frontmatter-v0.md`;
- `index.md` and `log.md`.

## Compilation Outputs

- updated maintained wiki pages;
- new concept pages when reusable concepts appear;
- repaired or added wiki links;
- updated provenance frontmatter;
- an append-only log entry.

## Related

- [[docs/llm-wiki-structure]]
- `docs/as-intern-task-brief.md` (local-only, not in the shared repo)
- [[schema/frontmatter-v0]]
