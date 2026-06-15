---
type: concept
name: 3D surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- 3D toric code
- 3D cubic code
- Bosonic-charge bosonic-loop (BcBl) surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bacon-shor
- concepts/qec/chamon
- concepts/qec/hamiltonian
- concepts/qec/higher-dimensional-surface
- concepts/qec/multisector-hypergraph
- concepts/qec/qudit-3d-surface
- concepts/qec/rotated-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/3d_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 3d_surface
---

# 3D surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/3d_surface) (`code_id: 3d_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A generalization of the Kitaev surface code defined on a 3D cubic lattice.
Qubits are placed on edges, $Z$-type stabilizer generators are placed on square plaquettes oriented in all three directions, and $X$-type stabilizers are placed on the six edges neighboring every vertex  ([arXiv:1404.4618](https://arxiv.org/abs/1404.4618)).

*3D toric code* often either refers to the construction on
the three-dimensional torus or is an alternative name for the general
construction.
The construction on surfaces with boundaries is often called the
*3D planar code*.
In the open-boundary hypercubic family of  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)), setting one linear dimension of the tesseract construction to $1$ yields a single-qubit *cubic code* that interpolates between the planar surface code and the 4D tesseract code.
There exists a rotated version of the 3D surface code, the *3D rotated surface code*, akin to the (2D) rotated surface code  ([arXiv:2211.02116](https://arxiv.org/abs/2211.02116)).
The *welded surface code*  ([arXiv:1406.4227](https://arxiv.org/abs/1406.4227)) consists of several 3D surface codes stitched together in a way that the distance scales faster than the linear size of the system.
In the rectified picture, three 3D surface codes can be supported on the same rectified cubic lattice, and the corresponding cubic-lattice realization is a gauge choice of the 3D Bacon-Shor code  ([arXiv:1801.04255](https://arxiv.org/abs/1801.04255)).

Related models  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736), [arXiv:1012.0859](https://arxiv.org/abs/1012.0859)) on lattices with certain colorability are equivalent to several copies of the 3D surface code  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).

(source: raw/error-correction-zoo.md)

## Protection

The planar 3D surface code family on a cubic lattice of length $L$ has parameters $⟦2L(L-1)^2+L^3,1,d_X=L^2,d_Z=L⟧$, while the 3D toric code has parameters $⟦3L^3,3,d_X=L^2,d_Z=L⟧$.
Rectangular open-boundary 3D versions furnish single-qubit $⟦71,1,6⟧$, $⟦177,1,9⟧$, $⟦331,1,12⟧$, and $⟦616,1,16⟧$ codes, illustrating an $n\propto 3d^2$ tradeoff between the 2D surface and 4D tesseract families  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).

Stability against Hamiltonian perturbations was determined using a tensor-network representation  ([arXiv:2012.15346](https://arxiv.org/abs/2012.15346)). The phase diagram of the perturbed tensor network maps to that of a 3D Ising gauge theory.

## Transversal gates

- For a stack of three 3D surface codes on the same rectified cubic lattice, pairwise logical $CZ$ and triple logical $CCZ$ gates are transversal  ([arXiv:1801.04255](https://arxiv.org/abs/1801.04255)).

## Decoders

- Flip decoder and its modification p-flip  ([arXiv:2212.06985](https://arxiv.org/abs/2212.06985)).
- Tensor-network decoder  ([arXiv:2310.10722](https://arxiv.org/abs/2310.10722)).
- Efficient MWPM decoder for 3D toric and 3D welded surface codes handling string-like syndromes only  ([arXiv:1808.03092](https://arxiv.org/abs/1808.03092)).
- Generalization of linear-time ML erasure decoder  ([arXiv:1703.01517](https://arxiv.org/abs/1703.01517)) to 3D surface codes  ([arXiv:1808.03092](https://arxiv.org/abs/1808.03092)).
- Equivariant machine learning decoder  ([arXiv:2409.04300](https://arxiv.org/abs/2409.04300)).

## General gates

- There is a CZ gate for the 3D toric code on a Klein bottle $\times S^1$  ([arXiv:2211.11764](https://arxiv.org/abs/2211.11764)).
- Lattice surgery  ([arXiv:1801.04255](https://arxiv.org/abs/1801.04255)).
- Single-shot lattice surgery for the 3D toric/surface code can be formulated using the fault-complex formalism  ([arXiv:2410.12963](https://arxiv.org/abs/2410.12963)).
- 3D and Hybrid 2D-3D surface code computation using lattice surgery and without magic-state distillation  ([arXiv:1801.04255](https://arxiv.org/abs/1801.04255)).
- Fault-tolerant Hadamard gate using teleportation and error correction  ([arXiv:1801.04255](https://arxiv.org/abs/1801.04255)).
- Three distance-$d$ 3D surface/toric codes with open boundaries and cyclically permuted lattice axes admit a logical $CCZ$ gate via transversal physical $CCZ$ gates; concatenating each supporting qubit triple with an $⟦8,3,2⟧$ block yields a $⟦8n,3,2d⟧$ 3D toric/color family whose smallest member has parameters $⟦72,3,4⟧$  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).
- Various inter-code $CZ$ and $CCZ$ gates implemented via constant-depth circuits on stacks or coupled collections of 3D surface/toric codes  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065), [arXiv:1801.04255](https://arxiv.org/abs/1801.04255), [arXiv:2106.05274](https://arxiv.org/abs/2106.05274), [arXiv:2108.00018](https://arxiv.org/abs/2108.00018), [arXiv:2310.16982](https://arxiv.org/abs/2310.16982), [arXiv:2312.09111](https://arxiv.org/abs/2312.09111), [arXiv:2404.05033](https://arxiv.org/abs/2404.05033)), with $CZ$ gates formulated in terms of the slant product  ([arXiv:1509.03626](https://arxiv.org/abs/1509.03626), [arXiv:2208.07367](https://arxiv.org/abs/2208.07367)) or cup product  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)) structures.

## Fault tolerance

- Fault-tolerant Hadamard gate using teleportation and error correction  ([arXiv:1801.04255](https://arxiv.org/abs/1801.04255)).

## Code capacity threshold

- Independent $X,Z$ noise: $12\%$ for bit-flip and $3\%$ for phase-flip channels with MWPM decoder for 3D toric code  ([arXiv:1808.03092](https://arxiv.org/abs/1808.03092)), and $17.2\%$ for the surface-like logical operator together with $3.3\%$ for the line-like logical operator of the 3D cubic code under RG decoding  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).
- Erasure noise: $24.8\%$ with generalization of linear-time ML erasure decoder  ([arXiv:1703.01517](https://arxiv.org/abs/1703.01517)) to 3D surface codes  ([arXiv:1808.03092](https://arxiv.org/abs/1808.03092)). No threshold was observed for the 3D welded surface code  ([arXiv:1808.03092](https://arxiv.org/abs/1808.03092)).

## Threshold

- Phenomenological noise model for the 3D toric code: $2.90(2)\%$ under BP-OSD decoder  ([arXiv:2009.11790](https://arxiv.org/abs/2009.11790)), $7.1\%$ under improved BP-OSD  ([arXiv:2206.03122](https://arxiv.org/abs/2206.03122)), and $2.6\%$ under flip decoder  ([arXiv:2212.06985](https://arxiv.org/abs/2212.06985)). For the line-like logical operator of the 3D cubic code, RG decoding yields $7.3\%$  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)). For 3D surface code: $3.08(4)\%$ under flip decoder  ([arXiv:2009.11790](https://arxiv.org/abs/2009.11790)). Optimal thresholds of $11\%$ under $X$-type and $2\%$ under $Z$-type noise derived in Ref.  ([arXiv:2510.20489](https://arxiv.org/abs/2510.20489)).

## Relations

- _parent_: [[concepts/qec/higher-dimensional-surface]]
- _parent_: [[concepts/qec/qudit-3d-surface]] — The qudit 3D surface code reduces to the 3D surface code for $q=2$. The 3D surface code realizes 3D $\mathbb{Z}_2$ gauge theory with bosonic charge and loop excitations (BcBl). The welded surface code does not satisfy homogeneous topological order  ([arXiv:2009.13551](https://arxiv.org/abs/2009.13551)).
- _cousin_: [[concepts/qec/bacon-shor]] — In the rectified-cubic construction, the resulting cubic-lattice 3D surface codes are particular gauge choices of the 3D Bacon-Shor code  ([arXiv:1801.04255](https://arxiv.org/abs/1801.04255)).
- _cousin_: [[concepts/qec/chamon]] — The 3D planar and toric code on a cubic lattice can be obtained from a hypergraph product of three repetition codes  ([arXiv:2311.01328](https://arxiv.org/abs/2311.01328)) ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)). The Chamon code is an XYZ product of three repetition codes  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).
- _cousin_: [[concepts/qec/rotated-surface]] — There exists a rotated version of the 3D surface code, akin to the (2D) rotated surface code  ([arXiv:2211.02116](https://arxiv.org/abs/2211.02116)).
- _cousin_: [[concepts/qec/hamiltonian]] — Stability of the 3D surface code against Hamiltonian perturbations was determined using a tensor-network representation  ([arXiv:2012.15346](https://arxiv.org/abs/2012.15346)). The phase diagram of the perturbed tensor network maps to that of a 3D Ising gauge theory.
- _cousin_: [[concepts/qec/multisector-hypergraph]] — The 3D planar and toric code on a cubic lattice can be obtained from a hypergraph product of three repetition codes  ([arXiv:2311.01328](https://arxiv.org/abs/2311.01328)) ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The 3D planar and toric code on a cubic lattice can be obtained from a hypergraph product of three repetition codes  ([arXiv:2311.01328](https://arxiv.org/abs/2311.01328)) ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).
