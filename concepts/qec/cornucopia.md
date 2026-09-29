---
type: concept
name: Cornucopia code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/gala
- concepts/qec/kasai
- concepts/qec/kasai-1152
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cornucopia
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cornucopia
---

# Cornucopia code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cornucopia) (`code_id: cornucopia`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

GALA code with rate just above one half whose $G$-lift entries are affine permutations of a $\mathbb{Z}_3\times\mathbb{Z}_q$ grid.
The layout and the syndrome-extraction schedule are designed together, so that a full syndrome cycle takes twelve entangling layers regardless of the code size.

The code has $n=36q$ qubits partitioned into twelve blocks of $P=3q$ with $\gcd(q,3)=1$, each block laid out as a $3\times q$ array, and three blocks of checks of each type.
The twelve lift entries $A_k$ and $B_k$, for $k\in\mathbb{Z}_6$, each act on the grid as an affine map $(x,y)\mapsto(ax+b,y+s)$, so the row part lies in the affine group of $\mathbb{Z}_3$, which is isomorphic to $S_3$, while the column part is a cyclic shift.
Two entries invert the row coordinate and two translate it, while the remaining eight are pure column shifts.
Among the pairs $(A_i,B_j)$ that enter the orthogonality condition, only $(A_1,B_2)$ and $(A_0,B_3)$ fail to commute, and both have $i+j\equiv3 \bmod 6$, an offset that the three retained check rows never realize  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)).
The twelve column shifts are left unconstrained by orthogonality and are the free parameters of the code search.

(source: raw/error-correction-zoo.md)

## Protection

Every stabilizer generator has weight twelve, one qubit in each data block.
The reported instances all satisfy $k=n/2+4$, giving rate just above one half  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)).

A weight-preserving bijection between the two logical sectors forces $d_X=d_Z$  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)).
Distances are certified exactly for $⟦252,130,6⟧$, $⟦576,292,8⟧$, $⟦900,454,10⟧$, $⟦1044,526,12⟧$, $⟦1764,886,14⟧$, $⟦2304,1156,16⟧$, and $⟦2844,1426,18⟧$, the last three of which exceed the generator weight  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)).

## General gates

- The global column shift $y\mapsto y+1$ is a code automorphism. For the reported instances, its logical action decomposes into parallel cyclic shifts of eighteen logical registers of length $q$, together with four invariant logical modes  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)).

## Decoders

- Relay belief propagation, with belief propagation and ordered-statistics decoding as a fallback for shots it does not resolve  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)).

## Fault tolerance

- The circuit-level distance, the least number of independent faults of the syndrome-extraction circuit producing an undetectable logical error, is reported only as an upper bound, and that bound falls strictly below $d$ for the $⟦252,130,6⟧$ and $⟦1044,526,12⟧$ instances  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)).

## Threshold

- Circuit-level simulations give pseudo-thresholds above $0.4\%$, defined by the break-even condition that the logical error rate per logical qubit per cycle equal the physical error rate  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)). At physical error rate $10^{-3}$, the $⟦2844,1426,18⟧$ code has an extrapolated logical error rate of $2.6\times10^{-16}$ at an overhead of about three physical qubits per logical qubit.

## Relations

- _parent_: [[concepts/qec/gala]] — Cornucopia codes lie in the direct-product monomial GALA sector with non-Abelian top factor $S_3$ and Abelian bottom factor $C_q$, and were obtained independently  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)). The affine maps of the $\mathbb{Z}_3\times\mathbb{Z}_q$ grid realize $S_3\times C_q$ because the row part of an affine map on $\mathbb{Z}_3$ ranges over the affine group of $\mathbb{Z}_3$, which is isomorphic to $S_3$. The depth-twelve syndrome-extraction schedule is the $J=L/4$ case of the GALA schedule condition, in which the two halves of the lift decouple  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
- _parent_: [[concepts/qec/kasai]] — Since $\gcd(q,3)=1$, the Chinese remainder theorem relabels the $P=3q$ coordinates of each block, identifying $\mathbb{Z}_3\times\mathbb{Z}_q$ with the ring $\mathbb{Z}_{3q}$  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)). Affine maps are preserved under this identification, so each lift entry $(x,y)\mapsto(ax+b,y+s)$ becomes a single affine permutation of $3q$ letters, whose multiplier reduces to $a$ modulo $3$ and to one modulo $q$  ([arXiv:2608.02773](https://arxiv.org/abs/2608.02773)).
- _cousin_: [[concepts/qec/kasai-1152]] — The $⟦1152,580,\leq 12⟧$ code is permutation equivalent to a $\mathrm{GALA}_{12,3}(S_3\times\mathbb{Z}_{32})$ code  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)), drawn from the same direct-product GALA sector as the Cornucopia family. It need not lie in the family itself since its lift takes mutually inverse row translations where the Cornucopia construction repeats a single one  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209), [arXiv:2608.02773](https://arxiv.org/abs/2608.02773)). Its $⟦2304,1156⟧$ sibling has non-cyclic Abelian factor $\mathbb{Z}_2\times\mathbb{Z}_{32}$ and also lies outside the family  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
