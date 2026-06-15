---
type: concept
name: Non-Abelian Kitaev honeycomb code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-bosonization
- concepts/qec/kitaev-honeycomb
- concepts/qec/qubits-into-qubits
- concepts/qec/tetron
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/nonabelian_kitaev_honeycomb
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: nonabelian_kitaev_honeycomb
---

# Non-Abelian Kitaev honeycomb code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/nonabelian_kitaev_honeycomb) (`code_id: nonabelian_kitaev_honeycomb`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose logical subspace in the gapped non-Abelian phase of the Kitaev honeycomb model with a magnetic field is labeled by different fusion outcomes of Ising anyons  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)).

The original Kitaev honeycomb spin model is exactly solvable by mapping spins to Majorana fermions in a static $\mathbb{Z}_2$ gauge field (equivalently, embedding each physical qubit into two fermions via the tetron code  ([arXiv:1701.05052](https://arxiv.org/abs/1701.05052))), yielding three gapped $A$ phases and one gapless $B$ phase  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)).
A magnetic field opens a gap in phase $B$ of the underlying Kitaev honeycomb code and yields the non-Abelian Ising-anyon phase  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) (a.k.a. $p+ip$ superconducting phase  ([arXiv:1104.5485](https://arxiv.org/abs/1104.5485))).
In the honeycomb model with magnetic field, the spectral Chern number is $\nu=\pm 1$ depending on the field direction; more generally, gapped free-fermion phases with $\mathbb{Z}_2$ vortices are classified by a spectral Chern number $\nu$, and their anyonic properties depend on $\nu \bmod 16$  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)).

Ising anyons also exist in other phases, such as the fractional quantum Hall phase  ([arXiv:quant-ph/0511178](https://arxiv.org/abs/quant-ph/0511178)).

(source: raw/error-correction-zoo.md)

## Encoders

- Anyon initialization via quantum control  ([arXiv:2205.10114](https://arxiv.org/abs/2205.10114)).

## General gates

- Clifford gates can be performed by braiding Majorana operators and Pauli measurements can be performed by measuring certain Majorana operators  ([arXiv:quant-ph/0511178](https://arxiv.org/abs/quant-ph/0511178), [arXiv:1701.05052](https://arxiv.org/abs/1701.05052)).
- CPHASE gate or a $\pi/8$ rotation with the help of ancilla states completes a universal gate set  ([arXiv:quant-ph/0511178](https://arxiv.org/abs/quant-ph/0511178), [arXiv:1701.05052](https://arxiv.org/abs/1701.05052)).

## Fault tolerance

- One can distill ancilla states to arbitrary precision for sufficiently small noise rates and assuming perfect Clifford operations  ([arXiv:quant-ph/0511178](https://arxiv.org/abs/quant-ph/0511178)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]] — The Kitaev honeycomb model with a magnetic field is a qubit many-body system in the Ising-anyon phase, and the underlying code stores information in the fusion space of its non-Abelian anyonic excitations.
- _parent_: [[concepts/qec/topological]] — The Kitaev honeycomb model with a magnetic field is a qubit many-body system in the Ising-anyon phase, and the underlying code stores information in the fusion space of its non-Abelian anyonic excitations.
- _cousin_: [[concepts/qec/kitaev-honeycomb]] — The gauge-group generators of the Kitaev honeycomb code are terms of the Kitaev honeycomb model Hamiltonian. Adding a magnetic field to this Hamiltonian for particular parameter values yields the non-Abelian Ising-anyon phase, whose anyons encode the logical information of the non-Abelian Kitaev honeycomb code  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)).
- _cousin_: [[concepts/qec/tetron]] — Embedding each physical qubit into two fermions via the tetron code allows the logical subspace of the Kitaev honeycomb model to be formulated as a joint eigenspace of certain Majorana operators  ([arXiv:1701.05052](https://arxiv.org/abs/1701.05052)), which admit braiding-based gates due to their non-Abelian statistics and which can be used for topological quantum computation.
When done in reverse, this embedding can be thought of as a 2D bosonization fermion-into-qubit encoding by converting to a relabeled square lattice and performing single-qubit rotations  ([arXiv:1711.00515](https://arxiv.org/abs/1711.00515)) ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).
- _cousin_: [[concepts/qec/2d-bosonization]] — Embedding each physical qubit into two fermions via the tetron code allows the logical subspace of the Kitaev honeycomb model to be formulated as a joint eigenspace of certain Majorana operators  ([arXiv:1701.05052](https://arxiv.org/abs/1701.05052)), which admit braiding-based gates due to their non-Abelian statistics and which can be used for topological quantum computation.
When done in reverse, this embedding can be thought of as a 2D bosonization fermion-into-qubit encoding by converting to a relabeled square lattice and performing single-qubit rotations  ([arXiv:1711.00515](https://arxiv.org/abs/1711.00515)) ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).
- _cousin_: [`honeycomb`](https://errorcorrectionzoo.org/c/honeycomb) — The Kitaev honeycomb model is defined on the honeycomb tiling.
