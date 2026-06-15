---
type: concept
name: Landau-level spin code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/homogeneous-space-quantum
- concepts/qec/single-spin
- concepts/qec/spin-gkp
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/landau_level
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: landau_level
---

# Landau-level spin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/landau_level) (`code_id: landau_level`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Approximate quantum code that encodes a qudit in the finite-dimensional Hilbert space of a single spin, i.e., a spherical Landau level.
Codewords are approximately orthogonal spin coherent states whose orientations are spaced maximally far apart along a great circle (equator) of the sphere.
The larger the spin, the better the performance.

(source: raw/error-correction-zoo.md)

## Protection

Protects against equatorial rotational errors acting on the overall spin.

## Relations

- _parent_: [[concepts/qec/single-spin]] — The Landau-level spin code lies in a particular irrep present in the induced representation $\text{Ind}_{U(1)}^{SU(2)} \lambda$, where $\lambda\in \mathbb{Z}$ labels irreps of $U(1)$ and quantifies the monopole strength  ([arXiv:2511.14840](https://arxiv.org/abs/2511.14840)).
- _parent_: [[concepts/qec/approximate-qecc]] — The Landau-level spin code approximately protects against rotational errors.
- _cousin_: [[concepts/qec/homogeneous-space-quantum]] — The Landau-level spin code lies in a particular irrep present in the induced representation $\text{Ind}_{U(1)}^{SU(2)} \lambda$, where $\lambda\in \mathbb{Z}$ labels irreps of $U(1)$ and quantifies the monopole strength  ([arXiv:2511.14840](https://arxiv.org/abs/2511.14840)).
- _cousin_: [[concepts/qec/spin-gkp]] — The Landau-level (spin-GKP) code are both GKP-like encodings expressed as superpositions of (squeezed) spin coherent states.
