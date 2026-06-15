---
type: concept
name: Hermitian qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Calderbank-Rains-Shor-Sloane (CRSS) code
- $\mathbb{F}_4$-linear qubit stabilizer code
- $M_{3}$ code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/qubit-css
- concepts/qec/qubit-stabilizer
- concepts/qec/stabilizer-over-gfqsq
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stabilizer_over_gf4
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stabilizer_over_gf4
---

# Hermitian qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stabilizer_over_gf4) (`code_id: stabilizer_over_gf4`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit stabilizer code constructed from a Hermitian self-orthogonal linear quaternary code using the Hermitian construction.

Hermitian codes are in one-to-one correspondence with Hermitian self-orthogonal additive codes via the $\mathbb{F_4$ representation}.
Quaternary linear codes are Hermitian self-orthogonal (self-dual) iff they are trace-Hermitian self-orthogonal (self-dual) additive  ([doi:10.1017/CBO9780511807077](https://doi.org/10.1017/CBO9780511807077)).
In other words, if the underlying quaternary code is linear, then the field trace can be removed from the definition of inner product.

An additive self-orthogonal code $C \subseteq \mathbb{F}_4^n$ of size $2^r$ yields an $⟦n,n-r⟧$ qubit stabilizer code  ([arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)) ([arXiv:quant-ph/0005008](https://arxiv.org/abs/quant-ph/0005008)).
When $C$ is $\mathbb{F}_4$-linear of parameters $[n,k]_4$, trace self-orthogonality is equivalent to Hermitian self-orthogonality, so $|C|=4^k$ and the construction specializes to a Hermitian $⟦n,n-2k⟧$ qubit stabilizer code.
In the standard-form analysis of the linear case, the associated additive code has type $4^{k}2^{0}$, i.e., the $k_1=0$ case of Ref.  ([arXiv:quant-ph/9709049](https://arxiv.org/abs/quant-ph/9709049)); equivalently, the parameters satisfy $k \equiv n$ mod 2  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
The stabilizer generator matrix is of the form
\begin{align}
H=\begin{pmatrix}H\\
\alpha H
\end{pmatrix}~,
\end{align}
where $H$ is the parity-check matrix of the classical code.

Every Hermitian qubit stabilizer code has stabilizer generators with *paired support*  ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)): Pauli operators $P$ and $Q$ have paired support if $P$, $Q$, and $P \cdot Q$ all have the same support, and a set of generators has paired support if it can be partitioned into such pairs. The converse does not hold in general.

All code automorphisms lie in the Clifford group  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043)).

(source: raw/error-correction-zoo.md)

## Protection

For an additive self-orthogonal code $C \subseteq \mathbb{F}_4^n$, the resulting qubit stabilizer code has distance
\begin{align}
d=\min\{\operatorname{wt}(v):v \in C^{\perp}\setminus C\}~,
\end{align}
where $\perp$ denotes duality under the trace inner product  ([arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)) ([arXiv:quant-ph/0005008](https://arxiv.org/abs/quant-ph/0005008)).
The distance $d_C$ of the classical code is the Hermitian code's pure distance, and it is equal to the code distance for a non-degenerate code  ([arXiv:2312.06504](https://arxiv.org/abs/2312.06504)).
There is an equivalence between pure $⟦n,n-2k⟧$ Hermitian qubit codes and certain sets of points in projective space $PG(k-1,4)$  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)).

## Transversal gates

- All code automorphisms lie in the Clifford group  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043)), so transversal physical gates implement only Clifford logical gates.
- Transversal $SH$ and $HS$ "facet" gates (a.k.a. $M_3$ gates) which cyclically permute Paulis as $X \to Y$, $Y \to Z$, and $Z \to X$  ([arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)).
- The three-block transversal gate mapping each physical $X \to XYZ$ and each $Z \to ZXY$ implements a logical gate  ([arXiv:quant-ph/9702029](https://arxiv.org/abs/quant-ph/9702029)) ([arXiv:quant-ph/9703048](https://arxiv.org/abs/quant-ph/9703048)).
- A qubit stabilizer code is Hermitian if and only if a transversal $R$ gate leaves the stabilizer group invariant  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
- Hermitian qubit codes admit the group $U(\ell,\mathbb{F}_4)$ of diagonal transversal gates on $\ell$ codeblocks  ([arXiv:2507.10519](https://arxiv.org/abs/2507.10519)).

## General gates

- Signed weight enumerators  ([arXiv:1702.06990](https://arxiv.org/abs/1702.06990)) determine performance of magic $T$-state distillation protocols  ([arXiv:2501.10163](https://arxiv.org/abs/2501.10163)).

## Fault tolerance

- Characterizing fault-tolerant multi-qubit gates under the $\mathbb{F_4$ representation} may involve characterizing all global automorphisms of some number of copies of a code that preserve the symplectic inner product  ([arXiv:quant-ph/9703048](https://arxiv.org/abs/quant-ph/9703048)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]]
- _parent_: [[concepts/qec/stabilizer-over-gfqsq]]
- _cousin_: [`dual`](https://errorcorrectionzoo.org/c/dual) — Hermitian qubit codes are constructed from Hermitian self-orthogonal linear codes over $\mathbb{F}_4$ via the $\mathbb{F_4$ representation}.
- _cousin_: [`constacyclic`](https://errorcorrectionzoo.org/c/constacyclic) — Duadic constacyclic codes yield many examples of Hermitian qubit codes  ([arXiv:2312.06504](https://arxiv.org/abs/2312.06504)).
- _cousin_: [`graph`](https://errorcorrectionzoo.org/c/graph) — Bounds on self-dual $⟦n,0,d⟧$ Hermitian codes based on graphs have been derived  ([doi:10.1016/S0012-365X(02)00513-7](https://doi.org/10.1016/S0012-365X(02)00513-7)).
- _cousin_: [[concepts/qec/ame]] — The sole codeword of some $⟦n,0,d⟧$ Hermitian codes is an AME state  ([arXiv:2005.01426](https://arxiv.org/abs/2005.01426)).
- _cousin_: [`self_dual`](https://errorcorrectionzoo.org/c/self_dual) — Hermitian qubit codes are constructed from Hermitian self-orthogonal linear codes over $\mathbb{F}_4$ via the $\mathbb{F_4$ representation}. This relation yields bounds on self-dual codes over $\mathbb{F}_4$  ([arXiv:2501.10163](https://arxiv.org/abs/2501.10163)).
- _cousin_: [[concepts/qec/qubit-css]] — A Hermitian qubit code that can be put into CSS form via single-qubit Clifford operations remains Hermitian  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
- _cousin_: [`projective`](https://errorcorrectionzoo.org/c/projective) — There is an equivalence between pure $⟦n,n-2k⟧$ Hermitian qubit codes and certain sets of points in projective space $PG(k-1,4)$  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)).
- _cousin_: [`divisible`](https://errorcorrectionzoo.org/c/divisible) — The commutation requirement for a Hermitian stabilizer code implies that its underlying Hermitian self-orthogonal linear code over $\mathbb{F}_4$ is even; the converse is also true  ([doi:10.1017/CBO9780511807077](https://doi.org/10.1017/CBO9780511807077)).

## Notes

- Hermitian $⟦n,0,d⟧$ codes, corresponding to a self-dual $\mathbb{F}_4$ representation, are always pure  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)). See Refs.  ([arXiv:quant-ph/0503236](https://arxiv.org/abs/quant-ph/0503236), [arXiv:math/0504522](https://arxiv.org/abs/math/0504522)) for tables. Bounds on self-dual $⟦n,0,d⟧$ Hermitian codes based on graphs have been derived  ([doi:10.1016/S0012-365X(02)00513-7](https://doi.org/10.1016/S0012-365X(02)00513-7)).
- Qubit Hermitian codes for $n < 10$ have been classified  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
