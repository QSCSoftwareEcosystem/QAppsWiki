---
type: activity-log
status: active
updated: 2026-06-13
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

## 2026-06-10 concept | Context scope: software, concepts, applications | touched: concepts/self-refreshing-context.md

Extended the self-refreshing-context design: a context is any seed node plus its
graph neighborhood, spanning three flavors — software (`packages/`, version
freshness), concepts (`concepts/`, literature freshness), and applications
(both `concept_kind: application` and `integrations/` / `workflow/`, with
composite freshness that rolls up from the software they compose). Generalized
the freshness principle from two modes to three.

## 2026-06-12 direction | Quantum-native GraphRAG engine roadmap | touched: PLAN.md, log.md

Committed the strategic direction to make `qappswiki` a graphify-class
knowledge-graph engine specialized for quantum computing and stronger where
graphify is structurally weak. Recorded that the engine already reaches parity
on graph.json/HTML, confidence-labeled edges, the god-node report, and the MCP
query server, and already exceeds graphify on provenance, freshness, the typed
quantum schema, and the curated authored layer. Identified the two real gaps
(no auto-extraction from raw input; no community detection) and the four
core differentiators (claim-level provenance, freshness/version-staleness,
curated authored layer, quantum domain specialization). Added a three-phase
roadmap — Phase 1 `extract.py` + `cluster.py` for parity, Phase 2 hardening the
four edges (incl. the discover → promote loop and a `cite`/`why` MCP tool),
Phase 3 the time-evolution corpus as the acceptance test — plus the design
invariant that extraction output never writes authored pages directly but stages
`INFERRED` candidates for promotion.

## 2026-06-12 tooling | Community detection (Phase 1B) | touched: tools/qappswiki/cluster.py, schema.py, analyze.py, report.py, export.py, cli.py, serve.py, tools/tests/test_cluster.py, tools/README.md, PLAN.md

Added `cluster.py`: Louvain community detection over the confidence-weighted
content subgraph (networkx built-in — no new dependency — deterministic via a
fixed seed). Each community is labeled by its dominant `domains` and local
god-node, with an `apply_labels` seam for a future LLM namer. Wired through the
pipeline: shared `schema.is_content` helper, communities embedded in
`analyze`, a Communities section in `GRAPH_REPORT.md`, community id + label
stamped onto `graph.json` nodes and drawn as compound groups in `graph.html`,
a `qappswiki cluster` CLI command, and a `list_communities` MCP tool. 13 new
tests (63 total, all green); the real corpus yields 3 coherent communities
(concepts / OpenQEvo / source-inventory) at modularity 0.22. First Phase-1B
deliverable of the quantum-native GraphRAG roadmap; reaches graphify parity on
clustering while keeping the deterministic, no-LLM core.

## 2026-06-13 tooling | Candidate extraction (Phase 1A) | touched: tools/qappswiki/extract.py, cli.py, tools/tests/test_extract.py, tools/README.md, PLAN.md

Added `extract.py`, the derive side of the engine — the one stage that reads
raw sources instead of authored pages. It proposes `INFERRED` `concept`
candidates from a curated quantum term lexicon (Trotter/Suzuki, qDRIFT,
Hamiltonian simulation, QPE/VQE/QAOA, QEC, …) plus section headings, each
carrying the source in its `sources` list. Two paths mirror the freshness
offline/online split: a deterministic, CI-safe core (no dependency) and an
optional injected LLM backend whose output is validated against the schema
vocab (invalid `concept_kind`/`domains`/relations scrubbed). The defining
invariant holds: candidates are staged to `wiki-out/extract/` (regenerable,
gitignored) and never written to authored pages; a later `promote` step
(Phase 2) turns reviewed candidates into real `concepts/` pages. Candidates
resolve against the existing graph (`exists` flag) and merge across the corpus
by id, ranked by source support. Exposed via `qappswiki extract` +
`EXTRACT_REPORT.md`. 12 new tests (75 total, all green). First real run over
the 18-paper time-evolution corpus produced 141 candidates with the top ranks
exactly right — Trotter Decomposition (17 sources), Suzuki-Trotter and Time
Evolution (14), Hamiltonian Simulation (10) — the Phase-3 acceptance signal
for what to promote first.
