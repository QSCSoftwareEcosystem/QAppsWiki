---
type: concept
name: Hemicubic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/distance-balanced
- concepts/qec/higher-dimensional-surface
- concepts/qec/qltc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hemicubic
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hemicubic
---

# Hemicubic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hemicubic) (`code_id: hemicubic`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Homological code constructed out of cubes in high dimensions.
The hemicubic code family has asymptotically diminishing soundness that scales as order $\Omega(1/\log n)$, locality of stabilizer generators scaling as order $O(\log n)$, and distance of order $\Theta(\sqrt{n})$.

(source: raw/error-correction-zoo.md)

## Decoders

- Polynomial-time decoding algorithm that corrects arbitrary errors of size up to the minimum distance multiplied by polylogarithmic factors  ([arXiv:1911.03069](https://arxiv.org/abs/1911.03069)). This was the first polynomial-time decoding algorithm for quantum locally testable codes.

## Relations

- _parent_: [[concepts/qec/higher-dimensional-surface]]
- _cousin_: [[concepts/qec/qltc]] — The hemicubic code family has asymptotically diminishing soundness that scales as order $\Omega(1/\log n)$, locality of stabilizer generators scaling as order $O(\log n)$, and distance of order $\Theta(\sqrt{n})$.
Soundness amplification and AEL distance amplification  ([doi:10.1109/SFCS.1995.492581](https://doi.org/10.1109/SFCS.1995.492581), [doi:10.1109/18.556669](https://doi.org/10.1109/18.556669)) can also yield improvements in various parameters  ([arXiv:2309.05541](https://arxiv.org/abs/2309.05541)).
Application of generalized distance balancing  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)) to hemicubic codes using an asymptotically good classical code of length $t$ yields $O( 1/(\log(n) t^2) )$ soundness and order $\Theta(\sqrt{n}t)$ distance while maintaining locality scaling and at the expense of a dimension scaling as order $\Theta(t^2)$  ([arXiv:2305.00689](https://arxiv.org/abs/2305.00689)).
- _cousin_: [[concepts/qec/distance-balanced]] — Application of generalized distance balancing  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)) to hemicubic codes using an asymptotically good classical code of length $t$ yields $O( 1/(\log(n) t^2) )$ soundness and order $\Theta(\sqrt{n}t)$ distance while maintaining locality scaling and at the expense of a dimension scaling as order $\Theta(t^2)$  ([arXiv:2305.00689](https://arxiv.org/abs/2305.00689)).
- _cousin_: [`hypercube`](https://errorcorrectionzoo.org/c/hypercube) — Hemicubic codes are built from cellulations derived from hypercubes.
