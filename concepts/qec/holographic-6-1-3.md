---
type: concept
name: Six-qubit-tensor holographic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/holographic-tensor
- concepts/qec/qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/holographic_6_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: holographic_6_1_3
---

# Six-qubit-tensor holographic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/holographic_6_1_3) (`code_id: holographic_6_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Holographic tensor-network code constructed out of a network of encoding isometries of the $⟦6,1,3⟧$ six-qubit stabilizer code.
The structure of the isometry is similar to that of the heptagon holographic code since both isometries are rank-six tensors, but the isometry in this case is neither a perfect tensor nor a planar-perfect tensor.

(source: raw/error-correction-zoo.md)

## Rate

Zero-rate version of the code surpasses the hashing bound for certain Pauli noise  ([arXiv:2408.06232](https://arxiv.org/abs/2408.06232)).

## Code capacity threshold

- $18.8\%$ under depolarizing noise using tensor-network decoder  ([arXiv:2009.10329](https://arxiv.org/abs/2009.10329)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]]
- _parent_: [[concepts/qec/holographic-tensor]] — The encoding of the six-qubit-tensor holographic code is a holographic tensor network consisting of the encoding isometry for the $⟦6,1,3⟧$ six-qubit stabilizer code.
