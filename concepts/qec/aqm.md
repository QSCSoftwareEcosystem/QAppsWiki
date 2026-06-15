---
type: concept
name: Auxiliary qubit mapping (AQM) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fermions-into-qubits
- concepts/qec/jw
- concepts/qec/qubit-concatenated
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/aqm
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: aqm
---

# Auxiliary qubit mapping (AQM) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/aqm) (`code_id: aqm`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A concatenation of the JW transformation code with a qubit stabilizer code.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/fermions-into-qubits]]
- _parent_: [[concepts/qec/qubit-concatenated]]
- _cousin_: [[concepts/qec/jw]] — The AQM fermion-into-qubit code reduces to the JW transformation code when the outer code is trivial.
