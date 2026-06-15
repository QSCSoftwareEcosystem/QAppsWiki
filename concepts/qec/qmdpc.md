---
type: concept
name: Quantum multi-dimensional parity-check (QMDPC) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-css
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/yoked-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qmdpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qmdpc
---

# Quantum multi-dimensional parity-check (QMDPC) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qmdpc) (`code_id: qmdpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

High-rate low-distance CSS code whose qubits lie on a $D$-dimensional rectangle, with $X$-type stabilizer generators defined on each $D-1$-dimensional rectangle.
The $Z$-type stabilizer generators are defined via permutations in order to commute with the $X$-type generators.

For example, the $D=2$ square geometry corresponds to a $⟦n^2,n^2-4n+2,4⟧$ code, with $X$-type stabilizer generators defined on rows and columns.

(source: raw/error-correction-zoo.md)

## Protection

The general construction for a $D$-dimensional rectangle with sides $n_i$ yields a $⟦\prod_{i=1}^{D}n_{i},2\prod_{i=1}^{D}(n_{i}-1)-\prod_{i=1}^{D}n_{i},2^{D}⟧$ code family.

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _cousin_: [[concepts/qec/yoked-surface]] — Yoked surface codes are concatenations of QMDPC codes with rotated surface codes.
- _cousin_: [[concepts/qec/small-distance-qubit-stabilizer]] — QMDPC codes for dimensions $D \leq 2$ are examples of small distance qubit stabilizer codes.
