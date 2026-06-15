---
type: package
name: TNQVM
status: provisional
updated: 2026-06-15
package_role: simulator
repository: https://github.com/ORNL-QCI/tnqvm
documentation:
  - https://github.com/ORNL-QCI/tnqvm
package_manager: [source]
language: [cpp, python]
license: TBD
maturity: unknown
version_source:
  kind: github-tags
  id: ORNL-QCI/tnqvm
capabilities: [simulation]
hardware_targets: [local-cpu, hpc]
interfaces: [python-api]
domains: [quantum-simulation, quantum-software, quantum-hpc]
sources:
  - https://github.com/ORNL-QCI/tnqvm
provenance_status: needs-verification
---

# TNQVM

> **Seed package page — `needs-verification`.** TNQVM's project status, license,
> and current interfaces must be confirmed against the repository before any
> capability claim here is treated as authoritative (the
> [[raw/source-inventory]] flags this explicitly). Metadata below is provisional.

TNQVM (Tensor Network Quantum Virtual Machine) is a tensor-network-based
simulator backend developed at ORNL, used as a simulation backend within the
XACC quantum programming framework. It targets simulation of quantum circuits
via tensor-network contraction, including on HPC resources.

## Capabilities

- Tensor-network simulation of quantum circuits (as an XACC accelerator
  backend).
- HPC-oriented execution.

These claims are **provisional** and must be verified against the repository and
current XACC integration status before being presented as support.

## Versioning & freshness

`version_source` points at GitHub tags for `ORNL-QCI/tnqvm`; if upstream
publishes no tags/releases, `qappswiki freshness` reports `unknown` rather than
stale. Confirm the authoritative version source (tags vs. a parent XACC release)
during verification.

## Related

- [[packages/openqevo]]
- [[schema/frontmatter-v0]]
