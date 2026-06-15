---
type: concept
name: Twist-defect color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Color code with a twist
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/qldpc
- concepts/qec/topological-abelian
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/twist_defect_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: twist_defect_color
---

# Twist-defect color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/twist_defect_color) (`code_id: twist_defect_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A non-CSS extension of the 2D color code whose non-CSS stabilizer generators are associated with twist defects of the associated lattice.
These twists terminate domain walls that permute color labels, Pauli labels, or interchange the two.

For lattices with dislocations and rotational disclinations, twist-defect stabilizer generators are placed at the location of the dislocations.
Logical dimension is determined by the genus of the underlying surface (for closed surfaces), types of boundaries (for open surfaces), and any twist defects present.

(source: raw/error-correction-zoo.md)

## Protection

Code properties depend on the number and size of the twist defects.
There are 72 types of twist defects in the 2D color code, organized by the $S_{3}\wr\mathbb{Z}_{2}$ symmetry of the anyons  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).

## General gates

- Clifford gates can be implemented via twist-based lattice surgery  ([arXiv:1709.02318](https://arxiv.org/abs/1709.02318)) or braiding twist defects
 ([arXiv:2104.03669](https://arxiv.org/abs/2104.03669)).
- Domino twists  ([arXiv:2411.05402](https://arxiv.org/abs/2411.05402)).

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/2d-stabilizer]]
- _cousin_: [[concepts/qec/topological-abelian]] — Twist-defect color codes realize $\mathbb{Z}_2 \times \mathbb{Z}_2$ topological order with twist defects.
- _cousin_: [[concepts/qec/twist-defect-surface]] — Twist-defect color codes and twist-defect surface codes both encode using twist defects in topological stabilizer codes.
