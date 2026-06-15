---
type: concept
name: Clifford group-representation QSC
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
- https://errorcorrectionzoo.org/c/clifford_qsc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: clifford_qsc
---

# Clifford group-representation QSC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/clifford_qsc) (`code_id: clifford_qsc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Non-uniform QSC whose projection is onto a copy of an irreducible representation of the single-qubit Clifford group, taken as the binary octahedral subgroup of the group $SU(2)$ of Gaussian rotations.
Its codewords consist of non-uniform superpositions of 40 coherent states drawn from a 48-element Clifford-group orbit.

(source: raw/error-correction-zoo.md)

## General gates

- The single-qubit Clifford group can be realized via Gaussian rotations. The $T$ and $CZ$ gates can be realized using quartic Kerr operations  ([arXiv:2306.11621](https://arxiv.org/abs/2306.11621)).

## Relations

- _parent_: [[concepts/qec/qsc]] — The Clifford group-representation QSC has non-uniform coefficients.
- _parent_: [[concepts/qec/group-representation]] — The Clifford group-representation QSC is a group-representation code with $G$ being single-qubit Clifford group, taken as the binary octahedral subgroup of the group $SU(2)$ of Gaussian rotations.
