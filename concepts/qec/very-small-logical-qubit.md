---
type: concept
name: Very small logical qubit (VSLQ) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/constant-excitation
- concepts/qec/fock-state
- concepts/qec/hybrid-qudit-oscillator
- concepts/qec/permutation-invariant
- concepts/qec/quantum-repetition
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/very-small-logical-qubit
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: very-small-logical-qubit
---

# Very small logical qubit (VSLQ) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/very-small-logical-qubit) (`code_id: very-small-logical-qubit`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code consisting of two logical codewords $|\pm\rangle \propto (|0\rangle\pm|2\rangle)(|0\rangle\pm|2\rangle)$, where the total Hilbert space is the tensor product of two transmon qudits (whose ground states $|0\rangle$ and second excited states $|2\rangle$ are used in the codewords).
Since the code is intended to protect against losses, the qutrits can equivalently be thought of as oscillator Fock-state subspaces.

In the original proposal for autonomous stabilization  ([arXiv:1510.06117](https://arxiv.org/abs/1510.06117)), the single logical qubit is given by the two lowest energy states of a time-dependent Hamiltonian acting on two transmon qutrits and two lossy oscillators.

(source: raw/error-correction-zoo.md)

## Protection

Protects against a single photon loss.

## Encoders

- Engineering a circuit made of two transmons and two oscillators coupled through three driven superconducting quantum interference devices (SQUIDs) results in passive stabilization of the logical states.

## General gates

- Single logical qubit operations implemented by resonant physical qubit driving and phase shifting the SQUID drives.
- A CZ gate between two logical qubits implemented by coupling devices through another driven SQUID and applying a pulse to the coupling squid simultaneously with a single qubit operation on one of the logical qubits.

## Decoders

- Logical qubit can be measured with physical qubit measurements along $X$. Can be implemented by engineering a coupling of one of the qubits to a readout cavity via the interaction $\sigma_x (a+a^\dagger)$  ([doi:10.1103/PhysRevLett.115.203601](https://doi.org/10.1103/PhysRevLett.115.203601)). This results in an $X$-dependent shift of the readout cavity resonance which can be measured.
- Star-code autonomous correction scheme  ([arXiv:2302.06707](https://arxiv.org/abs/2302.06707)).

## Realizations

- Star-code autonomous correction scheme realized using superconducting circuits  ([arXiv:2302.06707](https://arxiv.org/abs/2302.06707)).

## Relations

- _parent_: [[concepts/qec/fock-state]]
- _parent_: [[concepts/qec/constant-excitation]]
- _parent_: [[concepts/qec/permutation-invariant]]
- _cousin_: [[concepts/qec/hybrid-qudit-oscillator]] — VSLQ decoder utilizes two ancillary oscillators.
- _cousin_: [[concepts/qec/quantum-repetition]] — Parts of the VSLQ codewords resemble the two-qubit phase-flip repetition code, though the code cannot correct phase errors. Unlike the phase-flip code, the VSLQ code can correct for single photon loss because it uses the second excited state in the construction, which remains distinct from the vacuum even after photon loss.
