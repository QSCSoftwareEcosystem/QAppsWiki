---
type: package
name: ChatQEC
status: active
updated: 2026-09-18
package_role: framework
repository: https://github.com/QSCSoftwareEcosystem/ChatQEC
documentation: [https://github.com/QSCSoftwareEcosystem/ChatQEC#readme]
package_manager: [uv]
language: [python]
license: Apache-2.0
maturity: alpha
capabilities: [qec-retrieval, cited-answers, tool-use, qec-simulation]
hardware_targets: [local-cpu, simulator]
interfaces: [cli, python-api, mcp, web-ui]
domains: [quantum-error-correction, wiki-infrastructure, quantum-simulation]
sources: [https://github.com/QSCSoftwareEcosystem/ChatQEC, https://github.com/QSCSoftwareEcosystem/ChatQEC#enable-qappswiki-search]
provenance_status: source-backed
---

# ChatQEC

ChatQEC is a QEC research assistant with a curated corpus, hybrid retrieval,
inline citations, and optional sandboxed simulation tools. Its README describes
a CLI, Python library, and Streamlit interface. (source:
https://github.com/QSCSoftwareEcosystem/ChatQEC)

## QAppsWiki relationship

ChatQEC can query a locally cloned QAppsWiki through its MCP server and rerank
wiki sections alongside corpus retrieval candidates. This integration is
documented but its impact on ChatQEC's evaluation set has not yet been measured.
(source: https://github.com/QSCSoftwareEcosystem/ChatQEC#enable-qappswiki-search)

## Related

- [[packages/chatqec-mcp-tools]]
- [[packages/lightstim]]
- [[concepts/quantum-hpc-qec-llm-wiki]]
