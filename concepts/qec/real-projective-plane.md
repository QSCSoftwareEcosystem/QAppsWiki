---
type: concept
name: Projective-plane surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/honeycomb-floquet
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/real_projective_plane
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: real_projective_plane
---

# Projective-plane surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/real_projective_plane) (`code_id: real_projective_plane`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of Kitaev surface codes on the non-orientable 2-dimensional compact manifold $\mathbb{R}P^2$ (in contrast to a genus-$g$ surface).
Whereas genus-$g$ surface codes require $2g$ logical qubits, qubit codes on $\mathbb{R}P^2$ are made from a single logical qubit.

(source: raw/error-correction-zoo.md)

## Protection

If $\mathcal{C}$ is a cellulation of $\mathbb{R}P^2$, then the bit-flip distance $d_X$ is the shortest cycle in $\mathcal{C}$, and the phase-flip distance $d_Z$ is the shortest cycle in the dual cellulation $\mathcal{C}^*$.

## Rate

The rate is $1/n$, where $n$ is the number of edges of the particular cellulation.

## General gates

- Fault-tolerant Hadamard gate via constant-depth Clifford circuit  ([arXiv:2310.06917](https://arxiv.org/abs/2310.06917)).
- Complete logical gate set for a stack of projective-plane surface codes  ([arXiv:2310.06917](https://arxiv.org/abs/2310.06917)).

## Fault tolerance

- Fault-tolerant Hadamard gate via constant-depth Clifford circuit  ([arXiv:2310.06917](https://arxiv.org/abs/2310.06917)).

## Relations

- _parent_: [[concepts/qec/surface]] — The projective-plane surface code is the surface code on $\mathbb{R}P^2$.
- _cousin_: [[concepts/qec/honeycomb-floquet]] — Implementing the honeycomb Floquet code on a non-orientable cross-cap geometry allows for a logical-$HZ$ gate to be implemented via a measurement schedule  ([arXiv:2310.06917](https://arxiv.org/abs/2310.06917)).
