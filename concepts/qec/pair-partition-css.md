---
type: concept
name: Pair-partition CPM code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/kasai
- concepts/qec/qldpc
- concepts/qec/quasi-cyclic-qldpc
- concepts/qec/qubit-css
- concepts/qec/two-branch-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/pair_partition_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: pair_partition_css
---

# Pair-partition CPM code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/pair_partition_css) (`code_id: pair_partition_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit CSS code whose $X$- and $Z$-type stabilizer generator matrices are $J$-by-$L$ arrays of $P$-by-$P$ circulant permutation matrices (CPMs), with the CSS condition enforced by pairing up block columns  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).
Each block of $H_XH_Z^T$ is a sum of $L$ CPMs, one per block column.
A *pair partition*, one per block, splits the block columns into $L/2$ pairs, and the CPM exponents are constrained so that the two CPMs in each pair coincide and cancel over $\mathbb{F}_2$.
CSS orthogonality thereby becomes a homogeneous linear condition on the exponents  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).

Fix a column weight $J$, an even row weight $L>J$, and a prime lift size $P$.
Let $C(s)$ be the $P$-by-$P$ CPM with shift $s\in\mathbb{F}_P$, and let $(e_{i\ell})$ and $(d_{j\ell})$ be $J$-by-$L$ exponent arrays over $\mathbb{F}_P$.
The generator matrices $H_X=(C(e_{i\ell}))$ and $H_Z=(C(d_{j\ell}))$ are $G$-lifts of the complete $J$-by-$L$ protograph over the cyclic group of order $P$, with length $n=LP$, row weight $L$, and column weight $J$.
A $J$-by-$J$ array $(M_{ij})$ of pair partitions, one for each $X$-type block row $i$ and $Z$-type block row $j$, is fixed before the exponents.
For each pair $\{u,v\}\in M_{ij}$, the mixed-difference equation $e_{iu}-d_{ju}=e_{iv}-d_{jv}$ is imposed.
It makes the contributions of block columns $u$ and $v$ to block $(i,j)$ of $H_XH_Z^T$ identical.
The exponents are solutions of the resulting homogeneous system over $\mathbb{F}_P$  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).

Reported instances include the $(3,10)$-regular $⟦2230,896,24⟧$ code with $P=223$ and Tanner girth eight  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).
See Ref.  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)) for the full list of reported codes.

(source: raw/error-correction-zoo.md)

## Protection

Every CPM lift of the complete $J$-by-$L$ protograph with $J\geq 2$ and $L\geq 3$ has Tanner girth at most twelve  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).
For odd $P$, $J\geq 2$, $L\geq 2J+1$, and maximal binary ranks $\operatorname{rank}H_X=\operatorname{rank}H_Z=J(P-1)+1$, permanent-based logical witnesses give the lift-size-independent bound $d_X,d_Z,d\leq (J+1)!$  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).

The thirty-six reported codes have exact distances reaching $24$ and rates reaching $0.574$, attained by the $⟦1414,812,12⟧$ code  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).
Twenty-nine of them have Tanner girth six and seven have girth eight  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qldpc]] — Both stabilizer generator matrices are sparse arrays of circulant permutation matrices with constant column weight $J$ and constant row weight $L$  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)). The reported instances have Tanner girth at least six  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).
- _parent_: [[concepts/qec/quasi-cyclic-qldpc]] — Both stabilizer generator matrices of a pair-partition CPM code are arrays of circulant permutation matrices.
This structure makes the code invariant under simultaneous cyclic shifts of the lift coordinates.
This automorphism has order equal to the prime lift size  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)).
- _cousin_: [[concepts/qec/two-branch-css]] — Both pair-partition CPM codes and two-branch coset CSS codes realize CSS commutation by matching overlaps in pairs  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091), [arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
The pair-partition construction parameterizes the matching as a free combinatorial array of pair partitions solved by linear paired-difference equations.
The two-branch construction induces the matching from the structure of a multiplicative subgroup of a finite field.
- _cousin_: [[concepts/qec/kasai]] — Replacing the circulant permutation matrices by affine permutation matrices extends the pair-partition construction.
A structured subfamily of that extension has the same check matrices as the active rows of Kasai codes.
A separate condition on the pair partitions reproduces the complementary latent rows  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091), [arXiv:2601.08824](https://arxiv.org/abs/2601.08824)).
