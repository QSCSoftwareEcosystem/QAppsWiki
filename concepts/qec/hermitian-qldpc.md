---
type: concept
name: Camara-Ollivier-Tillich code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hermitian_qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hermitian_qldpc
---

# Camara-Ollivier-Tillich code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hermitian_qldpc) (`code_id: hermitian_qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A Hermitian qubit QLDPC code whose stabilizer generator matrix is constructed using two nested subgroups of $\mathbb{F}_4^n$.

Examples include a $(4,8)$-regular 8736-qubit code and a $(4,8)$-regular 3600-qubit code, both of rate one half.

(source: raw/error-correction-zoo.md)

## Decoders

- Iterative error estimation based on the MIN-SUM and SUM-PRODUCT algorithms  ([arXiv:quant-ph/0502086](https://arxiv.org/abs/quant-ph/0502086)).

## Relations

- _parent_: [[concepts/qec/stabilizer-over-gf4]]
