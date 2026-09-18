---
type: package
name: chatqec-mcp-tools
status: active
updated: 2026-09-18
package_role: backend
repository: https://github.com/QSCSoftwareEcosystem/chatqec-mcp-tools
documentation: [https://github.com/QSCSoftwareEcosystem/chatqec-mcp-tools#readme]
package_manager: [uv]
language: [python]
license: Apache-2.0
maturity: alpha
capabilities: [qec-simulation, decoding, threshold-estimation, hardware-calibration]
hardware_targets: [local-cpu, simulator, quantum-hardware]
interfaces: [mcp]
domains: [quantum-error-correction, wiki-infrastructure, quantum-simulation]
sources: [https://github.com/QSCSoftwareEcosystem/chatqec-mcp-tools]
provenance_status: source-backed
---

# chatqec-mcp-tools

This MCP server supplies ChatQEC with sandboxed QEC tools: Stim simulation and
diagrams, PyMatching decoding, threshold sweeps, code parameters, and optional
LightStim, Tsim, GLCB, and IBM Quantum integrations. IBM submission spends
account credits and should follow a preview. (source:
https://github.com/QSCSoftwareEcosystem/chatqec-mcp-tools)

## Related

- [[packages/chatqec]]
- [[packages/lightstim]]
- [[packages/stim]]
