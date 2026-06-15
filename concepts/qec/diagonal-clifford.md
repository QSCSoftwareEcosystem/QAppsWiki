---
type: concept
name: $⟦2^r-1,1,3⟧$ simplex code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $⟦2^r-1,1,3⟧$ quantum RM code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/color
- concepts/qec/quantum-divisible
- concepts/qec/quantum-k-orthogonal
- concepts/qec/quantum-reed-muller
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/xp-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/diagonal_clifford
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: diagonal_clifford
---

# $⟦2^r-1,1,3⟧$ simplex code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/diagonal_clifford) (`code_id: diagonal_clifford`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a color-code family constructed from a punctured first-order RM$(1,m=r)$ code and its even subcode for $r \geq 3$.
Each code transversally implements a diagonal gate at the $(r-1)$st level of the \term{Clifford hierarchy}  ([arXiv:quant-ph/0611214](https://arxiv.org/abs/quant-ph/0611214), [arXiv:1608.06596](https://arxiv.org/abs/1608.06596)).
Each code is a color code defined on a simplex in $r-1$ dimensions  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879), [arXiv:1503.08217](https://arxiv.org/abs/1503.08217)), where qubits are placed on the vertices, edges, and faces as well as on the simplex itself.

The family also admits an XP-stabilizer presentation at precision $N = 2^{r-2}$ whose generators are symmetric in $X$ and $P$, and only $2r$ such generators are needed to stabilize the codespace  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)).
Morphing the $r$-dimensional distance-three code in this family yields a $⟦2^r+r-1,1,2⟧$ code with a fault-tolerant logical gate at the $(r-1)$st level of the Clifford hierarchy  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- Each code transversally implements a diagonal gate at the $(r-1)$st level of the \term{Clifford hierarchy} in the form of a $Z$-rotation by angle $-\pi/2^{r-1}$  ([arXiv:quant-ph/0611214](https://arxiv.org/abs/quant-ph/0611214), [arXiv:1608.06596](https://arxiv.org/abs/1608.06596)). These are the smallest distance-three qubit stabilizer codes with such a (strongly) transversal gate  ([arXiv:2210.14066](https://arxiv.org/abs/2210.14066)).

## Fault tolerance

- Fault-tolerant syndrome extraction circuits using flag qubits  ([arXiv:1708.02246](https://arxiv.org/abs/1708.02246)).

## Relations

- _parent_: [[concepts/qec/quantum-reed-muller]] — $⟦2^r-1,1,3⟧$ simplex codes are special cases of the $⟦\sum_{i=w+1}^m \binom{m}{i}, \sum_{i=0}^{w} \binom{m}{i}, \sum_{i=w+1}^{r+1} \binom{r+1}{i}⟧$ quantum RM codes for $w=0$ and $r=1$, with $m$ equal to the present entry's parameter $r$  ([arXiv:1709.03543](https://arxiv.org/abs/1709.03543)).
- _parent_: [[concepts/qec/color]] — Each $⟦2^r-1,1,3⟧$ simplex code is a color code defined on a simplex in $r-1$ dimensions  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879), [arXiv:1503.08217](https://arxiv.org/abs/1503.08217)).
- _parent_: [[concepts/qec/quantum-divisible]] — $⟦2^r-1,1,3⟧$ simplex codes come from RM$(1,m=r)$ codes, which are $(r-1)$-even  ([doi:10.1016/0097-3165(71)90066-5](https://doi.org/10.1016/0097-3165(71)90066-5), [doi:10.1016/0012-365X(72)90032-5](https://doi.org/10.1016/0012-365X(72)90032-5)), and admit transversal gates at levels of the \term{Clifford hierarchy}. Building a tower of generalized divisible codes by starting with the Steane code yields the $⟦2^r-1,1,3⟧$ simplex codes  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/xp-stabilizer]] — Each $⟦2^r-1,1,3⟧$ simplex code can be viewed as an XP stabilizer code with precision $N = 2^{r-2}$  ([arXiv:2203.00103](https://arxiv.org/abs/2203.00103)).
- _cousin_: [[concepts/qec/quantum-k-orthogonal]] — $⟦2^r-1,1,3⟧$ simplex codes are $(r-1)$-orthogonal  ([arXiv:2210.14066](https://arxiv.org/abs/2210.14066)).
- _cousin_: [`biorthogonal`](https://errorcorrectionzoo.org/c/biorthogonal) — The $⟦2^r-1,1,3⟧$ simplex code is constructed with a punctured first-order RM code and its even subcode.
- _cousin_: [`simplex_spherical`](https://errorcorrectionzoo.org/c/simplex_spherical) — Each $⟦2^r-1,1,3⟧$ simplex code is a color code whose qubits are placed on the vertices, edges, and faces of an $(r-1)$-simplex  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879), [arXiv:1503.08217](https://arxiv.org/abs/1503.08217)).
