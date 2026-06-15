---
type: concept
name: Bivariate bicycle (BB) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2bga
- concepts/qec/2d-stabilizer
- concepts/qec/abelian-lifted-product
- concepts/qec/generalized-bicycle
- concepts/qec/qubit-generalized-homological-product-css
- concepts/qec/topological-abelian
- concepts/qec/triangular-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qcga
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qcga
---

# Bivariate bicycle (BB) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qcga) (`code_id: qcga`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

One of several Abelian 2BGA codes which admit time-optimal syndrome measurement circuits that can be implemented in a two-layer
architecture, a generalization of the square-lattice architecture
optimal for the surface codes.
Codes can be classified by the weight of their checks, e.g., by BB$w$ where $w$ is the check weight.

The qubit connectivity graph is not quite a 2D grid and is instead decomposable into two planar subgraphs of degree three; there exists an optimized layout minimizing Euclidean communication distance for check operators  ([arXiv:2404.18809](https://arxiv.org/abs/2404.18809)).
There are $n$ $X$ and $Z$ check operators, with each one of weight six.

See Refs.  ([arXiv:2510.05211](https://arxiv.org/abs/2510.05211), [arXiv:2510.06159](https://arxiv.org/abs/2510.06159)) for examples of self-dual BB codes.
Several variants and generalizations exist  ([arXiv:2406.19151](https://arxiv.org/abs/2406.19151), [arXiv:2408.10001](https://arxiv.org/abs/2408.10001)).
There exist qudit BB codes that achieve $kd^2 / n = 20$  ([arXiv:2602.20158](https://arxiv.org/abs/2602.20158)).

(source: raw/error-correction-zoo.md)

## Protection

Admits an $0.8\%$ pseudo-threshold for circuit-level noise under BP-OSD decoder  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)) (cf.  ([arXiv:0803.0272](https://arxiv.org/abs/0803.0272))).

## Transversal gates

- Logical Pauli operators and fold-transversal gates studied in Ref.  ([arXiv:2407.03973](https://arxiv.org/abs/2407.03973), [arXiv:2409.18175](https://arxiv.org/abs/2409.18175)).

## General gates

- Certain bivariate bicycle codes admit a cup product structure and can thus have logical gates in the \term{Clifford hierarchy} implemented by constant-depth Clifford circuits  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).

## Rate

When ancilla qubit overhead is included, the encoding rate surpasses that of the surface code. A general $⟦n,k,d⟧$ bivariate bicycle code requires $n$ ancilla qubits for encoding, meaning that its *ancilla-added encoding rate* is $k/2n$.

## Fault tolerance

- Fault-tolerant state initialization using lattice surgery techniques  ([arXiv:2110.10794](https://arxiv.org/abs/2110.10794), [arXiv:2308.08648](https://arxiv.org/abs/2308.08648)) and an ancillary surface code  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)).

## Decoders

- Syndrome extraction circuit requires seven layers of CNOT gates regardless of code length. BP-OSD decoder  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703)) has been extended  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)) to account for measurement errors (i.e., the circuit-based noise model  ([arXiv:0803.0272](https://arxiv.org/abs/0803.0272))).
- The depth-7 syndrome extraction schedules studied in Ref.  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)) are not generally distance-preserving; for the $⟦144,12,12⟧$ code, all $936$ depth-7 variants obtained by reordering the CNOT layers satisfy $d_{\mathrm{circ}}\leq 10 < d$.
- Some long-range check operators can be measured less frequently than others  ([arXiv:2404.17676](https://arxiv.org/abs/2404.17676)).
- Syndrome extraction circuits called *morphing circuits*  ([arXiv:2407.16336](https://arxiv.org/abs/2407.16336)), generalizing circuits for the color code  ([arXiv:2312.08813](https://arxiv.org/abs/2312.08813)).
- Decoding under circuit-level noise has been studied for the BP, BP+OSD, and AutDEC decoders  ([arXiv:2503.01738](https://arxiv.org/abs/2503.01738)).
- Transformer-based neural-network decoder  ([arXiv:2504.13043](https://arxiv.org/abs/2504.13043)).
- Matching decoder  ([arXiv:2602.22770](https://arxiv.org/abs/2602.22770)).

## Realizations

- Superconducting circuits: syndrome extraction has been implemented for the $⟦18,4,4⟧$ BB code on a 32-qubit Kunlun device by the Wang, Song, and Deng groups  ([arXiv:2505.09684](https://arxiv.org/abs/2505.09684)). The same is also shown for an $⟦18,6,3⟧$ code obtained by removing two check operators from the former code  ([arXiv:2505.09684](https://arxiv.org/abs/2505.09684)).

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]]
- _parent_: [[concepts/qec/2bga]] — Bivariate bicycle codes are Abelian 2BGA codes over groups of the form $\mathbb{Z}_{r} \times \mathbb{Z}_{s}$.
- _parent_: [[concepts/qec/abelian-lifted-product]] — Bivariate bicycle codes are Abelian LP codes over groups of the form $\mathbb{Z}_{r} \times \mathbb{Z}_{s}$.
- _parent_: [[concepts/qec/2d-stabilizer]] — Bivariate bicycle codes are defined on 2D lattices with periodic boundary conditions, and versions with open boundary conditions have been investigated  ([arXiv:2410.11942](https://arxiv.org/abs/2410.11942), [arXiv:2412.04181](https://arxiv.org/abs/2412.04181)). Bivariate bicycle codes are on par with the surface code in terms of threshold, but admit a much higher ancilla-added encoding rate at the expense of having non-geometrically local weight-six check operators. BB codes have been investigated in terms of their anyons and topological order  ([arXiv:2503.04699](https://arxiv.org/abs/2503.04699)).
- _cousin_: [[concepts/qec/triangular-color]] — Certain bivariate bicycle codes are equivalent to a family of 6.6.6 color codes  ([arXiv:2412.04181](https://arxiv.org/abs/2412.04181)).
- _cousin_: [[concepts/qec/topological-abelian]] — BB codes have been investigated in terms of their anyons and topological order  ([arXiv:2503.04699](https://arxiv.org/abs/2503.04699)).
- _cousin_: [[concepts/qec/generalized-bicycle]] — GB codes (BB codes) are 2BGA codes over the cyclic group $\mathbb{Z}_{\ell}$ (Abelian group $\mathbb{Z}_{r} \times \mathbb{Z}_{s}$). The two codes are the same when $r$ and $s$ are relatively prime due to the isomorphism $\mathbb{Z}_{r} \times \mathbb{Z}_{s} \cong \mathbb{Z}_{\ell = rs}$.

## Notes

- A database of bivariate bicycle codes is available in QECDB .
