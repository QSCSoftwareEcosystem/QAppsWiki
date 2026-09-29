---
type: concept
name: Multi-block CSS code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Multi-block chain complex (MBC) code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/data-syndrome
- concepts/qec/galois-css
- concepts/qec/multisector-hypergraph
- concepts/qec/single-shot
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/multi_block_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: multi_block_quantum
---

# Multi-block CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/multi_block_quantum) (`code_id: multi_block_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Galois-qudit CSS code constructed from $t \geq 2$ pairwise commuting square matrices $A_1,A_2,\ldots,A_t$ via a chain complex with $t+1$ non-trivial terms called a *multi-block chain (MBC) complex*  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
Its boundary maps have the block form of a $t$-fold product of two-term complexes with the Kronecker-product blocks replaced by the commuting matrices $A_i$, so that two-block CSS codes are the case $t=2$  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
Codes drawn from a sufficiently long complex carry redundant checks (metachecks) that enable single-shot decoding.

The level-$j$ space of the MBC complex $\text{mbc}(A_1,\ldots,A_t)$ consists of $\binom{t}{j}$ blocks, and its boundary matrices $Q_j$ satisfy $Q_j Q_{j+1}=0$ because the blocks commute.
Given the boundary matrices $Q_j$ of $\text{mbc}(A_1,\ldots,A_{t-1})$ and an additional commuting block $N=A_t$, the extended complex has boundary matrices  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910))
\begin{align}
  R_1=\left[N , Q_1\right],\quad
  R_i=\left[
  \begin{array}{cc}
    Q_{i-1} & 0\\ (-1)^{i-1} I\otimes N & Q_i
  \end{array}
  \right],\quad
  R_{t}=\left[
  \begin{array}{c}
    Q_{t-1}\\ (-1)^{t-1} N
  \end{array}
  \right]~,
\end{align}
where $1<i<t$ and $I$ is an identity matrix of appropriate size.
Complexes built from the same blocks taken in different orders are permutation equivalent.

A quantum code is obtained by placing qudits at any level $0<j<t$, with $H_X=Q_j$ and $H_Z=Q_{j+1}^T$.
Checks of multi-block codes are redundant: $Q_{j-1}$ yields $X$-type metachecks for $j \geq 2$, and $Q_{j+2}$ yields $Z$-type metachecks for $j \leq t-2$.
Explicit boundary matrices for $t=3$ are listed in the three-block CSS code entry, and matrices for $t=4$ are written out in Ref.  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).

(source: raw/error-correction-zoo.md)

## Protection

Code dimension and distance can be expressed in terms of ranks of matrices built out of the blocks $A_j$  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
See Ref.  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)) for dimension formulas and distance bounds in the Abelian group-algebra case (MM codes).

## Relations

- _parent_: [[concepts/qec/galois-css]]
- _cousin_: [[concepts/qec/multisector-hypergraph]] — Multi-block CSS codes are related to $t$-fold homological products of two-term chain complexes in the same way that two-block CSS codes are related to hypergraph-product codes  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
Commutativity of the blocks collapses the multi-sector tensor-product structure into square blocks  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
- _cousin_: [[concepts/qec/single-shot]] — Multi-block CSS codes at levels $2 \leq j \leq t-2$ admit metachecks in both bases, which can enable single-shot decoding  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
- _cousin_: [[concepts/qec/data-syndrome]] — The metacheck matrix of a multi-block CSS code is the boundary map just outside the code's two-term window ($Q_{j-1}$ for $X$-checks or $Q_{j+2}$ for $Z$-checks).
It provides linear relations that every valid syndrome must satisfy, flagging syndrome-measurement errors that violate them.
Such a metacheck matrix is precisely the parity-check matrix of a syndrome-measurement code.
A multi-block code with metachecks thus intrinsically realizes, via the chain complex, the redundant syndrome measurement that quantum data-syndrome codes adjoin extrinsically to a stabilizer code.
