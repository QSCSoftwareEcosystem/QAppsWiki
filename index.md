---
type: index
status: active
updated: 2026-06-08
---

# QAppsWiki Index

This index tracks maintained QAppsWiki pages. QAppsWiki is an LLM-maintained
knowledge base for quantum computing broadly — see [[README]] for scope and
domains. Raw sources live under `raw/`; synthesized wiki knowledge lives under
`packages/`, `concepts/`, `how-to/`, `integrations/`, and `schema/`.

## Project Docs

- [[README]]: project charter.
- [[PLAN]]: current work plan, DRIs, decisions, and milestones.
- [[CONTEXT]]: operating manual for LLM maintenance.
- [[docs/qsc-integration]]: QSC integration note.
- [[docs/llm-wiki-pattern]]: LLM Wiki pattern reference.
- [[docs/llm-wiki-structure]]: applied structure for the QAppsWiki LLM-wiki
  graph.
- [[docs/as-intern-task-brief]]: AS intern task brief for the Markdown
  compilation workflow.

## Package Pages

- [[packages/openqevo]]: OpenQEvo package entry.

## Concept Pages

- [[concepts/markdown-compilation]]: the core LLM-wiki compilation workflow
  that turns source markdown into maintained, interlinked pages.
- [[concepts/quantum-hpc-qec-llm-wiki]]: QSC-specific extension of the
  LLM-wiki pattern for quantum-HPC integration and QEC.

## How-To Pages

- [[how-to/openqevo-first-run]]: install OpenQEvo locally and run the first
  method/adapter checks.

## Integration Pages

- [[integrations/qiskit-to-openqevo]]: Qiskit adapter path into OpenQEvo.

## Schema

- [[schema/frontmatter-v0]]: draft frontmatter schema for package, concept,
  how-to, integration, and source pages, with the `domains` taxonomy and the
  inline-provenance convention.

## Source Tracking

- [[raw/source-inventory]]: first source choice for the seed corpus.
