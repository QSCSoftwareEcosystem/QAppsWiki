---
type: concept
name: Actively orthogonal CSS code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/lifted-product
- concepts/qec/pair-partition-css
- concepts/qec/qldpc
- concepts/qec/qubit-css
- concepts/qec/two-block-quantum
- concepts/qec/two-branch-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/actively_orthogonal_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: actively_orthogonal_css
---

# Actively orthogonal CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/actively_orthogonal_css) (`code_id: actively_orthogonal_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit CSS code whose stabilizer generator matrices are the first $J$ block rows, the *active* rows, of a pair of block-circulant parent matrices $\hat{H}_X$ and $\hat{H}_Z$, with the CSS orthogonality condition imposed only among those rows  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824)).
The discarded *latent* rows need not commute with the active checks of the opposite type, so neither they nor their low-weight combinations automatically become logical operators.
The distance can therefore exceed the stabilizer generator weight at rate at or above one half.

If the parents were orthogonal, every latent row would commute with all active checks, and a latent row outside the stabilizer row space would be a logical operator of weight equal to its row weight.
This caps the distance of any row-deleted fully orthogonal construction at the stabilizer generator weight  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824)).
The parents have $L/2$ block rows and $L$ block columns and are assembled by a $G$-lift, in which every nonzero entry of a circulant proto-matrix is replaced by a permutation matrix drawn from a group $G$.
Each block row of $\hat{H}_X$ is a cyclic shift of the lifts $\mathcal{F}=\{F_i\}$ in its left half and of the lifts $\mathcal{G}=\{G_i\}$ in its right half.
The matrix $\hat{H}_Z$ holds the transposed lifts with the two halves exchanged and the shift reversed  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824)).
Because both parents are block circulant, the $(i,j)$ block of $\hat{H}_X\hat{H}_Z^T$ depends only on the offset $j-i$ and collects the commutators of all lift pairs whose indices sum to that offset.
Requiring $[F_i,G_j]=0$ for every index pair $(i,j)$ in a chosen *active set* $\Gamma$ that covers the offsets between active rows makes these blocks vanish for all $0 \leq i,j < J$, so the retained rows define a CSS code  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824)).
Commutation is deliberately broken for at least one pair outside $\Gamma$, which keeps some block between an active and a latent row nonzero.

Kasai codes draw the lifts from the affine permutation group, and GALA codes from a product of a small non-Abelian *top factor*, which decides the commutation pattern, and an Abelian *bottom factor*, which supplies code automorphisms  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824), [arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
When the top factor is Abelian or trivial, no pair fails to commute and the parent matrices are fully orthogonal  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Polynomial variants replace a single permutation in each lift entry by a sum of group elements  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Loose active orthogonality then requires only the aggregate commutator sum at each active offset to vanish, rather than every contributing pair commuting individually  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
These variants remain actively orthogonal, but the pairwise condition above and the sharp monomial bounds below no longer apply.

(source: raw/error-correction-zoo.md)

## Protection

Retaining $J$ block rows in each basis yields encoding rate at least $1-2J/L$, so that $J \leq L/4$ guarantees rate at least one half  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Girth eight is attained by the original Kasai code  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824)) and girth at least six by most of the compact GALA instances  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

Any latent-row combination that commutes with the opposite-type active checks but lies outside the same-type stabilizer row space is a logical operator, and the least weight of such a combination upper bounds the minimum distance  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824)).

The sharpest limitations are proved for strict monomial GALA and Kasai lifts, for which every stabilizer row has weight $L$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Taking $J>L/4$ forces full orthogonality of the parents.
Provided at least one latent row lies outside the retained row space of its type, that row is a weight-$L$ logical operator and $d\leq L$.
If every latent row is already in the retained row space, the retained code equals its fully orthogonal parent and this augmentation argument supplies no distance bound.
At the other extreme, $J\leq 2$ gives $d\leq g/2$, where $g$ is the Tanner-graph girth.
Thus a monomial lift can break the weight barrier only in the window $L\geq 12$ and $2<J\leq L/4$, apart from the possibility of a block length exponential in the target distance.

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/two-block-quantum]] — Retaining the first $J$ block rows of the parent matrices $\hat{H}_X=[F|G]$ and $\hat{H}_Z=[G^{T}|F^{T}]$ gives $H_X=(A_1,B_1)$ and $H_Z=(B_2^{T},A_2^{T})$. Here $A_1,B_1$ are the active block rows of the two block circulants and $A_2,B_2$ their active block columns. Active orthogonality $H_XH_Z^{T}=0$ is exactly the two-block condition $A_1B_2-B_1A_2=0$, and the GALA sectors are defined as two-block CSS codes outright  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)) ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824)).
- _cousin_: [[concepts/qec/pair-partition-css]] — Both families impose CSS orthogonality algebraically rather than through a product construction, but by different mechanisms. Pair-partition CPM codes match column types in pairs so that every overlap between an $X$-type and a $Z$-type generator occurs an even number of times  ([arXiv:2607.14091](https://arxiv.org/abs/2607.14091)). Actively orthogonal CSS codes instead impose the condition only on the active rows retained from a larger pair of parent matrices  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824)).
- _cousin_: [[concepts/qec/two-branch-css]] — Both families impose CSS orthogonality algebraically rather than through a product construction, but by different mechanisms. Two-branch coset CSS codes reduce the commutation condition to equalities and disjointness conditions on multiplicative cosets of a finite field  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)). Actively orthogonal CSS codes instead impose the condition only on the active rows retained from a larger pair of parent matrices  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824)).
- _cousin_: [[concepts/qec/lifted-product]] — LP codes enforce the CSS orthogonality condition as an algebraic identity on all rows, whereas actively orthogonal CSS codes impose it only on the retained rows  ([arXiv:2601.08824](https://arxiv.org/abs/2601.08824), [arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
