---
type: concept
name: Diatomic molecular code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/homogeneous-space-quantum
- concepts/qec/molecular
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/diatomic_molecular
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: diatomic_molecular
---

# Diatomic molecular code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/diatomic_molecular) (`code_id: diatomic_molecular`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Approximate quantum code that encodes a qudit in the infinite-dimensional Hilbert space of a rigid body with $SO(2)$ symmetry, e.g., a heteronuclear diatomic molecule.
The physical space is $L^2(S^2)$, equivalently the orientation space $SO(3)/SO(2)$ of a linear rotor, consisting of a direct sum of all non-negative integer angular momenta.
Ideal codewords may not be normalizable because the space is infinite-dimensional, so approximate versions have to be constructed in practice.

Construction is based on nested subgroups $H\subset K \subset SO(3)$, where $H,K$ are finite.
Codewords consist of orbits of particular position states under $H$, while some elements of $K$ can cycle between codewords.

(source: raw/error-correction-zoo.md)

## Protection

Protects against sufficiently small rotations about any axis and small kicks in angular momentum.
In the simplest cyclic family, angular-momentum kicks with $\ell<N/2$ are correctable.
But unlike molecular codes on $SO(3)$, these codes cannot in general protect against arbitrary products of such rotations and kicks because the underlying state space $S^2$ is not a group and rotations on $S^2$ have fixed points.

## Relations

- _parent_: [[concepts/qec/homogeneous-space-quantum]] — Diatomic molecular codes are defined on the space of orientations of a heteronuclear diatomic molecule, equivalently the space of normalizable functions on the two-sphere homogeneous space $SO(3)/SO(2)=S^2$.
- _cousin_: [[concepts/qec/molecular]] — Molecular codes live on $SO(3)$ for asymmetric rigid bodies, whereas diatomic molecular codes live on the homogeneous space $S^2=SO(3)/SO(2)$ for linear rotors.
