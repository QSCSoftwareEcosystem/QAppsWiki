---
type: concept
name: Haah cubic code (CC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-color
- concepts/qec/3d-surface
- concepts/qec/4d-surface
- concepts/qec/cluster-state
- concepts/qec/generalized-bicycle
- concepts/qec/lifted-product
- concepts/qec/qldpc
- concepts/qec/qudit-cubic
- concepts/qec/sierpinsky-fractal-liquid
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/haah_cubic
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: haah_cubic
---

# Haah cubic code (CC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/haah_cubic) (`code_id: haah_cubic`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 3D lattice stabilizer code on a length-$L$ cubic lattice with one or two qubits per site.
Admits two types of stabilizer generators with support on each cube of the lattice.
In the non-CSS case, these two are related by spatial inversion.
For CSS codes, we require that the product of all corner operators is the identity.
We lastly require that there are no non-trivial string operators, meaning that single-site operators are a phase, and any period one logical operator $l \in \mathsf{S}^{\perp}$ is just a phase.

Haah showed in his original construction that there is exactly one non-CSS code of this form, and 17 CSS codes  ([arXiv:1101.1962](https://arxiv.org/abs/1101.1962)).
The non-CSS code is labeled code 0, and the rest are numbered from 1 - 17.
Codes CC1-CC4, CC7, CC8, and CC10 do not have string logical operators  ([arXiv:1101.1962](https://arxiv.org/abs/1101.1962), [arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).
The original cubic code in this family can be obtained by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) a fractal-symmetry Ising model  ([arXiv:1603.05182](https://arxiv.org/abs/1603.05182)); related fracton gauging constructions also appear in  ([arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182)).

Under renormalization group flow  ([arXiv:1310.4507](https://arxiv.org/abs/1310.4507)), cubic code 1 fragments into itself and the *Haah B-code* (a.k.a. *CC1B*), which has four qubits per unit cell  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)) ([arXiv:1909.12304](https://arxiv.org/abs/1909.12304)).
In this context, cubic code 1 is sometimes called the *Haah A-code* or *CC1A*.
Cubic codes 11-17 fragment into combinations of themselves, their corresponding B-codes, and stacks of surface codes  ([arXiv:1909.12304](https://arxiv.org/abs/1909.12304)).

The Haah A-code can be written in a similar form as the Sierpinski prism model code  ([arXiv:2112.14717](https://arxiv.org/abs/2112.14717)).
The Haah B-code admits a topological defect network construction out of two copies of the 3D surface code  ([arXiv:2002.05166](https://arxiv.org/abs/2002.05166)).

Encodings using geometries with boundaries as well as lattice defects have been studied  ([arXiv:2308.00138](https://arxiv.org/abs/2308.00138)).
CC1A and CC1B have been generalized to manifolds more general than 3D lattices  ([arXiv:1812.02101](https://arxiv.org/abs/1812.02101), [arXiv:1902.04543](https://arxiv.org/abs/1902.04543)).

(source: raw/error-correction-zoo.md)

## Protection

Cubic codes protect against simultaneous independent Pauli errors on different sites (not qubits, since there can be 2 qubits per site). Codes CC0-CC4 are known to have distance $d \ge L$, meaning they can achieve macroscopic code distance as $L\to\infty$.

## Decoders

- Hard-decisions RG decoder  ([arXiv:1112.3252](https://arxiv.org/abs/1112.3252)).
- BP-OSD decoder  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703)).

## Threshold

- The encoding rate depends on the code implemented, but code CC0 has been shown to have $k \ge L$ on a periodic finite cubic lattice of side length $L$. In general, we expect the number of logical qubits to scale as $k = \Omega(L)$.

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/qudit-cubic]]
- _cousin_: [[concepts/qec/surface]] — Under renormalization group flow  ([arXiv:1310.4507](https://arxiv.org/abs/1310.4507)), cubic codes 11-17 fragment into combinations of themselves, their corresponding B-codes, and stacks of surface codes  ([arXiv:1909.12304](https://arxiv.org/abs/1909.12304)).
- _cousin_: [[concepts/qec/3d-surface]] — The Haah B-code admits a topological defect network construction out of two copies of the 3D surface code  ([arXiv:2002.05166](https://arxiv.org/abs/2002.05166)).
- _cousin_: [[concepts/qec/3d-color]] — The 3D color and cubic code families both include 3D codes that do not admit string-like operators.
- _cousin_: [[concepts/qec/4d-surface]] — The energy of any partial implementation of CC1 is proportional to the boundary length, similar to the 4D toric code. This can potentially suppress the effects of thermal errors, but it is currently an open problem.
- _cousin_: [[concepts/qec/generalized-bicycle]] — A GB code for the group $G=\mathbb{Z}_{L}^{\times 3}$ is a cubic code  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068)).
- _cousin_: [[concepts/qec/cluster-state]] — A short-range entangled cluster-state model with fractal $X$-type symmetries on both sublattices can be built from the cubic-code gauging data. Gauging one sublattice yields, up to a local circuit, either the cubic code or its ungauged fractal-symmetry Ising model, while gauging both sublattices returns the cluster model up to local swaps and Hadamards  ([arXiv:1603.05182](https://arxiv.org/abs/1603.05182)).
- _cousin_: [[concepts/qec/lifted-product]] — A lifted-product code constructed with coefficients in the ring $R=\mathbb{F}_2[x,y,z]/(x^L-1,y^L-1,z^L-1)$ is a cubic code  ([arXiv:2111.03654](https://arxiv.org/abs/2111.03654)).
- _cousin_: [[concepts/qec/sierpinsky-fractal-liquid]] — The Haah A-code can be written in a similar form as the Sierpinski prism model code  ([arXiv:2112.14717](https://arxiv.org/abs/2112.14717)).
