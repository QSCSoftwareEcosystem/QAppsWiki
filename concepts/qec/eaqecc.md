---
type: concept
name: Entanglement-assisted (EA) QECC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Catalytic QECC
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/eaoecc
- concepts/qec/qecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/eaqecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: eaqecc
---

# Entanglement-assisted (EA) QECC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/eaqecc) (`code_id: eaqecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

QECC whose encoding and decoding utilize pre-shared entanglement between sender and receiver.

(source: raw/error-correction-zoo.md)

## Protection

Pre-shared entanglement can be prepared in a way that is robust to noise  ([arXiv:0904.1175](https://arxiv.org/abs/0904.1175)).

## Rate

The EA quantum capacity is the highest rate of quantum information transmission through a quantum channel with arbitrarily small error rate and access to arbitrary amounts of entanglement  ([arXiv:quant-ph/0106052](https://arxiv.org/abs/quant-ph/0106052)).
The fault-tolerant EA capacity is the capacity for the more general case where the encoding and decoding maps are also assumed to undergo noise  ([arXiv:2210.02939](https://arxiv.org/abs/2210.02939)).

## Relations

- _parent_: [`eaoaecc`](https://errorcorrectionzoo.org/c/eaoaecc) — An EAOA QECC that has no gauge structure (e.g., gauge qubits), that has no block structure that corresponds to a classical code, and that utilizes pre-shared entanglement is an EA QECC.
- _cousin_: [[concepts/qec/qecc]] — EA QECCs utilize additional ancillary subsystems in a pre-shared entangled state, but reduce to QECCs when said subsystems are interpreted as noiseless physical subsystems.
- _cousin_: [`eacq`](https://errorcorrectionzoo.org/c/eacq) — An EA hybrid QECC storing no classical information reduces to an EA QECC. Conversely, any EA QECC can be converted into an EA hybrid QECC by using a portion of its logical subspace to store only classical information.
- _cousin_: [[concepts/qec/eaoecc]] — An EAOQECC reduces to an EA QECC when the gauge subsystem is trivial. Conversely, any EA QECC with a tensor-product logical subspace can be turned into an EAOQECC by treating a logical tensor factor as a gauge subsystem.

## Notes

- See Ref.  ([arXiv:1610.04013](https://arxiv.org/abs/1610.04013), [doi:10.1017/CBO9781139034807.009](https://doi.org/10.1017/CBO9781139034807.009)) for an introduction to EAQECCs.
