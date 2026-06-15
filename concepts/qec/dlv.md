---
type: concept
name: Dinur-Lin-Vidick (DLV) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qltc
- concepts/qec/qubit-generalized-homological-product-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/dlv
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: dlv
---

# Dinur-Lin-Vidick (DLV) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/dlv) (`code_id: dlv`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of codes constructed using cubical chain complexes, which are $t$-order extensions of the complexes underlying expander codes ($t=1$) and expander lifted-product codes ($t=2$).

For $t=4$, assuming a conjecture about random linear maps, there exists a quantum locally testable family with linear dimension and inverse poly-logarithmic relative distance and soundness.
Applying weight reduction yields order $\Omega(1/\text{polylog}n)$ soundness, $\Omega(n/\text{polylog}n)$ distance and dimension, and constant locality  ([arXiv:2309.05541](https://arxiv.org/abs/2309.05541)).
Applying distance amplification and soundness amplification yields asymptotically constant soundness, order $\Theta(n)$ distance, order $\Theta(n)$ dimension, but poly-logarithmic locality  ([arXiv:2309.05541](https://arxiv.org/abs/2309.05541)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]] — DLV codes are codes constructed using a cubical chain complex, which is a $t$-order extension of the chain complexes underlying quantum generalized homological product CSS codes.
- _cousin_: [[concepts/qec/qltc]] — DLV codes have linear dimension and inverse poly-logarithmic relative distance and soundness, assuming a conjecture about random linear maps  ([arXiv:2402.07476](https://arxiv.org/abs/2402.07476)). Applying distance amplification and soundness amplification yields asymptotically constant soundness, order $\Theta(n)$ distance, order $\Theta(n)$ dimension, but poly-logarithmic locality  ([arXiv:2309.05541](https://arxiv.org/abs/2309.05541)).
