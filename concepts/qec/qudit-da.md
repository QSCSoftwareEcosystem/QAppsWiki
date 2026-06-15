---
type: concept
name: Modular-qudit dynamical code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Modular-qudit DA code
- Modular-qudit aperiodic Floquet code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dynamic-gen
- concepts/qec/qudits-into-qudits
- concepts/qec/random-stabilizer
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_da
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_da
---

# Modular-qudit dynamical code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_da) (`code_id: qudit_da`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Dynamically generated stabilizer-based modular-qudit code whose (not necessarily periodic) sequence of few-body measurements implements state initialization, logical gates and error detection.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qudits-into-qudits]]
- _parent_: [[concepts/qec/dynamic-gen]] — Dynamical code state initialization, logical gates, and error correction are done by a sequence of different (usually weight-two) stabilizer measurements.
- _cousin_: [[concepts/qec/random-stabilizer]] — Dynamical codes admit instantaneous stabilizer groups, and dynamical code state initialization, logical gates, and error correction are done by a sequence of different (usually weight-two) stabilizer measurements.
- _cousin_: [[concepts/qec/translationally-invariant-stabilizer]] — Dynamical codes are typically defined on 2D and 3D lattices, but they are not conventional stabilizer codes in that they use code switching for error correction and gates.
