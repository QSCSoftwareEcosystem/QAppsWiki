---
type: concept
name: Hayden-Nezami-Salton-Sanders bosonic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/analog-stabilizer
- concepts/qec/generalized-homological-product-css
- concepts/qec/niset-andersen-cerf
- concepts/qec/oscillator-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hnss
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hnss
---

# Hayden-Nezami-Salton-Sanders bosonic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hnss) (`code_id: hnss`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦n,1⟧_{\mathbb{R}}$ analog CSS code defined using homological structures associated with an $n-1$ simplex. Relevant to the study of spacetime replication of quantum information  ([arXiv:1210.0913](https://arxiv.org/abs/1210.0913)).

Stabilizer generators are defined by two orthogonal subspaces of $C_1$ in the chain complex. $C_X = \partial_2 C_2$ and $C_P = \partial_1^T Q$ for some $Q \subset C_0$. The standard approach would use $Q = C_0$, which would mean the logical dimension would be the dimension of the 1st cohomology group $H^1$. However, $H^1$ is trivial for the $n-1$ simplex, so one chooses $Q \neq C_0$ such that exactly one stabilizer is removed, yielding a stabilizer code instead of a single stabilized state.

(source: raw/error-correction-zoo.md)

## Protection

Protects against certain types of erasure errors (depending on the specific dimension). Certain constructions also protect arbitrarily sized errors on multiple-photon states.

## Encoders

- Encoding depends on the specific dimension, but can generally be done using generalized conditional-rotation and Fourier-transform gates.

## Decoders

- Decoding requires a different circuit for each possible erasure error, with no general circuit decoding any possible erasure error. Every circuit relies on a generalized conditional rotation, which Ref.  ([arXiv:1601.02544](https://arxiv.org/abs/1601.02544)) calls the *QND Gate* and which is defined as $QND_c | x , y \rangle = |x + c y, y \rangle$.

## Relations

- _parent_: [[concepts/qec/analog-stabilizer]]
- _parent_: [[concepts/qec/oscillator-css]]
- _cousin_: [[concepts/qec/generalized-homological-product-css]] — Hayden-Nezami-Salton-Sanders codes utilize chain complexes in code construction, but the complexes have trivial homology.
- _cousin_: [[concepts/qec/niset-andersen-cerf]] — The Niset-Andersen-Cerf code can be viewed as a scheme to replicate quantum information in multiple regions  ([arXiv:1601.02544](https://arxiv.org/abs/1601.02544)).
- _cousin_: [`spacetime`](https://errorcorrectionzoo.org/c/spacetime) — Hayden-Nezami-Salton-Sanders codes have been considered in the context of spacetime replication of quantum data  ([arXiv:1210.0913](https://arxiv.org/abs/1210.0913), [arXiv:1601.02544](https://arxiv.org/abs/1601.02544)), while STCs are designed to replicate classical data.

## Notes

- Proposed experimental optical procedure for realizing the simplest non-trivial code with 5 modes  ([arXiv:1601.02544](https://arxiv.org/abs/1601.02544)).
