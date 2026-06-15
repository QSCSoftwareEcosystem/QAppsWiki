---
type: concept
name: EAOA qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/oa-qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/eaoa_qubits_into_qubits
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: eaoa_qubits_into_qubits
---

# EAOA qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/eaoa_qubits_into_qubits) (`code_id: eaoa_qubits_into_qubits`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Entanglement-assisted qubit code in the operator-algebra framework.
This family encompasses ordinary entanglement-assisted subspace qubit codes, entanglement-assisted subsystem qubit codes, entanglement-assisted hybrid qubit codes, and their operator-algebra generalizations.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [`eaoaecc`](https://errorcorrectionzoo.org/c/eaoaecc) — An EAOA QECC defined over qubits is an EAOA qubit code.
- _cousin_: [[concepts/qec/oa-qubits-into-qubits]] — EAOA qubit codes utilize additional ancillary qubits in a pre-shared entangled state, but reduce to ordinary OA qubit codes when said qubits are interpreted as noiseless physical qubits.
