---
type: concept
name: Quantum-HPC QEC LLM-wiki
status: active
updated: 2026-06-08
owner: Vicente Leyton
concept_kind: workflow-pattern
aliases: [qec llm-wiki, quantum-hpc wiki graph, qapps domain graph]
related_concepts:
  - markdown-compilation
related_packages:
  - OpenQEvo
related_integrations: []
qsc_projects: [openqevo, data-schema, agentic-software, software-engineering, hybrid-workflows, compilation-tools, openqse]
sources:
  - ../docs/llm-wiki-pattern.md
  - ../docs/llm-wiki-structure.md
  - ../CONTEXT.md
provenance_status: source-backed
---

# Quantum-HPC QEC LLM-Wiki

The general LLM-wiki pattern can be used for QAppsWiki, but QSC needs a
domain-specific graph for quantum-HPC integration and QEC. The wiki should not
only summarize documents; it should make interfaces, artifacts, workflows,
hardware targets, validation status, and provenance visible.

## Adaptation

Generic LLM-wiki structure:

```text
raw sources -> wiki pages -> schema / operating rules
```

QAppsWiki structure:

```text
raw sources
  -> source markdown
  -> packages + concepts + integrations + how-to pages
  -> QEC artifacts + interfaces + workflows + benchmarks
  -> query / lint / agent workflow
```

## What Must Be Tracked

- packages and their capabilities;
- QEC protocols, circuit families, compiler outputs, and metadata bundles;
- interfaces such as Python APIs, adapters, schemas, QASM, QIR, STIM, MLIR
  dialects, and workflow contracts;
- simulator, HPC, GPU, vendor-QPU, and QHPC targets;
- validation state: unverified, source-backed, locally tested, benchmarked, or
  production;
- provenance for every important claim.

## Why This Matters

Quantum-HPC and QEC workflows depend on more than package names. They depend on
whether artifacts can move across compilation, simulation, workflow execution,
schema capture, validation, and agentic orchestration. QAppsWiki should make
those dependencies explicit so humans and agents can compose workflows without
reconstructing the stack from raw notes every time.

## Related

- [[concepts/markdown-compilation]]
- [[docs/llm-wiki-structure]]
- [[schema/frontmatter-v0]]
