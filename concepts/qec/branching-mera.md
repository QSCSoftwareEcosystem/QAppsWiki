---
type: concept
name: Branching MERA code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/eastab
- concepts/qec/quantum-lego
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/branching_mera
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: branching_mera
---

# Branching MERA code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/branching_mera) (`code_id: branching_mera`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit stabilizer code whose encoding circuit corresponds to a branching MERA  ([arXiv:1210.1895](https://arxiv.org/abs/1210.1895)) tensor network.
These codes generalize quantum polar codes by reinstating the disentanglers omitted in the branching-tree tensor-network construction  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

(source: raw/error-correction-zoo.md)

## Protection

Numerical evidence indicates that channel polarization rapidly suppresses channels that are bad in both quadratures, allowing good performance without entanglement assistance  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Rate

Numerics on depolarizing and erasure channels indicate low block-error rates at rates approaching coherent information, with better finite-size behavior than quantum polar codes  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Encoders

- Encoding uses a reversed branching-MERA CNOT circuit, with non-data inputs frozen to either $|0\rangle$ or $|+\rangle$ according to channel selection  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Decoders

- Decoding can be formulated as tensor-network contraction and supports successive-cancellation-style decoding inherited from branching-MERA constructions  ([arXiv:1312.4575](https://arxiv.org/abs/1312.4575), [arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).
- A symmetric decoder that jointly uses $x$- and $z$-error information remains efficiently contractible and improves finite-size performance over standard quantum polar decoding  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Relations

- _parent_: [[concepts/qec/eastab]]
- _cousin_: [`polar`](https://errorcorrectionzoo.org/c/polar) — Classical versions of branching MERA codes can be thought of as extensions of polar codes  ([arXiv:1312.4575](https://arxiv.org/abs/1312.4575), [doi:10.1109/ISIT.2014.6874999](https://doi.org/10.1109/ISIT.2014.6874999)).
- _cousin_: [[concepts/qec/quantum-lego]] — Encoders for branching MERA codes are related to branching MERA tensor networks  ([arXiv:1312.4575](https://arxiv.org/abs/1312.4575), [arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).
