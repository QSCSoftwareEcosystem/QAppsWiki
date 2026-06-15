---
type: concept
name: $SU(4)$ Tverberg spin code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/single-spin
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/su4_tverberg_spin
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: su4_tverberg_spin
---

# $SU(4)$ Tverberg spin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/su4_tverberg_spin) (`code_id: su4_tverberg_spin`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Single-spin code family in the totally symmetric $N$-particle irrep $\mathcal{H}=\mathrm{Sym}^N(\mathbb{C}^4)$ of $\mathfrak{su}(4)$, whose weight diagram is the discrete simplex $\Delta_{4,N}$, equivalently its centered tetrahedral realization.
The construction uses the two-step Tverberg-theorem method  ([arXiv:quant-ph/9908066](https://arxiv.org/abs/quant-ph/9908066)): first choose an intermediate subspace from a distance-two subset of $\Delta_{4,N}$, then combine basis states whose convex hulls contain the origin.

For $N$ divisible by eight, an optimal distance-two intermediate lattice is obtained as the kernel of
\begin{align}
  a_1L_1+a_2L_2+a_3L_3+a_4L_4 \mapsto a_1+2a_2+3a_3 \pmod 4~.
\end{align}
The second step pairs opposite points in the central octahedral region and can form additional triples and quadruples near the tetrahedron's corners; for $N=8$, this partition is optimal within the two-step framework .

More explicitly, write the normalized monomial basis of $\mathrm{Sym}^N(\mathbb{C}^4)$ as $|a_1a_2a_3a_4\rangle$, where $(a_1,a_2,a_3,a_4)\in\Delta_{4,N}$, and let $\Lambda_B^N$ be the kernel above.
For each block $Y\subset\Lambda_B^N$ whose convex hull contains the origin, choose barycentric weights $\{\beta_{\mathbf{a}}\}_{\mathbf{a}\in Y}$ satisfying $\beta_{\mathbf{a}}\geq0$, $\sum_{\mathbf{a}\in Y}\beta_{\mathbf{a}}=1$, and $\sum_{\mathbf{a}\in Y}\beta_{\mathbf{a}}\mathbf{a}=0$ in centered $\Delta_{4,N}$ coordinates.
The corresponding codeword is
\begin{align}
  |\psi_Y\rangle=\sum_{\mathbf{a}\in Y}\sqrt{\beta_{\mathbf{a}}}\,|\mathbf{a}\rangle~.
\end{align}
Thus opposite pairs give $(|p\rangle+|-p\rangle)/\sqrt{2}$; triples of the form $\{p,p',-(p+p')\}$ give $(|p\rangle+|p'\rangle+|-(p+p')\rangle)/\sqrt{3}$; and zero-sum quadruples give equal four-term superpositions.

(source: raw/error-correction-zoo.md)

## Protection

Detects single Lie-algebra errors from the $\mathfrak{su}(4)$ error set, equivalently errors in $V_1=\mathfrak{su}(4)\oplus \mathbb{C}I$ in the Lie-type graph metric.
The first step suppresses off-diagonal root-space errors by choosing weight vectors separated by graph distance at least two in the centered $\Delta_{4,N}$ discrete simplex, leaving only a commuting diagonal error algebra for the convex-geometric second step .

## Rate

The distance-two intermediate subset has asymptotic density $1/4$ in $\Delta_{4,N}$.
The generic Tverberg step gives an asymptotic code dimension at least $\dim\mathcal{H}/16$, while the extra triangle constructions improve finite-size instances but do not change the leading asymptotic rate in the construction described in Ref. .

## Relations

- _parent_: [[concepts/qec/single-spin]]
