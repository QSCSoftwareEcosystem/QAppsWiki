---
type: package
name: OpenQEvo
status: active
updated: 2026-06-02
package_role: library
repository: https://github.com/QSCSoftwareThrust/OpenQEvo
documentation:
  - ../OpenQEvo/README.md
  - ../OpenQEvo/docs/architecture.md
  - ../OpenQEvo/docs/cross-project.md
package_manager: [pip]
language: [python]
license: TBD
maturity: pre-alpha
capabilities: [time-evolution, trotterization, adapter, schema]
hardware_targets: [local-cpu, simulator, hpc]
interfaces: [python-api, registry, adapter, json-context]
qsc_projects: [openqevo, data-schema, agentic-software, software-engineering, hybrid-workflows]
sources:
  - ../OpenQEvo/README.md
  - ../OpenQEvo/pyproject.toml
  - ../OpenQEvo/docs/architecture.md
  - ../OpenQEvo/docs/cross-project.md
provenance_status: source-backed
---

# OpenQEvo

OpenQEvo is the Software Thrust's first concrete quantum application library.
It packages time-evolution methods, starting with Trotterization, into a
reusable Python library with tests, context metadata, and adapters to external
quantum frameworks.

## QSC Role

OpenQEvo is the first internal package entry for QAppsWiki and the main
integration testbed for the MVP. It exercises the same cross-project pattern
QAppsWiki needs to capture:

- DS contributes structured context and provenance schema.
- AS uses the context for method selection, recommendation, and future
  orchestration.
- SE contributes packaging, testing, CI/CD, documentation, and deployability.
- HW contributes workflow context, examples, and QHPC-relevant integration
  requirements.

## Package Shape

OpenQEvo uses a Strategy + Registry + Adapter pattern. Native methods and
external adapters implement a common evolution-method interface and register
with the package registry.

Current source-backed methods and adapters:

| Method or adapter | Status from local sources |
|-------------------|---------------------------|
| `exact` | Done reference method |
| `trotter_s1` | Placeholder / native method |
| `trotter_s2` | Placeholder / native method |
| `qiskit_trotter` | Working adapter |
| `pennylane_trotter` | Working adapter |
| `qrack_trotter` | Stub |

The package metadata in `pyproject.toml` declares version `0.1.0` and Python
`>=3.10`. The README describes v0.1.0 as a June 2026 target release; treat that
as a release target until verified against tags or release artifacts.

## Interfaces

- Python registry API: `openqevo.list_methods()` and `openqevo.get(name)`.
- Evolution method interface: `evolve(terms, t, **params)`.
- Optional adapters: Qiskit, PennyLane, and Qrack.
- Context JSON files under `context/`, validated against `context/schema.json`.

## QAppsWiki Follow-Ups

- Create method-level notes for Trotter-Suzuki first order, second order, exact
  evolution, qDRIFT, and Krylov once source markdown is ingested.
- Link OpenQEvo context JSON to `schema/frontmatter-v0.md`.
- Verify current adapter status against tests and local execution before
  presenting support as production-ready.
- Add QHPC/HW notes once the first simulator or backend target is selected.

## Related

- [[how-to/openqevo-first-run]]
- [[integrations/qiskit-to-openqevo]]
- [[schema/frontmatter-v0]]
