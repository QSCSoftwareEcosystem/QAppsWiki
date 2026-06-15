---
type: concept
name: EA mixed-alphabet Reed-Solomon c-q code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Mixed-alphabet Reed-Solomon EACC code
- Mixed-alphabet RS entanglement-assisted classical code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ea-classical-into-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_mixed_alphabet_reed_solomon
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_mixed_alphabet_reed_solomon
---

# EA mixed-alphabet Reed-Solomon c-q code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_mixed_alphabet_reed_solomon) (`code_id: ea_mixed_alphabet_reed_solomon`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Entanglement-assisted c-q code obtained from a mixed-alphabet Reed-Solomon construction over $\mathbb{F}_q$ and $\mathbb{F}_{q^2}$.
A codeword of an $[n,k,d;c]_q$ code consists of $n-c$ symbols transmitted directly over $q$-dimensional quantum systems and $c$ symbols transmitted through super-dense coding using $c$ pre-shared maximally entangled qudit pairs.

More explicitly, the code evaluates all polynomials $f\in\mathbb{F}_q[x]$ of degree at most $k-1$ at $n-c$ distinct points $\alpha_i\in\mathbb{F}_q$ and $c$ representatives $\gamma_j\in\mathbb{F}_{q^2}\setminus\mathbb{F}_q$, choosing at most one element from each conjugate pair $\{\gamma,\gamma^q\}$.
This yields codewords in $\mathbb{F}_q^{n-c}\times\mathbb{F}_{q^2}^{c}$, where each $\mathbb{F}_{q^2}$ symbol is identified with two $q$-ary symbols for dense coding.

(source: raw/error-correction-zoo.md)

## Protection

Let $n_1=n-c$ and $n_2=c$.
If $n_1\geq k-1$, then the minimum distance is $d=n-k+1$, saturating the classical Singleton bound.
If $n_1<k-1$, then
\begin{align}
  d=\left\lceil\frac{n-k+1+n_2}{2}\right\rceil~,
\end{align}
which can exceed the classical Singleton bound because a known erasure of an $\mathbb{F}_{q^2}$ position removes a two-symbol block  ([arXiv:2310.19774](https://arxiv.org/abs/2310.19774)).

## Rate

The construction can have $k>n$ when $c>0$, since each dense-coded position carries two $q$-ary symbols.
Its length is bounded by $n\leq q+(q^2-q)/2=(q^2+q)/2$, with a possible one-symbol extension using the point at infinity  ([arXiv:2310.19774](https://arxiv.org/abs/2310.19774)).
In the range $n\leq q+(q^2-q)/2$ and $n-q\leq c$, the distance formula above meets the block-erasure bound of Ref.  ([arXiv:2310.19774](https://arxiv.org/abs/2310.19774)).

## Relations

- _parent_: [[concepts/qec/ea-classical-into-quantum]]
- _cousin_: [`reed_solomon`](https://errorcorrectionzoo.org/c/reed_solomon) — EA mixed-alphabet RS c-q codes use Reed-Solomon polynomial evaluation, but evaluate over both $\mathbb{F}_q$ and selected representatives from $\mathbb{F}_{q^2}\setminus\mathbb{F}_q$ to support direct and dense-coded channel uses  ([arXiv:2310.19774](https://arxiv.org/abs/2310.19774)).
- _cousin_: [`mds`](https://errorcorrectionzoo.org/c/mds) — EA mixed-alphabet RS c-q codes can saturate a block-erasure bound and, in some parameter ranges, exceed the classical Singleton bound for ordinary $q$-ary codes  ([arXiv:2310.19774](https://arxiv.org/abs/2310.19774)).
