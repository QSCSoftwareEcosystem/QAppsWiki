---
type: concept
name: $⟦5,1,3⟧_q$ Galois-qudit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-true-stabilizer
- concepts/qec/graph-quantum
- concepts/qec/quantum-cyclic
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_5_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_5_1_3
---

# $⟦5,1,3⟧_q$ Galois-qudit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_5_1_3) (`code_id: galois_5_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

True stabilizer code that generalizes the five-qubit perfect code to Galois qudits of prime-power dimension $q=p^m$. It has $4m$ stabilizer generators expressed as $X_{\gamma} Z_{\gamma} Z_{-\gamma} X_{-\gamma} I$ and its cyclic permutations, with $\gamma$ iterating over basis elements of $\mathbb{F}_q$ over $\mathbb{F}_p$.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/galois-true-stabilizer]]
- _parent_: [[concepts/qec/quantum-cyclic]]
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/graph-quantum]] — The $⟦5,1,3⟧_q$ code admits a graph-quantum-code realization for the group $G=\mathbb{F}_q$  ([arXiv:quant-ph/0012111](https://arxiv.org/abs/quant-ph/0012111)).

## Notes

- This code is described in a QEC2014 talk by [Gottesman](https://www.qec14.ethz.ch/slides/DanielGottesman.pdf).
