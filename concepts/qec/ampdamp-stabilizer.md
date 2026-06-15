---
type: concept
name: $⟦2(m+1),m,2⟧$ single-loss AD code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-css
- concepts/qec/self-complementary
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ampdamp_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ampdamp_stabilizer
---

# $⟦2(m+1),m,2⟧$ single-loss AD code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ampdamp_stabilizer) (`code_id: ampdamp_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of a class of $⟦2(m+1),m,2⟧$ CSS codes for $m\geq 1$ that generalizes the $⟦4,1,2⟧$ approximate amplitude-damping code of Ref.  ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002)).
Its $Z$-type generators are $m+1$ pairwise products, with each qubit participating in only one check; the single $X$-type generator is the all-$X$ string.

(source: raw/error-correction-zoo.md)

## Protection

The $⟦2(m+1),m⟧$ family is designed to correct a single AD error  ([arXiv:0710.1052](https://arxiv.org/abs/0710.1052)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/self-complementary]] — The $⟦2(m+1),m,2⟧$ single-loss AD code is self-complementary, with the all-$X$ stabilizer enforcing the complement-pair structure of the codewords  ([arXiv:0710.1052](https://arxiv.org/abs/0710.1052)).
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
