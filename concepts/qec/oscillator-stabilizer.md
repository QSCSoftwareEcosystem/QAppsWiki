---
type: concept
name: Bosonic stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- CV stabilizer code
- Oscillator stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/oscillators
- concepts/qec/stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/oscillator_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: oscillator_stabilizer
---

# Bosonic stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/oscillator_stabilizer) (`code_id: oscillator_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Bosonic code whose codespace is defined as the common $+1$ eigenspace of a group of mutually commuting displacement operators.
Displacements form the stabilizers of the code, and have continuous eigenvalues, in contrast with the discrete set of eigenvalues of qubit stabilizers.
As a result, exact codewords are non-normalizable, so approximate constructions have to be considered.
Stabilizer groups are any locally compact Abelian subgroups of $\mathbb{R}^n$, can themselves contain discrete or continuous subgroups, and can admit logical qudit and/or oscillator logical subspaces.

Stabilizer codewords encoding a finite-dimensional codespace admit a discrete infinite stabilizer group and encode quantum information in a lattice.
Such qudit-into-oscillator stabilizer codes are GKP and multimode GKP codes.

Stabilizer codewords encoding a logical oscillator (i.e., CV quantum information) admit either a discrete or a continuous stabilizer group.
The former, called oscillator-into-oscillator GKP codes, are obtained from multimode GKP codes by removing stabilizer generators for some of the modes.
The latter encode information in hyperplanes and can be defined in terms of the continuous group's Lie algebra, i.e., as the common $0$-eigenvalue eigenspace of mutually commuting linear combinations of oscillator position and momentum operators called *nullifiers*  ([arXiv:0903.3233](https://arxiv.org/abs/0903.3233)) or *annihilators*. An oscillator-into-oscillator stabilizer code encoding $k$ logical modes into $n$ physical modes is denoted as $⟦n,k,d⟧_{\mathbb{R}}$, where $d$ is the code's distance.

(source: raw/error-correction-zoo.md)

## Protection

Protective properties can be delineated in terms of the nullifiers or displacements, and the most natural noise model for such codes is displacement noise. If an error operator does not commute with a stabilizer group element, then that error is detectable. Oscillator-into-oscillator stabilizer codes protect against erasures of a subset of modes, while GKP codes protect against sufficiently small displacements in any number of modes.

## General gates

- General gates can be done using the bosonic analogue of gate teleportation  ([arXiv:quant-ph/0208022](https://arxiv.org/abs/quant-ph/0208022)).

## Relations

- _parent_: [[concepts/qec/oscillators]]
- _parent_: [[concepts/qec/stabilizer]]
