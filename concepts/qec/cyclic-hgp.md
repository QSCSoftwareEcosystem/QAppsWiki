---
type: concept
name: Cyclic hypergraph product code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/abelian-2bga
- concepts/qec/generalized-bicycle
- concepts/qec/hypergraph-product
- concepts/qec/lacross
- concepts/qec/perm-self-dual-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cyclic_hgp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cyclic_hgp
---

# Cyclic hypergraph product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cyclic_hgp) (`code_id: cyclic_hgp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Hypergraph product code constructed from two circulant matrices, typically of low weight. The $\mathrm{C2}$ subfamily is the product of a cyclic LDPC code with itself, while the $\mathrm{CxR}$ subfamily is the product of the cyclic code with a repetition code  ([arXiv:2511.09683](https://arxiv.org/abs/2511.09683)).

The construction of $\mathrm{C2}$ uses a single generating polynomial $\sum a_ix^i$ for both factors, while the construction of $\mathrm{CxR}$ uses the generating polynomial $\sum a_ix^i$ along with the polynomial $1+x$, where $a_i\in\{0,1\}$.

(source: raw/error-correction-zoo.md)

## Protection

A CxC code built from circulant matrices $A$ and $B$ of sizes $a$ and $b$ and ranks $r_a$ and $r_b$ has parameters $⟦2ab,2(a-r_a)(b-r_b),\min(d_A,d_B)⟧$, where $d_A$ and $d_B$ are the distances of the two classical codes  ([arXiv:2511.09683](https://arxiv.org/abs/2511.09683)).
Such codes satisfy *balance criteria*: they have equal numbers of $X$- and $Z$-type stabilizer generators, $\text{rank}(H_X)=\text{rank}(H_Z)=(n-k)/2$, and all generators have the same weight $w(A)+w(B)$.
This yields near-identical performance in the $X$ and $Z$ logical bases, which is not guaranteed for a general HGP code  ([arXiv:2511.09683](https://arxiv.org/abs/2511.09683)).

## Decoders

- BP-OSD decoder  ([arXiv:2511.09683](https://arxiv.org/abs/2511.09683)).

## Relations

- _parent_: [[concepts/qec/hypergraph-product]] — A CxC code is a hypergraph product code constructed using two circulant matrices  ([arXiv:2511.09683](https://arxiv.org/abs/2511.09683)).
- _parent_: [[concepts/qec/abelian-2bga]] — A CxC code is an Abelian 2BGA code over $\mathbb{Z}_{n_1}\times\mathbb{Z}_{n_2}$ whose two group-algebra elements are polynomials in disjoint variables, $a=a(x)$ and $b=b(y)$; trivially intersecting supports turn a two-block code into a hypergraph product  ([arXiv:2306.16400](https://arxiv.org/abs/2306.16400)) ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
- _parent_: [[concepts/qec/perm-self-dual-css]] — CxC codes are permutationally self-dual since they are qubit Abelian 2BGA codes  ([arXiv:2306.16400](https://arxiv.org/abs/2306.16400)).
- _cousin_: [`qc_ldpc`](https://errorcorrectionzoo.org/c/qc_ldpc) — A classical cyclic LDPC code with parameters $[n,k,d]$ yields a $\mathrm{C2}$ code with parameters $⟦2n^2,2k^2,d⟧$ and a $\mathrm{CxR}$ code with parameters $⟦2nd,2k,d⟧$  ([arXiv:2511.09683](https://arxiv.org/abs/2511.09683)).
- _cousin_: [[concepts/qec/lacross]] — Periodic-boundary La-cross codes are CxC codes built from the seed polynomial $1+x+x^k$; the open-boundary La-cross family instead uses a rectangular full-rank seed  ([arXiv:2404.13010](https://arxiv.org/abs/2404.13010)).
- _cousin_: [[concepts/qec/generalized-bicycle]] — CxC codes and GB codes both use circulant matrices as building blocks  ([arXiv:2511.09683](https://arxiv.org/abs/2511.09683)).
