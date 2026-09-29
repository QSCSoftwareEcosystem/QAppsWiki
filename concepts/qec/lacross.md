---
type: concept
name: La-cross code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hypergraph-product
- concepts/qec/perm-self-dual-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/lacross
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: lacross
---

# La-cross code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/lacross) (`code_id: lacross`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

La-cross codes are hypergraph products of two copies of a classical seed code with generating polynomial $1+x+x^k$ for some $k$  ([arXiv:2404.13010](https://arxiv.org/abs/2404.13010)).
They are high-rate quantum LDPC codes with moderate-range, weight-six checks suited to neutral-atom registers.

A square circulant seed of length $n$ gives a periodic-boundary code with parameters $⟦2n^2,2k^2⟧$.
A rectangular full-rank seed $H\in\mathbb{F}_2^{(n-k)\times n}$ instead gives an open-boundary code with parameters $⟦(n-k)^2+n^2,k^2⟧$.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/hypergraph-product]] — La-cross codes are hypergraph products of two identical classical seed codes with generating polynomial $1+x+x^k$  ([arXiv:2404.13010](https://arxiv.org/abs/2404.13010)).
- _parent_: [[concepts/qec/perm-self-dual-css]] — La-cross codes are permutationally self-dual since both factors of the hypergraph product use the same seed check matrix  ([arXiv:2404.13010](https://arxiv.org/abs/2404.13010)). Reflecting each of the two grids of qubits about its principal diagonal is an involutive $XZ$-duality  ([arXiv:2204.10812](https://arxiv.org/abs/2204.10812)).
- _cousin_: [`qc_ldpc`](https://errorcorrectionzoo.org/c/qc_ldpc) — Periodic-boundary La-cross codes are hypergraph products of classical quasi-cyclic (cyclic) LDPC seed codes  ([arXiv:2404.13010](https://arxiv.org/abs/2404.13010)).
