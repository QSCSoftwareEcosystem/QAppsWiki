---
type: concept
name: Balanced product (BP) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/distance-balanced
- concepts/qec/galois-css
- concepts/qec/generalized-homological-product-css
- concepts/qec/qubit-subsystem-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/balanced_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: balanced_product
---

# Balanced product (BP) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/balanced_product) (`code_id: balanced_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Family of CSS quantum codes obtained from two classical-code chain complexes that share a common group symmetry.
The balanced product can be understood as taking the usual tensor or hypergraph product and then quotienting by the shared symmetry action.
This can reduce the overall number of physical qubits $n$ while, in favorable cases, preserving the number of encoded qubits and the code distance, thereby improving the encoding rate $k/n$ and normalized distance $d/n$ compared to the underlying tensor or hypergraph product.

For trivial group action, the construction reduces to a hypergraph product code.
For cyclic groups, it overlaps with fiber-bundle and lifted-product constructions  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271)).

(source: raw/error-correction-zoo.md)

## Rate

The original explicit balanced-product family is first constructed as a horizontal subsystem code with $k \in \Theta(n^{2/3})$, $d_X \in \Omega(n^{1/3})$, and $d_Z \in \Theta(n)$; after distance balancing, it yields an LDPC family with $k \in \Theta(n^{4/5})$ and $d \in \Omega(n^{3/5})$  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271)). For balanced products of two good classical LDPC codes over groups of order $\Theta(n)$, the original paper proves constant encoding rate and conjectures linear distance  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271)).

## General gates

- Logical gates via Dehn twists for balanced products of cyclic codes  ([arXiv:2411.03302](https://arxiv.org/abs/2411.03302)).

## Decoders

- BP-OSD decoder  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703)).

## Relations

- _parent_: [[concepts/qec/galois-css]]
- _parent_: [[concepts/qec/generalized-homological-product-css]] — Balanced product codes result from a tensor product of two classical-code chain complexes, followed by a factoring out of certain symmetries.
- _cousin_: [[concepts/qec/qubit-subsystem-stabilizer]] — The original explicit balanced-product family is first constructed as a horizontal subsystem balanced-product code built from expander codes and cyclic repetition codes  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271)).
- _cousin_: [[concepts/qec/distance-balanced]] — Applying distance balancing to the explicit subsystem balanced-product family of Ref.  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271)) yields an LDPC code family with $k \in \Theta(n^{4/5})$ and $d \in \Omega(n^{3/5})$.
