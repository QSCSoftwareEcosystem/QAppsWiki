---
type: concept
name: Concatenated quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-lego
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_concatenated
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_concatenated
---

# Concatenated quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_concatenated) (`code_id: quantum_concatenated`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A combination of two quantum codes, an inner code $C_{\text{in}}$ and an outer code $C_{\text{out}}$, where the physical subspace used for the inner code consists of the logical subspace of the outer code.
In other words, one first encodes in the inner code, and then encodes each of its physical registers in the outer code.
An inner $C_{\text{in}} = ((n_1,K,d_1))_{q_1}$ and outer $C_{\text{out}} = ((n_2,q_1,d_2))_{q_2}$ block quantum code yield an $((n_1 n_2, K, d \geq d_1d_2))_{q_2}$ concatenated block quantum code .

More generally, one can concatenate in blocks: several physical registers of the inner code can be grouped together so that each such block carries one logical register of the outer code.
Encoding then proceeds by first applying the inner encoding to each block and then applying the outer encoding across the resulting blocks.

Concatenating an $((n,q,d))_q$ block quantum code can be done recursively, with the $r$*th level* of concatenation yielding an $((n^r,q,d^r))_q$ code.

Other ways to combine quantum codes include pasting  ([arXiv:quant-ph/9607027](https://arxiv.org/abs/quant-ph/9607027)), and generalizations of concatenation exist  ([arXiv:0901.1319](https://arxiv.org/abs/0901.1319), [arXiv:0909.5103](https://arxiv.org/abs/0909.5103)).

(source: raw/error-correction-zoo.md)

## Encoders

- Standard encoding proceeds by first encoding into the inner code and then encoding each physical register of the inner code into the outer code.

## Decoders

- Standard decoding proceeds in the reverse order: first decode the outer code blocks and then use the resulting data to decode the inner code.
- Maximum-likelihood decoding can be formulated as contraction of a tree tensor network, yielding exact decoders that improve on minimum-distance decoding for recursively concatenated block codes  ([arXiv:quant-ph/0606126](https://arxiv.org/abs/quant-ph/0606126), [arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Fault tolerance

- Recursive concatenation is the standard route to threshold-theorem constructions: if one level of a fault-tolerant simulation suppresses logical error below the physical error rate, then further concatenation suppresses it rapidly, yielding the family of protocols used in polylogarithmic-overhead threshold theorems .

## Relations

- _parent_: [[concepts/qec/quantum-lego]] — Encoders for concatenated quantum codes correspond to tree tensor networks  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Notes

- See the book  for an introduction.
