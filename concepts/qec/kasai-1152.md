---
type: concept
name: $⟦1152,580,\leq 12⟧$ co-designed Kasai code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/gala
- concepts/qec/kasai
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/kasai_1152
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: kasai_1152
---

# $⟦1152,580,\leq 12⟧$ co-designed Kasai code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/kasai_1152) (`code_id: kasai_1152`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Kasai code with $J=3$, $L=12$, and lift size $P=96$ whose affine permutations are chosen so that every transition permutation of syndrome extraction commutes with a fixed reference affine permutation having three orbits of length $32$  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)).
In the qubit ordering along those orbits, each transition is a cyclic shift within the orbits plus a permutation between them, which yields a three-by-thirty-two layout with a syndrome-extraction schedule of constant qubit-movement cost  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)).

The code has $n=LP=1152$ qubits and girth at least six, and non-commutativity is imposed on the index pairs $(0,3)$ and $(1,2)$  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)).
The twelve affine permutations $f_i(x)=a_ix+b_i$ and $g_i(x)=c_ix+d_i$ defining the $G$-lift are tabulated in Ref.  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)).

The code is permutation equivalent to the GALA code $\mathrm{GALA}_{12,3}(S_3\times\mathbb{Z}_{32})$, and its $⟦2304,1156⟧$ sibling to $\mathrm{GALA}_{12,3}(S_3\times\mathbb{Z}_2\times\mathbb{Z}_{32})$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
The non-Abelian factor $S_3$ and Abelian factor $\mathbb{Z}_{32}$ of that presentation reproduce the reference-permutation orbit structure and recover the same movement schedule from the group data  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).

(source: raw/error-correction-zoo.md)

## Protection

The encoding rate is $0.503$, and the distance is reported only as the upper bound $d \leq 12$  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)).

## Decoders

- Hierarchical decoder combining the throughput of belief propagation with an exact integer-programming fallback  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)).

## Fault tolerance

- Syndrome extraction requires at most one horizontal shift together with one vertical shift or swap per step, on a three-by-thirty-two qubit layout  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)).
- Under a circuit-level noise model at physical error rate $10^{-3}$ without idling noise, the average per-logical-qubit-per-round error rate is directly observed to be $2.9^{+3.1}_{-1.5}\times10^{-11}$  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)). The $⟦2304,1156,\leq 14⟧$ instance reaches $1.3^{+3.0}_{-0.9}\times10^{-13}$  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)).

## Relations

- _parent_: [[concepts/qec/kasai]] — This Kasai code satisfies the reference-affine-permutation commutation condition, which relaxes the girth from eight to six in exchange for qubit-permutation schedules of constant cost  ([arXiv:2604.16209](https://arxiv.org/abs/2604.16209)).
- _parent_: [[concepts/qec/gala]] — The code is permutation equivalent to $\mathrm{GALA}_{12,3}(S_3\times\mathbb{Z}_{32})$  ([arXiv:2608.07431](https://arxiv.org/abs/2608.07431)).
