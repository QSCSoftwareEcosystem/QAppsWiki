---
type: concept
name: $k$-orthogonal code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-stabilizer
- concepts/qec/qudit-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_k-orthogonal
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_k-orthogonal
---

# $k$-orthogonal code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_k-orthogonal) (`code_id: quantum_k-orthogonal`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit stabilizer code whose $X$-type logicals and generators form a $k$-orthogonal matrix (defined below) in the symplectic representation.
In other words, the overlap between any $k$ $X$-type code-preserving Paulis (including the identity) is even.
The original definition is for qubit CSS codes  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)), but it can be extended to more general qubit stabilizer codes  ([arXiv:2210.14066](https://arxiv.org/abs/2210.14066)).
This entry is formulated for qubits, but an extension exists for modular qudits  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).

A matrix is $k$-orthogonal  ([arXiv:2210.14066](https://arxiv.org/abs/2210.14066)) if
\begin{align}
  |x^1|&\equiv 0 \mod 2 \\
  |x^1\cdot x^2|&\equiv 0 \mod 2 \\
  |x^1\cdot x^2\cdot x^3|&\equiv 0 \mod 2 \\
  &\vdots \\
  |x^1\cdot x^2\cdot x^3\cdot\ldots\cdot x^k|&\equiv 0 \mod 2 
\end{align}
for all its rows $x^j$, where the generalized dot-product notation means a sum of products of the respective coordinates of all vectors.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]]
- _cousin_: [[concepts/qec/qudit-color]] — The notion of $k$-orthogonality can be extended to modular-qudit codes and is known as $k^{\star}$-orthogonality  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)). Modular-qudit lattice color codes defined on lattices in $D$ spatial dimension whose $X$-type stabilizers are placed on cells of dimension $\nu \leq D$ are $k^{\star}$-orthogonal for all $k \leq \nu$  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).
