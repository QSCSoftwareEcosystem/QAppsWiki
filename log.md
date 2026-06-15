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

## 2026-06-13 tooling | Discover→promote loop (Phase 2) | touched: tools/qappswiki/promote.py, extract.py, cli.py, tools/tests/test_promote.py, tools/README.md, PLAN.md

Added `promote.py` — the discover→promote loop, the project's defining feature
and the loop graphify structurally cannot close. `qappswiki promote` turns a
reviewed candidate from the staged queue (`wiki-out/extract/candidates.json`)
into an authored, schema-valid `concepts/` page that carries the extractor's
source provenance, as a `status: draft` / `provenance_status: needs-verification`
stub awaiting authoring. Frontmatter is built from `schema.required_fields` (the
validator's source of truth) so a promoted page always passes structural
validation; `concept_kind`/`domains` are scrubbed to the vocab. Supports single
promotion (`promote <id|slug|title>`) and batch (`--all --min-sources N
[--kind ...]`), plus `--dry-run` and `--force`. Promotion is the only path from
staging into the authored layer — extraction itself writes nothing. Also
hardened `extract`'s edge heuristic to relate candidates to *content* pages only
(so common words like "context"/"index" in papers no longer create spurious nav
links) and taught `merge_corpus` to accumulate each candidate's related targets
for the promoted page's links. 12 new tests (87 total, all green) including a
round-trip that a promoted page validates with 0 errors and is non-orphan;
verified on the real corpus — promoting Trotterization produced a clean
9-source page (0 errors, only the expected needs-verification / not-in-index
warnings). With extract + cluster + promote in place, the Phase-3 acceptance
pass (raw corpus → curated concept pages) is now a mechanical run away.

## 2026-06-15 tooling | Phase 2 complete + contributor on-ramp | touched: tools/qappswiki/{validate,scaffold,cli,freshness,analyze,report,edges,schema,extract}.py, tools/tests/{test_new,test_domain_priors,test_validate,test_freshness}.py, .github/workflows/freshness.yml, CONTRIBUTING.md, schema/frontmatter-v0.md, PLAN.md

Closed the open Phase-2 software roadmap and finished the contributor structure.
**Provenance:** the two-level rule "every inline `(source:)` ∈ `sources:`" is now
a hard ERROR on content pages (was a warning); the coverage metric + `cite`
CLI/MCP tool shipped earlier in the day. **Freshness:** `freshness.stamp_graph`
stamps last-known package staleness onto the graph at build time from a
`wiki-out/freshness.json` cache (offline/deterministic; CI never has the cache)
and rolls the worst status up through `composes-with`/`uses`/… edges to the
integrations and applications built on stale software — the composite roll-up
from [[concepts/self-refreshing-context]] — surfaced in `GRAPH_REPORT.md` and
`graph.json`. A nightly `freshness` Action reports staleness out-of-band (job
summary + artifact), never blocking a build. **Domain specialization:** expanded
the typed edge vocabulary with `wraps` / `encodes-qec` / `validates-against`
(the last auto-derived for `benchmark` pages; the first two authored to keep the
derived graph high-precision) and broadened the deterministic extraction lexicon
beyond time-evolution (QEC codes, error mitigation, tensor networks,
transpilation, QASM, …). **Structure:** `qappswiki new <type> <slug>` scaffolds a
blank schema-valid page of any type (built from `schema.py`, the validator's
source of truth), and `CONTRIBUTING.md` documents the fill-in-the-blanks loop so
anyone can populate the wiki. Marked the schema `status: active` and reconciled
the stale PLAN.md Data-Schema checkboxes (all page-type fields + vocabularies
were already defined). 120 tests green; real corpus validates with 0 errors.

## 2026-06-15 tooling | Zoo catalog importer + first ingest | touched: tools/qappswiki/import_zoo.py, cli.py, tools/tests/test_import_zoo.py, CONTRIBUTING.md, index.md, concepts/qec/*, concepts/qem/*, raw/{error-correction-zoo,qem-zoo}.md, PLAN.md

Turned the two registered zoo sources into actual wiki content. New
`qappswiki import-zoo {eczoo,qemzoo}` command fetches upstream structured data —
Error Correction Zoo YAML (one file per code, CC-BY-SA) and QEM Zoo JSON (public
domain, The Unlicense) — and renders schema-valid `concept` pages
(`concept_kind: qec`, `domains: [quantum-error-correction]`) with provenance
back to the registered source page + the upstream entry URL, then links them
from `index.md` via an idempotent managed block. Rendering is pure/offline
(network is confined to `fetch_*`), so `qappswiki run` stays deterministic and
the importer is unit-tested without the wire. A LaTeX→markdown pass converts
`\cite`/`\href`/`\hyperref`, strips figure environments, and renders the
stabilizer `[[n,k,d]]` notation as `⟦n,k,d⟧` so it can't collide with
`[[wikilink]]` syntax. Seeded a bounded starter set: 11 flagship ECZ codes
(stabilizer/CSS/surface/toric/color/qLDPC/HGP/Bacon-Shor/Steane/Shor-9/5-qubit)
+ all 39 QEM techniques. Imported pages are `provisional` /
`needs-verification` — the 50 resulting warnings are the intended verify-me
to-do list, not defects. 127 tests green; corpus validates with 0 errors,
0 orphans (128 nodes, 361 edges).

## 2026-06-15 tooling | Local zoo processing + full quantum ECZ import | touched: tools/qappswiki/{import_zoo,cli,paths}.py, tools/tests/test_import_zoo.py, .gitignore, CONTRIBUTING.md, concepts/qec/*, index.md, log.md

Reworked the importer to gather once and process locally: a single shallow
`git clone` of each zoo's data repo into a gitignored `.zoo-cache/`, then all
reads are off disk — no per-code API calls, no token, no rate limit (full
~1100-code catalog parses in ~5s vs ~5min before). Then ran the full import:
all 649 **quantum** error-correcting codes (codes/quantum + classical_into_quantum)
now live in `concepts/qec/`. Purely-classical codes (~450) are excluded by
default — they don't fit the `quantum-error-correction` domain — with
`--include-classical` to opt in. Two bugs the full run exposed: `update_index`
must use a function replacement (code titles carry LaTeX like `\mathbb` that
broke the regex replacement template), and `paths.IGNORED_DIRS` must skip
`.zoo-cache/` so the pipeline doesn't walk the cloned repos' own frontmatter-less
README/CONTRIBUTING. Corpus: 708 pages, 0 errors, 0 orphans (1404 nodes, 4640
edges); 689 needs-verification warnings are the imported verify-me queue. 128
tests green.
