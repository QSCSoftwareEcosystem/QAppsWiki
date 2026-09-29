---
type: concept
name: $⟦13,1,5⟧$ quantum QR code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-quad-residue
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quad_residue_13_1_5
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quad_residue_13_1_5
---

# $⟦13,1,5⟧$ quantum QR code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quad_residue_13_1_5) (`code_id: quad_residue_13_1_5`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Thirteen-qubit cyclic Hermitian qubit code derived from a quaternary quadratic-residue code using the Hermitian construction  ([arXiv:quant-ph/9704019](https://arxiv.org/abs/quant-ph/9704019)) ([arXiv:2211.00891](https://arxiv.org/abs/2211.00891)).
The code admits a stabilizer tableau whose rows are cyclic permutations of the Pauli string $XXZZIZIIIZIZZ$ .

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/stabilizer-over-gf4]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/galois-quad-residue]] — The $⟦13,1,5⟧$ code is obtained from a quaternary QR code via the Hermitian construction and is not CSS, in contrast to quantum QR codes, which are obtained via the CSS construction  ([arXiv:quant-ph/9704019](https://arxiv.org/abs/quant-ph/9704019)).
- _cousin_: [`q-ary_quad_residue`](https://errorcorrectionzoo.org/c/q-ary_quad_residue) — The stabilizer group of the $⟦13,1,5⟧$ code is defined by a quaternary QR code of length 13  ([arXiv:quant-ph/9704019](https://arxiv.org/abs/quant-ph/9704019)).
