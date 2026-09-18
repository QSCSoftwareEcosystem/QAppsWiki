---
type: package
name: LightStim
status: active
updated: 2026-09-18
package_role: library
repository: https://github.com/QSCSoftwareEcosystem/LightStim
documentation: [https://github.com/QSCSoftwareEcosystem/LightStim#readme]
package_manager: [pip]
language: [python]
license: NOASSERTION
maturity: prototype
capabilities: [qec-simulation, decoding, noise-modeling, benchmarking]
hardware_targets: [local-cpu, local-gpu, simulator]
interfaces: [python-api, api]
domains: [quantum-error-correction, quantum-simulation, benchmarking-validation]
sources: [https://github.com/QSCSoftwareEcosystem/LightStim]
provenance_status: source-backed
---

# LightStim

LightStim is a modular QEC framework built on Stim. It provides reusable circuit
construction, detector generation, noise injection, decoder backends, and
logical-error-rate analysis across surface, toric, BB, color, PQRM, and
repetition-code workflows. (source:
https://github.com/QSCSoftwareEcosystem/LightStim)

## Related

- [[packages/stim]]
- [[packages/chatqec-mcp-tools]]
- [[concepts/qec/surface]]
