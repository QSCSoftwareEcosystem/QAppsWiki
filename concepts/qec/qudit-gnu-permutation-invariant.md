---
type: concept
name: Qudit GNU PI code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/qubit-permutation-invariant
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_gnu_permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_gnu_permutation_invariant
---

# Qudit GNU PI code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_gnu_permutation_invariant) (`code_id: qudit_gnu_permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Extension of the GNU PI codes to those encoding logical qudits into physical qubits.
Codewords can be expressed as superpositions of Dicke states with coefficients given by square roots of polynomial coefficients, with the case of binomial coefficients reducing to the GNU PI codes.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-permutation-invariant]]
- _parent_: [[concepts/qec/ampdamp]] — Qudit GNU PI codes protect against AD errors.
