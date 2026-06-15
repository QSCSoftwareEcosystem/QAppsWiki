---
type: concept
name: XYZ product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-homological-product
- concepts/qec/multisector-hypergraph
- concepts/qec/sc-qldpc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/xyz_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: xyz_product
---

# XYZ product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/xyz_product) (`code_id: xyz_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A non-CSS QLDPC code obtained from a three-fold variant of the hypergraph product applied to three classical binary codes with parity-check matrices $H_1,H_2,H_3$.  Unlike CSS three-fold hypergraph product codes, the third input code acts through Pauli-$Y$ checks  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).
Under mild assumptions, the code dimension is determined by a tensor Sylvester equation over $\mathbb{F}_2$, and the minimum-distance problem reduces up to constant factors to how closely a related inhomogeneous tensor Sylvester equation can be satisfied  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).  When the underlying classical codes are repetition codes, the construction yields the Chamon model code.

(source: raw/error-correction-zoo.md)

## Protection

The natural logical operators are membrane-like two-dimensional objects rather than strings  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).  For cyclic XYZ product codes, fractal operators yield large-weight errors with constant-weight syndromes, ruling out local testability  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).

## Rate

The logical dimension depends on properties of the input classical codes, specifically similarity invariants of the matrices $H_i H_i^T$. It is conjectured that specific instances of XYZ product codes have a constant encoding rate and a minimum distance of $d \in \Theta(n^{2/3})$  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).

## Relations

- _parent_: [[concepts/qec/sc-qldpc]] — XYZ product stabilizer generator matrices can be used as sub-matrices to define a 2D SC-QLDPC code  ([arXiv:2305.00137](https://arxiv.org/abs/2305.00137)).
- _parent_: [[concepts/qec/generalized-homological-product]] — The XYZ product code is a non-CSS three-fold variant of the hypergraph product built from three classical linear binary codes  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — The XYZ product code is a non-CSS three-fold variant of the hypergraph product built from three classical linear binary codes  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).
- _cousin_: [[concepts/qec/multisector-hypergraph]] — The XYZ product code is a non-CSS three-fold variant of the hypergraph product built from three classical linear binary codes  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).
