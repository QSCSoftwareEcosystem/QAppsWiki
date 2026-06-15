---
type: package
name: Qiskit
status: active
updated: 2026-06-15
package_role: framework
repository: https://github.com/Qiskit/qiskit
documentation:
  - https://docs.quantum.ibm.com/
package_manager: [pip]
language: [python]
license: Apache-2.0
maturity: production
version_scope: ">=1.0"
version_source:
  kind: pypi
  id: qiskit
capabilities: [circuit-framework, simulation, trotterization]
hardware_targets: [simulator, quantum-hardware, local-cpu]
interfaces: [python-api, qasm]
domains: [quantum-software, quantum-languages, compilation, quantum-simulation]
related_integrations: [integrations/qiskit-to-openqevo]
sources:
  - https://github.com/Qiskit/qiskit
  - https://docs.quantum.ibm.com/
provenance_status: needs-verification
---

# Qiskit

> **Seed package page — `needs-verification`.** Metadata (role, version source,
> capabilities) is grounded in the official repository and docs cited below;
> the body should be verified/enriched against converted source markdown
> (`raw/md/qiskit-official-docs.md`, see [[raw/source-inventory]]) before this
> page is marked `source-backed`.

Qiskit is IBM's open-source Python SDK for quantum computing. It provides a
circuit construction model, a transpiler for compiling circuits to target
backends, primitives for running on simulators and IBM Quantum hardware, and an
ecosystem of higher-level modules. It is one of the most widely used quantum
software frameworks and a primary adapter target for [[packages/openqevo]].

## Capabilities

- Circuit framework: build and manipulate quantum circuits.
- Transpilation / compilation to backend-native gate sets and topologies.
- Simulation (via Qiskit Aer) and execution on IBM Quantum hardware.
- Interoperates with OpenQASM.

## Versioning & freshness

`version_source` points at the PyPI `qiskit` distribution; `qappswiki freshness`
will report whether a tracked context is current against the latest release.
Confirm the supported `version_scope` against the adapter assumptions in
[[integrations/qiskit-to-openqevo]].

## Related

- [[integrations/qiskit-to-openqevo]]
- [[packages/openqevo]]
- [[schema/frontmatter-v0]]
