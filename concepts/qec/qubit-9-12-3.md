---
type: concept
name: $((9,12,3))$ qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cws
- concepts/qec/quantum-cyclic
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_9_12_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_9_12_3
---

# $((9,12,3))$ qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_9_12_3) (`code_id: qubit_9_12_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Nine-qubit cyclic CWS code correcting a single-qubit error.
This code has a logical subspace whose dimension is larger than that of the $⟦9,3,3⟧$ code, the best nine-qubit stabilizer code with the same distance  ([arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)).

Its codeword stabilizer consists of all cyclic shifts of $ZXZIIIIII$.
In the coding-clique framework, it is realized by the nine-vertex loop graph $L_9$; within a graph search  ([arXiv:0709.1780](https://arxiv.org/abs/0709.1780)), the realization $(L_9,12,3)$ is unique and there is no $(G,13,3)$ code on any nine-vertex graph.

The $((9,12,3))$ qubit code can be combined to form an infinite family of distance-three qubit codes whose logical dimension is $50\%$ larger than that of the optimal stabilizer code  ([arXiv:0901.1935](https://arxiv.org/abs/0901.1935)).

(source: raw/error-correction-zoo.md)

## Decoders

- Fault-tolerant scheme that converts the required POVM into 10 binary measurements whose redundancy is guaranteed by a classical code  ([arXiv:2402.04093](https://arxiv.org/abs/2402.04093)).

## Relations

- _parent_: [[concepts/qec/cws]] — The $((9,12,3))$ qubit code is a cyclic CWS code  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021)).
- _parent_: [[concepts/qec/quantum-cyclic]]
- _parent_: [[concepts/qec/small-distance-quantum]] — The $((9,12,3))$ qubit code can be combined to form an infinite family of distance-three qubit codes whose logical dimension is $50\%$ larger than that of the optimal stabilizer code  ([arXiv:0901.1935](https://arxiv.org/abs/0901.1935)).
