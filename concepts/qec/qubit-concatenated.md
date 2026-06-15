---
type: concept
name: Concatenated qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fusion
- concepts/qec/hamiltonian
- concepts/qec/quantum-concatenated
- concepts/qec/qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_concatenated
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_concatenated
---

# Concatenated qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_concatenated) (`code_id: qubit_concatenated`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A concatenated code whose outer code is a qubit code. In other words, a qubit code that can be thought of as a concatenation of an inner qubit code and an outer qubit code.
An inner $C_{\text{in}} = ((n_1,K,d_1))$ and outer $C_{\text{out}} = ((n_2,2,d_2))$ qubit code yield an $((n_1 n_2, K, d \geq d_1d_2))$ concatenated qubit code.

Concatenating an $((n,2,d))$ qubit code can be done recursively, with the $r$*th level* of concatenation yielding an $((n^r,2,d^r))$ code.

(source: raw/error-correction-zoo.md)

## Protection

Any distance-three recursively concatenated code protects against an open set of errors  ([arXiv:quant-ph/0409084](https://arxiv.org/abs/quant-ph/0409084)).
Concatenating stabilizer codes can help protect against catastrophic errors such as cosmic rays  ([arXiv:2203.16488](https://arxiv.org/abs/2203.16488)).

## Decoders

- Adaptive syndrome extraction for a concatenation of a small error-detecting code and a high-rate, high-distance QLDPC code  ([arXiv:2502.14835](https://arxiv.org/abs/2502.14835)).
- The effective channel for a concatenation of codes is the composition of the codes' effective channels  ([arXiv:quant-ph/0206061](https://arxiv.org/abs/quant-ph/0206061)).
- Message passing algorithm for concatenated codes can be equivalent to ML decoding  ([arXiv:quant-ph/0606126](https://arxiv.org/abs/quant-ph/0606126)).

## Fault tolerance

- Fault-tolerant message passing between devices  ([arXiv:2408.05260](https://arxiv.org/abs/2408.05260)).
- Blocklet concatenation uses concatenation and transversal gates in a way that is tailored to FBQC platforms  ([arXiv:2506.13619](https://arxiv.org/abs/2506.13619)).

## Threshold

- The first methods to achieve a concatenated threshold against local stochastic noise use concatenated qubit stabilizer codes  ([arXiv:quant-ph/9702058](https://arxiv.org/abs/quant-ph/9702058), [arXiv:quant-ph/9705031](https://arxiv.org/abs/quant-ph/9705031), [arXiv:quant-ph/9903099](https://arxiv.org/abs/quant-ph/9903099), [arXiv:quant-ph/9906129](https://arxiv.org/abs/quant-ph/9906129), [arXiv:quant-ph/0410047](https://arxiv.org/abs/quant-ph/0410047), [arXiv:quant-ph/0504218](https://arxiv.org/abs/quant-ph/0504218), [arXiv:quant-ph/0703230](https://arxiv.org/abs/quant-ph/0703230), [arXiv:quant-ph/0604090](https://arxiv.org/abs/quant-ph/0604090)); see the book .

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/quantum-concatenated]]
- _cousin_: [[concepts/qec/hamiltonian]] — Concatenated stabilizer code Hamiltonians have been investigated  ([arXiv:0806.2160](https://arxiv.org/abs/0806.2160)).
- _cousin_: [[concepts/qec/fusion]] — Blocklet concatenation uses concatenation and transversal gates in a way that is tailored to FBQC platforms  ([arXiv:2506.13619](https://arxiv.org/abs/2506.13619)).
