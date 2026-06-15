---
type: concept
name: Integer-homology bosonic CSS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-homological-product-css
- concepts/qec/homological-rotor
- concepts/qec/oscillator-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/homological_cv
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: homological_cv
---

# Integer-homology bosonic CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/homological_cv) (`code_id: homological_cv`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A bosonic stabilizer code whose physical modes have been restricted, via a single GKP stabilizer, from the space of functions on the real line to the space of periodic functions.
This restriction effectively realizes a rotor on each physical mode, allowing one to construct homological rotor codes out of displacement stabilizer groups.
The stabilizer group is continuous, but contains discrete components in the form of the single-mode GKP stabilizers.
The homology group of the logical operators has a torsion component because the chain complexes are defined over the ring of integers, which yields codes with finite logical dimension.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/oscillator-css]] — Integer-homology bosonic CSS codes are constructed from chain complexes over the integers and realize homological rotor codes out of continuous displacement stabilizer groups. The stabilizer group is continuous, but contains discrete components in the form of the single-mode GKP stabilizers.
- _parent_: [[concepts/qec/generalized-homological-product-css]] — Integer-homology bosonic CSS codes are constructed from chain complexes over the integers and realize homological rotor codes out of continuous displacement stabilizer groups. The homology group of the logical operators has a torsion component because the chain complexes are defined over the ring of integers, which yields codes with finite logical dimension.
- _cousin_: [[concepts/qec/homological-rotor]] — Integer-homology bosonic CSS codes are constructed from chain complexes over the integers and realize homological rotor codes out of continuous displacement stabilizer groups  ([arXiv:2411.04993](https://arxiv.org/abs/2411.04993)).
