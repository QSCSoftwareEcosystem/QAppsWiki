---
type: concept
name: Generalized five-squares code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/subsystem-hypergraph
- concepts/qec/toric
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/five_squares
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: five_squares
---

# Generalized five-squares code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/five_squares) (`code_id: five_squares`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of subsystem codes that are generalizations  ([arXiv:1207.0479](https://arxiv.org/abs/1207.0479), [arXiv:1805.12542](https://arxiv.org/abs/1805.12542)) of a code defined on a three-valent hypergraph associated with the five-squares lattice  ([arXiv:1012.0425](https://arxiv.org/abs/1012.0425)).
The original five-squares code is a 2D topological subsystem code with local two-qubit gauge generators; on a torus, it encodes two logical qubits  ([arXiv:1012.0425](https://arxiv.org/abs/1012.0425)).

(source: raw/error-correction-zoo.md)

## Decoders

- For the original five-squares code, preprocessing maps decoding onto two copies of the toric code, after which one can use minimum-weight matching or renormalization-group decoding  ([arXiv:1012.0425](https://arxiv.org/abs/1012.0425)).
- Generalized five-squares codes can also be decoded via a mapping to two copies of the surface code  ([arXiv:1805.12542](https://arxiv.org/abs/1805.12542)).

## Code capacity threshold

- For depolarizing noise, the original five-squares code has a threshold around $1.5\%$ under the simple decoder and around $2\%$ under the improved decoder  ([arXiv:1012.0425](https://arxiv.org/abs/1012.0425)).

## Relations

- _parent_: [[concepts/qec/subsystem-hypergraph]] — Generalized five-squares codes are special cases of Sarvepalli-Brown subsystem codes  ([arXiv:1805.12542](https://arxiv.org/abs/1805.12542)).
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _cousin_: [[concepts/qec/toric]] — For the original five-squares code, preprocessing maps decoding onto two copies of the toric code  ([arXiv:1012.0425](https://arxiv.org/abs/1012.0425)).
