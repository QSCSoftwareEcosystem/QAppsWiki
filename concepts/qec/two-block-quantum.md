---
type: concept
name: Two-block CSS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Two-sublattice code
- Two-square-block code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-css
- concepts/qec/general-qldpc
- concepts/qec/lifted-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/two_block_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: two_block_quantum
---

# Two-block CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/two_block_quantum) (`code_id: two_block_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Galois-qudit CSS code whose stabilizer generator matrices $H_X=(A_1,B_1)$ and $H_Z=(B^T_2,-A^T_2)$, are constructed from four matrices satisfying $A_1 B_2 - B_1 A_2 = 0$.
In the case the two pairs are equal, we have $H_X=(A,B)$ and $H_Z=(B^T,-A^T)$, constructed from a pair of square commuting matrices $A$ and $B$.

Generalized constructions utilizing more than two blocks have also been considered  ([arXiv:2310.15092](https://arxiv.org/abs/2310.15092)).

(source: raw/error-correction-zoo.md)

## Protection

Code parameters are generally unknown, although they can be formally expressed in terms of ranks of some matrices related to $A$ and $B$.
The corresponding expressions, as well as some upper and lower bounds on parameters are given in  ([arXiv:2306.16400](https://arxiv.org/abs/2306.16400)).

## Relations

- _parent_: [[concepts/qec/galois-css]]
- _cousin_: [[concepts/qec/general-qldpc]] — When matrices $A$ and $B$ have row and column weights bounded by $W$, a two-block CSS code is a quantum LDPC code with stabilizer generators bounded by $2W$.
- _cousin_: [[concepts/qec/lifted-product]] — LP codes can be constructed using non-square matrices and taking a hypergraph product over a group algebra, while two-block CSS codes are constructed directly using square matrices.
