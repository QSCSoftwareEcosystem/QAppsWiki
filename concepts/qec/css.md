---
type: concept
name: Calderbank-Shor-Steane (CSS) stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: css
---

# Calderbank-Shor-Steane (CSS) stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/css) (`code_id: css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A stabilizer code admitting a set of stabilizer generators that are either $Z$-type or $X$-type operators.
The two sets of stabilizer generators can often be related to parts of a chain complex over the appropriate ring or field.

CSS codes can also be viewed as an instance of a two-step convex-geometric construction: one first chooses an intermediate subspace stabilized by one type of generator, and then imposes the other type of generator so that the remaining diagonal error slopes vanish via an application of the Tverberg theorem .

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/stabilizer]]
- _parent_: [`group_gkp`](https://errorcorrectionzoo.org/c/group_gkp) — CSS codes are Abelian group GKP codes, i.e., group GKP codes constructed out of Pauli-type operators.
