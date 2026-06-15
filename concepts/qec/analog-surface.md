---
type: concept
name: Analog surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $\mathbb{R}$ gauge theory code
- Continuous-variable (CV) surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/ame
- concepts/qec/analog-stabilizer
- concepts/qec/oscillator-css
- concepts/qec/qudit-surface
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/analog_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: analog_surface
---

# Analog surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/analog_surface) (`code_id: analog_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An analog CSS version of the Kitaev surface code realizing a phase of 2D $\mathbb{R}$ gauge theory.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/analog-stabilizer]]
- _parent_: [[concepts/qec/oscillator-css]]
- _parent_: [[concepts/qec/2d-stabilizer]]
- _cousin_: [[concepts/qec/ame]] — Analog surface-code states are $3$-uniform  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).
- _cousin_: [[concepts/qec/qudit-surface]] — The analog surface code can be thought of as a realization of the $q\to\infty$ $\mathbb{R}$ oscillator limit  ([arXiv:1709.04460](https://arxiv.org/abs/1709.04460)) of the qudit surface code as a bosonic stabilizer code.
- _cousin_: [[concepts/qec/topological-abelian]] — The analog surface code realizes a straightforward extension of the modular-qudit surface code to infinite local dimension, $q\to\infty$  ([arXiv:1709.04460](https://arxiv.org/abs/1709.04460)).
The code realizes a phase of 2D $\mathbb{R}$ gauge theory.
There are two types of anyons, $e$ and $m$, with each type being valued in a continuous domain as opposed to $\mathbb{Z}_q$ for the qudit surface code.

## Notes

- See  ([arXiv:1302.3428](https://arxiv.org/abs/1302.3428)) for an exposition.
