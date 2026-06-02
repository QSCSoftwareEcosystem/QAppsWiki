---
type: integration-note
status: draft
updated: 2026-06-02
tags: [qsc, openqevo, openqse, quantum-wiki, agentic-software]
---

# QAppsWiki Integration in QSC

QAppsWiki is the Software Thrust knowledge layer for quantum application
software. It is not a replacement for package repositories such as OpenQEvo and
it is not only a document archive. Its role is to make package knowledge,
source provenance, and workflow-composition knowledge reusable by humans,
agents, and future openQSE services.

## Integration Role

QAppsWiki sits between raw project artifacts and user-facing agent workflows.

```text
raw sources -> source markdown -> wiki pages -> query / lint / orchestration agents
```

The wiki pages are the compounding layer. Agents should answer from the wiki
first, then return to raw sources only when the wiki is incomplete or a claim
needs verification.

## Project Interfaces

| QSC area | Interface with QAppsWiki |
|----------|--------------------------|
| OpenQEvo | First internal package entry, first how-to pages, first integration pages, and seed schema/provenance model. |
| Data Schema | Defines frontmatter, controlled vocabularies, provenance fields, and optional machine-readable export. |
| Agentic Software | Uses the wiki for ingest, query, lint, ChatQEC / Quantum Wiki workflows, and future workflow composition. |
| Software Engineering | Provides repo hygiene, validation, CI, packaging, and deployment/access paths. |
| Hybrid Workflows | Supplies QHPC execution targets, simulator/backend needs, and workflow constraints. |
| Compilation Tools | Supplies compiler/IR interfaces and lowering assumptions for cross-package workflows. |
| openQSE | Consumes QAppsWiki as a discovery and composition surface for packages and workflows. |

## Near-Term Integration Slice

The first slice should be OpenQEvo-centered because it exercises the full QSC
loop:

1. Ingest OpenQEvo documentation, examples, context/schema files, and relevant
   papers or reports.
2. Create `packages/openqevo.md`.
3. Create one first-run or adapter-focused how-to page.
4. Create one integration page for Qiskit to OpenQEvo.
5. Map OpenQEvo context-schema ideas to `schema/frontmatter-v0.md`.
6. Use the resulting pages to answer a workflow-composition question with
   citations.

## MarkItDown and Marker Role

MarkItDown and Marker support the source-ingest side of QAppsWiki. They make
papers, reports, and technical PDFs usable as source markdown while preserving
links back to immutable source files. This benefits OpenQEvo immediately by
turning time-evolution and adapter-related sources into reusable wiki pages,
and it benefits Quantum Wiki / ChatQEC by providing the same repeatable
document-to-knowledge workflow.

## Success Criteria

QAppsWiki is integrated into QSC when:

- OpenQEvo is represented as a package, a usage workflow, and at least one
  integration workflow.
- DS-approved frontmatter is used consistently across seed pages.
- AS can run an ingest/query/lint loop against wiki pages.
- SE has basic validation for required files, links, and frontmatter.
- A QSC user can ask how to choose or compose quantum software and receive an
  answer grounded in wiki pages with source provenance.
