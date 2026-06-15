---
type: concept
name: Hyperbolic tessellation code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/gkp-concatenated
- concepts/qec/group-representation
- concepts/qec/homogeneous-space-quantum
- concepts/qec/pauli-qsc
- concepts/qec/qutrit-pauli-gkp-subcode
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tesselation
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tesselation
---

# Hyperbolic tessellation code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tesselation) (`code_id: tesselation`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Homogeneous-space code whose codewords are superpositions of positional delta functions on the hyperbolic plane.
The positions are chosen according to regular triangle tessellations, and the code projector picks out an irreducible representation of the corresponding proper triangle group.
 
Examples in Ref.  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)) are the $\{5,5,5\}$ tessellation realizing the Pauli group of a five-dimensional qudit, the $\{6,4,8\}$ tessellation realizing the single-qubit Clifford group, and the $\{4,3,5\}$ tessellation realizing the binary icosahedral group $2I$.

(source: raw/error-correction-zoo.md)

## Protection

Protects against sufficiently small position and momentum shifts on the hyperbolic plane.
In the three explicit examples of Ref.  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)), position-translation errors are correctable up to resolutions $d_x \approx 1.6169$, $0.6605$, and $0.5011$, respectively.
Momentum errors are represented by hyperbolic Laplacian eigenfunctions; the $\{5,5,5\}$ example corrects all modes with angular index $n<5$, and more generally the compact quotient $\mathbb{H}^2/\Gamma$ provides a nonzero Laplacian gap that acts as a momentum-error distance scale.

## General gates

- Logical operations are realized by rotations around selected vertices of the hyperbolic tessellation. In the $\{6,4,8\}$ example, $S$ and $U$ are implemented by $\pi/4$ and $\pi/3$ rotations, while the $\{4,3,5\}$ example realizes binary-icosahedral non-Clifford gates by $2\pi/3$ and $2\pi/5$ rotations  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).

## Relations

- _parent_: [[concepts/qec/homogeneous-space-quantum]] — Hyperbolic tessellation codes are defined on the space of functions on the hyperbolic plane, the symmetric space $G/H$ for $G = SO(2,1)$ the proper Lorentz group and $H = O(2)$.
- _parent_: [[concepts/qec/group-representation]] — Hyperbolic tessellation-code projections are onto a copy of an irreducible representation of the proper triangle group associated with the tessellation, and the resulting logical gates are implemented geometrically by hyperbolic rotations  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).
- _cousin_: [`hyperbolic`](https://errorcorrectionzoo.org/c/hyperbolic) — Hyperbolic tessellation codes are quantum counterparts of hyperbolic sphere packings because they store information in quantum superpositions of points on the hyperbolic plane.
- _cousin_: [[concepts/qec/pauli-qsc]] — The tessellation-code framework spans spherical, Euclidean, and hyperbolic geometries; the Pauli tessellation QSC is the spherical member  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).
- _cousin_: [[concepts/qec/qutrit-pauli-gkp-subcode]] — The qutrit-Pauli tessellation code is the Euclidean $\{3,3,3\}$ member of the same curvature-dependent tessellation-code framework  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).
- _cousin_: [[concepts/qec/gkp-concatenated]] — The qubit-Pauli tessellation GKP code  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)) is the Euclidean $\{2,4,4\}$ member of the curvature-dependent tessellation-code framework. It is a two-mode code in which each Cartesian direction is a single-mode qubit GKP code, making the full code a 2-to-1 concatenated qubit encoding. The logical single-qubit Pauli group is implemented geometrically by one $\pi$ rotation and two $\pi/2$ rotations on the Euclidean tessellation  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).
