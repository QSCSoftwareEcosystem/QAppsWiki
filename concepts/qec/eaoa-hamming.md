---
type: concept
name: $⟦10,1,3;1,3,4⟧$ EAOA Hamming code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/eaoa-stabilizer
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/eaoa_hamming
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: eaoa_hamming
---

# $⟦10,1,3;1,3,4⟧$ EAOA Hamming code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/eaoa_hamming) (`code_id: eaoa_hamming`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An EAOA qubit stabilizer code constructed from the dual of a $[10,6,3]$ code obtained by shortening the classical $[15,11,3]$ Hamming code at five positions.
In the notation of the parent entry, the example of Ref.  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)) is a $⟦10,1,3;1,3,4⟧$ code: it encodes one logical qubit and four classical strings (equivalently, two classical bits), while retaining one gauge qubit and using three ebits.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/eaoa-stabilizer]]
- _cousin_: [`hamming`](https://errorcorrectionzoo.org/c/hamming) — The dual of a $[10,6,3]$ code obtained by shortening the $[15,11,3]$ Hamming code at five positions can be used to construct $⟦10,1,3;1,3,4⟧$ EAOA Hamming code  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).
- _cousin_: [[concepts/qec/small-distance-qubit-stabilizer]]
