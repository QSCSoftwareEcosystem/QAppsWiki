---
type: concept
name: $⟦7,1,3⟧$ XZZX cyclic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/twisted-xzzx
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/xzzx_7_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: xzzx_7_1_3
---

# $⟦7,1,3⟧$ XZZX cyclic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/xzzx_7_1_3) (`code_id: xzzx_7_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦7,1,3⟧$ cyclic non-CSS code whose stabilizer generators are the seven cyclic shifts of the weight-four Pauli string $XZIZXII$,
any six of which are independent.
The non-identity support of this generator is $XZZX$ (at positions 0, 1, 3, 4), making this a member of the twisted XZZX code family.
It is one of sixteen distinct indecomposable $⟦7,1,3⟧$ codes  ([arXiv:0709.1780](https://arxiv.org/abs/0709.1780)).

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{ccccccc}
  X & Z & I & Z & X & I & I \\
  I & X & Z & I & Z & X & I \\
  I & I & X & Z & I & Z & X \\
  X & I & I & X & Z & I & Z \\
  Z & X & I & I & X & Z & I \\
  I & Z & X & I & I & X & Z
\end{array}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/twisted-xzzx]] — The $⟦7,1,3⟧$ XZZX cyclic code is a cyclic non-CSS code whose generators are the cyclic shifts of the weight-four Pauli string $XZIZXII$, which has $XZZX$ support.
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
