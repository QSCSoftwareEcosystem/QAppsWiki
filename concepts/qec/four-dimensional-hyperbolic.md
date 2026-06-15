---
type: concept
name: Guth-Lubotzky code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hyperbolic-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/four_dimensional_hyperbolic
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: four_dimensional_hyperbolic
---

# Guth-Lubotzky code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/four_dimensional_hyperbolic) (`code_id: four_dimensional_hyperbolic`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Homological linear-rate code based on cellulations of certain 4D hyperbolic manifolds with particular homology and systolic properties.

Guth and Lubotzky  ([arXiv:1310.5555](https://arxiv.org/abs/1310.5555)) show that there exists $\epsilon$, a 4D hyperbolic manifold $M$, and a sequence of manifolds $M_i$ such that
each $M_i$ is a finite sheeted covering of $M$, and the 4D volumes of the manifolds $\text{Vol}_4(M_i)$ of the sequence tend to infinity.
Also, the dimension of the second homology and size of systoles are bounded by $H_2(M_i, \mathbb{Z}_2) \geq \frac{\text{Vol}_4(M_i)}{100}$ and $\text{Sys}_2(M_i) \geq \text{Vol}_4(M_i)^\epsilon$, respectively.

Then given any cellulation of $M$, it can naturally be extended to cellulations for each of the manifolds $M_i$ and used to define CSS codes via the homological construction by choosing the size three chain complex consisting of the $3,2$ and $1$-cells of the cellulations.

For dense cellulations (i.e. large $n$) the number of physical qubits for these codes will scale with the volume of the manifolds.
Therefore, bounds on the dimension of the second homology and size of systoles are achieved in terms of $n$ for large $n$.

(source: raw/error-correction-zoo.md)

## Protection

Protection stems from the relationship between properties of manifolds and CSS codes derived from their cellulation. The number of physical $k$ qubits and distance $d$ of the code will scale as order $\Omega(n)$ and $\Omega(n^\epsilon)$, respectively. A later explicit construction yields codes with $d \geq c n^{0.2}$, while the same work notes the upper bound $d = O(n^{0.3})$ for the Guth-Lubotzky construction  ([arXiv:1610.03870](https://arxiv.org/abs/1610.03870)).

## Rate

An explicit construction based on Coxeter groups yields a lower bound of $13/72$ on the asymptotic rate  ([arXiv:2001.03568](https://arxiv.org/abs/2001.03568)).

## Threshold

- Phenomenological noise: data is consistent with a threshold of about $4\%$ using BP-OSD or cellular-automaton decoders  ([arXiv:2001.03568](https://arxiv.org/abs/2001.03568)).

## Relations

- _parent_: [[concepts/qec/hyperbolic-surface]]
