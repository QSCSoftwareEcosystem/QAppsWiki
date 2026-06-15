---
type: concept
name: Subsystem qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Gauge qubit code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/oa-qubits-into-qubits
- concepts/qec/qubits-into-qubits
- concepts/qec/subsystem-galois-into-galois
- concepts/qec/subsystem-qudits-into-qudits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_qubits_into_qubits
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_qubits_into_qubits
---

# Subsystem qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_qubits_into_qubits) (`code_id: subsystem_qubits_into_qubits`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Subsystem QECC encoding into a $2^n$-dimensional (i.e., $n$-qubit) Hilbert space.

(source: raw/error-correction-zoo.md)

## Transversal gates

- If a subsystem qubit code $Q$ of length $n$ has compact subgroups $N\triangleleft G\leq \mathrm{Aut}(Q)$ such that $G/N$ is finite, non-Abelian, simple, and not $A_5$, then $n$ is at least the minimal permutation degree $\mu(G/N)$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).

## Relations

- _parent_: [[concepts/qec/oa-qubits-into-qubits]] — An OA qubit code which has gauge structure (e.g., gauge qubits) but no block structure is a subsystem qubit code.
- _parent_: [[concepts/qec/subsystem-qudits-into-qudits]] — Subsystem modular-qudit codes reduce to subsystem qubit codes for qudit dimension $q=2$.
- _parent_: [[concepts/qec/subsystem-galois-into-galois]] — Subsystem Galois-qudit quantum codes for $q=2$ correspond to subsystem qubit codes.
- _cousin_: [[concepts/qec/qubits-into-qubits]] — Subsystem qubit codes reduce to (subspace) qubit codes when there is no gauge subsystem.
