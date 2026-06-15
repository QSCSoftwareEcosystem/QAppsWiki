---
type: concept
name: Lechner-Hauke-Zoller (LHZ) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Lechner-Hauke-Zoller (LHZ) parity code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-classical-into-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/lhz
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: lhz
---

# Lechner-Hauke-Zoller (LHZ) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/lhz) (`code_id: lhz`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

LDPC c-q code designed to convert the long-range interactions of a quantum annealer into local constraints.
The code maps the pairwise couplings of a fully connected classical Ising model into local fields together with local parity constraints on a lattice of physical qubits.
An extension maps more general models onto the same lattice  ([arXiv:2105.06233](https://arxiv.org/abs/2105.06233)).

(source: raw/error-correction-zoo.md)

## Encoders

- Arbitrary quantum states  ([arXiv:2303.08602](https://arxiv.org/abs/2303.08602)).

## General gates

- Universal gate set  ([arXiv:2205.09505](https://arxiv.org/abs/2205.09505)).

## Decoders

- BP decoder  ([arXiv:1511.00004](https://arxiv.org/abs/1511.00004)).

## Relations

- _parent_: [[concepts/qec/qubit-classical-into-quantum]] — The LHZ code is an LDPC c-q code designed to convert the long-range interactions of a quantum annealer into local constraints.
- _cousin_: [`ldpc`](https://errorcorrectionzoo.org/c/ldpc) — The LHZ code is an LDPC c-q code designed to convert the long-range interactions of a quantum annealer into local constraints.
