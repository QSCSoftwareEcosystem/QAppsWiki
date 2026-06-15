---
type: concept
name: EAOA qubit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/eaoa-qubits-into-qubits
- concepts/qec/hybrid-stabilizer
- concepts/qec/qubit-stabilizer-oaqecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/eaoa_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: eaoa_stabilizer
---

# EAOA qubit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/eaoa_stabilizer) (`code_id: eaoa_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Entanglement-assisted qubit stabilizer code in the operator-algebra framework. In the generalized stabilizer formalism of  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)), such a code is specified on an extended qubit space by Pauli data consisting of stabilizer, gauge, logical, and sector-labeling operators, and is viewed on the original system as using noiseless ebits shared with a receiver.

EAOA qubit stabilize codes are denoted by $⟦n,k; r,e,c_b⟧$ or $⟦n,k,d; r,e,c_b⟧$, where $n$ is the number of transmitted physical qubits, $k$ is the number of logical qubits, $r$ is the number of gauge qubits, $e$ is the number of ebits, and $c_b$ is the number of classical strings encoded. When the hybrid component encodes $c$ classical bits, one has $c_b=2^c$.
This family encompasses ordinary entanglement-assisted qubit stabilizer codes, entanglement-assisted subsystem stabilizer codes, entanglement-assisted hybrid stabilizer codes, and operator-algebra generalizations described within that stabilizer formalism.
The framework also exhibits EA hybrid subspace and EA subsystem stabilizer codes that lie outside the earlier EACQ and EAOQECC formalisms  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).

There exist four constructions of EAOA qubit stabilizer codes with distance lower bounds:
gauge fixing $⟦n,k,d;r,e,c_b⟧ \to ⟦n,k,d';r-y,e,\leq 2^y c_b⟧$,
clean qubits $⟦n,k,d;r,0,c_b⟧ \to ⟦n-e,k,d';r,e,c_b⟧$,
entanglement-assisted gauge fixing $⟦n,k,d;r,0,c_b⟧ \to ⟦n,k,d';r-e,e,c_b⟧$, and
general gauge fixing $⟦n,k,d;r,e,c_b⟧ \to ⟦n,k,d';r-y_I-y_S,e+y_S,\leq 2^{y_I}c_b⟧$
 ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).

(source: raw/error-correction-zoo.md)

## Protection

For stabilizer-described qubit subclasses, the EAOAQEC framework yields explicit Pauli error-correction conditions for errors acting on the sender's qubits under the usual assumption that the receiver's halves of the ebits are noiseless  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).
Its dressed distance is the minimum weight over logical-centralizer operators outside the isotropic-plus-gauge subgroup together with inter-sector cosets, reducing to the usual distance notions for EAQEC, EAOQECC, EACQ, OAQEC, and related stabilizer code families in the appropriate limits  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).

## Relations

- _parent_: [[concepts/qec/eaoa-qubits-into-qubits]] — EAOA qubit stabilizer codes are EAOA qubit codes described within a generalized stabilizer formalism.
- _cousin_: [[concepts/qec/qubit-stabilizer-oaqecc]] — EAOA qubit stabilizer codes utilize additional ancillary subsystems in a pre-shared entangled state, but reduce to OA qubit stabilizer codes when said subsystems are interpreted as noiseless physical subsystems.
- _cousin_: [[concepts/qec/hybrid-stabilizer]] — EA hybrid qubit stabilizer codes utilize additional ancillary subsystems in a pre-shared entangled state, but reduce to hybrid qubit stabilizer codes when said subsystems are interpreted as noiseless physical subsystems. In the original EA hybrid stabilizer formalism, an $⟦n,q:c,d;e⟧$ EA hybrid stabilizer code is specified by a pair $(\mathcal{S}_Q,\mathcal{S}_C)$ of quantum and classical stabilizer groups, and in the equivalent symplectic formalism by a quantum parity-check matrix together with a classical parity-check matrix  ([arXiv:0802.2414](https://arxiv.org/abs/0802.2414)). Inside the EAOAQEC stabilizer framework, hybrid stabilizer codes are a proper subclass of the broader EA hybrid subspace codes because the EACQ transversal operators obey additional constraints not required in general  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).
- _cousin_: [`eacq`](https://errorcorrectionzoo.org/c/eacq) — The original EACQ formalism describes a proper subclass of EA hybrid subspace codes inside the EAOAQEC stabilizer framework; EACQ representability imposes extra constraints on the transversal operators beyond belonging to distinct normalizer cosets  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).
