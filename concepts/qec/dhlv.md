---
type: concept
name: Dinur-Hsieh-Lin-Vidick (DHLV) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/balanced-product
- concepts/qec/good-qldpc
- concepts/qec/lifted-product
- concepts/qec/qubit-generalized-homological-product-css
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/dhlv
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: dhlv
---

# Dinur-Hsieh-Lin-Vidick (DHLV) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/dhlv) (`code_id: dhlv`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of asymptotically good QLDPC codes which are related to expander LP codes in that the roles of the check operators and physical qubits are exchanged.

(source: raw/error-correction-zoo.md)

## Rate

Asymptotically good QLDPC codes.

## Decoders

- Linear-time decoder utilizing the small set-flip decoder  ([arXiv:2206.06557](https://arxiv.org/abs/2206.06557)) for $Z$ errors and a reconstruction procedure for $X$ errors  ([arXiv:2206.07750](https://arxiv.org/abs/2206.07750)).

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]]
- _parent_: [[concepts/qec/lifted-product]] — DHLV codes are LP codes  ([arXiv:2403.03651](https://arxiv.org/abs/2403.03651)).
- _cousin_: [[concepts/qec/good-qldpc]] — DHLV code construction yields asymptotically good QLDPC codes.
- _cousin_: [`regular_binary_tanner`](https://errorcorrectionzoo.org/c/regular_binary_tanner) — Regular binary Tanner codes are used in constructing quantum DHLV codes.
- _cousin_: [`tensor`](https://errorcorrectionzoo.org/c/tensor) — Tensor codes are used in constructing quantum DHLV codes.
- _cousin_: [[concepts/qec/balanced-product]] — DHLV codes can be obtained from a balanced product of two expander codes  ([arXiv:2403.03651](https://arxiv.org/abs/2403.03651)).
- _cousin_: [[concepts/qec/topological]] — DHLV codes are expected to realize topological quantum spin glass order  ([arXiv:2412.13248](https://arxiv.org/abs/2412.13248)).
