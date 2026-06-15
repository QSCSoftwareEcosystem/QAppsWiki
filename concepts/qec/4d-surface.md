---
type: concept
name: $(2,2)$ Loop toric code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Kitaev tesseract code
- 4D surface code
- All-loop toric code
- $(2,2)$ 4D toric code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-surface
- concepts/qec/4d-stabilizer
- concepts/qec/double-homological-product
- concepts/qec/higher-dimensional-surface
- concepts/qec/multisector-hypergraph
- concepts/qec/single-shot
- concepts/qec/surface
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/4d_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 4d_surface
---

# $(2,2)$ Loop toric code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/4d_surface) (`code_id: 4d_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A generalization of the Kitaev surface code defined on a 4D lattice.
The code is called a $(2,2)$ toric code because it admits 2D membrane $Z$-type and $X$-type logical operators.
Both types of operators create 1D (i.e., loop) excitations at their edges.
The code serves as a self-correcting quantum memory  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:0811.0033](https://arxiv.org/abs/0811.0033)).

The open-boundary hypercubic realization is often called the *tesseract code*.
It can be formulated using relative homology and encodes one logical qubit, in contrast to the six logical qubits of the periodic 4D toric code  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).

Qubits are placed on plaquettes, each $Z$-type stabilizer generator is supported on six plaquettes surrounding an edge, and $X$-type stabilizers are placed on the six plaquettes of every cube  ([arXiv:2010.02238](https://arxiv.org/abs/2010.02238)).

*Loop toric code* often either refers to the construction on
the 4D torus or is an alternative name for the general
construction.

The construction has been extended to modular qudits  ([arXiv:2112.02137](https://arxiv.org/abs/2112.02137)).

(source: raw/error-correction-zoo.md)

## Protection

Code parameters for an open hypercubic lattice of side-length $L$ are $⟦6L^4 − 12L^3 + 10L^2 - 4L + 1, 1, L^2⟧$  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286), [arXiv:2408.08865](https://arxiv.org/abs/2408.08865)).
In the open-boundary/tesseract realization, all bulk stabilizer generators have weight six and each qubit participates in eight stabilizer checks  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).

## Rate

For the open-boundary tesseract family, $k=1$ and $n=6d^2-12d^{3/2}+10d-4\sqrt{d}+1$ because $d=L^2$ and $n=6L^4-12L^3+10L^2-4L+1$  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).

## Encoders

- Lindbladian-based dissipative encoding, for which codespace is steady-state space of a Lindbladian  ([arXiv:1010.2901](https://arxiv.org/abs/1010.2901)).

## Transversal gates

- Only logical Clifford gates can be implemented transversally when defined on a hypercubic lattice  ([arXiv:2010.02238](https://arxiv.org/abs/2010.02238)).

## General gates

- Logical $S$ gate using physical $CS$ gates via the Pontryagin square  ([arXiv:2112.02137](https://arxiv.org/abs/2112.02137)).
- On a hypercubic lattice, electromagnetic duality implements a logical Hadamard gate  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).
- On closed 4-manifolds, the gauged-SPT operator $i^{\int \mathcal{P}(a)}$ realizes logical $CZ$ gates on $T^4$ and a logical $S$ gate on $\mathbb{CP}^2$  ([arXiv:2405.11719](https://arxiv.org/abs/2405.11719)).
- Single-shot lattice surgery for the 4D loop toric code can be formulated using the fault-complex formalism  ([arXiv:2410.12963](https://arxiv.org/abs/2410.12963)).

## Decoders

- A local recovery procedure that dispenses with fast classical processing, and can even be formulated without explicit measurements, is possible when the code is realized in four or more spatial dimensions  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143)).
- Single-shot repair-syndrome decoder for the open-boundary/tesseract code, followed by RG decoding on the repaired syndrome  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).
- Local automaton decoder  ([arXiv:1609.00510](https://arxiv.org/abs/1609.00510)) based on Toom's rule for the classical 2D repetition code  ([doi:10.1007/978-1-4612-2168-5_18](https://doi.org/10.1007/978-1-4612-2168-5_18), [doi:10.1147/rd.481.0005](https://doi.org/10.1147/rd.481.0005)).
- Local automaton decoder obtained from reinforcement learning  ([arXiv:2408.09524](https://arxiv.org/abs/2408.09524)).

## Code capacity threshold

- Independent $X,Z$ noise: $2.117\%$ with Hastings decoder  ([arXiv:1609.00510](https://arxiv.org/abs/1609.00510)) and $7.3\%$ with RG decoder for the open-boundary 4D tesseract code  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)). It is conjectured via a statistical-mechanical mapping that the optimal ML decoder yields a threshold of $11.003\%$  ([arXiv:hep-th/0310279](https://arxiv.org/abs/hep-th/0310279)).

## Threshold

- Phenomenological noise model for the open-boundary 4D tesseract code: $4.35\%$ with RG decoder  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)), and $4.3\%$ under improved BP-OSD decoder  ([arXiv:2206.03122](https://arxiv.org/abs/2206.03122)).
- Gate-based depolarizing noise: $0.31\%$ with RG decoder for the open-boundary 4D tesseract code  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).
- $1.59\%$ for independent $X,Z$ noise and faulty syndrome measurements using the Hastings decoder  ([arXiv:1609.00510](https://arxiv.org/abs/1609.00510)).

## Realizations

- Trapped ions: single-shot QEC realized using a $⟦33,1,4⟧$ rotated version of the loop toric code on the Quantinuum H2 device  ([arXiv:2408.08865](https://arxiv.org/abs/2408.08865)).

## Relations

- _parent_: [[concepts/qec/higher-dimensional-surface]] — The 4D loop toric code realizes 4D $\mathbb{Z}_2$ gauge theory with only loop excitations  ([arXiv:2112.02137](https://arxiv.org/abs/2112.02137)).
- _parent_: [[concepts/qec/4d-stabilizer]]
- _parent_: [[concepts/qec/single-shot]] — Single-shot QEC has been realized using the $⟦33,1,4⟧$ loop toric code on the Quantinuum H2 device  ([arXiv:2408.08865](https://arxiv.org/abs/2408.08865)).
- _parent_: [[concepts/qec/topological-abelian]] — The 4D loop toric code realizes 4D $\mathbb{Z}_2$ gauge theory with only loop excitations  ([arXiv:2112.02137](https://arxiv.org/abs/2112.02137)).
- _cousin_: [[concepts/qec/multisector-hypergraph]] — The 4D loop planar (toric) code on a hypercubic lattice can be obtained from a particular choice of chain complex from a hypergraph product of four repetition codes  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The 4D loop planar (toric) code on a hypercubic lattice can be obtained from a particular choice of chain complex from a hypergraph product of four repetition codes  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).
- _cousin_: [[concepts/qec/double-homological-product]] — The 4D loop planar (toric) code on a hypercubic lattice can be obtained from a particular choice of chain complex from a hypergraph product of four repetition codes  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)). As such, it is a particular Campbell double homological product code  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)).
- _cousin_: [[concepts/qec/3d-surface]] — Setting one linear size of the open-boundary tesseract construction to $1$ yields the cubic/3D surface code  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).
- _cousin_: [[concepts/qec/surface]] — Setting $L_2=L_4=1$ in the open-boundary tesseract construction yields the planar surface code  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).
