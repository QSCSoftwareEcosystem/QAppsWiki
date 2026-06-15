---
type: concept
name: Spin cat code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/single-spin
- concepts/qec/spins-into-spins
- concepts/qec/two-legged-cat
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/spin_cat
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: spin_cat
---

# Spin cat code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/spin_cat) (`code_id: spin_cat`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An analogue of the two-component cat code for a large spin, which is often realized in the PI subspace of atomic ensembles.

The encoding was designed by using the Holstein-Primakoff mapping  ([doi:10.1103/PhysRev.58.1098](https://doi.org/10.1103/PhysRev.58.1098), [doi:10.2307/3212170](https://doi.org/10.2307/3212170), [doi:10.1103/RevModPhys.63.375](https://doi.org/10.1103/RevModPhys.63.375)) to pull back the phase-space structure of a bosonic system to the compact phase space of a quantum spin.

The codewords can be approximated by two spin-coherent states.
The version where the two spin-coherent states are antipodal has been considered in Ref.  ([arXiv:2401.04271](https://arxiv.org/abs/2401.04271)).

An extended version of the spin cat code, the dark spin-cat code, encodes in two spins, both thought of as hyperfine manifolds  ([arXiv:2408.04421](https://arxiv.org/abs/2408.04421)).

(source: raw/error-correction-zoo.md)

## General gates

- CNOT gate preserving the rank of spherical-tensor noise operators  ([arXiv:2401.04271](https://arxiv.org/abs/2401.04271)).

## Decoders

- Measurement-free error correction protocol  ([arXiv:2401.04271](https://arxiv.org/abs/2401.04271)).

## Realizations

- Trapped ions: autonomous error-correction scheme reduces errors by a factor up to 2.2, as demonstrated by the Chiaverini group  ([arXiv:2503.13908](https://arxiv.org/abs/2503.13908)).
- Silicon spin qubits: cat-state initialization  ([arXiv:2405.15494](https://arxiv.org/abs/2405.15494)).
- Synthetic spin system inside a microwave cavity: universal control using linear and nonlinear pulses  ([arXiv:2405.15695](https://arxiv.org/abs/2405.15695)).
- Neutral atoms: cat-state initialization, universal single-qubit gates, and benchmarking of gate fidelity, coherence, and biased-noise properties  ([arXiv:2602.22883](https://arxiv.org/abs/2602.22883)).

## Relations

- _parent_: [[concepts/qec/single-spin]]
- _cousin_: [[concepts/qec/two-legged-cat]] — The spin-cat code construction utilizes the Holstein-Primakoff mapping  ([doi:10.1103/PhysRev.58.1098](https://doi.org/10.1103/PhysRev.58.1098), [doi:10.2307/3212170](https://doi.org/10.2307/3212170), [doi:10.1103/RevModPhys.63.375](https://doi.org/10.1103/RevModPhys.63.375)) to convert cat codes into codes for spin systems.
- _cousin_: [[concepts/qec/spins-into-spins]] — An extended version of the spin cat code, the dark spin-cat code, encodes in two spins, both thought of as hyperfine manifolds  ([arXiv:2408.04421](https://arxiv.org/abs/2408.04421)).
