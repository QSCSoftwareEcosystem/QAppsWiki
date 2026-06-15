---
type: concept
name: Quantum check-product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/distance-balanced
- concepts/qec/qltc
- concepts/qec/quantum-tensor-product
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/check_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: check_product
---

# Quantum check-product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/check_product) (`code_id: check_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

CSS code constructed from an extension of the check product (between two classical codes) to a product between a classical and a quantum code.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qltc]] — Quantum check-product constructions yield an SLTC code with constant soundness $2\rho$ from a classical LTC code with soundness $\rho$  ([arXiv:2209.11405](https://arxiv.org/abs/2209.11405)). These form the first bona-fide QLTC family because they admit asymptotically constant soundness, but they are not practical because their distance is two.
- _cousin_: [`tensor`](https://errorcorrectionzoo.org/c/tensor) — Quantum check-product codes extend the concept of a check product, which yields the dual of a tensor code, to a product between a classical and a quantum code.
- _cousin_: [[concepts/qec/quantum-tensor-product]] — Quantum check-product codes extend the concept of a check product, which yields the dual of a tensor code, to a product between a classical and a quantum code.
- _cousin_: [[concepts/qec/distance-balanced]] — Quantum check-product code constructions use distance balancing to increase distance  ([arXiv:2209.11405](https://arxiv.org/abs/2209.11405)).
