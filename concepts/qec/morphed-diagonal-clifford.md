---
type: concept
name: $⟦2^r+r-1,1,2⟧$ morphed simplex code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $⟦2^r+r-1,1,2⟧$ morphed quantum RM code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/diagonal-clifford
- concepts/qec/hypercube-quantum
- concepts/qec/qubit-css
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/morphed_diagonal_clifford
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: morphed_diagonal_clifford
---

# $⟦2^r+r-1,1,2⟧$ morphed simplex code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/morphed_diagonal_clifford) (`code_id: morphed_diagonal_clifford`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of a family of codes obtained by morphing the $⟦2^{r+1}-1,1,3⟧$ simplex codes on a region whose child code is a $⟦2^r,r,2⟧$ hypercube code  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
The morphing process replaces a subset of qubits with their logical qubits, yielding a code with parameters $⟦2^r+r-1,1,2⟧$ that inherits a diagonal gate at the $(r-1)$st level of the Clifford hierarchy from the parent code.

(source: raw/error-correction-zoo.md)

## General gates

- Each code implements a diagonal gate at the $(r-1)$st level of the \term{Clifford hierarchy} using transversal operations and $C^{r}Z$ gates  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/diagonal-clifford]] — The $⟦2^r+r-1,1,2⟧$ morphed simplex code is obtained by morphing the $⟦2^{r+1}-1,1,3⟧$ simplex code on a region whose child code is a $⟦2^r,r,2⟧$ hypercube code  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
- _cousin_: [[concepts/qec/hypercube-quantum]] — The $⟦2^r+r-1,1,2⟧$ morphed simplex code is obtained by morphing the $⟦2^{r+1}-1,1,3⟧$ simplex code on a region whose child code is a $⟦2^r,r,2⟧$ hypercube code  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
