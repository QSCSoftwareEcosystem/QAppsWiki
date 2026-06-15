---
type: concept
name: Chiral semion subsystem code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/double-semion
- concepts/qec/qudit-subsystem-stabilizer
- concepts/qec/qudit-znone
- concepts/qec/topological-abelian
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/semion
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: semion
---

# Chiral semion subsystem code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/semion) (`code_id: semion`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit subsystem stabilizer code with qudit dimension $q=4$ that is characterized by the chiral semion topological phase.
The code admits a set of geometrically local stabilizer generators on a torus.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qudit-subsystem-stabilizer]]
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _parent_: [[concepts/qec/topological-abelian]] — The semion code is a subsystem code characterized by the chiral semion topological phase.
- _cousin_: [[concepts/qec/double-semion]] — The semion code can be obtained from the double-semion stabilizer code by gauging out the anyon $\bar{s}$  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
- _cousin_: [[concepts/qec/qudit-znone]] — The semion code can be obtained from the $\mathbb{Z}_4^{(1)}$ subsystem code by condensing the anyon $s^2$  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
