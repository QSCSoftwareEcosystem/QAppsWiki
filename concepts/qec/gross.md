---
type: concept
name: $⟦144,12,12⟧$ gross code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- $(3,3)$ BB6 code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
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

The polynomials $A=x^3+y+y^2$ and $B=y^3+x+x^2$ of the gross code on $\ell=m=12$ yield an indecomposable $⟦288,16,12⟧$ code  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).
A different BB QLDPC code with the same parameters was introduced in  ([arXiv:2407.16336](https://arxiv.org/abs/2407.16336)).

(source: raw/error-correction-zoo.md)

## Rate

An ancilla-added rate of $1/24$. In contrast, the distance-13 surface code has ancilla-added rate $1/338$.

## Transversal gates

- Logical Pauli operators and fold-transversal gates studied in Ref.  ([arXiv:2409.18175](https://arxiv.org/abs/2409.18175)).
- Two-fold transversal gates, i.e., depth-one circuits of two-local code-preserving physical gates, realize a logical group of order at least $460800$, short of the full logical Clifford group  ([arXiv:2608.05688](https://arxiv.org/abs/2608.05688)).

## General gates

- Clifford gates  ([arXiv:2407.18393](https://arxiv.org/abs/2407.18393)).

## Decoders

- The GDG sliding-window decoder  ([arXiv:2403.18901](https://arxiv.org/abs/2403.18901)), with a realization achieving a worst-case decoding latency of 3ms per window.
- AC decoder is faster than ordinary BP-OSD with no reduction of fidelity  ([arXiv:2406.14527](https://arxiv.org/abs/2406.14527)).
- Transformer-based neural-network decoder  ([arXiv:2504.13043](https://arxiv.org/abs/2504.13043)).
- [Frontier decoder](https://github.com/aleverrier/frontier), a pruned dynamic-programming decoder, retains on average fewer than 100 states under circuit-level noise at $p=10^{-3}$  ([arXiv:2606.20513](https://arxiv.org/abs/2606.20513)).

## Fault tolerance

- At physical error rate $p=10^{-3}$ under circuit-level noise, the code suppresses the logical error rate to about $2\times 10^{-7}$, enough to preserve $12$ logical qubits for nearly one million syndrome cycles using $288$ total physical qubits  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)).
- Fault-tolerant modular quantum computing framework  ([arXiv:2506.03094](https://arxiv.org/abs/2506.03094)).

## Code capacity threshold

- Bit-flip noise: pseudo-threshold of $\approx 5\%$ for the block logical error rate under BP-OSD decoding  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).

## Threshold

- Admits a pseudo-threshold of $\approx 0.7\%$ for the circuit-based noise model  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)).

## Realizations

- An FPGA implementation of the Relay-BP decoder  ([arXiv:2510.21600](https://arxiv.org/abs/2510.21600)).

## Relations

- _parent_: [[concepts/qec/qcga]]
- _parent_: [[concepts/qec/2d-stabilizer]] — The gross code belongs to the $(3,3)$-BB family of 2D lattice stabilizer codes obtained by holding the check pattern fixed while enlarging the torus  ([arXiv:2410.11942](https://arxiv.org/abs/2410.11942)).
- _cousin_: [[concepts/qec/surface]] — The gross code requires less physical and ancilla qubits (for syndrome extraction) than the surface code with the same number of logical qubits and distance. The gross code is equivalent to 8 copies of the surface code via a constant-depth Clifford circuit, and is an element of a larger family of 2D stabilizer codes  ([arXiv:2410.11942](https://arxiv.org/abs/2410.11942)). An architecture combining the surface and gross codes was proposed in  ([arXiv:2411.03202](https://arxiv.org/abs/2411.03202)).
