---
type: concept
name: Hyperbolic color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/color
- concepts/qec/hyperbolic-surface
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hyperbolic_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hyperbolic_color
---

# Hyperbolic color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hyperbolic_color) (`code_id: hyperbolic_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An extension of the color code construction to hyperbolic manifolds.
As opposed to there being only three types of uniform three-valent and three-colorable lattice tilings in the 2D Euclidean plane, there is an infinite number of admissible hyperbolic tilings in the 2D hyperbolic plane  ([arXiv:1804.06382](https://arxiv.org/abs/1804.06382)).
Certain double covers of hyperbolic tilings also yield admissible tilings  ([arXiv:1301.6588](https://arxiv.org/abs/1301.6588)).
Other admissible hyperbolic tilings can be obtained via a fattening procedure  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)); see also a construction based on the more general quantum pin codes  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).

(source: raw/error-correction-zoo.md)

## Protection

The use of hyperbolic surfaces allows one to circumvent bounds on code parameters (such as the \term{BPT bound}) that are valid for lattice geometries.
Hyperbolic color codes can have high rate but tend to have small distance.
For example, a $\{4g,4g\}$ tiling with periodic boundary conditions (i.e., a $g$-torus) yields a $⟦4g+8,4g,4⟧$ code family  ([arXiv:1804.06382](https://arxiv.org/abs/1804.06382)).
More examples, such as the $⟦160,20,8⟧$ code on the 4.10.10 tiling, are provided in  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).

## Rate

In the double-cover construction  ([arXiv:1301.6588](https://arxiv.org/abs/1301.6588)), an $\{\ell,m\}$ input tiling yields a code family with an asymptotic rate of $1 - 2/\ell - 2/m$.

## Decoders

- Two flag-based decoders  ([arXiv:2409.14283](https://arxiv.org/abs/2409.14283)).

## Relations

- _parent_: [[concepts/qec/color]]
- _cousin_: [[concepts/qec/hyperbolic-surface]] — Hyperbolic color codes and hyperbolic surface codes are both defined on hyperbolic tilings.
- _cousin_: [[concepts/qec/small-distance-qubit-stabilizer]] — Many hyperbolic color codes have distance $\leq 5$.

## Notes

- A database of 2D hyperbolic color codes is available in QECDB , where the color codes form the subset of self-dual codes.
