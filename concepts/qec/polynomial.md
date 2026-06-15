---
type: concept
name: Prime-qudit RS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Prime-qudit polynomial code (QPyC)
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-polynomial
- concepts/qec/qudit-css
- concepts/qec/qudit-triorthogonal
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/polynomial
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: polynomial
---

# Prime-qudit RS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/polynomial) (`code_id: polynomial`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Prime-qudit CSS code constructed using two RS codes.

The original construction  ([arXiv:quant-ph/9910059](https://arxiv.org/abs/quant-ph/9910059)) was for a qubit code ($p=2$) by using a basis for a larger Galois field over $\mathbb{F}_2$, yielding an $⟦kN,k(N-2K),K+1⟧$ qubit code from a $[N,K,\delta]_{2^k}$ RS code with $N=2^k-1$ and $K=N-\delta+1$.

An alternative construction  yields an $⟦n,k,d⟧_{p>n}$ prime-qudit CSS code with $d=\min(n-g,g+2-k)$ that is constructed using two RS codes over $\mathbb{F}_p=\mathbb{Z}_p$.
Let $\{\alpha_1,\cdots,\alpha_n\}$ be $n$ distinct nonzero elements of $\mathbb{Z}_p$, and let $g$ be a number satisfying $0\leq k \leq g < n$. Then, define degree-$g$ polynomials
\begin{align}
  f_{\mu\cup c}\left(x\right)=\mu_{0}+\mu_{1}x+\cdots+\mu_{k-1}x^{k-1}+c_{k}x^{k}+\cdots+c_{g}x^{g}\,,
\end{align}
where the first $k$ coefficients are indexed by the coefficient vector $\mu\in\mathbb{Z}_p^{ k}$, and the remaining coefficients are indexed by the vector $c\in\mathbb{Z}_p^{ (g+1-k)}$.
Logical states, labeled by $\mu$, are superpositions of canonical basis states whose $i$th entry is $f_{\mu\cup c}$ evaluated at $\alpha_i$, summed over all possible vectors $c$,
\begin{align}
  |\overline{\mu}\rangle=\sum_{c\in\mathbb{Z}_{p}^{(g+1-k)}}|f_{\mu\cup c}(\alpha_{1}),f_{\mu\cup c}(\alpha_{2}),\cdots,f_{\mu\cup c}(\alpha_{n})\rangle.
\end{align}

(source: raw/error-correction-zoo.md)

## Magic scaling exponent

Triorthogonal $p$-dimensional prime-qudit RS codes achieve a magic-state yield parameter $\gamma = O(1/\log p)$  ([arXiv:1811.08461](https://arxiv.org/abs/1811.08461)).

## Relations

- _parent_: [[concepts/qec/qudit-css]]
- _parent_: [[concepts/qec/galois-polynomial]] — Galois-qudit RS codes for prime-dimensional qudits are prime-qudit RS codes.
- _cousin_: [[concepts/qec/qudit-triorthogonal]] — Triorthogonal $p$-dimensional prime-qudit RS codes achieve a magic-state yield parameter $\gamma = O(1/\log p)$  ([arXiv:1811.08461](https://arxiv.org/abs/1811.08461)).
