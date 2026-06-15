---
type: concept
name: Surface-code-fragment (SCF) holographic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-perfect
- concepts/qec/holographic-tensor
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/holographic_5_1_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: holographic_5_1_2
---

# Surface-code-fragment (SCF) holographic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/holographic_5_1_2) (`code_id: holographic_5_1_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Holographic tensor-network code constructed out of a network of encoding isometries of the $⟦5,1,2⟧$ rotated surface code.
The structure of the isometry is similar to that of the HaPPY code since both isometries are rank-six tensors.
In the case of the SCF holographic code, the isometry is only a planar-perfect tensor (as opposed to a perfect tensor).

(source: raw/error-correction-zoo.md)

## Rate

Zero-rate version of the code surpasses the hashing bound under certain Pauli noise  ([arXiv:2408.06232](https://arxiv.org/abs/2408.06232)).

## Code capacity threshold

- $7.1\%$ and $8.2\%$ for even- and odd-radii reduced-rate codes, respectively, under depolarizing noise using the integer-optimization decoder  ([arXiv:2008.10206](https://arxiv.org/abs/2008.10206)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/holographic-tensor]] — The encoding of the heptagon holographic code is a holographic tensor network consisting of the encoding isometry for the $⟦5,1,2⟧$ rotated surface code, which is a planar-perfect tensor.
- _cousin_: [[concepts/qec/block-perfect]] — The encoding of the heptagon holographic code is a holographic tensor network consisting of the encoding isometry for the $⟦5,1,2⟧$ rotated surface code, which is a planar-perfect tensor.
