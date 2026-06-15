---
type: concept
name: Khesin-Lu-Shor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-css
- concepts/qec/steane
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/kls
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: kls
---

# Khesin-Lu-Shor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/kls) (`code_id: kls`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of $⟦m 2^m / (m+1), 2^m / (m+1), d(m)⟧$ qubit CSS codes derived from the Hamming code, where $m = 2^r - 1$.
Their encoder-respecting form is the graph of a hypercube in $m$ dimensions, and input nodes in the graph are codewords of the $[2^r-1,2^r-r-1,3]$ Hamming code  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).

(source: raw/error-correction-zoo.md)

## Protection

The code distance satisfies $\lfloor (m-1)/2 \rfloor \leq d(m) \leq m$ and is conjectured to be $m$ for $m \geq 7$  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).

## Decoders

- A greedy graph decoder on the hypercube representation corrects at least $\lfloor (m-1)/4 \rfloor - 1$ Pauli errors  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _cousin_: [`hamming`](https://errorcorrectionzoo.org/c/hamming) — The encoder-respecting form of the $⟦m 2^m / (m+1), 2^m / (m+1), d(m)⟧$ Khesin-Lu-Shor code is the graph of a hypercube in $m = 2^r - 1$ dimensions, and input nodes in the graph are codewords of the $[2^r-1,2^r-r-1,3]$ Hamming code  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).
- _cousin_: [`hypercube`](https://errorcorrectionzoo.org/c/hypercube) — The encoder-respecting form of the $⟦m 2^m / (m+1), 2^m / (m+1), d(m)⟧$ Khesin-Lu-Shor code is the graph of a hypercube in $m = 2^r - 1$ dimensions, and input nodes in the graph are codewords of the $[2^r-1,2^r-r-1,3]$ Hamming code  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).
- _cousin_: [[concepts/qec/steane]] — The encoder-respecting form of both the Steane and Khesin-Lu-Shor codes is the graph of a hypercube  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).
