---
type: concept
name: Majorana checkerboard code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Majorana cubic model code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fracton
- concepts/qec/majorana-stab
- concepts/qec/qldpc
- concepts/qec/xcube
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/majorana_checkerboard
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: majorana_checkerboard
---

# Majorana checkerboard code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/majorana_checkerboard) (`code_id: majorana_checkerboard`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A Majorana analogue of the X-cube model defined on a cubic lattice.
The code admits weight-eight Majorana stabilizer generators on the eight vertices of each cube of a checkerboard sublattice.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/majorana-stab]]
- _parent_: [[concepts/qec/qldpc]] — The Majorana checkerboard code is a 3D qubit stabilizer code with respect to the Majorana operator basis.
- _parent_: [[concepts/qec/fracton]] — The Majorana checkerboard code is a foliated type-I fracton code  ([arXiv:1904.01111](https://arxiv.org/abs/1904.01111)).
- _cousin_: [[concepts/qec/xcube]] — The Majorana checkerboard code is equivalent via a constant-depth unitary to a semionic version of the X-cube model and some decoupled fermionic modes  ([arXiv:1904.01111](https://arxiv.org/abs/1904.01111)).
