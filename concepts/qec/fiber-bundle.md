---
type: concept
name: Fiber-bundle code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Twisted product code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/balanced-product
- concepts/qec/distance-balanced
- concepts/qec/lifted-product
- concepts/qec/qubit-generalized-homological-product-css
- concepts/qec/random-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fiber_bundle
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fiber_bundle
---

# Fiber-bundle code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fiber_bundle) (`code_id: fiber_bundle`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CSS code constructed by combining one code as the base and another as the fiber of a fiber bundle.
In particular, taking a random LDPC code as the base and a cyclic repetition code as the fiber yields, after distance balancing, a QLDPC code with distance of order $\Omega( n^{3/5}/\text{polylog}(n) )$ and rate of order $\Omega( n^{-2/5}/\text{polylog}(n) )$.

(source: raw/error-correction-zoo.md)

## Rate

Rate $k/n = \Omega( n^{-2/5}/\text{polylog}(n) )$, distance $d=\Omega( n^{3/5}/\text{polylog}(n) )$. This is the first QLDPC code to achieve a distance scaling better than $\sqrt{n}~\text{polylog}(n)$.

## Decoders

- Greedy algorithm can be used to efficiently decode $X$ errors, but no known efficient decoding of $Z$ errors yet  ([arXiv:2009.03921](https://arxiv.org/abs/2009.03921)).

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]]
- _parent_: [[concepts/qec/balanced-product]] — Fiber-bundle codes can be formulated in terms of a balanced product  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271)).
- _cousin_: [[concepts/qec/lifted-product]] — The specific fiber-bundle QLDPC code achieving a distance scaling better than $\sqrt{n}~\text{polylog}(n)$ can also be formulated directly as an LP code (see published version of Ref. ([arXiv:2009.03921](https://arxiv.org/abs/2009.03921))).
Lifted products of a length-one with a length-$m$ chain complex can be thought of as fiber-bundle codes  ([arXiv:2012.09271](https://arxiv.org/abs/2012.09271)).
- _cousin_: [[concepts/qec/distance-balanced]] — Fiber-bundle code constructions use distance balancing and weight reduction to increase distance.
- _cousin_: [[concepts/qec/random-stabilizer]] — Taking a random LDPC code as the base and a cyclic repetition code as the fiber yields, after distance balancing, a QLDPC code with distance of order $\Omega( n^{3/5}\text{polylog}(n) )$ and rate of order $\Omega( n^{-2/5}\text{polylog}(n) )$.
