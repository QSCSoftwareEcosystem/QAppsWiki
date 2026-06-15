---
type: concept
name: $⟦14,3,3⟧$ Rhombic dodecahedron surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Landahl jaunty code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rhombic_dodecahedron_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rhombic_dodecahedron_surface
---

# $⟦14,3,3⟧$ Rhombic dodecahedron surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rhombic_dodecahedron_surface) (`code_id: rhombic_dodecahedron_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦14,3,3⟧$ twist-defect surface code whose qubits lie on the vertices of a rhombic dodecahedron.
Its non-CSS nature is due to twist defects  ([arXiv:1004.1838](https://arxiv.org/abs/1004.1838)) stemming from the geometry of the polytope.
A local-Clifford-equivalent clean realization has only $X$- and $Z$-type operators on its four-valent vertices, and its symplectic double is a $⟦28,6,3⟧$ genus-three code  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).

A stabilizer tableau for the code is  ([arXiv:2010.06628](https://arxiv.org/abs/2010.06628))
\begin{align}
\begin{smallmatrix}
  X & X & X & I & I & X & I & I & I & I & I & I & I & I \\
  I & I & X & X & I & I & X & X & I & I & I & I & I & I \\
  I & I & I & I & I & I & I & X & X & I & I & X & X & I \\
  X & I & I & I & I & I & I & I & I & X & I & I & X & X \\
  I & Y & Y & Y & Y & I & I & I & I & I & I & I & I & I \\
  I & I & Y & I & I & Y & Y & I & I & I & Y & I & I & I \\
  I & I & I & I & Y & I & I & I & Y & Y & I & I & Y & I \\
  I & I & I & I & I & I & I & I & I & I & Y & Y & Y & Y \\
  Z & Z & I & I & Z & I & I & I & I & Z & I & I & I & I \\
  I & I & I & Z & Z & I & I & Z & Z & I & I & I & I & I \\
  I & I & I & I & I & I & Z & Z & I & I & Z & Z & I & I
\end{smallmatrix}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/twist-defect-surface]] — The rhombic dodecahedron surface code is a twist-defect surface code whose degree-three vertices can be interpreted as disclination twists  ([arXiv:2010.06628](https://arxiv.org/abs/2010.06628)).
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [`rhombic_dodecahedron`](https://errorcorrectionzoo.org/c/rhombic_dodecahedron) — The qubits of the $⟦14,3,3⟧$ rhombic dodecahedron surface code lie on the vertices of the small rhombic dodecahedron.
