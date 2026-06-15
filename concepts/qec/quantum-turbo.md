---
type: concept
name: Quantum turbo code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-convolutional
- concepts/qec/qubit-concatenated
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_turbo
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_turbo
---

# Quantum turbo code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_turbo) (`code_id: quantum_turbo`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A quantum version of the turbo code, obtained from an interleaved serial quantum concatenation  ([arXiv:0712.2888](https://arxiv.org/abs/0712.2888)) of quantum convolutional codes.
The interleaver induces long-range entanglement and can increase the minimum distance relative to the constituent convolutional codes  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

(source: raw/error-correction-zoo.md)

## Encoders

- Encoders of codes with polynomial distance yield catastrophic errors, but codes with bounded distance admit non-catastrophic encoders.

## Decoders

- Turbo decoder  ([arXiv:0712.2888](https://arxiv.org/abs/0712.2888)).
- Modified decoder yields improvement over the memoryless depolarizing channel  ([arXiv:1010.1256](https://arxiv.org/abs/1010.1256)).
- Iterative decoding is analogous to a mean-field treatment of two matrix-product-state chains coupled by random non-local interactions  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).
- EXIT charts  ([arXiv:1502.00910](https://arxiv.org/abs/1502.00910)).

## Relations

- _parent_: [[concepts/qec/quantum-convolutional]]
- _parent_: [[concepts/qec/qubit-concatenated]]
- _cousin_: [`turbo`](https://errorcorrectionzoo.org/c/turbo) — Quantum turbo codes are quantum analogues of turbo codes.
