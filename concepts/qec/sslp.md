---
type: concept
name: Subset-Sum-Linear-Programming (SS-LP) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/binary-dihedral-permutation-invariant
- concepts/qec/qubits-into-qubits
- concepts/qec/small-distance-quantum
- concepts/qec/stab-15-1-3
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/sslp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: sslp
---

# Subset-Sum-Linear-Programming (SS-LP) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/sslp) (`code_id: sslp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit block quantum code that encodes a logical qubit and that is constructed using the Subset-Sum-Linear-Programming (SS-LP) numerical construction.
SS-LP codes are optimized to admit diagonal gates transversally and include $((7,2,3))$ codes that realize the $\mathsf{BD}_{16}$ and $\mathsf{BD}_{32}$ groups transversally, yielding $T$ and $\sqrt{T}$ gates, respectively. Larger codes include an $((8,2,3))$ code that transversally realizes $\mathsf{BD}_{64}$.

(source: raw/error-correction-zoo.md)

## Transversal gates

- SS-LP codes are optimized to admit diagonal gates transversally and include $((7,2,3))$ codes that realize the $\mathsf{BD}_{16}$ and $\mathsf{BD}_{32}$ groups transversally, yielding $T$ and $\sqrt{T}$ gates, respectively. Larger codes include an $((8,2,3))$ code that transversally realizes $\mathsf{BD}_{64}$.

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/stab-15-1-3]] — The $((7,2,3))$ SS-LP code realizes the $T$ gate transversally, but requires fewer qubits than the $⟦15,1,3⟧$ quantum RM code.
- _cousin_: [[concepts/qec/binary-dihedral-permutation-invariant]] — SS-LP codes are optimized to admit diagonal gates transversally and include $((7,2,3))$ codes that realize the $\mathsf{BD}_{16}$ and $\mathsf{BD}_{32}$ groups transversally, yielding $T$ and $\sqrt{T}$ gates, respectively. Larger codes include an $((8,2,3))$ code that transversally realizes $\mathsf{BD}_{64}$.
