---
type: concept
name: $⟦4,1,2⟧$ twist-defect code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-4-2-2
- concepts/qec/toric
- concepts/qec/twist-defect-color
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_4_1_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_4_1_2
---

# $⟦4,1,2⟧$ twist-defect code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_4_1_2) (`code_id: stab_4_1_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A four-qubit non-CSS stabilizer code that can be interpreted as the smallest triangular color code with $x$-, $y$-, and $z$-type Pauli boundaries  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)), and equivalently as a small twist-defect surface code on a tetrahedron inscribed in a sphere  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).
It is the only non-CSS qubit stabilizer code with parameters $⟦4,1,2⟧$.
The code admits weight-three stabilizer generators and weight-two logical Pauli $X,Y,Z$ operators.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{cccc}
  X & I & X & X \\
  Y & Y & I & Y \\
  Z & Z & Z & I
\end{array}~.
\end{align}

Stabilizer generators are shown in \ref{figure:412-operators}.

(source: raw/error-correction-zoo.md)

## Protection

Detects a single-qubit error or single erasure as a distance-two code.

## Transversal gates

- Weight-two transversal logical Pauli $X,Y,Z$ operations  ([arXiv:quant-ph/0512170](https://arxiv.org/abs/quant-ph/0512170)).

## General gates

- A set of local Clifford operations and permutations (in the twist-defect realization, braiding the four genons) generates the full single-qubit Clifford group  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).

## Realizations

- Logical Clifford gates were realized in a trapped-ion device by Quantinuum  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).

## Relations

- _parent_: [[concepts/qec/twist-defect-color]] — The $⟦4,1,2⟧$ twist-defect code is the smallest triangular color code with $x$-, $y$-, and $z$-type Pauli boundaries, which make the code non-CSS  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).
- _parent_: [[concepts/qec/twist-defect-surface]] — The $⟦4,1,2⟧$ twist-defect code is equivalent to a twist-defect surface code on a tetrahedron inscribed in a sphere  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)) via a single-qubit Clifford circuit.
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/stab-4-2-2]] — Adding $XYZI$ to the stabilizer group of the $⟦4,2,2⟧$ four-qubit code yields the $⟦4,1,2⟧$ twist-defect subcode  ([arXiv:quant-ph/0512170](https://arxiv.org/abs/quant-ph/0512170)).
- _cousin_: [[concepts/qec/toric]] — The symplectic double of the $⟦4,1,2⟧$ twist-defect code is the $⟦8,2,2⟧$ twisted toric code  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).
