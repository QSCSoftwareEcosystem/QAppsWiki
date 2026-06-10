---
type: activity-log
status: active
updated: 2026-06-10
---

# QAppsWiki Log

## 2026-06-02 repo | Initial private repository | touched: README.md, PLAN.md, CONTEXT.md, docs/llm-wiki-pattern.md

Created the private `QSCSoftwareThrust/QAppsWiki` repository from the local
workspace and pushed the initial planning material.

## 2026-06-02 planning | Goals and QSC integration revised | touched: README.md, PLAN.md, CONTEXT.md, docs/qsc-integration.md

Reframed QAppsWiki as an active QSC knowledge layer for OpenQEvo, Quantum Wiki /
ChatQEC planning, openQSE discovery, and future agentic workflow composition.

## 2026-06-02 scaffold | MVP scaffold and OpenQEvo slice started | touched: index.md, log.md, schema/frontmatter-v0.md, packages/openqevo.md, how-to/openqevo-first-run.md, integrations/qiskit-to-openqevo.md, raw/source-inventory.md, PLAN.md

Recorded open decisions and DRI assignments, created the first wiki scaffold,
and added the first OpenQEvo package, how-to, and integration pages.

## 2026-06-08 revision | Markdown compilation direction | touched: README.md, PLAN.md, CONTEXT.md, index.md, packages/openqevo.md, docs/as-intern-task-brief.md

Updated QAppsWiki for the June 2026 direction: AS has an intern path for a
RAG-like Markdown compilation workflow, the scaffold status is now current, the
operating manual includes explicit compile/query/lint workflows, and the
OpenQEvo Qrack status is recorded as a registered adapter stub pending
implementation verification.

## 2026-06-08 structure | First-class concept layer | touched: docs/llm-wiki-structure.md, concepts/markdown-compilation.md, schema/frontmatter-v0.md, CONTEXT.md, README.md, PLAN.md, index.md, docs/as-intern-task-brief.md

Revised the LLM-wiki structure so QAppsWiki is not only a package/how-to/
integration catalog. Added `concepts/` as a first-class page family, defined
knowledge layers, node types, edge types, and scale rules, and created the
first concept page for Markdown compilation.

## 2026-06-08 structure | Quantum-HPC and QEC domain adaptation | touched: docs/llm-wiki-structure.md, concepts/quantum-hpc-qec-llm-wiki.md, schema/frontmatter-v0.md, CONTEXT.md, PLAN.md, index.md

Adapted the generic LLM-wiki pattern for QSC needs. Added domain-specific
structure for quantum-HPC/QEC integration, including QEC artifacts, workflows,
benchmarks, compiler artifacts, hardware targets, validation state, and
artifact/interface relationships.

## 2026-06-08 structure | Broaden scope and harden provenance | touched: README.md, CONTEXT.md, PLAN.md, schema/frontmatter-v0.md, docs/llm-wiki-structure.md, index.md

Generalized QAppsWiki from a QSC-software-thrust knowledge layer to a general
quantum computing knowledge base (quantum information, algorithms, simulation,
software, languages, implementation, QEC, compilation, QHPC), with QSC drivers
setting ingest priority rather than scope. Added a `domains` controlled
vocabulary and tagging rule. Added a two-level provenance convention: page-level
`sources:` frontmatter plus claim-level inline `(source: ...)` citations, with a
`provenance_granularity` field. Marked the QEC-artifact, benchmark, and workflow
page/node types `provisional` until a compilation pass over real sources
validates them, and expanded `concept_kind` for the broader domain coverage.

## 2026-06-10 concept | Self-refreshing context design | touched: concepts/self-refreshing-context.md, index.md

Added a design-proposal concept page for "Context7 for quantum computing":
version-stamped, demand-fresh context units served to LLMs. Records the
two-tier model (auto-fresh source under curated compiled knowledge), the five
principles (version range, two tiers, check-on-read/update-out-of-band,
deterministic version check, separate software vs. literature freshness modes),
the refresh flow, and the cross-package-graph differentiator. Marked
`needs-verification` (proposal, not yet implemented). Linked from `index.md`.
