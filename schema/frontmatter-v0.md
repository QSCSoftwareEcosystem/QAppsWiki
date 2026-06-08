---
type: schema
status: draft
updated: 2026-06-08
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
status: draft | active | deprecated | blocked
updated: YYYY-MM-DD
owner: <person or project>
tags: []
sources: []
source_markdown: []
provenance_status: source-backed | partially-source-backed | needs-verification
```

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
```

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
concept_kind: algorithm | capability | interface | workflow-pattern | schema | provenance | failure-mode | qec | qhpc | validation | other
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
- `capability`
- `interface`
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
