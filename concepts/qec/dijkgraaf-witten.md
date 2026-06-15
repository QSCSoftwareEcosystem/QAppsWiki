---
type: concept
name: Dijkgraaf-Witten gauge theory code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Cohomological gauge theory code
- Twisted $G$ gauge theory code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-quantum
- concepts/qec/yetter-gauge-theory
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/dijkgraaf_witten
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: dijkgraaf_witten
---

# Dijkgraaf-Witten gauge theory code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/dijkgraaf_witten) (`code_id: dijkgraaf_witten`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code whose codewords realize $D$-dimensional lattice Dijkgraaf-Witten gauge theory  ([doi:10.1007/BF02096988](https://doi.org/10.1007/BF02096988), [arXiv:hep-th/9111004](https://arxiv.org/abs/hep-th/9111004)) for a finite group $G$ and a $D+1$-cocycle $\omega$ in the cohomology class $H^{D+1}( G, U(1) )$.
When the cocycle is non-trivial, the gauge theory is called a *twisted gauge theory*.
There exist lattice-model formulations in arbitrary spatial dimension  ([arXiv:1212.0835](https://arxiv.org/abs/1212.0835)).
Boundaries and excitations have been studied for arbitrary dimension  ([arXiv:1905.08673](https://arxiv.org/abs/1905.08673)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/group-quantum]]
- _parent_: [[concepts/qec/yetter-gauge-theory]] — Replacing the two-group data in a two-gauge theory with a group and a cocycle reproduces the phase of the Dijkgraaf-Witten gauge theory, with the two theories equivalent in 2D  ([arXiv:1309.4721](https://arxiv.org/abs/1309.4721)). Generalizations of Ocneanu's tube algebras  ([doi:10.2969/aspm/03110235](https://doi.org/10.2969/aspm/03110235)) can be used to characterize excitations in both theories  ([arXiv:1909.07937](https://arxiv.org/abs/1909.07937)). A Dijkgraaf-Witten Lagrangian can also be re-expressed as a two-group gauge theory Lagrangian by relating the electric and magnetic gauge fields via the equations of motion  ([arXiv:1309.4721](https://arxiv.org/abs/1309.4721)).
