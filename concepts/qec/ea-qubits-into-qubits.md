---
type: concept
name: EA qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ea-galois-into-galois
- concepts/qec/eaoa-qubits-into-qubits
- concepts/qec/qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_qubits_into_qubits
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_qubits_into_qubits
---

# EA qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_qubits_into_qubits) (`code_id: ea_qubits_into_qubits`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit code designed to utilize pre-shared entanglement between sender and receiver.

(source: raw/error-correction-zoo.md)

## Protection

The quantum GV bound and Plotkin bound have been extended to EA qubit codes  ([arXiv:1010.5506](https://arxiv.org/abs/1010.5506)).

## Rate

There are EA versions of classical and quantum capacities  ([arXiv:quant-ph/9904023](https://arxiv.org/abs/quant-ph/9904023)), and the ratio of the entanglement-assisted and unassisted classical capacities of a channel is bounded by a function of the input channel's dimension  ([arXiv:2408.17290](https://arxiv.org/abs/2408.17290)). EA hashing bounds on the minimum entanglement required to achieve the entanglement-assisted channel capacity are derived  ([arXiv:quant-ph/0205117](https://arxiv.org/abs/quant-ph/0205117)).

## Encoders

- Encoding algorithm  ([arXiv:0806.4214](https://arxiv.org/abs/0806.4214)).

## Decoders

- Decoding algorithm  ([arXiv:0806.4214](https://arxiv.org/abs/0806.4214)).

## Relations

- _parent_: [[concepts/qec/eaoa-qubits-into-qubits]] — An EAOA qubit code with no gauge or block structure is an EA qubit code.
- _parent_: [[concepts/qec/ea-galois-into-galois]] — EA Galois-qudit codes reduce to EA qubit codes for $q=2$.
- _cousin_: [[concepts/qec/qubits-into-qubits]] — EA qubit codes utilize additional ancillary qubits in a pre-shared entangled state, but reduce to ordinary qubit codes when said qubits are interpreted as noiseless physical qubits.
