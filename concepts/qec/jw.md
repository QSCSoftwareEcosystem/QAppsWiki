---
type: concept
name: Jordan-Wigner transformation code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fermions-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/jw
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: jw
---

# Jordan-Wigner transformation code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/jw) (`code_id: jw`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A mapping between qubit Pauli strings and Majorana operators that can be thought of as a trivial $⟦n,n⟧$ code.
The mapping is best described as converting a chain of $n$ qubits into a chain of $2n$ Majorana modes (i.e., $n$ fermionic modes).
It maps Majorana operators into Pauli strings of weight $O(n)$.

The Majorana modes $\{\gamma_j\}$ are defined from Pauli strings as follows,
\begin{align}
\begin{split}
  \gamma_{0}&=Z\\
 -\gamma_{1}&=Y\\
  \gamma_{2}&=X\otimes Z\\
 -\gamma_{3}&=X\otimes Y\\
  \gamma_{4}&=X\otimes X\otimes Z\\
 -\gamma_{5}&=X\otimes X\otimes Y\\&\vdots
\end{split}
\end{align}
The $X$-type Pauli strings ensure that the resulting Majorana operators satisfy the appropriate anti-commutation relations, namely, $\{\gamma_i,\gamma_j\} = 2\delta_{ij}$.

(source: raw/error-correction-zoo.md)

## Encoders

- Circuit of depth linear in the number of qubits $n$. The depth can be reduced for particle-preserving systems  ([arXiv:2211.04501](https://arxiv.org/abs/2211.04501)) and in other contexts  ([arXiv:2110.12792](https://arxiv.org/abs/2110.12792)).

## Relations

- _parent_: [[concepts/qec/fermions-into-qubits]]
