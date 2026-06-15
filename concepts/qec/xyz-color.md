---
type: concept
name: XYZ color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fracton
- concepts/qec/triangular-color
- concepts/qec/twist-defect-color
- concepts/qec/xzzx
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/xyz_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: xyz_color
---

# XYZ color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/xyz_color) (`code_id: xyz_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A variant of the 6.6.6 color code whose generators are $XZXZXZ$ and $ZYZYZY$ Pauli strings associated to each hexagonal in the hexagonal (6.6.6) tiling. 
A further variation called the *domain wall color code* admits generators of the form $XXXZZZ$ and $ZZZXXX$  ([arXiv:2307.00054](https://arxiv.org/abs/2307.00054)).
While such codes are equivalent to CSS color codes with the same distance, other properties like noise-bias performance can differ significantly.

(source: raw/error-correction-zoo.md)

## Decoders

- Efficient ML decoder at infinite bias  ([arXiv:2203.16534](https://arxiv.org/abs/2203.16534)).
- Cellular-automaton decoder  ([arXiv:2203.16534](https://arxiv.org/abs/2203.16534)).

## Code capacity threshold

- $50\%$ threshold for noise infinitely biased towards $X$ or $Y$ or $Z$ errors using cellular-automaton decoder  ([arXiv:2203.16534](https://arxiv.org/abs/2203.16534)).
- Independent $X,Y$ noise: threshold value of the sum of both noise probabilities is between $9\%$ and $14\%$, depending on the noise bias  ([arXiv:2203.16534](https://arxiv.org/abs/2203.16534)).

## Relations

- _parent_: [[concepts/qec/twist-defect-color]]
- _cousin_: [[concepts/qec/triangular-color]] — The XYZ color code is obtained from the 6.6.6 color code by applying single-qubit Clifford rotations on a subset of qubits such that the $X$- and $Z$-type generators are mapped to $XZXZXZ$ and $ZYZYZY$, respectively.
- _cousin_: [[concepts/qec/xzzx]] — The XZZX surface (XYZ color) is a non-CSS analogue of the rotated surface (6.6.6 color) code such that the two codes are related by single-qubit Clifford rotations.
- _cousin_: [[concepts/qec/fracton]] — The XYZ color code resembles a Type-II fracton code in the limit of infinite noise bias  ([arXiv:2203.16534](https://arxiv.org/abs/2203.16534)).
