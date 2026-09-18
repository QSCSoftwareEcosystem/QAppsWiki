---
type: package
name: HardwareAwareMapping
status: active
updated: 2026-09-18
package_role: workflow
repository: https://github.com/QSCSoftwareEcosystem/HardwareAwareMapping
documentation: [https://github.com/QSCSoftwareEcosystem/HardwareAwareMapping#readme]
language: [python]
maturity: prototype
capabilities: [hardware-mapping, qec, benchmarking, calibration-aware]
hardware_targets: [quantum-hardware, simulator, local-cpu]
interfaces: [python-api, cli]
domains: [compilation, quantum-error-correction, quantum-software]
sources: [https://github.com/QSCSoftwareEcosystem/HardwareAwareMapping]
provenance_status: source-backed
---

# HardwareAwareMapping

HardwareAwareMapping turns a natural-language circuit request into a validated,
QEC-encoded, calibration-aware mapped circuit. It keeps LLM generation confined
to the logical circuit while QEC encoding, hardware-region retrieval, mapping,
routing, and benchmarking are deterministic. (source:
https://github.com/QSCSoftwareEcosystem/HardwareAwareMapping)

## Related

- [[packages/ftqc]]
- [[packages/chatqec]]
