---
type: concept
name: $((5,3,2))_3$ qutrit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/su3-spin
- concepts/qec/t-group
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/su3_sigma360
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: su3_sigma360
---

# $((5,3,2))_3$ qutrit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/su3_sigma360) (`code_id: su3_sigma360`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Smallest qutrit block code realizing the $\Sigma(360\phi)=3.A_6$ subgroup of $SU(3)$ transversally.
The next smallest code is $((7,3,2))_3$.

(source: raw/error-correction-zoo.md)

## Transversal gates

- $\Sigma(360\phi)=3.A_6$ group gates can be realized transversally.

## Relations

- _parent_: [[concepts/qec/t-group]] — The $((5,3,2))_3$ qutrit code admits a transversal representation of the twisted $1$-group $\Sigma(360\phi)=3.A_6$  ([arXiv:2402.01638](https://arxiv.org/abs/2402.01638)).
- _cousin_: [[concepts/qec/su3-spin]] — The $((5,3,2))_3$ qutrit code can be interpreted as a $SU(3)$ single-spin code via the simplex mapping  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
