---
type: concept
name: Pauli tessellation QSC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-representation
- concepts/qec/qsc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/pauli_qsc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: pauli_qsc
---

# Pauli tessellation QSC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/pauli_qsc) (`code_id: pauli_qsc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Two-mode non-uniform QSC whose projection is onto a copy of an irreducible representation of the single-qubit Pauli group, realized geometrically by the $\{2,2,4\}$ tessellation of the sphere  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).
For the canonical choice in the paper, each logical codeword is a $\pm 1$ superposition of four vertices of a cube, i.e., of one tetrahedron in the cube decomposition.

(source: raw/error-correction-zoo.md)

## Protection

For the $\theta_0=\arccos(1/\sqrt{3})$, $\phi_0=\pi/4$ configuration of Ref.  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)), the code corrects arbitrary spherical rotation errors of angle smaller than $\frac{1}{2}\arccos(1/3)$.
The lowest uncorrectable spherical-harmonic momentum-error pair is $Y_1^{0\dagger}Y_2^{\pm 2}$, so all momentum errors with $\ell \leq 1$ are correctable.

## General gates

- The single-qubit Pauli group is realized by geometric rotations of the sphere, namely $\pi$ rotations for $X$ and $Z$ and a $\pi/2$ rotation for $XZ$  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).

## Relations

- _parent_: [[concepts/qec/qsc]] — The Pauli tessellation QSC has non-uniform $\pm 1$ coefficients.
- _parent_: [[concepts/qec/group-representation]] — The Pauli tessellation QSC is a group-representation code with $G$ being the single-qubit Pauli group.
- _cousin_: [`simplex_spherical`](https://errorcorrectionzoo.org/c/simplex_spherical) — Each codeword of the Pauli tessellation QSC is a quantum superposition of vertices of a tetrahedron with $\pm 1$ coefficients.
