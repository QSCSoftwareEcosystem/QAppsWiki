---
type: concept
name: Smolin-Smith-Wehner (SSW) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cws
- concepts/qec/rains
- concepts/qec/self-complementary
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ssw
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ssw
---

# Smolin-Smith-Wehner (SSW) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ssw) (`code_id: ssw`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of $((n=4k+2l+3,M_{k,l},2))$ self-complementary CWS codes, where $M_{k,l} \approx 2^{n-2}(1-\sqrt{2/(\pi(n-1))})$.
For $n \geq 11$, these codes have a logical subspace whose dimension is larger than that of the largest stabilizer code for the same $n$ and $d$.
Ref.  ([arXiv:0709.1780](https://arxiv.org/abs/0709.1780)) augments a star-graph-based subfamily $((4n+1,M_n,2))$ by one additional graph-state basis word, yielding $((4n+1,M_n+1,2))$ codes with $M_n=2^{4n-1}-\frac{1}{2}\binom{4n}{2n}$.
In the CWS description of Ref.  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021)), the underlying stabilizer state is locally Clifford-equivalent to a GHZ state and its standard-form graph is a star graph.

(source: raw/error-correction-zoo.md)

## Realizations

- The $((5,5,2))$ SSW code has been realized in an NMR device  ([arXiv:1111.5445](https://arxiv.org/abs/1111.5445)).

## Relations

- _parent_: [[concepts/qec/cws]] — SSW codes can be formulated as CWS codes  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021)).
- _parent_: [[concepts/qec/self-complementary]]
- _cousin_: [[concepts/qec/rains]] — The SSW code outperforms the Rains codes in terms of code parameters at odd $n > 11$  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021)).
