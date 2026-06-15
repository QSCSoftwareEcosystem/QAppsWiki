---
type: concept
name: $⟦2^r+r, 2^r-r-2, 3⟧$ Ring CPC code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cpc
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ring_cpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ring_cpc
---

# $⟦2^r+r, 2^r-r-2, 3⟧$ Ring CPC code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ring_cpc) (`code_id: ring_cpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of $⟦2^r+r, 2^r-r-2, 3⟧$ CPC codes for $r \geq 3$ whose matrices are based on the shortened version of the $[2^r-1,2^r-r-1,3]$ Hamming code.
See  ([arXiv:1611.08012](https://arxiv.org/abs/1611.08012)) for their stabilizer generator matrix.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/cpc]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [`hamming`](https://errorcorrectionzoo.org/c/hamming) — The ring CPC code is obtained from the shortened Hamming code via the CPC construction  ([arXiv:1611.08012](https://arxiv.org/abs/1611.08012)).
