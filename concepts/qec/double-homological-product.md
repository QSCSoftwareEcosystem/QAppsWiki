---
type: concept
name: Campbell double homological product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/multisector-hypergraph
- concepts/qec/single-shot
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/double_homological_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: double_homological_product
---

# Campbell double homological product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/double_homological_product) (`code_id: double_homological_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A multi-dimensional HGP code derived from two applications of the hypergraph product to a classical code, resulting in a length-$4$ chain complex.
The construction method allows for the use of two different classical codes as inputs, with Ref.  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)) assuming identical input codes for simplicity.

Explicitly, the resulting chain complex is
\begin{align}
A_{-2}\xrightarrow{\partial_{-2}}A_{-1}\xrightarrow{\partial_{-1}}A_{0}\xrightarrow{\partial_{0}}A_{1}\xrightarrow{\partial_{1}}A_{2}\,.
\end{align}
The boundary maps $\partial_j$ are constructed using tensor products of the original boundary maps, ensuring the chain condition $\partial_{j+1} \partial_j = 0$.
The additional parts of the chain complex yield metachecks to detect measurement errors, enabling single-shot error correction.

(source: raw/error-correction-zoo.md)

## Protection

For the minimal length-one chain complex associated with a classical $[n, k, d]$ code, the double homological product yields a quantum code with parameters $⟦n^4 + 4n^2(n-k)^2 + (n-k)^4, k^4, \geq d⟧$ and single-shot distance $d_{\text{ss}}=\infty$  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)).

In this minimal-input setting, the Campbell double homological product code is $(d, f)$-sound with $f(x) = x^3/4$, meaning that small syndromes can be explained by errors whose weight grows at most cubically in the syndrome weight  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)). Its check redundancy is bounded by $<2$, and the construction preserves LDPC properties if the original classical-code family is LDPC.

## Rate

If the input classical-code family has asymptotically constant rate, then the resulting Campbell double homological product family also has asymptotically constant rate because both $k_Q$ and $n_Q$ scale as $n^4$  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)).

## Decoders

- The minimum-weight decoder optimizes the recovery operation $ E_{\text{rec}} $ to minimize the residual error $ E_{\text{rec}} \cdot E $ given a noisy syndrome $ s = \sigma(E) + u $. The decoder's performance is intrinsically tied to the code's soundness: when the code is $(t, f)$-sound, the minimum-weight decoder guarantees that the residual error's min-weight scales as $ f(2|u|) $ for measurement errors $ |u| < t/2 $  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)). This property is particularly robust in double homological product codes, where soundness follows a cubic scaling ($ f(x) \sim x^3 $).
- A meta-check-based decoder operates through a two-stage process: first, it identifies a minimal correction $ s_{\text{rec}} $ to the syndrome $ s $ such that the repaired syndrome $ s + s_{\text{rec}} $ satisfies all metachecks ($ H(s + s_{\text{rec}}) = 0 $). Second, it computes a minimal-weight physical error $ E_{\text{rec}} $ consistent with the repaired syndrome. This approach uniquely tolerates up to $ \lfloor (d_{*ss*} - 1)/2 \rfloor $ measurement errors in a single round (where $d_{*ss*}$ is the single-shot distance), eliminating the need for repeated syndrome measurements.

## Relations

- _parent_: [[concepts/qec/multisector-hypergraph]]
- _parent_: [[concepts/qec/single-shot]] — For a minimal input chain complex associated with a classical $[n,k,d]$ code, the Campbell double homological product code is a single-shot code with $d_{\text{ss}}=\infty$, $(d,f)$-soundness for $f(x)=x^3/4$, and check redundancy bounded by $<2$  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)).
