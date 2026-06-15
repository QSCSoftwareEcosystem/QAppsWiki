---
type: concept
name: $⟦8,3,2⟧$ Surface code on a cube
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Landahl plucky code
- Cubic surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cubic_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cubic_surface
---

# $⟦8,3,2⟧$ Surface code on a cube

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cubic_surface) (`code_id: cubic_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦8,3,2⟧$ twist-defect surface code whose qubits lie on the vertices of a cube.
It is obtained by three-coloring the faces of a cube and placing $X$, $Y$, and $Z$ stabilizer generators on each pair of faces of the same color.
Its non-CSS nature is due to twist defects  ([arXiv:1004.1838](https://arxiv.org/abs/1004.1838)) stemming from the geometry of the polytope.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{cccccccc}
  I & Y & Y & I & Z & I & Z & I \\
  X & I & Z & Z & X & I & I & I \\
  I & X & I & X & Y & Y & I & I \\
  I & Z & I & I & I & Z & X & Z \\
  Z & I & I & Y & I & X & I & Y
\end{array}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/twist-defect-surface]] — The surface code on a cube is a twist-defect surface code whose degree-three vertices can be interpreted as disclination twists  ([arXiv:2010.06628](https://arxiv.org/abs/2010.06628)).
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [`hypercube`](https://errorcorrectionzoo.org/c/hypercube) — The surface code on a cube, whose qubits lie on the vertices of a cube, is obtained by three-coloring the faces of a cube and placing $X$, $Y$, and $Z$ stabilizer generators on each pair of faces of the same color.
