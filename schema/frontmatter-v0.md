---
type: schema
status: active
updated: 2026-06-15
owner: Thomas Naughton
fallback_owner: Vicente Leyton
tags: [frontmatter, provenance, data-schema]
---

# Frontmatter Schema v0

This is the first draft schema for QAppsWiki markdown pages. It is intended to
map cleanly to QSC Data Schema work and to reuse OpenQEvo context-schema ideas
where possible.

## Common Fields

All maintained wiki pages should include:

```yaml
type: package | concept | how-to | integration | workflow | qec-artifact | benchmark | source | schema | index | activity-log | note
status: draft | provisional | active | deprecated | blocked
updated: YYYY-MM-DD
owner: <person or project>
domains: []
tags: []
sources: []
source_markdown: []
provenance_status: source-backed | partially-source-backed | needs-verification
provenance_granularity: page | section | claim
```

`status: provisional` marks a page or page type defined ahead of evidence; it
should be validated or revised by a compilation pass over real sources before
becoming `active`. `domains` records topic areas (see Domain Tags below).
`provenance_granularity` records whether claims are cited at the page, section,
or individual-claim level (see Inline Provenance below).

Recommended optional fields:

```yaml
related_packages: []
related_concepts: []
related_integrations: []
related_how_to: []
related_workflows: []
related_artifacts: []
qsc_projects: []
openqse_relevance: ""
version_scope: ""
license: ""
```

### Typed Edges (optional)

Most relationships are derived automatically by the `qappswiki` tooling from
`[[wikilinks]]`, `related_*` fields, and `sources:`. Add an explicit `edges:`
list only when the relationship is **not** already obvious from those, or when
you need to pin a specific relation or confidence the heuristics cannot infer
(for example `supersedes` or `derived-from`). This field is optional and
additive — tooling merges explicit edges with derived ones and de-duplicates on
`(source, target, relation)`.

```yaml
edges:
  - target: concepts/trotterization   # node id (rel path without .md) or external path
    relation: implements              # see relation vocabulary below
    confidence: EXTRACTED             # EXTRACTED | INFERRED | AMBIGUOUS (default EXTRACTED)
    note: ""                          # optional; surfaced in the AMBIGUOUS-edge review
```

Relation vocabulary (closed). Generic software-graph relations: `integrates`,
`depends-on`, `supersedes`, `uses`, `implements`, `derived-from`, `cites`,
`related`, `has-how-to`, `composes-with`, `uses-interface`. Quantum-domain
relations (the higher-precision specialization): `wraps` (a package wraps/adapts
another, e.g. a framework over a backend), `encodes-qec` (an artifact/workflow
encodes a QEC scheme or code), `validates-against` (a benchmark validates a
package/workflow/concept). `wraps` and `encodes-qec` are authored or
LLM-extracted; `validates-against` is auto-derived for `benchmark` pages.
Hardware targeting is expressed with the `hardware_targets` controlled
vocabulary field, not an edge relation.

Confidence reuses the three-label provenance system the tooling applies to all
edges: `EXTRACTED` (explicitly stated), `INFERRED` (a reasonable deduction), or
`AMBIGUOUS` (uncertain; flagged for human review). A `target` that does not
resolve to a page produces an `AMBIGUOUS` edge to a `missing` node and a
validation warning.

## Package Pages

Package pages describe software entities under `packages/`.

Required fields:

```yaml
type: package
name: ""
status: draft | active | deprecated
updated: YYYY-MM-DD
package_role: library | framework | simulator | compiler | workflow | backend | dataset | other
capabilities: []
hardware_targets: []
interfaces: []
sources: []
provenance_status: source-backed | partially-source-backed | needs-verification
```

Recommended fields:

```yaml
repository: ""
documentation: ""
package_manager: []
language: []
license: ""
maturity: prototype | pre-alpha | alpha | beta | production | unknown
qsc_projects: []
version_built: ""              # exact upstream version this page was compiled from
version_source:                # authoritative place to check the latest version
  kind: pypi                   # see the version_source_kind vocabulary below
  id: ""                       # identifier within that source (PyPI name, owner/repo, URL)
```

`version_scope` (a common recommended field) holds the validity range.

### Versioning & Freshness (optional)

These fields let a package page act as a *self-refreshing context unit* (see
[[concepts/self-refreshing-context]]). They are optional and additive; existing
package pages without them are unaffected.

- `version_built` — the exact upstream version the page was compiled from
  (provenance). Example: `"1.2.0"`.
- `version_scope` — the range the compiled knowledge claims validity for, as a
  PEP 440-style specifier. Example: `">=1.0,<2.0"`. Drift *within* this range is
  not staleness.
- `version_source` — where to look up the current upstream version, as
  `{ kind, id }`.

```yaml
version_source:
  kind: pypi
  id: qiskit
version_built: "1.2.0"
version_scope: ">=1.0,<2.0"
```

**`version_source_kind` controlled vocabulary:**

| `kind` | `id` form | how "latest" is resolved | check mode |
|--------|-----------|--------------------------|------------|
| `pypi` | PyPI project name | `pypi.org/pypi/<id>/json` → `info.version` | deterministic |
| `github-releases` | `owner/repo` | latest release `tag_name` | deterministic |
| `github-tags` | `owner/repo` | highest semver tag | deterministic |
| `conda` | `channel/package` | registry metadata | deterministic |
| `npm` | package name | registry metadata | deterministic |
| `crates` | crate name | registry metadata | deterministic |
| `git` | repo URL | latest tag or commit | semi |
| `docs` | docs URL | no version API; read by an LLM | fuzzy |

**Freshness is checked separately from validation.** `qappswiki validate`
verifies only the *form* of these fields (`kind` in the vocabulary, `id`
present, `version_built` / `version_scope` parseable) and never makes a network
call, so CI stays deterministic. The staleness comparison — fetch the latest
version, test membership in `version_scope`, stamp `fresh` / `stale` — is an
online operation performed by the serving layer (and a future
`qappswiki freshness` command); it produces a banner and an update flag, not a
build failure.

Concepts, papers, and other non-software pages do not use `version_source`: a
published source is fixed, so their freshness is a separate "is there newer
literature?" check.

## Concept Pages

Concept pages describe reusable ideas under `concepts/`. A concept page should
exist when an idea appears across multiple packages, sources, or workflows, or
when it is needed to answer package-selection and workflow-composition
questions.

Required fields:

```yaml
type: concept
name: ""
status: draft | active | deprecated
updated: YYYY-MM-DD
concept_kind: algorithm | application | capability | interface | language | hardware | simulation | information | workflow-pattern | schema | provenance | failure-mode | qec | qhpc | validation | other
aliases: []
related_concepts: []
related_packages: []
related_integrations: []
sources: []
provenance_status: source-backed | partially-source-backed | needs-verification
```

Recommended fields:

```yaml
qsc_projects: []
openqse_relevance: ""
version_scope: ""
known_uncertainties: []
```

## How-To Pages

How-to pages describe task-specific usage under `how-to/`.

Required fields:

```yaml
type: how-to
status: draft | active | deprecated
updated: YYYY-MM-DD
task: ""
packages: []
version_scope: ""
sources: []
provenance_status: source-backed | partially-source-backed | needs-verification
```

Recommended fields:

```yaml
prerequisites: []
commands_verified: true | false
failure_modes: []
```

## Integration Pages

Integration pages describe package-to-package or package-to-workflow composition
under `integrations/`.

Required fields:

```yaml
type: integration
status: draft | active | deprecated
updated: YYYY-MM-DD
packages: []
interfaces: []
inputs: []
outputs: []
sources: []
provenance_status: source-backed | partially-source-backed | needs-verification
```

Recommended fields:

```yaml
version_scope: ""
adapter: ""
hardware_targets: []
qsc_projects: []
known_failure_modes: []
validation_status: unverified | locally-tested | source-tested | production
```

## Provisional Page Types

The Workflow, QEC Artifact, and Benchmark page types below are **provisional**.
They were defined ahead of evidence to describe quantum-HPC/QEC artifact flow,
but no real source has yet been compiled to confirm the fields fit. Use
`status: provisional` on pages of these types, and treat the field lists as
hypotheses to validate or revise during the first compilation pass over real
sources. Do not expand them further until a source demonstrates the need.

The Package, Concept, How-To, Integration, and Source page types are the
validated core and are not provisional.

## Workflow Pages

Workflow pages describe end-to-end quantum-HPC or QSC software flows. They
should make package composition, artifact movement, hardware targets, and
validation explicit.

Required fields:

```yaml
type: workflow
status: draft | active | deprecated
updated: YYYY-MM-DD
packages: []
interfaces: []
inputs: []
outputs: []
artifacts: []
hardware_targets: []
validation_status: unverified | locally-tested | source-tested | benchmarked | production
sources: []
provenance_status: source-backed | partially-source-backed | needs-verification
```

Recommended fields:

```yaml
qsc_projects: []
benchmarks: []
known_failure_modes: []
open_questions: []
```

## QEC Artifact Pages

QEC artifact pages describe protocol packages, circuit families, compiler
outputs, IR/lowering artifacts, syndrome extraction/correction representations,
or metadata bundles that move through CT-HW-QHPC workflows.

Required fields:

```yaml
type: qec-artifact
status: draft | active | deprecated
updated: YYYY-MM-DD
artifact_kind: protocol-package | circuit-family | compiler-output | ir | metadata-bundle | benchmark-input | other
formats: []
producers: []
consumers: []
interfaces: []
hardware_targets: []
sources: []
provenance_status: source-backed | partially-source-backed | needs-verification
```

Recommended fields:

```yaml
qec_assumptions: []
validation_status: unverified | locally-tested | source-tested | benchmarked | production
known_failure_modes: []
```

## Benchmark Pages

Benchmark pages describe validation cases, performance datasets, simulator
comparisons, or workflow metrics.

Required fields:

```yaml
type: benchmark
status: draft | active | deprecated
updated: YYYY-MM-DD
benchmark_kind: validation-case | performance-dataset | simulator-comparison | workflow-metric | other
packages: []
workflows: []
metrics: []
hardware_targets: []
sources: []
provenance_status: source-backed | partially-source-backed | needs-verification
```

## Source Pages

Source pages or source inventory entries describe raw material under `raw/`.

Required fields:

```yaml
type: source
status: draft | active
updated: YYYY-MM-DD
title: ""
source_type: documentation | repository | paper | issue | release-note | report | dataset | other
location: ""
preferred_ingest_path: raw/md | raw/pdf | external
provenance_status: source-backed | partially-source-backed | needs-verification
```

## Controlled Vocabularies

Domain (topic-area) tags. Every maintained content page should carry one or
more `domains` values:

- `quantum-information`
- `quantum-algorithms`
- `quantum-simulation`
- `quantum-software`
- `quantum-languages`
- `quantum-implementation`
- `quantum-error-correction`
- `quantum-hpc`
- `compilation`
- `benchmarking-validation`
- `wiki-infrastructure`

Initial capability tags:

- `time-evolution`
- `trotterization`
- `circuit-framework`
- `differentiable-programming`
- `simulation`
- `stabilizer-simulation`
- `adapter`
- `workflow-composition`
- `schema`
- `agentic-query`
- `markdown-compilation`
- `knowledge-graph`
- `provenance`
- `qec`
- `qhpc`
- `resource-estimation`
- `benchmarking`

Initial hardware target tags:

- `local-cpu`
- `local-gpu`
- `hpc`
- `quantum-hardware`
- `simulator`
- `unknown`

Initial interface tags:

- `python-api`
- `registry`
- `adapter`
- `json-context`
- `markdown-source`
- `qasm`
- `qir`
- `stim`
- `mlir`
- `metadata-bundle`
- `mcp`
- `cli`
- `hybrid-agent-interface`

Initial concept-kind tags:

- `algorithm`
- `application`
- `capability`
- `interface`
- `language`
- `hardware`
- `simulation`
- `information`
- `workflow-pattern`
- `schema`
- `provenance`
- `failure-mode`
- `qec`
- `qhpc`
- `validation`
- `other`

Initial artifact-kind tags:

- `protocol-package`
- `circuit-family`
- `compiler-output`
- `ir`
- `metadata-bundle`
- `benchmark-input`
- `other`

## Inline Provenance

QAppsWiki records provenance at two levels:

- **Page level** — the `sources:` / `source_markdown:` frontmatter lists every
  source a page draws on, and `provenance_status` rates how well-supported the
  page is overall.
- **Claim level** — individual non-obvious claims cite their source inline as
  `(source: <path>)`, so an agent can attribute a specific sentence. Combined
  claims use `(synthesis: <pathA>, <pathB>)`; inferred or unverified claims use
  `(inferred)` or `(needs-verification)`.

Set `provenance_granularity` to the level a page actually uses:

- `page` — only frontmatter sources (acceptable for short notes and indexes);
- `section` — one citation per paragraph/table/section;
- `claim` — inline citation on individual claims (the default for synthesized
  package, concept, how-to, and integration pages).

Every path cited inline must also appear in the page's `sources:` frontmatter.
The full inline convention is defined in [`CONTEXT.md`](../CONTEXT.md) under
"Provenance Convention".

## OpenQEvo Context Mapping

OpenQEvo context JSON fields should inform QAppsWiki package and integration
pages as follows:

| OpenQEvo context concept | QAppsWiki field |
|--------------------------|-----------------|
| method name | `name`, `capabilities`, package page sections |
| description | package/how-to summary |
| source | `sources`, `provenance_status`, `qsc_projects` |
| parameters | how-to prerequisites and usage notes |
| limitations | known failure modes and version-scope notes |
| references | `sources` and `source_markdown` |

This mapping is draft until DS review.
