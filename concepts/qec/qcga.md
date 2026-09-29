---
type: concept
name: Bivariate bicycle (BB) code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/abelian-2bga
- concepts/qec/generalized-bicycle
- concepts/qec/mirror
- concepts/qec/perm-self-dual-css
- concepts/qec/perturbed-bb
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
Bivariate bicycle codes are on par with the surface code in terms of threshold, but admit a much higher ancilla-added encoding rate at the expense of having non-geometrically local weight-six check operators.

See Refs.  ([arXiv:2510.05211](https://arxiv.org/abs/2510.05211), [arXiv:2510.06159](https://arxiv.org/abs/2510.06159)) for examples of self-dual BB codes.
Multivariate (e.g., trivariate) bicycle codes generalize BB codes to Abelian 2BGA codes with polynomials in more than two variables  ([arXiv:2406.19151](https://arxiv.org/abs/2406.19151)); other variants and generalizations exist  ([arXiv:2408.10001](https://arxiv.org/abs/2408.10001)).
Versions with open boundary conditions are tile codes  ([arXiv:2504.09171](https://arxiv.org/abs/2504.09171)), obtained by pruning  ([arXiv:2412.04181](https://arxiv.org/abs/2412.04181)) or by condensing boundary anyons  ([arXiv:2410.11942](https://arxiv.org/abs/2410.11942), [arXiv:2504.08887](https://arxiv.org/abs/2504.08887)).
There exist qudit BB codes that achieve $kd^2 / n = 20$  ([arXiv:2602.20158](https://arxiv.org/abs/2602.20158)).

(source: raw/error-correction-zoo.md)

## Protection

A BB code with $A=B$ and $k>0$ has distance two regardless of check weight  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).

## Transversal gates

- Logical Pauli operators and fold-transversal gates studied in Ref.  ([arXiv:2407.03973](https://arxiv.org/abs/2407.03973), [arXiv:2409.18175](https://arxiv.org/abs/2409.18175)).

## General gates

- Certain bivariate bicycle codes admit a cup product structure and can thus have logical gates in the \term{Clifford hierarchy} implemented by constant-depth Clifford circuits  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).

## Rate

When ancilla qubit overhead is included, the encoding rate surpasses that of the surface code. A general $⟦n,k,d⟧$ bivariate bicycle code requires $n$ ancilla qubits for encoding, meaning that its *ancilla-added encoding rate* is $k/2n$.

## Fault tolerance

- Fault-tolerant state initialization using lattice surgery techniques  ([arXiv:2110.10794](https://arxiv.org/abs/2110.10794), [arXiv:2308.08648](https://arxiv.org/abs/2308.08648)) and an ancillary surface code  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)).
- Syndrome extraction circuit requires seven layers of CNOT gates regardless of code length  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)).
- The depth-7 syndrome extraction schedules studied in Ref.  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)) are not generally distance-preserving; for the $⟦144,12,12⟧$ code, all $936$ depth-7 variants obtained by reordering the CNOT layers satisfy $d_{\mathrm{circ}}\leq 10 < d$.
- Some long-range check operators can be measured less frequently than others  ([arXiv:2404.17676](https://arxiv.org/abs/2404.17676)).
- Syndrome extraction circuits called *morphing circuits*  ([arXiv:2407.16336](https://arxiv.org/abs/2407.16336)), generalizing circuits for the color code  ([arXiv:2312.08813](https://arxiv.org/abs/2312.08813)).

## Code capacity threshold

- Fully postselected failure rates of weight-six BB codes under bit-flip noise cross near $p=1/(2+\sqrt{2})\approx 0.2929$  ([arXiv:2607.21160](https://arxiv.org/abs/2607.21160)). This value is the self-dual critical point of zero-rate PSD code families with a unique threshold  ([arXiv:2607.21160](https://arxiv.org/abs/2607.21160)). Without postselection, the $k=12$ weight-six family of Ref.  ([arXiv:2511.13560](https://arxiv.org/abs/2511.13560)) has a threshold of $8.38(6)\%$ under BP-OSD decoding  ([arXiv:2607.21160](https://arxiv.org/abs/2607.21160)).

## Threshold

- Admits a $0.8\%$ pseudo-threshold for circuit-level noise under BP-OSD decoder  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)) (cf.  ([arXiv:0803.0272](https://arxiv.org/abs/0803.0272))).

## Decoders

- BP-OSD decoder  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703)) has been extended  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915)) to account for measurement errors (i.e., the circuit-based noise model  ([arXiv:0803.0272](https://arxiv.org/abs/0803.0272))).
- Decoding under circuit-level noise has been studied for the BP, BP+OSD, and AutDEC decoders  ([arXiv:2503.01738](https://arxiv.org/abs/2503.01738)).
- Transformer-based neural-network decoder  ([arXiv:2504.13043](https://arxiv.org/abs/2504.13043)).
- Matching decoder  ([arXiv:2602.22770](https://arxiv.org/abs/2602.22770)).

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]]
- _parent_: [[concepts/qec/abelian-2bga]] — Bivariate bicycle codes are Abelian 2BGA (equivalently, two-variable multivariate bicycle) codes over groups of the form $\mathbb{Z}_{r} \times \mathbb{Z}_{s}$.
- _parent_: [[concepts/qec/perm-self-dual-css]] — Bivariate bicycle codes are permutationally self-dual. Their standard $XZ$-duality exchanges the two blocks of qubits while sending $x\mapsto x^{-1}$ and $y\mapsto y^{-1}$. This involution yields a Hadamard-type fold-transversal gate  ([arXiv:2407.03973](https://arxiv.org/abs/2407.03973)). BB codes on $\mathbb{Z}_{\ell}\times\mathbb{Z}_{\ell}$ whose two polynomials are exchanged by swapping $x$ and $y$ admit a second $XZ$-duality. It sends $x\mapsto y^{-1}$ and $y\mapsto x^{-1}$ within each block and yields a phase-type fold-transversal gate  ([arXiv:2407.03973](https://arxiv.org/abs/2407.03973)).
- _parent_: [[concepts/qec/perturbed-bb]] — BB codes are PBB codes with $C=D=0$  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).
- _parent_: [[concepts/qec/mirror]] — BB codes are mirror codes up to qubit permutations and Hadamard gates  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
- _cousin_: [[concepts/qec/triangular-color]] — Certain bivariate bicycle codes are equivalent to a family of 6.6.6 color codes  ([arXiv:2412.04181](https://arxiv.org/abs/2412.04181)).
- _cousin_: [[concepts/qec/topological-abelian]] — BB codes have been investigated in terms of their anyons and topological order  ([arXiv:2503.04699](https://arxiv.org/abs/2503.04699)).
- _cousin_: [[concepts/qec/generalized-bicycle]] — GB codes (BB codes) are 2BGA codes over the cyclic group $\mathbb{Z}_{\ell}$ (Abelian group $\mathbb{Z}_{r} \times \mathbb{Z}_{s}$). The two codes are the same when $r$ and $s$ are relatively prime due to the isomorphism $\mathbb{Z}_{r} \times \mathbb{Z}_{s} \cong \mathbb{Z}_{\ell = rs}$.

## Notes

- A database of bivariate bicycle codes is available in QECDB .
- A catalogue of BB codes found by LLM-guided search is available at [qcode-discovery](https://github.com/qiskit-community/qcode-discovery)  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).
