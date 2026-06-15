---
type: concept
name: La-cross code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hypergraph-product
- concepts/qec/quantum-cyclic
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

Code constructed using a hypergraph product of two copies of a cyclic LDPC code.
The construction uses cyclic LDPC codes with generating polynomials $1+x+x^k$ for some $k$.
Using a length-$n$ seed code yields an $⟦2n^2,2k^2⟧$ family for periodic boundary conditions and an $⟦(n-k)^2+n^2,k^2⟧$ family for open boundary conditions.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/hypergraph-product]] — La-cross codes are constructed using a hypergraph product of a cyclic LDPC code with itself.
- _parent_: [[concepts/qec/quantum-cyclic]]
- _cousin_: [`qc_ldpc`](https://errorcorrectionzoo.org/c/qc_ldpc) — La-cross codes are constructed using a hypergraph product of a cyclic LDPC code with itself.
