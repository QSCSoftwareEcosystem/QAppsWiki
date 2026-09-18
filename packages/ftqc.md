---
type: package
name: FTQC
status: active
updated: 2026-09-18
package_role: compiler
repository: https://github.com/QSCSoftwareEcosystem/FTQC
documentation: [https://github.com/QSCSoftwareEcosystem/FTQC#readme]
language: [cpp, mlir]
maturity: prototype
capabilities: [fault-tolerant-compilation, qec, resource-estimation, qasm]
hardware_targets: [simulator, quantum-hardware]
interfaces: [mlir, qasm, cli]
domains: [compilation, quantum-error-correction, quantum-languages]
sources: [https://github.com/QSCSoftwareEcosystem/FTQC]
provenance_status: source-backed
---

# FTQC

FTQC is an LLVM/MLIR 22 compiler infrastructure for fault-tolerant quantum
computing. It uses logical and physical dialect layers: the logical layer models
QEC-aware operations, then a lowering pass makes data and ancilla qubits
explicit for backend emission. It documents Steane, surface, and color-code
flows plus QASM, Stim, and IQM-oriented lowering. (source:
https://github.com/QSCSoftwareEcosystem/FTQC)

## Related

- [[packages/qhpc-ecosystem]]
- [[packages/hardware-aware-mapping]]
- [[concepts/qec/steane]]
- [[concepts/qec/surface]]
