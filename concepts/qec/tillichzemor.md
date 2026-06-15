---
type: concept
name: Tillich-Zémor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Quantum $(n, m, r)$-structured LDPC code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hypergraph-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tillichzemor
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tillichzemor
---

# Tillich-Zémor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tillichzemor) (`code_id: tillichzemor`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of $⟦n^2 + m^2, (n - \text{rank}([C \mid M]) )^2 + (m - \text{rank}([C \mid M]^\top) )^2, d⟧$ quantum LDPC codes constructed via the hypergraph product of two classical $(n, m, r)$-structured LDPC seed codes

A code's parity-check matrix $H = [C \mid M]$ consists of an $m \times m$ circulant core $C$ with column weight $2$ (enabling linear-time encoding) and an $m \times (n-m)$ matrix $M$ with column weight $r \geq 3$ and no zero rows.
The resulting code has block length $N = n^2 + m^2$ and code dimension $K = (n - \text{rank}([C \mid M]) )^2 + (m - \text{rank}([C \mid M]^\top) )^2$.

(source: raw/error-correction-zoo.md)

## Protection

The structured construction inherits the classical seed code's sub-linear distance scaling of order $O(n^{\frac{r-2}{r-1}+\epsilon})$ while preserving efficient encoding; see Ref.  ([arXiv:2501.19125](https://arxiv.org/abs/2501.19125)) for distance upper bounds.

## Relations

- _parent_: [[concepts/qec/hypergraph-product]]
