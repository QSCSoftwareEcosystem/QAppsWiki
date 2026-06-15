---
type: concept
name: $U(1)_{2n} \times U(1)_{-2m}$ Chern-Simons GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/analog-surface
- concepts/qec/multimodegkp
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/chern_simons_gkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: chern_simons_gkp
---

# $U(1)_{2n} \times U(1)_{-2m}$ Chern-Simons GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/chern_simons_gkp) (`code_id: chern_simons_gkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A non-CSS multimode GKP code defined on a 2D mode lattice that encodes a qudit logical space and whose excitations are characterized by the $U(1)_{2n} \times U(1)_{-2m}$ Chern-Simons theory.
The code can be obtained from the analog surface code by condensing certain anyons  ([arXiv:2411.04993](https://arxiv.org/abs/2411.04993)). 

The $U(1)_{2} \times U(1)_{-4}$ case admits a topological order that is Witt non-trivial, i.e., that does not admit a gapped boundary. This order is not chiral (i.e., chiral central charge is zero) and does not admit a bosonic anyon.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/multimodegkp]]
- _parent_: [[concepts/qec/2d-stabilizer]]
- _cousin_: [[concepts/qec/topological-abelian]] — The $U(1)_{2n} \times U(1)_{-2m}$ Chern-Simons GKP code realizes $U(1)_{2n} \times U(1)_{-2m}$ Chern-Simons theory on bosonic modes. The code can be obtained from the analog surface code by condensing certain anyons  ([arXiv:2411.04993](https://arxiv.org/abs/2411.04993)).
- _cousin_: [[concepts/qec/analog-surface]] — The $U(1)_{2n} \times U(1)_{-2m}$ Chern-Simons GKP code can be obtained from the analog surface code by condensing charge-flux composite anyons  ([arXiv:2411.04993](https://arxiv.org/abs/2411.04993)).
