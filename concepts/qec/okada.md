---
type: concept
name: Okada spin code
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
- https://errorcorrectionzoo.org/c/okada
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: okada
---

# Okada spin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/okada) (`code_id: okada`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Non-diagonal $SU(2)$ single-spin code in the spin-$J = 3m$ irrep for integer $m \geq 1$, encoding a logical $(2m+1)$-dimensional space.
The construction uses a *non-diagonal* subspace (one for which the projected error space $P_{\mathcal{B}}\mathcal{E}P_{\mathcal{B}}$ is block-diagonal rather than diagonal) to exceed the dimension bound achievable by the Tverberg theorem construction  ([arXiv:quant-ph/9908066](https://arxiv.org/abs/quant-ph/9908066)).

The code is defined in terms of a subspace $\mathcal{B} = \mathrm{span}\{|k, n-k\rangle : k \equiv 0 \text{ or } 1 \pmod{3}\}$ of the spin-$n/2$ Hilbert space $\mathcal{H}_n$ (with $n = 2J = 6m$), where $|k, n-k\rangle$ denotes the state with $k$ particles in the first mode and $n-k$ in the second }.
The codespace has dimension $\dim \mathcal{C} = 2m+1$, which is approximately $(n+1)/3$.

The $m = 1$ ($J = 3$) instance encodes a logical qutrit and admits the unnormalized codewords
\begin{align}
\begin{split}
  |\overline{0}\rangle&=|_{0}^{3}\rangle\\|\overline{1}\rangle&\propto\sqrt{2}|_{-2}^{3}\rangle-|_{4}^{3}\rangle\\|\overline{2}\rangle&\propto|_{-4}^{3}\rangle+\sqrt{2}|_{2}^{3}\rangle~.
\end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

Detects distance-1 errors from the $\mathfrak{su}(2)$ Lie algebra, i.e., any linear combination of the angular momentum operators $\{E, F, H\}$  ([arXiv:2502.14165](https://arxiv.org/abs/2502.14165)).
The codespace dimension $2m+1 \approx (n+1)/3$ improves on the Tverberg theorem construction  ([arXiv:quant-ph/9908066](https://arxiv.org/abs/quant-ph/9908066)), which gives $\lceil (n+1)/4 \rceil$  ([arXiv:1205.4517](https://arxiv.org/abs/1205.4517)).

## Relations

- _parent_: [[concepts/qec/single-spin]]
