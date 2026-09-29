---
type: concept
name: Homological product code
status: provisional
updated: '2026-09-29'
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

The tensor product of the chain complexes of two CSS codes $⟦n_i,k_i⟧$ yields a code with $n=n_1 n_2+m_1^X m_2^Z+m_1^Z m_2^X$ and $k=k_1 k_2+\ell_1^X \ell_2^Z+\ell_1^Z \ell_2^X$  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)) ([arXiv:2603.08711](https://arxiv.org/abs/2603.08711)).
Here, $m_i^X$ ($m_i^Z$) is the number of $X$-type ($Z$-type) stabilizer generators of code $i$.
The number of independent relations among these generators is $\ell_i^X$ ($\ell_i^Z$).
The row and column weights of the product boundary operators are at most $w_1+w_2$  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)) ([arXiv:1311.0885](https://arxiv.org/abs/1311.0885)).
Here, $w_i$ is the maximum row and column weight of the boundary operators of the $i$th complex.

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
- _cousin_: [[concepts/qec/random-stabilizer]] — Random homological codes are asymptotically good with high probability  ([arXiv:1311.0885](https://arxiv.org/abs/1311.0885)).
- _cousin_: [[concepts/qec/single-shot]] — It is conjectured that a particular class of codes called three-dimensional product codes is single shot  ([arXiv:2009.11790](https://arxiv.org/abs/2009.11790)).
