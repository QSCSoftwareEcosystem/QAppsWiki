---
type: concept
name: $U(d)$-covariant approximate erasure code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/covariant
- concepts/qec/stab-5-1-3
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/nonabelian_covariant_erasure
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: nonabelian_covariant_erasure
---

# $U(d)$-covariant approximate erasure code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/nonabelian_covariant_erasure) (`code_id: nonabelian_covariant_erasure`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Covariant code whose construction takes an arbitrary erasure-correcting code as input and yields an approximate QECC that is also covariant with respect to the unitary group.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/covariant]]
- _parent_: [[concepts/qec/approximate-qecc]] — Any finite-dimensional code covariant w.r.t. a continuous group has to be approximate because of the Eastin-Knill theorem.
- _cousin_: [[concepts/qec/stab-5-1-3]] — The five-qubit code can be used to construct an approximate code that is also covariant with respect to the unitary group.
