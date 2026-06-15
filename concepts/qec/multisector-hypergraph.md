---
type: concept
name: Higher-dimensional homological product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Higher-dimensional tensor product code
- Multi-sector homological product code
- Multi-sector tensor product code
- Iterative homological product code
- Iterative tensor product code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/asymmetric-qecc
- concepts/qec/quantum-reed-muller
- concepts/qec/qubit-generalized-homological-product-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/multisector_hypergraph
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: multisector_hypergraph
---

# Higher-dimensional homological product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/multisector_hypergraph) (`code_id: multisector_hypergraph`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit CSS code formulated using a tensor product of two or more chain complexes, each of length one or greater.
The number of chain complexes participating in the product is the *dimension* of the code.
When all chain complexes are length-one, meaning that they correspond to classical codes, the code is called a *higher-dimensional HGP code* (a.k.a. multi-sector HGP code or iterative HGP code).

The stabilizer generator matrices of an $m$-dimensional homological product code are the boundary and co-boundary operators of a 2-dimensional chain complex contained within an $m$-complex that is recursively constructed by taking the tensor product of an $(m-1)$-complex and a 1-complex.
There is freedom in choosing which 2-dimensional chain complex to pick for the code.

(source: raw/error-correction-zoo.md)

## Protection

The Künneth formula gives code properties in terms of those of the underlying chain complexes.
Hypergraph products of multiple classical codes were considered first  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)).
Homological products of CSS-code and classical chain complexes are used as a building block in Hastings' weight-reduction construction  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790)), while later work studied explicit product-code families built from length-two chain complexes  ([arXiv:1805.09271](https://arxiv.org/abs/1805.09271)) (which correspond to qubit CSS codes per the qubit CSS-to-homology correspondence).

Ref.  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)) gives explicit parameter formulas for the tensor product $\mathcal{A}\times\mathcal{K}(P)$ of an $m$-complex $\mathcal{A}$ with the 1-complex $\mathcal{K}(P)$ built from an $r\times c$ binary matrix $P$.
Let $u=\mathrm{rank}(P)$ and $\delta$ be the minimum distance of the binary code with parity-check matrix $P$.
Writing $n_j$, $k_j$, $d_j$ for the block length, logical dimension, and homological distance of the $j$-th sector of $\mathcal{A}$, and primes for the corresponding parameters of the product, the Künneth theorem gives
$n_j'=n_{j-1}c+n_j r$ and $k_j'=k_{j-1}(c-u)+k_j(r-u)$.
The main result of  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)) establishes tight bounds on the homological distance:
$d_j'=\min(d_j,d_{j-1}\delta)$ when $r>u$ (P does not have full row rank), and $d_j'=d_{j-1}\delta$ when $r=u$ (P has full row rank).

## Rate

A notable special case uses a single full-row-rank $r\times c$ seed matrix $P$ (so $r=u$, $\kappa=c-r$ logical bits per block, classical distance $\delta$, row/column weights bounded by $(\omega,\upsilon)$).
Taking $a$ copies of $\mathcal{K}(P)$ and $b$ copies of the dual 1-complex $\tilde{\mathcal{K}}=\mathcal{K}(P^T)$ yields the $(a+b)$-complex $\mathcal{K}^{(a,b)}=\mathcal{K}^{\times a}\times \tilde{\mathcal{K}}^{\times b}$, which has a single non-trivial homology sector $H_a$ with
\begin{align}
  n_a&=\sum_{i=0}^{a} c^{2i} r^{a+b-2i} {a\choose i}{b\choose i} < (r+c)^{a+b}~,\\
  k_a&=\kappa^{a+b}~,
\end{align}
yielding a quantum CSS code with $d_X=\delta^a$, $d_Z=\delta^b$, and stabilizer-generator weights bounded by $(a+b)\max(\omega,\upsilon)$  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).
The parameters $a$ and $b$ can be chosen independently to trade off $X$- and $Z$-distance, enabling asymmetric codes optimized for channels with unequal bit-flip and phase-flip rates.
For asymptotically good LDPC seed-code families, these higher-dimensional HGP families have finite rate and $d_X d_Z$ scaling linearly with block length.

## Fault tolerance

- For $(a,b)$ constructions with $a,b>1$, the check matrices $G_X=K_a$ and $G_Z=K_{a+1}^T$ satisfy many linear relations coming from neighboring boundary maps; these redundant checks can be used to handle syndrome-measurement errors in repeated-measurement schemes  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).

## Transversal gates

- Transversal gates for multi-dimensional HGP codes of all dimensions lie in the Clifford group  ([arXiv:2507.16797](https://arxiv.org/abs/2507.16797)).

## General gates

- Gates in the \term{Clifford hierarchy} can be implemented via constant-depth circuits  ([arXiv:2507.16797](https://arxiv.org/abs/2507.16797)).
- Parallel Pauli product measurements via homomorphic CNOT gates for 3- and 4-dimensional HGP codes  ([arXiv:2407.18490](https://arxiv.org/abs/2407.18490)).

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]]
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — $D$-dimensional HGP codes are constructed using a hypergraph product of $D$ linear binary codes.
- _cousin_: [`binary_cyclic`](https://errorcorrectionzoo.org/c/binary_cyclic) — Higher-dimensional homological-product codes can be constructed out of CSS codes that in turn stem from cyclic codes  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)).
- _cousin_: [[concepts/qec/quantum-reed-muller]] — Higher-dimensional homological-product codes can be constructed out of quantum RM codes  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)).
- _cousin_: [`qc_ldpc`](https://errorcorrectionzoo.org/c/qc_ldpc) — Higher-dimensional hypergraph-product codes can be constructed out of QC-LDPC codes  ([arXiv:2407.18490](https://arxiv.org/abs/2407.18490)).
- _cousin_: [[concepts/qec/asymmetric-qecc]] — The $(a,b)$-complex construction yields asymmetric CSS codes with $d_X=\delta^a$ and $d_Z=\delta^b$, allowing independent tuning of the two distances for channels with unequal bit-flip and phase-flip rates  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).
