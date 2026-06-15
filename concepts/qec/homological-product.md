---
type: concept
name: Homological product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Tensor product code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fiber-bundle
- concepts/qec/multisector-hypergraph
- concepts/qec/random-stabilizer
- concepts/qec/single-shot
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/homological_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: homological_product
---

# Homological product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/homological_product) (`code_id: homological_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

CSS code formulated using the tensor product of two chain complexes of length one or greater (see \ref{topic:CSS-to-homology-correspondence}).

Homological products and ordinary tensor products of chain complexes differ in a way that depends on whether the underlying code is defined by a general or a length-three chain complex  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)).

(source: raw/error-correction-zoo.md)

## Protection

Given two codes $⟦n_i, k_i, d_i, w_i⟧$ for $i\in\{1,2\}$, where $w_i$ denotes the maximum hamming weight of all rows and columns of $\partial_i$, the homological product code has parameter $⟦n=n_1 n_2, k=k_1 k_2, d\leq d_1 d_2, w\leq w_1+w_2⟧$.
From this formula, and the fact that a randomly selected boundary operator $\partial$ yields a CSS code that is good with high probability, we see that the product code has $k=\Theta(n)$ and $w=O(\sqrt{n})$ with high probability.
The main result in Ref.  ([arXiv:1311.0885](https://arxiv.org/abs/1311.0885)) is to show that the product code has linear distance with high probability as well.
To sum up, it is shown that we have a family of $⟦n,k=c_1 n, d=c_2 n, w=c_3 \sqrt{n}⟧$ codes given small enough $c_1,c_2,c_3$.

## General gates

- Universal set of gates can be obtained by fault-tolerantly mapping between different encoded representations of a given logical state  ([arXiv:1807.09783](https://arxiv.org/abs/1807.09783)).
- Parallel Pauli product measurements via homomorphic CNOT gates  ([arXiv:2407.18490](https://arxiv.org/abs/2407.18490)).

## Fault tolerance

- Universal set of gates can be obtained by fault-tolerantly mapping between different encoded representations of a given logical state  ([arXiv:1807.09783](https://arxiv.org/abs/1807.09783)).

## Decoders

- Union-find decoder  ([arXiv:2009.14226](https://arxiv.org/abs/2009.14226)).
- BP-OSD-like post-processing  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703)).

## Relations

- _parent_: [[concepts/qec/multisector-hypergraph]] — Multi-dimensional homological products of two length-two chain complexes reduce to homological product codes.
- _parent_: [[concepts/qec/fiber-bundle]] — A fiber-bundle code can be viewed as a homological product code with a twisted product.
- _cousin_: [[concepts/qec/random-stabilizer]] — Random homological codes are asymptotically good with high probability  ([arXiv:1301.1363](https://arxiv.org/abs/1301.1363)).
- _cousin_: [[concepts/qec/single-shot]] — It is conjectured that a particular class of codes called three-dimensional product codes is single shot  ([arXiv:2009.11790](https://arxiv.org/abs/2009.11790)).
