---
type: concept
name: 2D hyperbolic surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hyperbolic-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/two_dimensional_hyperbolic_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: two_dimensional_hyperbolic_surface
---

# 2D hyperbolic surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/two_dimensional_hyperbolic_surface) (`code_id: two_dimensional_hyperbolic_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Hyperbolic surface codes based on a tessellation of a closed 2D manifold with a hyperbolic geometry (i.e., non-Euclidean geometry, e.g., saddle surfaces when defined on a 2D plane).

For a tessellation involving regular polygons with $ r $ sides and $ s $ polygons meeting at each vertex, the number of logical qubits is given by $ k = (1-2/r - 2/s) n + 2 $.
Some possible tilings include $ \{r,s\}: \{7,3\}, \{5,4\} $.
The weights of the stabilizer generators depend on the tiling, with $\{5,4\}$ having lower weight than $\{7,3\}$.

A *semi-hyperbolic surface code*  ([arXiv:1703.00590](https://arxiv.org/abs/1703.00590)) is a code defined on a $\{4,s\}$ tiling, but where each square is replaced with a square region of a 2D lattice.

(source: raw/error-correction-zoo.md)

## Protection

Protects against Pauli errors with distance $ d \propto \log(n) $. Code parameters are $ ⟦n, (1-2/r - 2/s)  n + 2, O(\log n) ⟧ $

## Rate

2D hyperbolic surface codes have an asymptotically constant encoding rate $ k/n $ with a distance scaling logarithmically with $ n$ when the surface is closed. The encoding rate depends on the tiling $ {r,s} $ and is given by $ k/n = (1-2/r - 2/s) + 2/n $, which approaches a constant value as the number of physical qubits grows. The weight of the stabilizers is $ r $ for $ Z $-checks and $ s $ for $ X $-checks. For open boundary conditions, the code reduces to constant distance.

## Decoders

- Due to the symmetries of hyperbolic surface codes, optimal measurement schedules of the stabilizers can be found  ([arXiv:2010.09626](https://arxiv.org/abs/2010.09626)).
- Bounds on code capacity thresholds using ML decoding can be obtained by mapping the effect of noise on the code to a statistical mechanical model  ([arXiv:1804.01950](https://arxiv.org/abs/1804.01950)).
- Two flag-based decoders  ([arXiv:2409.14283](https://arxiv.org/abs/2409.14283)).

## Code capacity threshold

- Bounds on code capacity thresholds using ML decoding can be obtained by mapping the effect of noise on the code to a statistical mechanical model  ([arXiv:1805.00644](https://arxiv.org/abs/1805.00644)).
- $1.3\%$ for a phenomenological noise model for the $\{4,5\}$-hyperbolic surface code  ([arXiv:1703.00590](https://arxiv.org/abs/1703.00590)).

## Threshold

- 1$\%$ - 5$\%$ for a ${5,4}$ tiling under minimum-weight decoding  ([arXiv:1208.2317](https://arxiv.org/abs/1208.2317)). For larger tilings, the lower bound on the distance decreases, suggesting the threshold will also decrease.

## Relations

- _parent_: [[concepts/qec/hyperbolic-surface]]

## Notes

- See  ([arXiv:2103.06309](https://arxiv.org/abs/2103.06309)) for a description of this code.
- Connection to percolation theory as shown in  ([arXiv:1205.7036](https://arxiv.org/abs/1205.7036)).
- A database of 2D hyperbolic surface codes is available in QECDB , where the surface codes form the subset of non-self-dual codes.
