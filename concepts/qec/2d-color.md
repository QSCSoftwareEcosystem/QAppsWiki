---
type: concept
name: 2D color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-color
- concepts/qec/color
- concepts/qec/galois-color
- concepts/qec/generalized-color
- concepts/qec/hamiltonian
- concepts/qec/quantum-double-abelian
- concepts/qec/qudit-color
- concepts/qec/surface
- concepts/qec/twist-defect-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/2d_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 2d_color
---

# 2D color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/2d_color) (`code_id: 2d_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Color code defined on a graph embedded in a two-dimensional surface.
Each face hosts two stabilizer generators, a Pauli-$X$ and a Pauli-$Z$ string acting on all the qubits of the face.

Most translation-invariant color codes are defined on trivalent planar graphs with three-colorable faces.
The three admissible uniform tilings are the 6.6.6 (honeycomb) tiling, the 4.8.8 (square octagon) tiling, and the 4.6.12 tiling  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)).
Non-uniform tilings include the [4.6.8, 6.8.8] and [4.6.8, 4.8.12] tilings  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
More general admissible tilings can be obtained via a fattening procedure  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)); see also a construction based on the more general quantum pin codes  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).

Logical dimension is determined by the genus of the underlying surface (for closed surfaces) and the types of boundaries (for open surfaces).
There are six basic boundary types: three color boundaries corresponding to the three face colors  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)) and three Pauli boundaries corresponding to the three Pauli labels  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).

String operators are defined on paths along edges of the qubit lattice.
These paths can have branching points. Each path has two string operators, one corresponding to the $X$ basis and one corresponding to the $Z$ basis.
In correspondence with the coloring of the lattice faces, string operators also come in three colors.
A string of one color must end in a boundary of that same color.

(source: raw/error-correction-zoo.md)

## Rate

For general 2D manifolds, $kd^2 \leq c(\log k)^2 n$ for some constant $c$ in what can be thought of as an extension of the BPT bound to codes on hyperbolic geometries  ([arXiv:1301.6588](https://arxiv.org/abs/1301.6588)), meaning that color codes with finite rate can only achieve an asymptotic minimum distance that is logarithmic in $n$.

## Transversal gates

- CNOT gate because the code is CSS.
- Hadamard gates for any qubit geometry which yields a self-dual CSS code.
- Certain triangular 2D color codes on suitably chosen lattices admit transversal implementations of the full Clifford group, including $H$, $S^\dagger$, and $CNOT$, without selective addressing  ([arXiv:quant-ph/0605138](https://arxiv.org/abs/quant-ph/0605138)).

## General gates

- Magic-state distillation protocols  ([doi:10.7907/059V-MG69](https://doi.org/10.7907/059V-MG69)).
- Non-clifford gates can be implemented via code switching  ([doi:10.7907/059V-MG69](https://doi.org/10.7907/059V-MG69)).

## Decoders

- Projection decoder of $O(n^4)$ complexity  ([arXiv:1308.6207](https://arxiv.org/abs/1308.6207)), modified to account for syndrome errors  ([arXiv:1402.3037](https://arxiv.org/abs/1402.3037)).
- Exact minimum-weight decoding is $NP$-hard for 2D color codes, including for solely Pauli-$Z$ noise  ([arXiv:2603.04234](https://arxiv.org/abs/2603.04234), [arXiv:2603.22064](https://arxiv.org/abs/2603.22064)).
- Chromöbius, an open-source implementation of the Möbius decoder, works for many 2D color codes  ([arXiv:2312.08813](https://arxiv.org/abs/2312.08813)).
- Concatenated MPWM decoder  ([arXiv:2404.07482](https://arxiv.org/abs/2404.07482)).
- Syndrome extraction circuits based on superdense coding and a middle-out strategy  ([arXiv:2312.08813](https://arxiv.org/abs/2312.08813)).

## Relations

- _parent_: [[concepts/qec/color]]
- _parent_: [[concepts/qec/generalized-color]] — The generalized color code for $G=\mathbb{Z}_2$ reduces to the 2D color code.
- _parent_: [[concepts/qec/twist-defect-color]] — Twist-defect color codes reduce to 2D color codes when there are no defects. See Ref.  ([arXiv:2112.13617](https://arxiv.org/abs/2112.13617)) for an alternative non-CSS extension of 2D color codes.
- _parent_: [[concepts/qec/qudit-color]] — Modular-qudit 2D color codes reduce to 2D color codes for $q=2$.
- _parent_: [[concepts/qec/galois-color]] — Galois-qudit 2D color codes reduce to 2D color codes for $q=2$.
- _parent_: [[concepts/qec/quantum-double-abelian]] — When treated as ground states of the code Hamiltonian, states of the color code on a torus geometry realize $\mathbb{Z}_2\times\mathbb{Z}_2$ topological order  ([arXiv:0906.4127](https://arxiv.org/abs/0906.4127)), equivalent to the phase realized by two copies of the toric code (i.e., the surface code on a torus) via a local constant-depth Clifford circuit  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065)).
This process can be viewed as an ungauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) of certain symmetries.
- _cousin_: [[concepts/qec/surface]] — On closed surfaces, the 2D color code is equivalent to two decoupled copies of the 2D toric/surface code via a local constant-depth Clifford circuit  ([arXiv:1007.4601](https://arxiv.org/abs/1007.4601), [arXiv:1503.02065](https://arxiv.org/abs/1503.02065), [arXiv:1804.00866](https://arxiv.org/abs/1804.00866)) and has the same topological entanglement entropy  ([arXiv:0809.4276](https://arxiv.org/abs/0809.4276)). For triangular patches with three differently colored boundaries, it is instead equivalent to a folded surface/toric code with two smooth and two rough boundaries  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065)). The conversion process can be viewed as an ungauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) of certain symmetries. Conversely, the 2D color code can condense to form the 2D surface code in nine different ways, i.e., by adding two-body hopping terms along one of its three triangular directions to the stabilizer group and then taking the center of the resulting nonabelian group  ([arXiv:2212.00042](https://arxiv.org/abs/2212.00042)). Both the surface and 2D color codes can be constructed from two distinct types of lattices, namely, 4-valent and 3-valent 3-colorable lattices, respectively  ([arXiv:1107.3502](https://arxiv.org/abs/1107.3502)).
- _cousin_: [[concepts/qec/3d-color]] — Gauge fixing can be used to code switch between 2D and 3D color codes, thereby yielding fault-tolerant computation with constant time overhead using only local quantum operations  ([arXiv:1412.5079](https://arxiv.org/abs/1412.5079)). There is a fault-tolerant measurement-free scheme for code switching between 2D and 3D color codes  ([arXiv:2410.13568](https://arxiv.org/abs/2410.13568)).
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — As CSS codes, variants of the 2D color code are constructed out of self-dual classical codes on cubic planar graphs  ([doi:10.1016/0095-8956(91)90066-S](https://doi.org/10.1016/0095-8956(91)90066-S)).
- _cousin_: [[concepts/qec/hamiltonian]] — 2D color code Hamiltonians can be simulated, with the help of perturbation theory, by two-dimensional weight-two (two-body) Hamiltonians with non-commuting terms  ([arXiv:0906.4127](https://arxiv.org/abs/0906.4127)).
