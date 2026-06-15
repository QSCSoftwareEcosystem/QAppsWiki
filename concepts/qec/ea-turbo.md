---
type: concept
name: EA quantum turbo code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/eastab
- concepts/qec/maximal-entanglement-galois-stabilizer
- concepts/qec/quantum-turbo
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_turbo
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_turbo
---

# EA quantum turbo code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_turbo) (`code_id: ea_turbo`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A quantum turbo code which uses pre-shared entanglement.
This allows its encoder to be both recursive and non-catastrophic.

(source: raw/error-correction-zoo.md)

## Rate

Maximal-entanglement EA quantum turbo codes come close to achieving the EA hashing bound  ([arXiv:1010.1256](https://arxiv.org/abs/1010.1256)); see  ([arXiv:1302.4150](https://arxiv.org/abs/1302.4150)).

## Encoders

- As opposed to quantum turbo codes with no pre-shared entanglement, EA encoders can be both recursive and non-catastrophic  ([arXiv:1010.1256](https://arxiv.org/abs/1010.1256)).

## Relations

- _parent_: [[concepts/qec/eastab]]
- _cousin_: [`turbo`](https://errorcorrectionzoo.org/c/turbo) — EA quantum turbo codes are entanglement-assisted quantum analogues of turbo codes.
- _cousin_: [[concepts/qec/quantum-turbo]] — EA quantum turbo codes are entanglement-assisted versions of quantum turbo codes.
- _cousin_: [[concepts/qec/maximal-entanglement-galois-stabilizer]] — Maximal-entanglement EA quantum turbo codes come close to achieving the EA hashing bound  ([arXiv:1010.1256](https://arxiv.org/abs/1010.1256)); see  ([arXiv:1302.4150](https://arxiv.org/abs/1302.4150)).
