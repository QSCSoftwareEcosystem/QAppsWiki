---
type: concept
name: Lifted-product (LP) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Panteleev-Kalachev (PK) code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/balanced-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/lifted_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: lifted_product
---

# Lifted-product (LP) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/lifted_product) (`code_id: lifted_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Galois-qudit code that utilizes the notion of a lifted product in its construction. Lifted products of certain classical Tanner codes are the first (asymptotically) *good QLDPC codes*.

A code can be defined by $LP(A,B)$, where $A$ and $B$ are a pair of matrices with elements from a group algebra.
Heuristically, the code is constructed as a hypergraph product code over the group algebra, with each entry subsequently extended into a matrix.

More technically, a *lifted product over* a ring $R$ is a product of two chain complexes whose chains are free modules over $R$.
An interesting case is when $R=\mathbb{F}_q [G]$, the group-$G$ algebra over the finite field ${\mathbb{F}}_q = \mathbb{F}_q$; in this case, the product can be called a $G$-*lifted product*.
Just like its further generalization the balanced product, a lifted product code generalizes a hypergraph product code in that a reduction of symmetry is exploited to decrease the number of physical qubits required.
The first version of this construction appeared as a family of generalized hypergraph product codes that contains hypergraph product codes in the case where one of the two input parity-check matrices is square  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703)).

The key operation behind the $G$-lifted product is the $G$-*lift*, a group-algebraic version of the lifting procedure of protograph LDPC codes.
A combination of the lift and the usual hypergraph product yields lifted-product codes.
The two operations commute: one can first take the usual hypergraph product of two chain complexes, and then lift the resulting product complex; equivalently, one can take the hypergraph product of the two lifted complexes.

(source: raw/error-correction-zoo.md)

## Protection

Code performance strongly depends on the group $G$ used in the product  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068)).

## Rate

There is no known simple way to compute the logical dimension $k$ in the general case  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068)).

## General gates

- Transversal dimension jump, a code switching protocol between two LP codes  ([arXiv:2510.07269](https://arxiv.org/abs/2510.07269)).

## Decoders

- Linear time iterative decoder  ([arXiv:2504.01728](https://arxiv.org/abs/2504.01728)).

## Relations

- _parent_: [[concepts/qec/balanced-product]] — Coarsely speaking, a lifted product is a balanced product where the group $G$ acts freely. In principle, a lifted product can be defined for rings that are more general than group algebras $ \mathbb{F}_q G $.

## Notes

- Formerly known as *generalized hypergraph product codes*  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703)), and later renamed to lifted-product codes  ([arXiv:2012.04068](https://arxiv.org/abs/2012.04068), [arXiv:2103.06309](https://arxiv.org/abs/2103.06309)).
