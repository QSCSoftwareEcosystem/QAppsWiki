---
type: index
status: active
updated: 2026-06-08
---

# QAppsWiki Index

This index tracks maintained QAppsWiki pages. QAppsWiki is an LLM-maintained
knowledge base for quantum computing broadly — see [[README]] for scope and
domains. Raw sources live under `raw/`; synthesized wiki knowledge lives under
`packages/`, `concepts/`, `how-to/`, `integrations/`, and `schema/`.

## Project Docs

- [[README]]: project charter.
- [[PLAN]]: current work plan, DRIs, decisions, and milestones.
- [[CONTEXT]]: operating manual for LLM maintenance.
- [[docs/qsc-integration]]: QSC integration note.
- [[docs/llm-wiki-pattern]]: LLM Wiki pattern reference.
- [[docs/llm-wiki-structure]]: applied structure for the QAppsWiki LLM-wiki
  graph.
- [[docs/as-intern-task-brief]]: AS intern task brief for the Markdown
  compilation workflow.

## Package Pages

- [[packages/openqevo]]: OpenQEvo package entry.

## Concept Pages

- [[concepts/markdown-compilation]]: the core LLM-wiki compilation workflow
  that turns source markdown into maintained, interlinked pages.
- [[concepts/quantum-hpc-qec-llm-wiki]]: QSC-specific extension of the
  LLM-wiki pattern for quantum-HPC integration and QEC.
- [[concepts/self-refreshing-context]]: design proposal for version-stamped,
  demand-fresh context units served to LLMs ("Context7 for quantum").

## How-To Pages

- [[how-to/openqevo-first-run]]: install OpenQEvo locally and run the first
  method/adapter checks.

## Integration Pages

- [[integrations/qiskit-to-openqevo]]: Qiskit adapter path into OpenQEvo.

## Schema

- [[schema/frontmatter-v0]]: draft frontmatter schema for package, concept,
  how-to, integration, and source pages, with the `domains` taxonomy and the
  inline-provenance convention.

## Source Tracking

- [[raw/source-inventory]]: first source choice for the seed corpus.

<!-- BEGIN imported:eczoo -->
## QEC Codes (imported from the Error Correction Zoo)

- [[concepts/qec/bacon-shor]]: Bacon-Shor code.
- [[concepts/qec/css]]: Calderbank-Shor-Steane (CSS) stabilizer code.
- [[concepts/qec/hypergraph-product]]: Hypergraph product (HGP) code.
- [[concepts/qec/qldpc]]: Qubit QLDPC code.
- [[concepts/qec/shor-nine]]: $⟦9,1,3⟧$ Shor code.
- [[concepts/qec/stab-5-1-3]]: $⟦5,1,3⟧$ Five-qubit perfect code.
- [[concepts/qec/stabilizer]]: Stabilizer code.
- [[concepts/qec/steane]]: $⟦7,1,3⟧$ Steane code.
- [[concepts/qec/surface]]: Kitaev surface code.
- [[concepts/qec/toric]]: Toric code.
- [[concepts/qec/triangular-color]]: Honeycomb (6.6.6) color code.
<!-- END imported:eczoo -->

<!-- BEGIN imported:qemzoo -->
## QEM Techniques (imported from the QEM Zoo)

- [[concepts/qem/accreditation]]: Accreditation.
- [[concepts/qem/bnzne]]: Benchmarked-Noise Zero-Noise Extrapolation.
- [[concepts/qem/cdr]]: Clifford Data Regression.
- [[concepts/qem/crosstalk-mitigation]]: Crosstalk-Adaptive Scheduling.
- [[concepts/qem/dd]]: Dynamical Decoupling.
- [[concepts/qem/dual-state-purification]]: Dual-State Purification.
- [[concepts/qem/echo-verification]]: Echo Verification.
- [[concepts/qem/emre]]: Error Mitigation by Restricted Evolution.
- [[concepts/qem/fcqem]]: Fictitious Copy Quantum Error Mitigation.
- [[concepts/qem/gse]]: Generalized Subspace Expansion.
- [[concepts/qem/hemre]]: Hybrid Error Mitigation by Restricted Evolution.
- [[concepts/qem/ide]]: Infinite Distance Extrapolation.
- [[concepts/qem/kik]]: K-Inverse-K (KIK).
- [[concepts/qem/logical-shadow-tomography]]: Logical Shadow Tomography.
- [[concepts/qem/lre]]: Layerwise Richardson Extrapolation.
- [[concepts/qem/measurement-error-mitigation]]: Readout Error Mitigation.
- [[concepts/qem/ml-qem]]: Machine Learning QEM.
- [[concepts/qem/n-representability]]: N-Representability Constraints.
- [[concepts/qem/nepec]]: Noise-Extended Probabilistic Error Cancellation.
- [[concepts/qem/noise-aware-compilation]]: Noise-Aware Compilation.
- [[concepts/qem/nox]]: Noiseless Output eXtrapolation.
- [[concepts/qem/odr]]: Operator Decoherence Renormalization.
- [[concepts/qem/partial-pauli-twirling]]: Partial Pauli Twirling.
- [[concepts/qem/pauli-twirling]]: Pauli Twirling.
- [[concepts/qem/pea]]: Probabilistic Error Amplification.
- [[concepts/qem/pec]]: Probabilistic Error Cancellation.
- [[concepts/qem/pie]]: Physics-Inspired Extrapolation.
- [[concepts/qem/pseudo-twirling]]: Pseudo Twirling.
- [[concepts/qem/purification]]: Virtual Distillation.
- [[concepts/qem/qed]]: Quantum Error Detection.
- [[concepts/qem/robust-shadows]]: Robust Shadow Estimation.
- [[concepts/qem/sqd]]: Sample-Based Quantum Diagonalization.
- [[concepts/qem/subspace-expansion]]: Quantum Subspace Expansion.
- [[concepts/qem/symmetric-clifford-twirling]]: Symmetric Clifford Twirling.
- [[concepts/qem/symmetry-adjusted-shadows]]: Symmetry-Adjusted Classical Shadows.
- [[concepts/qem/symmetry-verification]]: Symmetry Verification.
- [[concepts/qem/tem]]: Tensor Network Error Mitigation.
- [[concepts/qem/trex]]: Twirled Readout Error eXtinction.
- [[concepts/qem/zne]]: Zero-Noise Extrapolation.
<!-- END imported:qemzoo -->
