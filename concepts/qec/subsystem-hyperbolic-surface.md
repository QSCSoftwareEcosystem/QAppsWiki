---
type: concept
name: Subsystem hyperbolic surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/subsystem-higher-dimensional-surface
- concepts/qec/two-dimensional-hyperbolic-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_hyperbolic_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_hyperbolic_surface
---

# Subsystem hyperbolic surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_hyperbolic_surface) (`code_id: subsystem_hyperbolic_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Subsystem generalization of the surface code on a 2D hyperbolic tessellation with gauge-group generators of weight at most three.
An $\{r,4\}$ hyperbolic tessellation with $E$ edges yields a $⟦3E/2,(1/2-2/r)E+2,(1-2/r)E,d⟧$ subsystem code.

(source: raw/error-correction-zoo.md)

## Protection

Distance $d$ is bounded between $d_X/2$ and $d_X$, where $d_X$ is the $X$-distance of the subspace hyperbolic surface code derived from the same tessellation  ([arXiv:2010.09626](https://arxiv.org/abs/2010.09626)).

## Relations

- _parent_: [[concepts/qec/subsystem-higher-dimensional-surface]]
- _cousin_: [[concepts/qec/two-dimensional-hyperbolic-surface]] — Subsystem hyperbolic surface codes are subsystem versions of 2D hyperbolic surface codes.
