---
type: concept
name: Hypersphere product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/distance-balanced
- concepts/qec/higher-dimensional-surface
- concepts/qec/qltc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hypersphere_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hypersphere_product
---

# Hypersphere product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hypersphere_product) (`code_id: hypersphere_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Homological code based on products of hyperspheres.
The hypersphere product code family has asymptotically diminishing soundness that scales as order $O(1/\log (n)^2)$, locality of stabilizer generators scaling as order $O(\log n/ \log\log n)$, and distance of order $\Theta(\sqrt{n})$.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/higher-dimensional-surface]]
- _cousin_: [[concepts/qec/qltc]] — The hypersphere product code family has asymptotically diminishing soundness that scales as order $O(1/\log (n)^2)$, locality of stabilizer generators scaling as order $O(\log n/ \log\log n)$, and distance of order $\Theta(\sqrt{n})$. Applying Hastings' weight-reduction construction yields QLDPC families with distance $\Theta^*(\sqrt{n})$ and inverse-polylogarithmic soundness  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790)). Application of generalized distance balancing  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)) to hypersphere product codes using an asymptotically good classical code of length $t$ yields $O( 1/(\log(n)^2 t^2) )$ soundness and order $\Theta(\sqrt{n}t)$ distance while maintaining locality scaling and at the expense of a dimension scaling as order $\Theta(t^2)$  ([arXiv:2305.00689](https://arxiv.org/abs/2305.00689)).
- _cousin_: [[concepts/qec/distance-balanced]] — Application of generalized distance balancing  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)) to hypersphere product codes using an asymptotically good classical code of length $t$ yields $O( 1/(\log(n)^2 t^2) )$ soundness and order $\Theta(\sqrt{n}t)$ distance while maintaining locality scaling and at the expense of a dimension scaling as order $\Theta(t^2)$  ([arXiv:2305.00689](https://arxiv.org/abs/2305.00689)).
