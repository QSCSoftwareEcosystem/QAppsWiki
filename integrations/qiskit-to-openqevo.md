---
type: integration
status: draft
updated: 2026-06-02
packages: [Qiskit, OpenQEvo]
interfaces: [python-api, adapter, registry]
inputs: [Hamiltonian terms as matrices, evolution time, Trotter steps, order]
outputs: [unitary evolution matrix]
adapter: qiskit_trotter
version_scope: local OpenQEvo source tree, Qiskit optional dependency >=1.0
hardware_targets: [local-cpu, simulator]
qsc_projects: [openqevo, agentic-software, software-engineering]
validation_status: source-tested
sources:
  - ../OpenQEvo/README.md
  - ../OpenQEvo/pyproject.toml
  - ../OpenQEvo/tests/test_qiskit_adapter.py
provenance_status: source-backed
---

# Qiskit to OpenQEvo

This integration page captures the first QAppsWiki package-composition path:
using OpenQEvo's Qiskit adapter through the OpenQEvo registry.

## Integration Summary

OpenQEvo exposes a `qiskit_trotter` method that can be retrieved through the
registry:

```python
import openqevo

method = openqevo.get("qiskit_trotter")
result = method.evolve(terms, t=1.0, steps=10, order=2)
```

The OpenQEvo package metadata declares Qiskit as an optional dependency:

```bash
pip install -e ".[qiskit]"
```

## Interface Contract

Source-backed adapter behavior from the local tests:

- The adapter is registered as `qiskit_trotter`.
- Input `terms` should contain at least one Hamiltonian term.
- `steps` is required and must be at least 1.
- `order` can distinguish first-order and second-order behavior.
- The returned result is expected to be a unitary matrix.

## Why This Matters for QSC

This is the first concrete integration pattern for QAppsWiki:

- Qiskit is a common circuit framework.
- OpenQEvo provides the QSC-owned package interface and registry.
- The adapter path gives AS agents a concrete method-selection target.
- The same structure can later be extended to PennyLane, TNQVM, Qrack, or QHPC
  execution paths.

## Known Failure Modes

- Missing Qiskit optional dependency.
- Empty `terms`.
- Missing `steps`.
- `steps=0` or another invalid step count.
- Version drift between Qiskit and the adapter implementation.

## Follow-Ups

- Verify the adapter with a local command and mark this page active.
- Add a concrete minimal example once the source is ingested into `raw/md/`.
- Add a comparison page for Qiskit vs. native OpenQEvo Trotter methods.

## Related

- [[packages/openqevo]]
- [[how-to/openqevo-first-run]]
