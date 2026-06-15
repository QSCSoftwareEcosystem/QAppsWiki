---
type: concept
name: Frobenius code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-cyclic
- concepts/qec/qudit-stabilizer
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/frobenius
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: frobenius
---

# Frobenius code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/frobenius) (`code_id: frobenius`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A cyclic prime-qudit stabilizer code whose length $n$ divides $p^t + 1$ for some positive integer $t$.

(source: raw/error-correction-zoo.md)

## Decoders

- Adapted from the Berlekamp decoding algorithm for classical BCH codes. There exists a polynomial-time quantum algorithm to correct errors of weight at most $\tau$, where $\delta=2\tau+1$ is the BCH distance of the code  ([arXiv:1011.5814](https://arxiv.org/abs/1011.5814)).

## Relations

- _parent_: [[concepts/qec/qudit-stabilizer]]
- _parent_: [[concepts/qec/quantum-cyclic]]
- _cousin_: [[concepts/qec/stabilizer-over-gf4]] — Frobenius Hermitian codes have been completely classified; no such codes exist when $t$ is odd  ([arXiv:1011.5814](https://arxiv.org/abs/1011.5814)).

## Notes

- Frobenius Hermitian codes have been completely classified; no such codes exist when $t$ is odd  ([arXiv:1011.5814](https://arxiv.org/abs/1011.5814)).
