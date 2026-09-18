---
type: package
name: qiris-qflow
status: active
updated: 2026-09-18
package_role: workflow
repository: https://github.com/QSCSoftwareEcosystem/qiris-qflow
documentation: [https://github.com/QSCSoftwareEcosystem/qiris-qflow#readme]
language: [python, c]
maturity: prototype
capabilities: [workflow-orchestration, chemistry-simulation, provenance]
hardware_targets: [local-cpu, hpc, simulator]
interfaces: [cli, json]
domains: [quantum-hpc, quantum-simulation, quantum-software]
sources: [https://github.com/QSCSoftwareEcosystem/qiris-qflow]
provenance_status: source-backed
---

# qiris-qflow

qiris-qflow integrates ExaChem QFlow, QIRIS/IRIS, and NWQSim. QFlow owns
chemistry state and accepts only complete cycle results; QIRIS handles durable
task scheduling; NWQSim provides a VQE/UCCSD execution lane. The repository
marks direct IRIS C API/QIR-EE production use as deferred. (source:
https://github.com/QSCSoftwareEcosystem/qiris-qflow)

## Related

- [[packages/qhpc-ecosystem]]
- [[packages/openqevo]]
