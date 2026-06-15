---
type: concept
name: Spin code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qecc-finite
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/spins_into_spins
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: spins_into_spins
---

# Spin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/spins_into_spins) (`code_id: spins_into_spins`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes a $K$-dimensional Hilbert space into a tensor-product or direct sum of factors, with each factor spanned by states of a quantum mechanical spin or, more generally, an irreducible representation of a compact Lie group.

In the simplest case of a single-spin $SU(2)$ system, the canonical states $|^J_m\rangle$ of a single $2J+1$-dimensional factor are labeled by total angular momentum $J$ (either integer or half-integer) and its $z$-axis projection $m$.
There can be multiple factors of the same size, as in the case of atomic or molecular state spaces, and the number of factors can be infinite.
In contrast to other qudit codes, spin codes are closely associated with the angular momentum Lie algebra and/or $SU(2)$, $SO(3)$, or more general Lie groups.

(source: raw/error-correction-zoo.md)

## Protection

Codes can be designed to protect against rotations by small angles, which effectively means they protect against low-order products of powers of the Lie algebra generators.
In the molecular ($SU(2)$) setting, there is a larger basis of error operators causing changes in the total angular momentum $J$ and its projection $m$ and modeling processes such as spontaneous emission, stray electromagnetic fields, and Raman scattering  ([arXiv:2311.12324](https://arxiv.org/abs/2311.12324)).

## Relations

- _parent_: [[concepts/qec/qecc-finite]]
