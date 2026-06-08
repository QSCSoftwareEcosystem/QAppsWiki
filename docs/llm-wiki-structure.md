---
type: reference
status: active
updated: 2026-06-08
owner: Vicente Leyton
tags: [llm-wiki, structure, graph, markdown-compilation]
sources:
  - docs/llm-wiki-pattern.md
  - CONTEXT.md
  - schema/frontmatter-v0.md
provenance_status: source-backed
---

# LLM-Wiki Structure

QAppsWiki is not only a documentation repository. It is a compiled knowledge
graph written as markdown. Raw sources provide evidence; maintained wiki pages
provide the durable synthesis that humans and agents query later.

The structure must support three things:

1. source-backed claims;
2. stable pages that can be updated over time;
3. explicit links between packages, concepts, interfaces, workflows, and
   sources.

## Page Families

| Family | Directory | Role |
|---|---|---|
| Package pages | `packages/` | Software entities: libraries, frameworks, simulators, compilers, backends, datasets. |
| Concept pages | `concepts/` | Reusable ideas that appear across sources and packages: algorithms, patterns, capabilities, constraints, schemas, provenance topics. |
| How-to pages | `how-to/` | Task-specific instructions grounded in package and source pages. |
| Integration pages | `integrations/` | Package-to-package or package-to-workflow compositions, with interfaces, inputs, outputs, failure modes, and validation status. |
| Source inventory | `raw/source-inventory.md` | Catalog of source material and preferred ingest path. |
| Schema pages | `schema/` | Frontmatter, controlled vocabularies, and graph/export conventions. |
| Project docs | `docs/` | Operating pattern, QSC integration, implementation briefs, and structure references. |

## Knowledge Layers

QAppsWiki has four layers.

| Layer | Files | Mutability | Purpose |
|---|---|---|---|
| Raw originals | `raw/pdf/`, external docs, local source repos | Immutable | Evidence source and recovery path. |
| Source markdown | `raw/md/`, local markdown sources | Regenerated or refreshed | LLM-readable extraction layer. |
| Maintained wiki | `packages/`, `concepts/`, `how-to/`, `integrations/` | Updated by LLM workflow | Compiled, linked knowledge. |
| Navigation/control | `index.md`, `log.md`, `CONTEXT.md`, `schema/` | Updated every pass | Routing, audit trail, and operating rules. |

This follows the general LLM-wiki pattern but adapts it to QSC. The "wiki"
layer must capture not only summaries, but also quantum-HPC and QEC
relationships: compiler artifacts, QEC protocols, simulator/backend targets,
hardware constraints, validation status, provenance, and workflow interfaces.

## Graph Model

The wiki graph should be understandable from frontmatter and page links.

Minimum node types:

- `package`
- `concept`
- `how-to`
- `integration`
- `qec-artifact`
- `benchmark`
- `workflow`
- `source`
- `schema`
- `note`

Important edge types:

| Edge | Meaning | Example |
|---|---|---|
| `implements` | Package implements a concept or capability. | OpenQEvo implements time evolution. |
| `wraps` | Package or adapter wraps another framework. | OpenQEvo Qiskit adapter wraps Qiskit evolution tooling. |
| `uses-interface` | Page depends on a technical interface. | Qiskit-to-OpenQEvo uses Python API and registry. |
| `has-how-to` | Package is supported by a task page. | OpenQEvo has first-run instructions. |
| `composes-with` | Packages appear together in an integration. | Qiskit composes with OpenQEvo. |
| `produces-artifact` | Workflow or compiler produces an artifact. | A CT workflow produces QASM, QIR, STIM, or MLIR-derived artifacts. |
| `consumes-artifact` | Package or workflow consumes an artifact. | HW benchmarking consumes compiler output. |
| `targets-hardware` | Workflow is intended for a hardware/simulator target. | An integration targets simulator, HPC, or quantum hardware. |
| `validates-against` | Workflow or package is validated against benchmark, source, or test. | OpenQEvo adapter status is checked against local tests. |
| `encodes-qec` | Page describes QEC-specific content. | A protocol package encodes syndrome extraction or correction assumptions. |
| `source-backed-by` | Claim or page is grounded in source material. | Package page cites README and tests. |
| `needs-verification` | Claim or edge is plausible but not verified. | Qrack status pending implementation verification. |

In markdown, edges appear in two places:

1. frontmatter fields such as `related_packages`, `related_concepts`,
   `related_integrations`, `interfaces`, and `sources`;
2. Obsidian-style links in page text, such as `[[packages/openqevo]]`.

## Concept Pages

Concept pages are essential. Without them, the wiki becomes a package catalog
instead of a knowledge graph.

A concept page should exist when an idea:

- appears in more than one package, source, or integration;
- defines a recurring capability or interface;
- is needed to answer package-selection or workflow-composition questions;
- helps identify contradictions or version-sensitive claims.

Examples:

- `concepts/markdown-compilation`
- `concepts/trotterization`
- `concepts/time-evolution`
- `concepts/provenance`
- `concepts/qec-aware-compilation`
- `concepts/adapter-pattern`

## QSC Domain Extension

The generic LLM-wiki pattern is necessary but not sufficient for QAppsWiki.
QAppsWiki should specialize the pattern for quantum-HPC integration and QEC.

### Domain Nodes

| Node | Purpose |
|---|---|
| Package | Software tool, library, simulator, compiler, backend, or framework. |
| Concept | Reusable idea such as time evolution, provenance, adapter pattern, QEC-aware compilation, or resource estimation. |
| Interface | API, schema, IR, file format, adapter contract, or service boundary. |
| QEC artifact | Protocol package, circuit family, syndrome extraction/correction representation, QASM/QIR/STIM output, MLIR dialect/pass output, or metadata bundle. |
| Workflow | End-to-end composition of packages, interfaces, artifacts, hardware targets, and validation steps. |
| Benchmark | Workload, metric set, validation case, simulator comparison, or performance dataset. |
| Hardware target | HPC, GPU, simulator, QPU/vendor backend, architecture resource, or QHPC operating environment. |
| Source | Evidence layer: paper, docs, code, meeting notes, issue, release note, benchmark report. |

### Domain Questions

The structure should support questions like:

- Which packages support a given quantum algorithm or QEC workflow?
- What interfaces connect Algorithms, Applications, CT, HW, DS, AS, and SE?
- Which compiler artifacts are produced, consumed, and validated?
- Which workflows target simulator, HPC, GPU, vendor QPU, or QHPC resources?
- Which claims are source-backed, locally tested, or still unverified?
- Where does a QEC protocol enter the software stack, and what metadata is
  required for reproducibility?

### QEC/QHPC Page Expectations

For QEC and quantum-HPC integration, pages should explicitly capture:

- input and output artifacts;
- interface or schema assumptions;
- hardware/simulator targets;
- validation status and benchmark evidence;
- provenance;
- failure modes and version-sensitive constraints;
- cross-thrust ownership.

## Markdown Compilation Pass

A compilation pass takes sources and updates the maintained wiki.

1. Select source set.
2. Read `index.md` and existing relevant pages.
3. Extract candidate nodes:
   - packages;
   - concepts;
   - capabilities;
   - interfaces;
   - adapters;
   - QEC artifacts;
   - compiler artifacts;
   - hardware targets;
   - workflows;
   - benchmarks;
   - failure modes;
   - open questions.
4. Match candidates to existing pages.
5. Create missing concept pages only when the concept is reusable.
6. Update package/how-to/integration pages with source-backed claims.
7. Add frontmatter edges and wiki links.
8. Update `index.md`.
9. Append to `log.md`.

The output is not an answer to a single prompt. The output is a better wiki.

## Scale Rules

As the wiki grows, avoid one giant summary page. Prefer small, durable pages
with explicit links.

- Package pages should summarize identity, capabilities, interfaces, maturity,
  QSC relevance, and related pages.
- Concept pages should summarize an idea and point to packages, workflows, and
  sources where the concept appears.
- How-to pages should stay operational and version-aware.
- Integration pages should make interfaces, inputs, outputs, validation status,
  and failure modes explicit.
- Source pages should record evidence, not duplicate every maintained page.

## Query Rule

A user question should usually resolve through maintained pages first:

1. `index.md`
2. relevant concept pages
3. relevant package pages
4. relevant how-to/integration pages
5. raw/source markdown only if the maintained wiki is incomplete

This is the practical difference from RAG: the wiki has already compiled the
main concepts and relationships.
