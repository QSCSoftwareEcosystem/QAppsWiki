---
type: concept
name: Binary quantum Goppa code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-css
- concepts/qec/quantum-ag
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/binary_quantum_goppa
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: binary_quantum_goppa
---

# Binary quantum Goppa code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/binary_quantum_goppa) (`code_id: binary_quantum_goppa`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A quantum AG code obtained from algebraic-geometric Goppa codes via the Galois-qudit CSS construction.

For $q=2^m$, let $F/\mathbb{F}_q$ be an algebraic function field of one variable with an automorphism $\sigma$ of order two fixing $\mathbb{F}_q$, and let $P_1,\ldots,P_n$ be pairwise distinct degree-one places such that $\sigma P_i \neq P_j$ for all $i,j$.
If $\eta$ is a differential with $v_{P_i}(\eta)=v_{\sigma P_i}(\eta)=-1$, $\operatorname{res}_{P_i}(\eta)=1$, and $\operatorname{res}_{\sigma P_i}(\eta)=-1$, and if $G$ is a $\sigma$-invariant divisor satisfying $v_{P_i}(G)=v_{\sigma P_i}(G)=0$, then
\begin{align}
  C(G)=\{(f(P_1),\ldots,f(P_n),f(\sigma P_1),\ldots, f(\sigma P_n) )\,|\,f\in\mathcal{L}(G)\}\subseteq \mathbb{F}_q^{2n}
\end{align}
obeys $C(G)^{\perp_s}=C(H)$, where $H=(P_1+\cdots+P_n+\sigma P_1+\cdots+\sigma P_n)-G+(\eta)$  ([arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)).
Whenever $G \geq H$, this yields an $⟦n,k,d⟧_q$ quantum stabilizer code with
\begin{align}
  k=\dim G-\dim(G-P_1-\cdots-P_n-\sigma P_1-\cdots-\sigma P_n)-n
\end{align}
and $d \geq n-\lfloor \deg G/2 \rfloor$  ([arXiv:quant-ph/0006061](https://arxiv.org/abs/quant-ph/0006061), [doi:10.1007/s11128-006-0047-9](https://doi.org/10.1007/s11128-006-0047-9)) ([arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)).

(source: raw/error-correction-zoo.md)

## Protection

For a code with distance $d$, detects errors on up to $d-1$ qudits and corrects errors on up to $\lfloor (d-1)/2 \rfloor$ qudits. In Matsumoto's construction, $d \geq n-\lfloor \deg G/2 \rfloor$.

## Rate

For every $m \geq 2$, there are binary quantum Goppa-code families with $\liminf k_i/n_i \geq 1-\frac{2}{2^m-1}-4m\delta$ and $\liminf d_i/n_i \geq \delta$  ([arXiv:quant-ph/0006061](https://arxiv.org/abs/quant-ph/0006061), [arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)).

## Encoders

- Encoding defined in Ref.  ([arXiv:quant-ph/0107129](https://arxiv.org/abs/quant-ph/0107129)) uses a technique from Ref.  ([arXiv:quant-ph/0005008](https://arxiv.org/abs/quant-ph/0005008)) to encode quantum stabilizer codes.

## Decoders

- Farran's decoder can be used for the underlying AG construction; under the bound $2\,\mathrm{wt}(e)+1 \leq n-\lfloor \deg G/2 \rfloor$, the relevant minimum-weight error can be recovered in $O(n^{2.81})$ time  ([arXiv:math/9910151](https://arxiv.org/abs/math/9910151), [arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)).

## Relations

- _parent_: [[concepts/qec/galois-css]]
- _parent_: [[concepts/qec/quantum-ag]]
- _cousin_: [`goppa`](https://errorcorrectionzoo.org/c/goppa) — Classical Goppa codes over various algebraic curves are used to construct quantum Goppa codes.
