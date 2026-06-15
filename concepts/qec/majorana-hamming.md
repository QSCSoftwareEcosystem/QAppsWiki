---
type: concept
name: $⟦2^{m-1},2^{m-1}-m-1,4⟧_{f}$ Hamming Majorana code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/majorana-color
- concepts/qec/majorana-reed-muller
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-4-2-2
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/majorana_hamming
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: majorana_hamming
---

# $⟦2^{m-1},2^{m-1}-m-1,4⟧_{f}$ Hamming Majorana code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/majorana_hamming) (`code_id: majorana_hamming`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of the $⟦2^{m-1},2^{m-1}-m-1,4⟧_{f}$ family of Majorana stabilizer codes for $m \geq 3$ constructed from a self-orthogonal first-order RM code (whose dual is the extended Hamming code).
A shortened $⟦2^{m-1}-1,2^{m-1}-m-2,3⟧_{f}$ version can also be defined  ([arXiv:2502.14165](https://arxiv.org/abs/2502.14165)).
The logical subspace of the $⟦8,3,4⟧_{f}$ Hamming Majorana code is a Cartan subspace of the $E_8$ Lie algebra  ([arXiv:1801.06998](https://arxiv.org/abs/1801.06998)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/majorana-reed-muller]] — A Hamming Majorana code is constructed from a first-order RM code (whose dual is the extended Hamming code).
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [`extended_hamming`](https://errorcorrectionzoo.org/c/extended_hamming) — A Hamming Majorana code is constructed from a first-order RM code (whose dual is the extended Hamming code).
- _cousin_: [`biorthogonal`](https://errorcorrectionzoo.org/c/biorthogonal) — A Hamming Majorana code is constructed from a first-order RM code (whose dual is the extended Hamming code).
- _cousin_: [`eeight`](https://errorcorrectionzoo.org/c/eeight) — The logical subspace of the $⟦8,3,4⟧_{f}$ Hamming Majorana code is a Cartan subspace of the $E_8$ Lie algebra  ([arXiv:1801.06998](https://arxiv.org/abs/1801.06998)).
- _cousin_: [[concepts/qec/stab-4-2-2]] — The $⟦8,3,4⟧_{f}$ Hamming Majorana code is a Majorana stabilizer code obtained by combining two four-qubit codes  ([arXiv:1801.06998](https://arxiv.org/abs/1801.06998)).
- _cousin_: [[concepts/qec/majorana-color]] — The $⟦8,3,4⟧_{f}$ Hamming Majorana code can replace stacks of three tetrons in a 4.8.8 Majorana surface code to yield an order-3 Majorana color code with maximum stabilizer weight $16$  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
