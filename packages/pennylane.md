---
type: package
name: PennyLane
status: active
updated: 2026-06-15
package_role: framework
repository: https://github.com/PennyLaneAI/pennylane
documentation:
  - https://docs.pennylane.ai/
package_manager: [pip]
language: [python]
license: Apache-2.0
maturity: production
version_scope: ">=0.35"
version_source:
  kind: pypi
  id: pennylane
capabilities: [differentiable-programming, circuit-framework, simulation]
hardware_targets: [simulator, quantum-hardware, local-cpu, local-gpu]
interfaces: [python-api]
domains: [quantum-software, quantum-algorithms, quantum-simulation]
related_integrations: [integrations/qiskit-to-openqevo]
sources:
  - https://github.com/PennyLaneAI/pennylane
  - https://docs.pennylane.ai/
provenance_status: needs-verification
---

# PennyLane

> **Seed package page — `needs-verification`.** Metadata is grounded in the
> official repository and docs cited below; verify/enrich the body against
> converted source markdown (`raw/md/pennylane-official-docs.md`, see
> [[raw/source-inventory]]) before marking `source-backed`.

PennyLane is Xanadu's open-source Python framework for differentiable quantum
programming and quantum machine learning. It treats quantum circuits as
differentiable functions, enabling gradient-based optimization across
simulators and hardware backends, and integrates with autodiff/ML libraries. It
is a primary adapter target for [[packages/openqevo]].

## Capabilities

- Differentiable programming: quantum circuits as differentiable nodes with
  gradient support.
- Circuit framework and a device abstraction over many simulator/hardware
  backends.
- Simulation on CPU/GPU; hybrid quantum-classical optimization.

## Versioning & freshness

`version_source` points at the PyPI `pennylane` distribution; confirm the
supported `version_scope` against the OpenQEvo PennyLane adapter assumptions.

## Related

- [[packages/openqevo]]
- [[integrations/qiskit-to-openqevo]]
- [[schema/frontmatter-v0]]
