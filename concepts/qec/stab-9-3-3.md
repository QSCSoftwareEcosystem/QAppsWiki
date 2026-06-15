---
type: concept
name: $⟦9,3,3⟧$ Quadric code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_9_3_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_9_3_3
---

# $⟦9,3,3⟧$ Quadric code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_9_3_3) (`code_id: stab_9_3_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Nine-qubit pure Hermitian qubit code constructed from the almost MDS $[9,3,6]_4$ Hermitian self-orthogonal code.
It is the only pure Hermitian code with its parameters and is the highest-distance qubit stabilizer code for its $n$ and $k$.

The code can be constructed from the elliptic quadric in $PG(5, 2)$, or equivalently from the complement of the union of two disjoint hyperovals in $PG(2, 4)$  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)).
A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{ccccccccc}
  Y & X & X & Y & X & X & I & I & I \\
  Z & Z & X & I & I & I & X & Y & X \\
  Z & I & Z & Z & Z & I & Z & Y & I \\
  I & X & Z & Y & I & Z & I & Z & Z \\
  X & Z & Z & X & Z & Z & I & I & I \\
  X & I & X & X & X & I & X & Z & I
\end{array}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/stabilizer-over-gf4]] — The $⟦9,3,3⟧$ code is Hermitian .
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [`projective`](https://errorcorrectionzoo.org/c/projective) — The $⟦9,3,3⟧$ quadric code can be constructed from the elliptic quadric in $PG(5, 2)$  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)).
