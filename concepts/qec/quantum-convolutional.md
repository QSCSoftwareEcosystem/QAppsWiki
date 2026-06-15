---
type: concept
name: Quantum convolutional code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/1d-stabilizer
- concepts/qec/qldpc
- concepts/qec/quantum-lego
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_convolutional
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_convolutional
---

# Quantum convolutional code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_convolutional) (`code_id: quantum_convolutional`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

1D translationally invariant qubit stabilizer code whose stabilizer group can be partitioned into constant-size subsets of constant support and of constant overlap between neighboring sets.
Initially formulated as a quantum analogue of convolutional codes, which were designed to protect a continuous and never-ending stream of information.
Precise formulations sometimes begin with a finite-dimensional lattice, with the intent to take the thermodynamic limit; logical dimension can be infinite as well.

Quantum convolutional codes, like their classical counterparts, can also be understood in terms of frames. Let each encoding frame take in $n$ qubits, carry $m$ qubits of information between frames, and act on them with $n-k$ Pauli generators. Each generator, countably infinite in length, must commute with each $n$ register shift of itself, but need not commute with the other generators  ([arXiv:quant-ph/0703182](https://arxiv.org/abs/quant-ph/0703182)). The $m$ qubits of information carried between each frame are also stabilized by additional memory Pauli operators. It is known that the minimal value for $m$ is given by $\text{dim}(M)-\frac{1}{2}\text{rank}(M)$, with $M$ being the matrix containing the required commutation relations of the memory qubits  ([arXiv:1105.0649](https://arxiv.org/abs/1105.0649), [arXiv:1011.5535](https://arxiv.org/abs/1011.5535), [arXiv:0804.1404](https://arxiv.org/abs/0804.1404)). These operators can be efficiently determined  ([arXiv:2206.13040](https://arxiv.org/abs/2206.13040)).

(source: raw/error-correction-zoo.md)

## Encoders

- Encoding is efficient and uses only Clifford gates. Some encoders yield *catastrophic* errors, i.e., errors that require a circuit of infinite depth to correct  ([arXiv:quant-ph/0401134](https://arxiv.org/abs/quant-ph/0401134)).
- Pearl-necklace encoding  ([arXiv:quant-ph/0304189](https://arxiv.org/abs/quant-ph/0304189), [arXiv:quant-ph/0401134](https://arxiv.org/abs/quant-ph/0401134), [arXiv:quant-ph/0602129](https://arxiv.org/abs/quant-ph/0602129), [arXiv:1004.5179](https://arxiv.org/abs/1004.5179)).
- Quantum shift register encoding  ([arXiv:0903.3894](https://arxiv.org/abs/0903.3894)).
- Encoding circuits can be viewed as matrix-product-state tensor networks  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Decoders

- Quantum Viterbi decoder  ([arXiv:quant-ph/9806032](https://arxiv.org/abs/quant-ph/9806032), [arXiv:quant-ph/0304189](https://arxiv.org/abs/quant-ph/0304189), [arXiv:quant-ph/0401134](https://arxiv.org/abs/quant-ph/0401134)).
- ML decoder  ([arXiv:quant-ph/0304189](https://arxiv.org/abs/quant-ph/0304189)).

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/1d-stabilizer]] — Quantum convolutional codes are lattice stabilizer codes on a semi-infinite or infinite lattice in one dimension  ([arXiv:1305.6973](https://arxiv.org/abs/1305.6973)). Some notions may be extendable to non-stabilizer codes  ([arXiv:quant-ph/0401134](https://arxiv.org/abs/quant-ph/0401134)).
Any prime-qudit code can be converted using a constant-depth Clifford circuit to several copies of the 1D repetition code along with some trivial codes  ([arXiv:1607.01387](https://arxiv.org/abs/1607.01387)).
- _cousin_: [[concepts/qec/quantum-lego]] — Quantum convolutional encoding circuits can be viewed as matrix-product-state tensor networks  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).
- _cousin_: [`generalized_reed_solomon`](https://errorcorrectionzoo.org/c/generalized_reed_solomon) — GRS codes can be used to construct quantum convolutional codes  ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)).
- _cousin_: [`generalized_reed_muller`](https://errorcorrectionzoo.org/c/generalized_reed_muller) — GRM codes can be used to construct quantum convolutional codes  ([arXiv:quant-ph/0604102](https://arxiv.org/abs/quant-ph/0604102), [doi:10.1201/9781584889007-18](https://doi.org/10.1201/9781584889007-18)) ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)).

## Notes

- See Refs.  ([arXiv:quant-ph/0304189](https://arxiv.org/abs/quant-ph/0304189), [arXiv:quant-ph/0511016](https://arxiv.org/abs/quant-ph/0511016), [arXiv:quant-ph/0602129](https://arxiv.org/abs/quant-ph/0602129), [arXiv:quant-ph/0703181](https://arxiv.org/abs/quant-ph/0703181)) for explicit and simple examples.
- See Ref.  ([doi:10.1017/CBO9781139034807.011](https://doi.org/10.1017/CBO9781139034807.011)) and the book  for an introduction to quantum convolutional codes.
- Quantum convolutional codes are briefly reviewed in .
