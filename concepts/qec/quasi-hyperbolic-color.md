---
type: concept
name: Quasi-hyperbolic color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/color
- concepts/qec/higher-dimensional-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quasi_hyperbolic_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quasi_hyperbolic_color
---

# Quasi-hyperbolic color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quasi_hyperbolic_color) (`code_id: quasi_hyperbolic_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An extension of the color code construction to quasi-hyperbolic 3-manifolds, e.g., a product of a 2D hyperbolic surface and a circle.

(source: raw/error-correction-zoo.md)

## Protection

There exists a quasi-hyperbolic family with rate of order $O(1/\log n)$ and distance of order $O(\log n)$  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)).
These codes support collective logical $CCZ$ gates via transversal $T$ and exponentially many individually addressable, parallelizable logical $CZ$ gates via transversal $S$ on codimension-1 submanifolds  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)).

## Rate

A Torelli mapping-torus construction yields a code with constant rate, although its distance scaling is currently unknown  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)).

## Fault tolerance

- The quasi-hyperbolic family supports collective logical $CCZ$ gates via transversal $T$ and exponentially many individually addressable, parallelizable logical $CZ$ gates via transversal $S$ on codimension-1 submanifolds  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)).

## Relations

- _parent_: [[concepts/qec/color]]
- _cousin_: [[concepts/qec/higher-dimensional-surface]] — Quasi-hyperbolic color codes are related to quasi-hyperbolic surface codes via a constant-depth Clifford circuit  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)).
