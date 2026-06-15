---
type: concept
name: Renormalization group (RG) cat code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/coherent-constellation
- concepts/qec/holographic
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rg_cat
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rg_cat
---

# Renormalization group (RG) cat code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rg_cat) (`code_id: rg_cat`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose codespace is spanned by $q$ field-theoretic coherent states which are flowing under the renormalization group (RG) flow of massive free fields. The code approximately protects against displacements that represent local (i.e., short-distance, ultraviolet, or UV) operators. Intuitively, this is because RG cat codewords represent non-local (i.e., long-distance) degrees of freedom, which should only be excitable by acting on a macroscopically large number of short-distance degrees of freedom.

(source: raw/error-correction-zoo.md)

## Protection

Approximately protects against displacements that represent ultraviolet coherent operators, i.e., short-distance degrees of freedom of the field theory.

## Relations

- _parent_: [[concepts/qec/coherent-constellation]]
- _parent_: [[concepts/qec/holographic]] — The RG cat code encoder has coarse-graining features reminiscent of holography  ([arXiv:2012.14001](https://arxiv.org/abs/2012.14001)).
- _parent_: [[concepts/qec/approximate-qecc]] — RG cat codes approximately protect against displacements that represent ultraviolet coherent operators.
