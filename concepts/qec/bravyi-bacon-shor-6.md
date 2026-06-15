---
type: concept
name: $⟦6,2,3,2⟧$ BBS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/trapezoid
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bravyi_bacon_shor_6
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bravyi_bacon_shor_6
---

# $⟦6,2,3,2⟧$ BBS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bravyi_bacon_shor_6) (`code_id: bravyi_bacon_shor_6`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Error-detecting six-qubit BBS subsystem code with parameters $⟦6,2,3,2⟧$ that can suppress errors in adiabatic quantum computation  ([arXiv:1511.01997](https://arxiv.org/abs/1511.01997)).

The code is defined by the $3\times 3$ binary matrix
\begin{align}
A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \\ 1 & 0 & 1 \end{pmatrix},
\end{align}
with physical qubits placed at the six nonzero entries of $A$ and labeled $1$–$6$ in row-major order  ([arXiv:1008.1029](https://arxiv.org/abs/1008.1029)).
The gauge generators (excluding phases) are
\begin{align}
\begin{array}{cccccc}
  X & X & I & I & I & I \\
  I & I & X & X & I & I \\
  I & I & I & I & X & X \\
  Z & I & I & I & Z & I \\
  I & Z & Z & I & I & I \\
  I & I & I & Z & I & Z
\end{array}~,
\end{align}
where each $XX$ row corresponds to a same-row pair in $A$ and each $ZZ$ row to a same-column pair.

(source: raw/error-correction-zoo.md)

## Protection

This code detects arbitrary single-qubit errors and is used as an error-suppressing encoding with non-commuting two-local Hamiltonian terms built from gauge generators  ([arXiv:1511.01997](https://arxiv.org/abs/1511.01997)).
For the symmetric choice of coefficients considered in  ([arXiv:1511.01997](https://arxiv.org/abs/1511.01997)), the resulting two-local suppression Hamiltonian has energy separation $4-2\sqrt{3}$.

## General gates

- When both logical qubits are encoded in the same block, $X_{L1}X_{L2}$ and $Z_{L1}Z_{L2}$ are implementable using two-local physical interactions up to stabilizers  ([arXiv:1511.01997](https://arxiv.org/abs/1511.01997)).

## Relations

- _parent_: [[concepts/qec/trapezoid]] — The even-logical-qubit trapezoid family at $l=k=1$ reduces to the $⟦6,2,3,2⟧$ BBS code.
- _cousin_: [[concepts/qec/small-distance-qubit-stabilizer]]
