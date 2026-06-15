---
type: concept
name: Lossless expander balanced-product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/balanced-product
- concepts/qec/good-qldpc
- concepts/qec/qubit-generalized-homological-product-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/lossless_expander
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: lossless_expander
---

# Lossless expander balanced-product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/lossless_expander) (`code_id: lossless_expander`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

QLDPC code constructed by taking the balanced product of lossless expander graphs.
Using one part of a quantum-code chain complex constructed with one-sided loss expanders  ([doi:10.1145/509907.510003](https://doi.org/10.1145/509907.510003)) yields a $c^3$-LTC  ([arXiv:2201.11369](https://arxiv.org/abs/2201.11369)).
Using two-sided expanders  ([arXiv:2504.15087](https://arxiv.org/abs/2504.15087)) yields an asymptotically good QLDPC code family  ([arXiv:2203.03581](https://arxiv.org/abs/2203.03581)).

(source: raw/error-correction-zoo.md)

## Rate

Asymptotically good QLDPC codes  ([arXiv:2203.03581](https://arxiv.org/abs/2203.03581), [arXiv:2504.15087](https://arxiv.org/abs/2504.15087)).

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]]
- _parent_: [[concepts/qec/balanced-product]]
- _cousin_: [`ltc`](https://errorcorrectionzoo.org/c/ltc) — Using one part of a quantum-code chain complex constructed with one-sided loss expanders yields a $c^3$-LTC  ([arXiv:2201.11369](https://arxiv.org/abs/2201.11369)).
- _cousin_: [[concepts/qec/good-qldpc]] — Taking a balanced product of two-sided expanders  ([arXiv:2504.15087](https://arxiv.org/abs/2504.15087)) yields an asymptotically good QLDPC code family  ([arXiv:2203.03581](https://arxiv.org/abs/2203.03581)).
