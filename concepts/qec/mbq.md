---
type: concept
name: Majorana box qubit
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/1d-stabilizer
- concepts/qec/hamiltonian
- concepts/qec/majorana-color
- concepts/qec/majorana-stab
- concepts/qec/majorana-surface
- concepts/qec/qldpc
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/mbq
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: mbq
---

# Majorana box qubit

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/mbq) (`code_id: mbq`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of Majorana stabilizer codes obtained by fixing the total fermion parity of $n$ fermionic modes, equivalently $2n$ Majorana zero modes, within the ground-state subspace of $n$ Kitaev Majorana chain Hamiltonians.
The resulting positive-parity subspace encodes $n-1$ logical qubits and has Majorana distance $2$.

The $⟦2,1,2⟧_{f}$ member is called the tetron Majorana code, while an $⟦3,2,2⟧_{f}$ extension using three Kitaev chains and housing two logical qubits of the same parity is called the *hexon Majorana code*.
Similarly, the $⟦4,3,2⟧_{f}$ *octon*, $⟦5,4,2⟧_{f}$ *decon*, and $⟦6,5,2⟧_{f}$ *dodecon* are codes defined by the positive-parity subspace of $4$, $5$, and $6$ fermionic modes, respectively  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

(source: raw/error-correction-zoo.md)

## Protection

Fixing total fermion parity detects single-Majorana events as parity violations if that parity is measured.
However, these distance-two box-qubit codes do not correct errors: two-Majorana operators act within the fixed-parity sector and can implement logical Pauli errors without changing the stabilizer outcome, while treating the parity constraint as a Hamiltonian term turns single-Majorana events into leakage errors  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

## General gates

- Braiding and fusion of MZMs, which act as Ising anyons  ([arXiv:1006.4395](https://arxiv.org/abs/1006.4395), [arXiv:1511.05153](https://arxiv.org/abs/1511.05153)).

## Decoders

- Qubit readout can be done by charge sensing  ([arXiv:1511.05153](https://arxiv.org/abs/1511.05153), [arXiv:1609.01697](https://arxiv.org/abs/1609.01697), [arXiv:1610.05289](https://arxiv.org/abs/1610.05289), [arXiv:2004.02124](https://arxiv.org/abs/2004.02124)).

## Fault tolerance

- Fault-tolerant computation scheme  ([arXiv:2502.12252](https://arxiv.org/abs/2502.12252)).

## Relations

- _parent_: [[concepts/qec/majorana-stab]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _parent_: [[concepts/qec/topological-abelian]] — When treated as ground states of the code Hamiltonian, codewords of a single Kitaev chain realize $\mathbb{Z}_2$ fermionic topological order.
- _parent_: [[concepts/qec/qldpc]] — The Majorana box qubit is a 1D qubit stabilizer code with respect to the Majorana operator basis.
- _parent_: [[concepts/qec/1d-stabilizer]] — The Majorana box qubit is a 1D qubit stabilizer code with respect to the Majorana operator basis.
- _cousin_: [[concepts/qec/hamiltonian]] — A Majorana box qubit forms a fixed-parity subspace of the ground-state subspace of one or more Kitaev Majorana chain Hamiltonians.
- _cousin_: [[concepts/qec/majorana-surface]] — The 4.8.8, 6.6.6, and 4.6.12 Majorana surface-code families realize logical tetrons and hexons as fault-tolerant versions of these small Majorana blocks, using tetrons, hexons, or dodecons as parity-fixed building blocks  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
- _cousin_: [[concepts/qec/majorana-color]] — Majorana color codes are obtained by stacking Majorana surface-code layers and replacing stacked building blocks by small Majorana fermion codes such as hexons, octons, and a $⟦10,4,4⟧_{f}$ decon-based code  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
