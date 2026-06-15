---
type: concept
name: Polar c-q code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-classical-into-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/polar_for_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: polar_for_quantum
---

# Polar c-q code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/polar_for_quantum) (`code_id: polar_for_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Polar code adapted to transmit classical information over channels with classical inputs and quantum outputs.

(source: raw/error-correction-zoo.md)

## Rate

Codes achieve the symmetric Holevo information for sending classical information over channels with classical inputs and quantum outputs  ([arXiv:1109.2591](https://arxiv.org/abs/1109.2591)).

## Decoders

- Quantum-limited successive-cancellation (SC) joint-detection receiver  ([arXiv:1109.2591](https://arxiv.org/abs/1109.2591)).

## Relations

- _parent_: [[concepts/qec/qubit-classical-into-quantum]]
