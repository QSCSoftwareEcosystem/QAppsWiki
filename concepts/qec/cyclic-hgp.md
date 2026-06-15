---
type: concept
name: Cyclic Hypergraph Product Code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-bicycle
- concepts/qec/hypergraph-product
- concepts/qec/lacross
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cyclic_hgp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cyclic_hgp
---

# Cyclic Hypergraph Product Code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cyclic_hgp) (`code_id: cyclic_hgp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

The hypergraph product code constructed using two low-weight circulant matrices. The code family $\mathrm{C2}$ is the product of a cyclic LDPC code with itself, and the family $\mathrm{CxR}$ is the product of the cyclic code with a repetition code. 

The construction of $\mathrm{C2}$ uses a single generating polynomial $\sum a_ix^i$ for both factors, while the construction of $\mathrm{CxR}$ uses the generating polynomial $\sum a_ix^i$ along with the polynomial $1+x$, where $a_i\in\{0,1\}$.

(source: raw/error-correction-zoo.md)

## Decoders

- BP-OSD decoder

## Relations

- _parent_: [[concepts/qec/hypergraph-product]] — A cyclic hypergraph product code is a hypergraph product code constructed using two circulant matrices.
- _cousin_: [`qc_ldpc`](https://errorcorrectionzoo.org/c/qc_ldpc) — A classical cyclic LDPC code with parameters $[n,k,d]$ yields a $\mathrm{C2}$ code with parameters $⟦2n^2,2k^2,d⟧$ and a $\mathrm{CxR}$ code with parameters $⟦2nd,2k,d⟧$.
- _cousin_: [[concepts/qec/lacross]] — The La-cross code is a reduced block length, full-rank cyclic HGP code with generator polynomials of the form $1+x+x^k$
- _cousin_: [[concepts/qec/generalized-bicycle]] — Cyclic HGP codes and GB codes both use circulant matrices as building blocks.
