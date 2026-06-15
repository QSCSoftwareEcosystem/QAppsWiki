---
type: concept
name: Freedman-Meyer-Luo code
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
- https://errorcorrectionzoo.org/c/freedman_meyer_luo
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: freedman_meyer_luo
---

# Freedman-Meyer-Luo code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/freedman_meyer_luo) (`code_id: freedman_meyer_luo`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Hyperbolic surface code constructed using cellulation of a Riemannian Manifold $M$ exhibiting systolic freedom  ([doi:10.2140/gtm.1999.2.113](https://doi.org/10.2140/gtm.1999.2.113)). Codes derived from such manifolds can achieve distances scaling better than $\sqrt{n}$, something that is impossible using closed 2D surfaces or 2D surfaces with boundaries  ([doi:10.1063/1.4726034](https://doi.org/10.1063/1.4726034)). Improved codes are obtained by studying a weak family of Riemann metrics on closed 4-dimensional manifolds $S^2\otimes S^2$ with the $\mathbb{Z}_2$-homology.

(source: raw/error-correction-zoo.md)

## Protection

4D manifolds with weak systolic freedom yield $⟦n,2,\Omega(\sqrt{n \sqrt{\log n}})⟧$ surface codes.

## Rate

Codes held a 20-year record the best lower bound on asymptotic scaling of the minimum code distance, $d=\Omega(\sqrt{n \sqrt{\log n}})$, broken by Ramanujan tensor-product codes.

## Relations

- _parent_: [[concepts/qec/hyperbolic-surface]]

## Notes

- See thesis by Fetaya for pedagogical exposition  ([arXiv:1108.2886](https://arxiv.org/abs/1108.2886)).
