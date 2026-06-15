---
type: concept
name: Quantum tensor-product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-polynomial
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_tensor_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_tensor_product
---

# Quantum tensor-product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_tensor_product) (`code_id: quantum_tensor_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

CSS code constructed from a tensor code. In some cases, only one of the classical codes forming the tensor code needs to be self-orthogonal.

(source: raw/error-correction-zoo.md)

## Protection

If one of the classical codes forming the tensor code protects against burst errors, the resulting quantum code does also  ([arXiv:1605.09598](https://arxiv.org/abs/1605.09598)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _cousin_: [`tensor`](https://errorcorrectionzoo.org/c/tensor) — Quantum tensor-product codes are quantum analogues of tensor-product codes.
- _cousin_: [`reversible`](https://errorcorrectionzoo.org/c/reversible) — Reversible cyclic codes can be used to construct quantum tensor-product codes  ([arXiv:1605.09598](https://arxiv.org/abs/1605.09598)).
- _cousin_: [`q-ary_cyclic`](https://errorcorrectionzoo.org/c/q-ary_cyclic) — Reversible cyclic codes can be used to construct quantum tensor-product codes  ([arXiv:1605.09598](https://arxiv.org/abs/1605.09598)).
- _cousin_: [`mds`](https://errorcorrectionzoo.org/c/mds) — MDS codes can be used to construct quantum tensor-product codes  ([arXiv:1605.09598](https://arxiv.org/abs/1605.09598)).
- _cousin_: [[concepts/qec/galois-polynomial]] — Product codes constructed from a self-orthogonal and an arbitrary RS code yield an RS code  ([arXiv:quant-ph/0703181](https://arxiv.org/abs/quant-ph/0703181)).
