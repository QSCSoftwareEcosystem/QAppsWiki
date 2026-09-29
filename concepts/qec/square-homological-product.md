---
type: concept
name: Square homological product code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Single-sector homological code
- Bravyi-Hastings homological code
- Square tensor product code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/homological-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/square_homological_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: square_homological_product
---

# Square homological product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/square_homological_product) (`code_id: square_homological_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Homological product code whose underlying quantum-code boundary operators are square matrices (see \ref{topic:CSS-to-homology-correspondence}).

Each base code is associated with the chain complex $ C_i \longrightarrow C_i\longrightarrow C_i$ such that the boundary operator (a.k.a. parity-check matrix) satisfies $H_i^{2}=0$  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)). 
The parity-check matrix of the resulting product code is 
\begin{align}
  H_1 \otimes I_2 + I_1 \otimes H_2~,
\end{align}
where $I_i$ is the identity on the check space of code $i$.

(source: raw/error-correction-zoo.md)

## Protection

The product of two codes $⟦n_i,k_i⟧$ is an $⟦n_1 n_2,k_1 k_2⟧$ code  ([arXiv:1311.0885](https://arxiv.org/abs/1311.0885)).
Its $X$-type and $Z$-type distances satisfy $\max(d_1^{\alpha},d_2^{\alpha})\leq d^{\alpha}\leq d_1^{\alpha}d_2^{\alpha}$ for $\alpha\in\{X,Z\}$  ([arXiv:1311.0885](https://arxiv.org/abs/1311.0885)).
The product of two random codes of length $M$ and dimension $\rho M$ has distance $\Omega(M^2)$ with high probability for small enough $\rho>0$  ([arXiv:1311.0885](https://arxiv.org/abs/1311.0885)).
This yields a family of $⟦n,\Theta(n),\Theta(n)⟧$ codes with stabilizer weight $O(\sqrt{n})$  ([arXiv:1311.0885](https://arxiv.org/abs/1311.0885)).
Square homological-product codes admit different properties than those with rectangular boundary operators  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)).

## Relations

- _parent_: [[concepts/qec/homological-product]] — Square homological product codes are homological product codes whose boundary operators are square matrices  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)).
