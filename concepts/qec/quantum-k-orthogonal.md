---
type: concept
name: $k$-orthogonal code
status: provisional
updated: '2026-09-29'
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

Qubit stabilizer code for which the binary space $S_X$ of $X$ components of stabilizers is $k$-orthogonal in the symplectic representation.
In other words, the overlap of any $j$ vectors in $S_X$ is even for every $1\leq j\leq k$  ([arXiv:2210.14066](https://arxiv.org/abs/2210.14066)).
This definition applies to general qubit stabilizer codes and does not require a CSS presentation.
This entry is formulated for qubits, but an extension exists for modular qudits  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).

Equivalently, a generator matrix for $S_X$ is $k$-orthogonal if
\begin{align}
  |x^1|&\equiv 0 \mod 2 \\
  |x^1\cdot x^2|&\equiv 0 \mod 2 \\
  |x^1\cdot x^2\cdot x^3|&\equiv 0 \mod 2 \\
  &\vdots \\
  |x^1\cdot x^2\cdot x^3\cdot\ldots\cdot x^k|&\equiv 0 \mod 2 
\end{align}
for all vectors $x^j$ in its row space, where the generalized dot-product notation means a sum of products of the respective coordinates of all vectors.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]]
- _cousin_: [[concepts/qec/qudit-color]] — The notion of $k$-orthogonality can be extended to modular-qudit codes and is known as $k^{\star}$-orthogonality  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)). Modular-qudit lattice color codes defined on lattices in $D$ spatial dimension whose $X$-type stabilizers are placed on cells of dimension $\nu \leq D$ are $k^{\star}$-orthogonal for all $k \leq \nu$  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).
