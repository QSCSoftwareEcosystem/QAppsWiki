---
type: concept
name: Random stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Random Clifford-circuit code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/random-circuit
- concepts/qec/stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/random_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: random_stabilizer
---

# Random stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/random_stabilizer) (`code_id: random_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $n$-qubit, modular-qudit, or Galois-qudit stabilizer code whose construction is non-deterministic.
Since stabilizer encoders are Clifford circuits, such codes can be thought of as arising from random Clifford circuits.

(source: raw/error-correction-zoo.md)

## Rate

Random qubit stabilizer codes asymptotically saturate the non-degenerate quantum Hamming bound, and hence achieve the  quantum GV bound, because a typical random stabilizer has negligible degeneracy   ([arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)); see notes . In fact, sampling random CSS codes is sufficient   ([arXiv:quant-ph/9512032](https://arxiv.org/abs/quant-ph/9512032)); see also the original random-coding argument  ([arXiv:quant-ph/9605005](https://arxiv.org/abs/quant-ph/9605005)).

## Relations

- _parent_: [[concepts/qec/stabilizer]]
- _cousin_: [[concepts/qec/random-circuit]] — Random stabilizer codes can be constructed by sampling random Clifford circuits.
