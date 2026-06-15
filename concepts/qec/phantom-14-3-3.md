---
type: concept
name: $⟦14,3,3⟧$ CE phantom code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/constant-excitation
- concepts/qec/phantom
- concepts/qec/quantum-repetition
- concepts/qec/qubit-concatenated
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/steane
- concepts/qec/xz-7-3-2
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/phantom_14_3_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: phantom_14_3_3
---

# $⟦14,3,3⟧$ CE phantom code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/phantom_14_3_3) (`code_id: phantom_14_3_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

CSS phantom code obtained by concatenating the $⟦7,3,(d_X=3,d_Z=2)⟧$ punctured hypercube code with the two-qubit phase-flip repetition code.
The code is equivalent to the $⟦14,3,3⟧$ constant-excitation (CE) CSS code obtained by applying dual-rail concatenation to the $⟦7,3,2⟧$ punctured hypercube code, up to single-qubit Clifford gates, a physical-qubit permutation, and a Pauli frame  ([arXiv:2507.10395](https://arxiv.org/abs/2507.10395)).

One stabilizer tableau for the code is
\begin{align}
\begin{smallmatrix}
  Z & Z & Z & Z & Z & Z & I & I & I & I & I & I & Z & Z \\
  I & I & Z & Z & I & I & Z & Z & I & I & Z & Z & Z & Z \\
  Z & Z & Z & Z & I & I & I & I & Z & Z & Z & Z & I & I \\
  X & X & I & I & I & I & I & I & I & I & I & I & I & I \\
  I & I & X & X & I & I & I & I & I & I & I & I & I & I \\
  I & I & I & I & X & X & I & I & I & I & I & I & I & I \\
  I & I & I & I & I & I & X & X & I & I & I & I & I & I \\
  I & I & I & I & I & I & I & I & X & X & I & I & I & I \\
  I & I & I & I & I & I & I & I & I & I & X & X & I & I \\
  I & I & I & I & I & I & I & I & I & I & I & I & X & X \\
  X & I & X & I & X & I & X & I & X & I & X & I & X & I
\end{smallmatrix}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

Corrects a single-qubit error. Its $X$- and $Z$-sector distances are $d_X=3$ and $d_Z=4$, respectively  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

## General gates

- The code is phantom, so every ordered-pair in-block logical CNOT gate between its three logical qubits can be implemented by a physical-qubit permutation  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- The Hadamard-dual code admits fold-diagonal logical $S_iS_j$ and $CZ_{ij}$ gates  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

## Fault tolerance

- In the locally Clifford-equivalent CE CSS frame, fault-tolerant syndrome extraction can use modified Shor and Steane methods adapted for CE codes: weight-$2w$ stabilizers are measured using $w$-CE cat states, and zero-controlled NOT ($\mathrm{C}_0 X$) gates replace standard CNOT gates to preserve the constant-excitation structure  ([arXiv:2507.10395](https://arxiv.org/abs/2507.10395)).

## Relations

- _parent_: [[concepts/qec/phantom]] — This $⟦14,3,3⟧$ code is a CSS phantom code obtained from the punctured hypercube code and the two-qubit phase-flip repetition code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _parent_: [[concepts/qec/constant-excitation]] — This code is single-qubit Clifford equivalent to the $⟦14,3,3⟧$ CE CSS code obtained by dual-rail concatenation of the $⟦7,3,2⟧$ punctured hypercube code  ([arXiv:2507.10395](https://arxiv.org/abs/2507.10395)).
- _parent_: [[concepts/qec/qubit-concatenated]] — This code is a concatenation of the $⟦7,3,2⟧$ punctured hypercube code with the two-qubit phase-flip repetition code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/xz-7-3-2]] — Concatenating the $⟦7,3,(d_X=3,d_Z=2)⟧$ punctured hypercube code with the two-qubit phase-flip repetition code yields this $⟦14,3,(d_X=3,d_Z=4)⟧$ CSS phantom code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)). Dual-rail concatenation of the same punctured hypercube code yields a single-qubit Clifford-equivalent CE CSS frame  ([arXiv:2507.10395](https://arxiv.org/abs/2507.10395)).
- _cousin_: [[concepts/qec/steane]] — Dual-rail concatenation of the $⟦7,1,3⟧$ Steane code yields a $⟦14,1,3⟧$ CE CSS code, from which the locally Clifford-equivalent $⟦14,3,3⟧$ CE CSS frame is obtained by removing two independent $Z$-type stabilizer generators  ([arXiv:2507.10395](https://arxiv.org/abs/2507.10395)).
- _cousin_: [[concepts/qec/quantum-repetition]] — The inner code in the construction is the two-qubit phase-flip repetition code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
