---
type: concept
name: Subsystem homological code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Subsystem generalized surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/higher-dimensional-surface
- concepts/qec/qubit-subsystem-css
- concepts/qec/sparse-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_higher_dimensional_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_higher_dimensional_surface
---

# Subsystem homological code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_higher_dimensional_surface) (`code_id: subsystem_higher_dimensional_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A subsystem CSS code that is a subsystem version of the homological code, defined on cellulations of manifolds in arbitrary dimensions.
Gauge-group generators are of lower weight than the stabilizers of the corresponding surface code, enabling fault-tolerant syndrome extraction with simpler circuits.
The stabilizer group may contain generators of unbounded weight, distinguishing these codes from stabilizer codes with bounded-weight generators for which some logical qubits were re-assigned to be gauge qubits.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-subsystem-css]]
- _parent_: [[concepts/qec/sparse-subsystem]]
- _cousin_: [[concepts/qec/higher-dimensional-surface]] — Subsystem homological codes are subsystem versions of homological codes, with gauge-group generators of lower weight than the corresponding surface-code stabilizers.
