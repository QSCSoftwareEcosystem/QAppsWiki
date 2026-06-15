---
type: concept
name: Log-depth geometrically local Clifford-circuit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/1d-stabilizer
- concepts/qec/qubit-stabilizer
- concepts/qec/random-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/approximate_log_depth
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: approximate_log_depth
---

# Log-depth geometrically local Clifford-circuit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/approximate_log_depth) (`code_id: approximate_log_depth`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A random $⟦n,k⟧$ stabilizer code whose encoder is a random Clifford circuit of depth of order $O(\log n)$ on a 1D Euclidean geometry.

(source: raw/error-correction-zoo.md)

## Rate

Log-depth Clifford circuits on a 1D geometry yield approximate codes whose encoding rate achieves the hashing bound for Pauli noise and the channel capacity for erasure errors  ([arXiv:2503.17759](https://arxiv.org/abs/2503.17759), [arXiv:2602.20900](https://arxiv.org/abs/2602.20900)).

## Encoders

- Random $\log$-depth Clifford circuit on a 1D Euclidean geometry.

## Decoders

- Minimum-weight decoding using tropical tensor networks  ([arXiv:2311.17985](https://arxiv.org/abs/2311.17985)).

## Fault tolerance

- Fault-tolerant state preparation  ([arXiv:2311.17985](https://arxiv.org/abs/2311.17985)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]]
- _parent_: [[concepts/qec/random-stabilizer]] — Log-depth Clifford circuits on a 1D geometry yield approximate codes whose encoding rate achieves the hashing bound for Pauli noise and the channel capacity for erasure errors  ([arXiv:2503.17759](https://arxiv.org/abs/2503.17759), [arXiv:2602.20900](https://arxiv.org/abs/2602.20900)).
- _cousin_: [[concepts/qec/1d-stabilizer]] — Log-depth Clifford circuits on a 1D geometry yield approximate codes whose encoding rate achieves the hashing bound for Pauli noise and the channel capacity for erasure errors  ([arXiv:2503.17759](https://arxiv.org/abs/2503.17759), [arXiv:2602.20900](https://arxiv.org/abs/2602.20900)).
