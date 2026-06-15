---
type: concept
name: Hybrid qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hybridqecc
- concepts/qec/oa-qubits-into-qubits
- concepts/qec/qubit-classical-into-quantum
- concepts/qec/qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hybrid_qubits_into_qubits
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hybrid_qubits_into_qubits
---

# Hybrid qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hybrid_qubits_into_qubits) (`code_id: hybrid_qubits_into_qubits`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit code which stores both quantum and classical information.
Usually denoted as $((n,K:M))$ or $((n,K:M,d))$, where $K$ is the dimension of the underlying quantum code, $M$ is the size of the classical code, and $d$ is the distance.

(source: raw/error-correction-zoo.md)

## Protection

Any qubit code can be converted into a hybrid qubit code by using some of its logical qubits to store only classical information  ([arXiv:0802.2414](https://arxiv.org/abs/0802.2414)).
An $((n,K:M))$ hybrid qubit code can detect more errors than an $((n,KM))$ qubit code  ([arXiv:1901.02913](https://arxiv.org/abs/1901.02913)).
A hybrid Hamming bound has been constructed  ([arXiv:1806.03702](https://arxiv.org/abs/1806.03702)).

Quantum weight enumerators, quantum MacWilliams identities, and linear programming bounds have been extended to hybrid qubit codes  ([arXiv:1701.06963](https://arxiv.org/abs/1701.06963), [arXiv:1901.02913](https://arxiv.org/abs/1901.02913), [arXiv:1911.12260](https://arxiv.org/abs/1911.12260)).

## Relations

- _parent_: [[concepts/qec/oa-qubits-into-qubits]] — An OA qubit code that has no gauge structure (e.g., gauge qubits) but has a block structure that corresponds to a classical code is a hybrid qubit code.
- _parent_: [[concepts/qec/hybridqecc]]
- _cousin_: [[concepts/qec/qubits-into-qubits]] — A hybrid qubit code storing no classical information reduces to a qubit code. Conversely, any qubit code can be converted into a hybrid qubit code by using some of its logical qubits to store only classical information  ([arXiv:0802.2414](https://arxiv.org/abs/0802.2414)).
- _cousin_: [[concepts/qec/qubit-classical-into-quantum]] — A hybrid qubit code storing no quantum information reduces to a qubit c-q code.
