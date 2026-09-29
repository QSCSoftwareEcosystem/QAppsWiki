---
type: concept
name: Prime-qudit RS code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Prime-qudit polynomial code (QPyC)
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-polynomial
- concepts/qec/qudit-reed-muller
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

A construction  yields an $⟦n,k,d⟧_{p>n}$ prime-qudit CSS code with $d=\min(n-g,g+2-k)$ that is constructed using two RS codes over $\mathbb{F}_p=\mathbb{Z}_p$.
Let $\{\alpha_1,\cdots,\alpha_n\}$ be $n$ distinct nonzero elements of $\mathbb{Z}_p$, and let $g$ be a number satisfying $0\leq k \leq g < n$. Then, define degree-$g$ polynomials
\begin{align}
  f_{\mu\cup c}\left(x\right)=\mu_{0}+\mu_{1}x+\cdots+\mu_{k-1}x^{k-1}+c_{k}x^{k}+\cdots+c_{g}x^{g}\,,
\end{align}
where the first $k$ coefficients are indexed by the coefficient vector $\mu\in\mathbb{Z}_p^{ k}$, and the remaining coefficients are indexed by the vector $c\in\mathbb{Z}_p^{ (g+1-k)}$.
Logical states, labeled by $\mu$, are superpositions of canonical basis states whose $i$th entry is $f_{\mu\cup c}$ evaluated at $\alpha_i$, summed over all possible vectors $c$,
\begin{align}
  |\overline{\mu}\rangle=\sum_{c\in\mathbb{Z}_{p}^{(g+1-k)}}|f_{\mu\cup c}(\alpha_{1}),f_{\mu\cup c}(\alpha_{2}),\cdots,f_{\mu\cup c}(\alpha_{n})\rangle.
\end{align}

Logical states can instead be labeled by the $k$ highest-degree coefficients, with the superposition running over the $g+1-k$ lowest-degree ones.
Inverting the evaluation points and applying single-qudit multiplication gates maps the code above onto a code of this form with the same parameters.
This second form also allows zero as an evaluation point, so that $p\geq n$.
The case $n=p$, for which the evaluation points exhaust $\mathbb{Z}_p$, is constructed from extended GRS codes.

A related qubit construction  ([arXiv:quant-ph/9910059](https://arxiv.org/abs/quant-ph/9910059)) expands a $[N,K,\delta]_{2^k}$ RS code with $N=2^k-1$, $K=N-\delta+1$, and $\delta>N/2+1$ in a self-dual basis of $\mathbb{F}_{2^k}$ over $\mathbb{F}_2$.
This yields an $⟦kN,k(N-2K),d\geq K+1⟧$ qubit code.
These qubit codes are binarizations of Galois-qudit RS codes rather than members of this family.

(source: raw/error-correction-zoo.md)

## Magic scaling exponent

Triorthogonal $p$-dimensional prime-qudit RS codes achieve a magic-state yield parameter $\gamma = O(1/\log p)$  ([arXiv:1811.08461](https://arxiv.org/abs/1811.08461)).

## Relations

- _parent_: [[concepts/qec/qudit-reed-muller]] — Prime-qudit RS codes are the prime-qudit RM codes with $m=1$ whose two GRM codes are punctured to the same $n$ evaluation points. For $m=1$, GRM codes are extended RS codes  ([arXiv:quant-ph/0502001](https://arxiv.org/abs/quant-ph/0502001)). Every prime-qudit RS code takes this form when its logical states are labeled by the highest-degree coefficients, possibly after inverting the evaluation points and applying single-qudit multiplication gates.
- _parent_: [[concepts/qec/galois-polynomial]] — Galois-qudit RS codes for prime-dimensional qudits are prime-qudit RS codes.
- _cousin_: [[concepts/qec/qudit-triorthogonal]] — Triorthogonal $p$-dimensional prime-qudit RS codes achieve a magic-state yield parameter $\gamma = O(1/\log p)$  ([arXiv:1811.08461](https://arxiv.org/abs/1811.08461)).
