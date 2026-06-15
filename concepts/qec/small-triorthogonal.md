---
type: concept
name: $⟦3k + 8, k, 2⟧$ triorthogonal code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-divisible
- concepts/qec/quantum-h
- concepts/qec/quantum-triorthogonal
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/small_triorthogonal
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: small_triorthogonal
---

# $⟦3k + 8, k, 2⟧$ triorthogonal code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/small_triorthogonal) (`code_id: small_triorthogonal`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of the $⟦3k + 8, k, 2⟧$ family (for even $k$) of triorthogonal and quantum divisible codes that admit a transversal $T$ gate and are relevant for magic-state distillation  ([arXiv:1209.2426](https://arxiv.org/abs/1209.2426)) ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).

(source: raw/error-correction-zoo.md)

## Magic scaling exponent

The family yields the asymptotic exponent $\gamma = \log_2 \frac{3k+8}{k} \to \log_2 3 \approx 1.6$ for sufficiently large $k$  ([arXiv:1612.07330](https://arxiv.org/abs/1612.07330)); see  ([arXiv:1709.02789](https://arxiv.org/abs/1709.02789)).

## Transversal gates

- The code admits a transversal $T$ gate  ([arXiv:1209.2426](https://arxiv.org/abs/1209.2426)).

## Relations

- _parent_: [[concepts/qec/quantum-triorthogonal]]
- _parent_: [[concepts/qec/quantum-divisible]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/quantum-h]] — The H code $⟦k+4,k,2⟧$ family yields the $⟦3k + 8, k, 2⟧$ family of triorthogonal codes when level-lifted  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
