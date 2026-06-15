---
type: concept
name: Quantum polar code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/branching-mera
- concepts/qec/quantum-lego
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_polar
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_polar
---

# Quantum polar code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_polar) (`code_id: quantum_polar`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Entanglement-assisted CSS code utilized in a quantum polar coding scheme producing entangled pairs of qubits between sender and receiver. In such a scheme, the amplitude and phase information of a quantum state is handled in complementary fashion  ([arXiv:0803.3096](https://arxiv.org/abs/0803.3096)) using an encoding based on classical polar codes. Variants of the initial scheme have been developed for degradable channels  ([arXiv:1201.2906](https://arxiv.org/abs/1201.2906)) and extended to arbitrary channels  ([arXiv:1109.5346](https://arxiv.org/abs/1109.5346)).

The scheme requires some a priori quantum side information in the general case, making the associated code entanglement-assisted  ([arXiv:1109.3195](https://arxiv.org/abs/1109.3195)). 
They require assistance only to determine positions to store information which optimally protect against both bit and phase noise. Without this assistance, they are just CSS codes constructed out of polar codes.
The requirement of having quantum side information vanishes when the sum of the amplitude channel fidelity and the phase channel fidelity is not greater than 1. 
It is shown to vanish for the case of degradable noise channels  ([arXiv:1109.5346](https://arxiv.org/abs/1109.5346)). 
A more complicated quantum polar-coding scheme that does not require pre-shared entanglement has also been derived  ([arXiv:1307.1136](https://arxiv.org/abs/1307.1136)).

(source: raw/error-correction-zoo.md)

## Protection

Protects against Pauli noise and erasures.

## Rate

The rate approaches the symmetric coherent information of arbitrary quantum channels  ([arXiv:1201.2906](https://arxiv.org/abs/1201.2906)).

## Encoders

- Encoding circuits can be viewed as branching-tree tensor networks  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Decoders

- Arikan-style successive-cancellation decoding can be recast as a tensor-network contraction  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).
- Quantum successive-cancellation list decoder (SCL-E) for quantum polar codes that do not need entanglement assistance  ([arXiv:2304.04743](https://arxiv.org/abs/2304.04743)).
- Numerics for tensor-network-based decoders on depolarizing and erasure channels indicate that good performance is possible without entanglement assistance, with channel polarization rapidly suppressing channels that are bad in both quadratures  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Fault tolerance

- State preparation of a single logical qubit  ([arXiv:2209.06673](https://arxiv.org/abs/2209.06673)).

## Relations

- _parent_: [[concepts/qec/branching-mera]] — Branching MERA codes generalize quantum polar codes by restoring the branching-MERA disentanglers while retaining efficient tensor-network decoding  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).
- _cousin_: [[concepts/qec/qubit-css]] — Quantum polar codes are CSS codes used in an entanglement generation scheme that generally requires entanglement assistance. They require assistance only to determine positions to store information which optimally protect against both bit and phase noise. Without this assistance, they are just CSS codes constructed out of polar codes. A variant of quantum polar codes exists that does not require entanglement assistance  ([arXiv:1307.1136](https://arxiv.org/abs/1307.1136)).
- _cousin_: [`polar`](https://errorcorrectionzoo.org/c/polar) — Without entanglement assistance, quantum polar codes are CSS codes constructed out of polar codes.
- _cousin_: [[concepts/qec/quantum-lego]] — Quantum polar encoding circuits can be viewed as branching-tree tensor networks  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).
