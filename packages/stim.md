---
type: package
name: Stim
status: active
updated: 2026-06-15
package_role: simulator
repository: https://github.com/quantumlib/Stim
documentation:
  - https://github.com/quantumlib/Stim/blob/main/doc/python_api_reference_vDev.md
package_manager: [pip]
language: [python, cpp]
license: Apache-2.0
maturity: production
version_scope: ">=1.12"
version_source:
  kind: pypi
  id: stim
capabilities: [stabilizer-simulation, qec, benchmarking]
hardware_targets: [local-cpu]
interfaces: [python-api, cli, stim]
domains: [quantum-error-correction, quantum-simulation, benchmarking-validation]
sources:
  - https://github.com/quantumlib/Stim
provenance_status: needs-verification
---

# Stim

> **Seed package page — `needs-verification`.** Metadata is grounded in the
> official repository cited below; verify/enrich the body against converted
> source markdown (`raw/md/stim-official-docs.md`, see [[raw/source-inventory]])
> before marking `source-backed`.

Stim is a fast stabilizer-circuit simulator from Google Quantum AI, built for
quantum error correction research. It simulates Clifford circuits and large
stabilizer systems efficiently, samples measurement outcomes and detector
events, and generates data for decoder benchmarking. It is the natural software
anchor for QAppsWiki's quantum-error-correction coverage (the
[[raw/error-correction-zoo]] code pages).

## Capabilities

- Stabilizer-circuit simulation at scale (Clifford circuits, Pauli frames).
- QEC tooling: detector/observable sampling, circuit error models, and
  decoder-input ("detector error model") generation.
- High-throughput benchmarking of error-correcting codes and decoders.

## Versioning & freshness

`version_source` points at the PyPI `stim` distribution; `qappswiki freshness`
flags whether a tracked context is current against the latest release.

## Related

- [[concepts/qec/stabilizer]] — the code class Stim simulates.
- [[concepts/qec/surface]] — a primary QEC target for Stim-based decoding studies.
- [[raw/error-correction-zoo]]
- [[schema/frontmatter-v0]]
