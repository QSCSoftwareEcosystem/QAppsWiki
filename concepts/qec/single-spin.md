---
type: concept
name: Single-spin code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-permutation-invariant
- concepts/qec/single-subsystem
- concepts/qec/spins-into-spins
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/single_spin
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: single_spin
---

# Single-spin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/single_spin) (`code_id: single_spin`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An encoding into a monolithic (i.e. non-tensor-product) Hilbert space that houses an irreducible representation of $SU(2)$ or, more generally, another Lie group.
In some cases, this space can be thought of as the permutation invariant subspace of a particular tensor-product space.

The analogue of oscillator coherent states for single spins are the spin coherent states  ([doi:10.1088/0305-4470/4/3/009](https://doi.org/10.1088/0305-4470/4/3/009)).

(source: raw/error-correction-zoo.md)

## Protection

For the $SU(2)$ case, a continuous-time single-spin noise channel akin to the depolarizing channel is the Landau-Streater channel  ([doi:10.1016/0024-3795(93)90274-R](https://doi.org/10.1016/0024-3795(93)90274-R)).
A particular error basis of interest consists of the spherical tensors  ([arXiv:2304.08611](https://arxiv.org/abs/2304.08611)).

The $SU(2)$ Lie Algebra can also be used as a noise model; it connects states whose angular momentum projections differ by at most an integer  ([arXiv:2005.10910](https://arxiv.org/abs/2005.10910)).
More generally, the group's Lie algebra induces a metric on the carrying vector space, and its operators can be chosen as a noise basis  ([arXiv:1205.4517](https://arxiv.org/abs/1205.4517)). Code existence is guaranteed by the Tverberg theorem  ([arXiv:1205.4517](https://arxiv.org/abs/1205.4517)).
There are quantum MacWilliams identities for such metric spaces  ([arXiv:1205.4517](https://arxiv.org/abs/1205.4517)).

## Rate

For every $K,t \geq 2$, there are explicitly constructible $K$-dimensional single-spin codes for $SU(q=N)$ with total spin $N=(K-1)t(t+1)$ and distance $t+1$; there also exist families with logical dimension $K = o(2^N)$ and distance of order $o(N/\log N)$  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).

For the spin-$n/2$ irrep of $\mathfrak{su}(2)$, the Tverberg theorem construction  ([arXiv:quant-ph/9908066](https://arxiv.org/abs/quant-ph/9908066)) yields a distance-1 error-detecting code of dimension $\lceil (n+1)/4 \rceil$ against the $\mathfrak{su}(2)$ Lie algebra error set $\{E, F, H\}$  ([arXiv:1205.4517](https://arxiv.org/abs/1205.4517))}.

## Relations

- _parent_: [[concepts/qec/spins-into-spins]]
- _parent_: [[concepts/qec/single-subsystem]]
- _cousin_: [[concepts/qec/qubit-permutation-invariant]] — Single-spin codes are subspaces of a single large $SU(2)$ spin, which can be either standalone or correspond to the PI subspace of a set of spins via the Dicke state mapping.
