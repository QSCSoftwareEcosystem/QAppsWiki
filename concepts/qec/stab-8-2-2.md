---
type: concept
name: $⟦8,2,2⟧$ hyperbolic color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hyperbolic-color
- concepts/qec/self-dual-css
- concepts/qec/shor-nine
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_8_2_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_8_2_2
---

# $⟦8,2,2⟧$ hyperbolic color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_8_2_2) (`code_id: stab_8_2_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦8,2,2⟧$ hyperbolic color code defined on the projective plane. It is a self-dual CSS code.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{cccccccc}
  Z & Z & Z & Z & I & I & I & I \\
  X & X & X & X & I & I & I & I \\
  Z & Z & I & I & Z & Z & I & I \\
  X & X & I & I & X & X & I & I \\
  Z & Z & I & I & I & I & Z & Z \\
  X & X & I & I & I & I & X & X
\end{array}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Transversal gates

- Applying transversal $S$ and $S^{\dagger}$, $\sqrt{X}$, and Hadamard gates yields various logical gates  ([arXiv:1912.10063](https://arxiv.org/abs/1912.10063)). For instance, the physical gate $S^{\dagger}_{2}S^{\dagger}_{3}S_{4}S_{5}S_{6}S_{7}CZ_{01}$ implements the logical action $\bar{S}_{0} \bar{Z}_{1} \overline{CZ}_{01}$.

## Relations

- _parent_: [[concepts/qec/hyperbolic-color]] — The $⟦8,2,2⟧$ hyperbolic color code is defined on the projective plane.
- _parent_: [[concepts/qec/stabilizer-over-gf4]] — The $⟦8,2,2⟧$ hyperbolic color code is Hermitian .
- _parent_: [[concepts/qec/self-dual-css]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/shor-nine]] — Like the Shor code, the $⟦8,2,2⟧$ hyperbolic color code is a small code defined on the projective plane.
