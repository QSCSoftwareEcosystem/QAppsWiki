---
type: concept
name: $⟦144,12,12⟧$ gross code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $(3,3)$ BB6 code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qcga
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/gross
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: gross
---

# $⟦144,12,12⟧$ gross code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/gross) (`code_id: gross`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A BB code which requires less physical and ancilla qubits (for syndrome extraction) than the surface code with the same number of logical qubits and distance.
The gross code is equivalent to 8 copies of the surface code via a constant-depth Clifford circuit, and is an element of a larger family of 2D stabilizer codes  ([arXiv:2410.11942](https://arxiv.org/abs/2410.11942)).
The name stems from the fact that a gross is a dozen dozen.

A different BB QLDPC code with the same parameters was introduced in  ([arXiv:2407.16336](https://arxiv.org/abs/2407.16336)).

(source: raw/error-correction-zoo.md)

## Protection

Admits a pseudo-threshold of $\approx 0.7\%$ for the circuit-based noise model.
At physical error rate $p=10^{-3}$, the code suppresses the logical error rate to about $2\times 10^{-7}$, enough to preserve $12$ logical qubits for nearly one million syndrome cycles using $288$ total physical qubits  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)).

## Rate

An ancilla-added rate of $1/24$. In contrast, the distance-13 surface code has ancilla-added rate $1/338$.

## Transversal gates

- Logical Pauli operators and fold-transversal gates studied in Ref.  ([arXiv:2409.18175](https://arxiv.org/abs/2409.18175)).

## General gates

- Clifford gates  ([arXiv:2407.18393](https://arxiv.org/abs/2407.18393)).

## Decoders

- The GDG sliding-window decoder  ([arXiv:2403.18901](https://arxiv.org/abs/2403.18901)), with a realization achieving a worst-case decoding latency of 3ms per window.
- AC decoder is faster than ordinary BP-OSD with no reduction of fidelity  ([arXiv:2406.14527](https://arxiv.org/abs/2406.14527)).
- Transformer-based neural-network decoder  ([arXiv:2504.13043](https://arxiv.org/abs/2504.13043)).

## Fault tolerance

- Fault-tolerant modular quantum computing framework  ([arXiv:2506.03094](https://arxiv.org/abs/2506.03094)).

## Realizations

- An FPGA implementation of the Relay-BP decoder  ([arXiv:2510.21600](https://arxiv.org/abs/2510.21600)).

## Relations

- _parent_: [[concepts/qec/qcga]]
- _cousin_: [[concepts/qec/surface]] — The gross code requires less physical and ancilla qubits (for syndrome extraction) than the surface code with the same number of logical qubits and distance. The gross code is equivalent to 8 copies of the surface code via a constant-depth Clifford circuit, and is an element of a larger family of 2D stabilizer codes  ([arXiv:2410.11942](https://arxiv.org/abs/2410.11942)). An architecture combining the surface and gross codes was proposed in  ([arXiv:2411.03202](https://arxiv.org/abs/2411.03202)).
