---
type: concept
name: Hypergraph product (HGP) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Quantum hypergraph (QHG) code
- Tillich-Zemor product code
- HP code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-hypergraph-product
- concepts/qec/homological-product
- concepts/qec/qubit-concatenated
- concepts/qec/reinforcement-learning
- concepts/qec/sc-qldpc
- concepts/qec/stab-4-2-2
- concepts/qec/xyz-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hypergraph_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hypergraph_product
---

# Hypergraph product (HGP) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hypergraph_product) (`code_id: hypergraph_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of a family of CSS codes whose stabilizer generator matrix is obtained from a hypergraph product of two classical linear binary codes.

More technically, the $X$- and $Z$-type stabilizer generator matrices of a hypergraph product code are, respectively, the boundary and coboundary operators of the 2-complex obtained from the tensor product of a chain complex and cochain complex corresponding to two classical linear binary *seed* codes.
Let the two seed codes be $C_i$ for $i\in\{1,2\}$ with parameters $[n_i, k_i, d_i]$, defined as the kernel of $r_i \times n_i$ check matrices $H_i$ of rank $n_i - k_i$.
The hypergraph product yields two classical codes $C_{X,Z}$ with parity-check matrices
\begin{align}
  H_{X}&=\begin{pmatrix}H_{1}\otimes I_{n_{2}} & \,\,I_{r_{1}}\otimes H_{2}^{T}\end{pmatrix}\\
  H_{Z}&=\begin{pmatrix}I_{n_{1}}\otimes H_{2} & \,\,H_{1}^{T}\otimes I_{r_{2}}\end{pmatrix}~,
\end{align}
where $I_m$ is the $m$-dimensional identity matrix.
These two codes then yield a hypergraph product code via the CSS construction.
The case when the two seed codes are equal, $C_1=C_2$, is called a *square hypergraph product code*.
If, in addition, $\text{im} H = \text{im} H^T$, the hypergraph product code is called a *symmetric hypergraph product code*  ([arXiv:2204.10812](https://arxiv.org/abs/2204.10812)).

In terms of the \ref{topic:CSS-to-homology-correspondence}, the hypergraph product can be viewed as a homological product of two length-one chain complexes. The resulting code corresponds to the length-two chain complex that is called the *total chain complex* of the product of the input complexes (see  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879))).

(source: raw/error-correction-zoo.md)

## Protection

If $[n_i, k_i, d_i]$ and $[r_i, k_i^T, d_i^T]$ are the parameters of the codes $\mathrm{ker}H_i$ and $\mathrm{ker}H_i^T$, respectively, taking $d_i^T=\infty$ when $k_i^T=0$, then the hypergraph product has parameters $⟦n_1 n_2 + r_1 r_2, k_1 k_2 + k_1^T k_2^T, \min(d_1, d_2, d_1^T, d_2^T)⟧$.

An algebraic reformulation of HGP codes, together with rate-improved square, symmetric, and two-tile variants, was given in Ref.  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).
Using square seed parity-check matrices yields $⟦2n_1 n_2,2k_1 k_2,\min(d_1,d_2)⟧$, symmetric seeds yield $⟦n_1 n_2,k_1 k_2,\min(d_1,d_2)⟧$, and two-tile cyclic constructions yield $⟦n_1^2,2k_1^2,d_1⟧$; these variants improve the rate of the original Tillich-Zemor family by factors up to four at small block length  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).

## Encoders

- Fault-tolerant state preparation via dimension jump  ([arXiv:2410.05171](https://arxiv.org/abs/2410.05171)).

## Transversal gates

- Hadamard (up to logical SWAP gates) and control-$Z$ on all logical qubits  ([arXiv:2204.10812](https://arxiv.org/abs/2204.10812)).
- Patch-transversal gates inherited from the automorphism group of the underlying classical codes  ([arXiv:2309.11719](https://arxiv.org/abs/2309.11719)).
- Orientation-preserving constant-depth circuits can only implement gates in the Clifford group  ([arXiv:2507.16797](https://arxiv.org/abs/2507.16797)).
- Permutation-based gates (automorphism gadgets) can be inherited from the underlying classical codes in the hypergraph construction  ([arXiv:2508.04794](https://arxiv.org/abs/2508.04794)).

## Decoders

- Single-ancilla syndrome extraction circuits do not admit hook errors  ([arXiv:2409.02193](https://arxiv.org/abs/2409.02193)).
- ReShape decoder that uses minimum weight decoders for the classical codes used in the hypergraph construction  ([arXiv:2105.02370](https://arxiv.org/abs/2105.02370)).
- 2D geometrically local syndrome extraction circuits with depth order $O(\sqrt{n})$ using order $O(n)$ ancilla qubits  ([arXiv:2109.14599](https://arxiv.org/abs/2109.14599)).
- BP-OSD decoder  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703)) and an improved BP-OSD decoder  ([arXiv:2206.03122](https://arxiv.org/abs/2206.03122)).
- Erasure correction can be implemented approximately with $O(n^2)$ operations with quantum generalizations  ([arXiv:2208.01002](https://arxiv.org/abs/2208.01002)) of the peeling and pruned peeling decoders  ([doi:10.1109/18.910575](https://doi.org/10.1109/18.910575)), with a probabilistic version running in $O(n^{1.5})$ operations. Other nearly optimal erasure decoders exist  ([arXiv:2411.08177](https://arxiv.org/abs/2411.08177), [arXiv:2412.08817](https://arxiv.org/abs/2412.08817)). Initial hypergraph product codes can be further optimized against the erasure channel using reinforcement learning  ([arXiv:2501.09622](https://arxiv.org/abs/2501.09622)).
- Syndrome measurements are distance-preserving because syndrome extraction circuits can be designed to avoid hook errors  ([arXiv:2308.15520](https://arxiv.org/abs/2308.15520)).
- Generalization  ([arXiv:2310.07868](https://arxiv.org/abs/2310.07868)) of Viderman's algorithm for expander codes  ([doi:10.1145/2493252.2493255](https://doi.org/10.1145/2493252.2493255)).
- Linear time iterative decoder  ([arXiv:2504.01728](https://arxiv.org/abs/2504.01728)).

## General gates

- Code deformation techniques yield Clifford gates  ([arXiv:1909.07424](https://arxiv.org/abs/1909.07424)).
- Pieceable fault-tolerant circuits, transversal gates, and magic-state injection yield a universal gate set for symmetric hypergraph product codes  ([arXiv:2204.10812](https://arxiv.org/abs/2204.10812)).
- Targeted logical gates  ([arXiv:2411.17050](https://arxiv.org/abs/2411.17050)).
- Logical gates via Dehn twists for hypergraph products of cyclic codes  ([arXiv:2411.03302](https://arxiv.org/abs/2411.03302)).

## Code capacity threshold

- Some thresholds were determined in Ref.  ([arXiv:1208.2317](https://arxiv.org/abs/1208.2317)).
- Bounds on code capacity thresholds using ML decoding can be obtained by mapping the effect of noise on the code to a statistical mechanical model  ([arXiv:1804.01950](https://arxiv.org/abs/1804.01950)). For example, a threshold of $7\%$ was obtained under independent $X$ and $Z$ noise for codes obtained from random $(3,4)$-regular Gallager codes.

## Fault tolerance

- Pieceable fault-tolerant circuits, transversal gates, and magic-state injection yield a universal gate set for symmetric hypergraph product codes  ([arXiv:2204.10812](https://arxiv.org/abs/2204.10812)).
- Single-ancilla syndrome extraction circuits do not admit hook errors  ([arXiv:2409.02193](https://arxiv.org/abs/2409.02193)).
- There is a fault-tolerant universal computation scheme for hypergraph-product codes concatenated with the $⟦4,2,2⟧$ code in which the full syndrome measurement on the lower hypergraph product code is performed only if an error is detected at the upper four-qubit code  ([arXiv:2502.14835](https://arxiv.org/abs/2502.14835)).

## Threshold

- Circuit-level noise: $0.1\%$ with all-to-all connected syndrome extraction circuits  ([arXiv:2109.14599](https://arxiv.org/abs/2109.14599)) and DiVincenzo-Aliferis syndrome extraction circuits  ([arXiv:quant-ph/0607047](https://arxiv.org/abs/quant-ph/0607047)) combined with non-local gates  ([arXiv:2409.05818](https://arxiv.org/abs/2409.05818)). No threshold observed above physical noise rates at or above $10^{-6}$ using 2D geometrically local syndrome extraction circuits.

## Relations

- _parent_: [[concepts/qec/homological-product]] — A homological-product code of length-one chain complexes reduces to an HGP code, which is also a special case of multi-dimensional homological products of two length-one chain complexes.
- _parent_: [[concepts/qec/sc-qldpc]] — Hypergraph-product stabilizer generator matrices can be used as sub-matrices to define a 2D SC-QLDPC code  ([arXiv:2305.00137](https://arxiv.org/abs/2305.00137)).
- _parent_: [[concepts/qec/galois-hypergraph-product]] — Hypergraph product codes are Galois-qudit hypergraph-product codes for qudit dimension $q=2$.
- _cousin_: [`ltc`](https://errorcorrectionzoo.org/c/ltc) — Applying the hypergraph product to an LTC yields a code which provides an explicit example of *No Low-Error Trivial States (NLETS)*  ([arXiv:1510.02082](https://arxiv.org/abs/1510.02082)).
- _cousin_: [[concepts/qec/xyz-product]] — Hypergraph (XYZ) product codes are constructed out of hypergraph products of two (three) classical linear codes.
- _cousin_: [[concepts/qec/reinforcement-learning]] — Using reinforcement learning, hypergraph product codes can be further optimized against the erasure channel  ([arXiv:2501.09622](https://arxiv.org/abs/2501.09622)) and can be weight reduced while maintaining distance  ([arXiv:2502.14372](https://arxiv.org/abs/2502.14372)).
- _cousin_: [[concepts/qec/stab-4-2-2]] — There is a fault-tolerant universal computation scheme for hypergraph-product codes concatenated with the $⟦4,2,2⟧$ code in which the full syndrome measurement on the lower hypergraph product code is performed only if an error is detected at the upper four-qubit code  ([arXiv:2502.14835](https://arxiv.org/abs/2502.14835)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — There is a fault-tolerant universal computation scheme for hypergraph-product codes concatenated with the $⟦4,2,2⟧$ code in which the full syndrome measurement on the lower hypergraph product code is performed only if an error is detected at the upper four-qubit code  ([arXiv:2502.14835](https://arxiv.org/abs/2502.14835)).

## Notes

- A database of hypergraph-product codes is available in QECDB .
