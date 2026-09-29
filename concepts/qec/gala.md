---
type: concept
name: Group-action lift with active orthogonality (GALA) code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/actively-orthogonal-css
- concepts/qec/kasai
- concepts/qec/perm-self-dual-css
- concepts/qec/quasi-cyclic-qldpc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/gala
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: gala
---

# Group-action lift with active orthogonality (GALA) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/gala) (`code_id: gala`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Actively orthogonal CSS code whose lifts are drawn from a direct product $H_k \times C_m$, or a semidirect product $H_k \ltimes C_m^k$, of a small non-Abelian group $H_k$ and a large Abelian group $C_m$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
For a direct product, two lifts commute exactly when their $H_k$ parts commute, so the non-Abelian *top factor* alone decides the active orthogonality pattern.
The Abelian *bottom factor* is unconstrained by that pattern, and its shifts are code automorphisms.
They also make the qubit permutation between syndrome-extraction rounds one rigid row move and one rigid column move, the parallel moves native to crossed acousto-optic deflectors  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

Given $L$, $J \leq L/2$, and an active set $\Gamma$, a *direct product* GALA code $\mathrm{GALA}_{L,J}(H_k \times C_m)$ is defined on $n=Lkm$ qubits by choosing lifts
\begin{align}
  \mathcal{F}=\{(F_i,f_i)\}_{i\in[L/2]}~,\qquad \mathcal{G}=\{(G_i,g_i)\}_{i\in[L/2]}~,
\end{align}
with $F_i,G_i$ in the non-Abelian permutation group $H_k$ and $f_i,g_i$ in the Abelian permutation group $C_m$, such that $[F_i,G_j]=0$ for every $(i,j)\in\Gamma$.
The stabilizer generator matrices are the first $J$ block rows of the parents $\hat{H}_X=[F|G]$ and $\hat{H}_Z=[G^T|F^T]$.
The Abelian entries are unconstrained by the commutation pattern and can be chosen freely to improve girth and distance  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Semidirect product GALA codes replace the direct product with $H_k \ltimes C_m^k$, in which $H_k$ permutes the $k$ blocks and $C_m$ acts within each block  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Polynomial GALA codes replace each single-element lift by a sum of group elements, which decouples the stabilizer generator weight from $L$, and admit loose active orthogonality  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
When the top factor is Abelian or trivial, the group ring is commutative and no pair fails to commute, so the parents are fully orthogonal  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

When $4 \mid L$, a ZX duality is obtained by requiring $F_i G_{r(i)} = t$ for a group element $t$ and one of four block-index involutions $r$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
The involutions are $i\mapsto i$ and $i\mapsto i+L/4$ (translations) or $i\mapsto -i$ and $i\mapsto L/4-i$ (reflections).
The duality is a qubit permutation $\tau$ with $H_Z = H_X \tau$.
For monomial GALA codes, the reflection $i\mapsto -i$ forces girth four whenever $J\geq 2$, and the reflection $i\mapsto L/4-i$ does so in the balanced case $J=L/4$.
In that balanced case the latter reflection also forces full parent orthogonality and, whenever some latent row lies outside the retained row space, $d\leq L$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Within the parameter range covered by these results, only translation-type involutions are compatible with girth at least six.

The $⟦2232,1120,16⟧$ code has stabilizer generator weight $12$ and an exactly certified distance above that weight at rate above one half  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
See Ref.  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)) for all certified instances.

(source: raw/error-correction-zoo.md)

## Protection

For monomial lifts, the encoding rate bound $1-2J/L$ of the parent family sharpens to $1-2J/L+2(J-1)/n$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

Distance bounds follow both directly from $J$ and $L$ and from the quotient codes obtained by collapsing subgroups of the lift group  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
For monomial lifts, $J>L/4$ forces full parent orthogonality and, whenever some latent row lies outside the retained row space of its type, $d\leq L$.
Taking $J\leq2$ instead gives $d\leq g/2$, and for $L<12$ the weight barrier persists unless $n\geq L(L-1)^{d/2-1}$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Polynomial lifts evade the $J\leq2$ mechanism, which is how the compact $L=8$, weight-$12$ instances below reach distances $10$ and $12$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

All of the following have exactly certified distances, stabilizer generator weight $12$, and girth at least six unless noted  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
Rate-one-half instances include $⟦480,240,10⟧$, $⟦672,336,12⟧$, and $⟦720,360,12⟧$, the latter two sitting at the ceiling where the distance equals the generator weight.
The $⟦672,336,12⟧$ code has a trivial top factor, showing that the Abelian sector together with a polynomial lift already suffices for a compact rate-one-half code at that ceiling  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
The $⟦1752,880,14⟧$ code also has distance above the generator weight.
Instances with a ZX duality include $⟦1056,532,12⟧$ and the girth-four $⟦132,30,12⟧$ self-dual GALA code.

## Transversal gates

- A ZX duality $\tau$ yields Hadamard-type and phase-type fold-transversal Clifford operations  ([arXiv:2202.06647](https://arxiv.org/abs/2202.06647)). Each is realized by one layer of physical Clifford gates together with one qubit permutation, the same primitives and cost as a round of syndrome extraction  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). Their encoded actions depend on the logical basis and need not be tensor products of one-logical-qubit Hadamard and phase gates. When the duality is the identity permutation, both physical operations reduce to a single depth-one layer of single-qubit gates.
- The diagonal copy of the Abelian factor is central and therefore consists of code automorphisms, which act as logical permutations and cyclic shifts  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

## General gates

- Collapsing a subgroup of the Abelian factor gives a chain homomorphism onto a quotient code, yielding transversal CNOT gadgets and logical measurements addressing several logical qubits in parallel  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). These gadgets are in principle sufficient for arbitrary logical Clifford operations, but fault tolerance is not established because the quotient maps are not distance preserving in general.

## Decoders

- Relay-BP decoding cascade with a mixed-integer linear-programming fallback  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

## Fault tolerance

- For monomial direct-product and restricted semidirect-product lifts, syndrome extraction runs in $L$ rounds. The Abelian factor is written as $C_m\cong C_p\times C_q$ and the qubits are laid out on a $kp\times Lq$ array. The permutation relating consecutive rounds then factors into a rigid row move and a rigid column move  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). The two act on disjoint coordinates and can be applied at the same time. The non-Abelian factor is placed on the row axis so that its permutations do not conflict. Unrestricted semidirect products instead give per-block shifts applied in sequence  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). Polynomial lifts, whose stabilizer weight can exceed $L$, use a separately colored syndrome-extraction circuit  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

## Threshold

- Circuit-level noise: pseudo-thresholds of about $0.4\%$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). At physical error rate $10^{-3}$, the $⟦672,336,12⟧$ code has an extrapolated logical error rate of about $5\times10^{-11}$ at an overhead of three physical qubits per logical qubit.

## Relations

- _parent_: [[concepts/qec/actively-orthogonal-css]] — GALA codes are actively orthogonal CSS codes whose direct-product monomial lifts are generally drawn from a product of a non-Abelian and an Abelian group  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). Polynomial and special sectors allow Abelian or trivial top factors  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
- _cousin_: [[concepts/qec/perm-self-dual-css]] — GALA codes satisfying the block-index involution condition have check matrices related by a qubit permutation, $H_Z = H_X \tau$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). Such a code is permutationally self-dual whenever $\tau$ is an involution, since $\tau$ then also maps $H_Z$ onto $H_X$.
- _cousin_: [[concepts/qec/quasi-cyclic-qldpc]] — GALA codes with a cyclic Abelian lift action are QC-QLDPC codes, but the framework also permits more general Abelian permutation actions  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
- _cousin_: [[concepts/qec/kasai]] — Kasai codes whose reference affine permutation acts freely, or which admit a coprime factorization of the lift size with commuting reductions, are GALA codes  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). The GALA framework replaces the affine permutations, whose symmetries arise incidentally, with an explicit group product in which the non-Abelian factor governs orthogonality and the Abelian factor governs symmetry.
