---
type: concept
name: Self-refreshing context
status: draft
updated: 2026-06-10
owner: Vicente Leyton
concept_kind: workflow-pattern
aliases:
  - context-as-a-service
  - living context
  - Context7-for-quantum
  - dynamic context units
domains:
  - wiki-infrastructure
  - quantum-software
related_concepts:
  - markdown-compilation
  - quantum-hpc-qec-llm-wiki
related_packages:
  - openqevo
qsc_projects:
  - agentic-software
  - data-schema
  - software-engineering
  - openqse
provenance_status: needs-verification
provenance_granularity: page
sources:
  - CONTEXT.md
  - PLAN.md
  - docs/llm-wiki-pattern.md
  - tools/README.md
  - https://context7.com
---

# Self-refreshing context

> **Status: design proposal (`needs-verification`).** This page records an
> agreed architectural direction, not yet implemented. It builds on the
> [[concepts/markdown-compilation]] pattern and the `qappswiki` engine
> (`tools/`).

QAppsWiki should serve **version-stamped, demand-fresh context to LLMs** —
"Context7 for quantum computing." Each quantum software package (and, with a
different freshness mode, each concept or paper) becomes a *context unit* an
agent can request over MCP. As the QSC thrust adds software, it adds contexts.

## The unit

A **context** is a version-scoped, package-scoped bundle — the compiled
[[packages/openqevo]]-style page plus its `how-to/`, `integrations/`, and current
source — served to a consuming LLM on demand. Adding a package = adding a context.
The first contexts are the seed corpus: Qiskit, PennyLane, TNQVM, Stim, and
OpenQEvo (see [[PLAN]]).

## Two-tier model

The wiki already separates an evidence layer from a compiled layer; contexts
exploit both:

- **Tier 1 — auto-fresh source.** Upstream docs / release pulled into `raw/md/`,
  version-stamped, re-run on each release. Cheap, current API surface.
- **Tier 2 — curated, compiled.** The durable package page + integrations,
  carrying provenance and cross-links, synthesized from Tier 1.

The graph ties them, so an agent receives both *current API* (Tier 1) and *why /
how it composes* (Tier 2) in one pack.

## Five principles

1. **Version-stamped, always.** Every context declares a `version_scope` as a
   *range*, not a point — version drift is not the same as knowledge drift.
2. **Two tiers.** Auto-fresh source under curated compiled knowledge, linked by
   the graph.
3. **Check on read, update out-of-band.** Freshness checks are cheap and run at
   use; the heavy re-ingest is a separate, gated write through
   `qappswiki run --strict` (see [[concepts/markdown-compilation]]) — never
   inline during a query.
4. **Deterministic check, not "go google it."** Each context pins an
   authoritative version source (PyPI / GitHub for software); the serving layer
   compares and stamps `fresh` / `stale`. The LLM is reserved for *synthesizing*
   new content, not for guessing versions.
5. **Two freshness modes.** Software → exact version compare against the pinned
   source. Concepts / papers → "is there newer literature?" (a search, not a
   version compare). A published paper is fixed; the *field* moves, so the paper
   side must not reuse the software mechanism.

## The refresh flow

```
context(qiskit, built@1.2, version_source=pypi, scope=1.x)
        │  on use
        ▼
serving layer GETs pypi -> latest = 1.4
        │
   in scope? --yes--> serve as-is (fast path, the common case)
        │ no
        ▼
serve context + "STALE: built 1.2, latest 1.4" banner
        │
        ├─ answering agent: fetch delta just-in-time for its answer (no write)
        └─ flag update task -> maintainer agent re-ingests current docs
             -> qappswiki run --strict -> commit (version bumped, provenance stamped)
```

The directive carried by a context is therefore not "go search the web" but a
small, tool-managed **freshness protocol**: *my version, the authoritative
endpoint to check, and where to route an update if I am stale.*

## Why this beats a single-library doc service

A generic doc-context service indexes one library in isolation. QAppsWiki adds
two things it structurally cannot: the **cross-package integration graph** (how
Qiskit composes with OpenQEvo, TNQVM, or a QHPC backend) and **provenance** (each
claim traced to a source and version). That cross-library, source-backed context
is the differentiator for quantum software users.

## What is genuinely new to build

Most of this sits on existing pieces — the typed graph, the MCP server, and the
`qappswiki ingest` + validation gate. The new pieces are narrow:

- a **per-package version source** (canonical endpoint) in frontmatter;
- a **staleness signal** (validator flags `version_scope` behind the latest pull);
- a **context-pack serving format** (a bounded, token-budgeted MCP response);
- a **freshness check** in the serving layer for software, with an LLM-driven
  literature check for concepts/papers.

## Open questions

- Where the freshness check runs per type (serving layer for software vs.
  LLM-driven for literature).
- Selection/expansion policy for a context pack (hop depth, token budget,
  whether to include `raw/md` evidence).
- How aggressively Tier 2 re-compiles on a Tier 1 bump (API-affecting changes
  only vs. every release).

## Related

- [[concepts/markdown-compilation]]
- [[concepts/quantum-hpc-qec-llm-wiki]]
- [[packages/openqevo]]
- [[CONTEXT]]
- [[PLAN]]
- [[docs/llm-wiki-pattern]]
