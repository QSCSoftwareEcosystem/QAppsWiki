---
type: concept
name: Compactified $\mathbb{R}$ gauge theory code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/analog-surface
- concepts/qec/homological-cv
- concepts/qec/hypergraph-product
- concepts/qec/qudit-surface
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/compactified_r
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: compactified_r
---

# Compactified $\mathbb{R}$ gauge theory code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/compactified_r) (`code_id: compactified_r`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An integer-homology bosonic CSS code realizing 2D $U(1)$ gauge theory on bosonic modes.
The code can be obtained from the analog surface code by condensing certain anyons  ([arXiv:2411.04993](https://arxiv.org/abs/2411.04993)). 
This results in a pinning of each mode to the space of periodic functions, which is the Hilbert space of a physical rotor, and can be thought of as compactification of the 2D $\mathbb{R}$ gauge theory phase realized by the analog surface code.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/homological-cv]] — The compactified $\mathbb{R}$ gauge theory code realizes $U(1)$ gauge theory on bosonic modes.
- _parent_: [[concepts/qec/2d-stabilizer]]
- _parent_: [[concepts/qec/topological-abelian]] — The compactified $\mathbb{R}$ gauge theory code can be obtained from the analog surface code by condensing certain anyons  ([arXiv:2411.04993](https://arxiv.org/abs/2411.04993)). This results in a pinning of each mode to the space of periodic functions, which is the Hilbert space of a physical rotor, and can be thought of as compactification of the 2D $\mathbb{R}$ gauge theory phase realized by the analog surface code.
- _cousin_: [[concepts/qec/analog-surface]] — The compactified $\mathbb{R}$ gauge theory code can be obtained from the analog surface code by condensing certain anyons  ([arXiv:2411.04993](https://arxiv.org/abs/2411.04993)). This results in a pinning of each mode to the space of periodic functions, which is the Hilbert space of a physical rotor, and can be thought of as compactification of the 2D $\mathbb{R}$ gauge theory phase realized by the analog surface code.
- _cousin_: [[concepts/qec/qudit-surface]] — The compactified $\mathbb{R}$ gauge theory code can be thought of as a realization of the $q\to\infty$ $U(1)$ rotor limit  ([arXiv:1709.04460](https://arxiv.org/abs/1709.04460)) of the qudit surface code as a bosonic stabilizer code.
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The compactified $\mathbb{R}$ gauge theory code is constructed from a hypergraph product of two repetition codes over the integers.
- _cousin_: [[concepts/qec/hypergraph-product]] — The compactified $\mathbb{R}$ gauge theory code is constructed from a hypergraph product of two repetition codes over the integers.
