---
type: concept
name: $⟦7,1,3⟧$ twist-defect surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $⟦7,1,3⟧$ triangle code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/triangle-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/twist_defect_7_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: twist_defect_7_1_3
---

# $⟦7,1,3⟧$ twist-defect surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/twist_defect_7_1_3) (`code_id: twist_defect_7_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦7,1,3⟧$ code (different from the Steane code) that is a small example of a twist-defect surface code.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{ccccccc}
  X & I & I & I & I & I & Z \\
  I & X & I & I & I & Z & I \\
  I & I & X & I & Z & I & I \\
  I & I & Z & X & X & Z & I \\
  I & Z & I & Y & I & Y & Z \\
  Z & I & I & Z & Z & I & X
\end{array}~.
\end{align}
It is one of sixteen distinct indecomposable $⟦7,1,3⟧$ codes  ([arXiv:0709.1780](https://arxiv.org/abs/0709.1780)).

(source: raw/error-correction-zoo.md)

## Protection

Fully fault-tolerant depolarizing-noise designs using $13$ or $15$ total qubits, including ancillas, have exREC pseudothresholds of order $10^{-4}$  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## Transversal gates

- Admits certain transversal order-three single-qubit Clifford gates (e.g., $SH$)  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## General gates

- Within the triangle-code architecture, supports the full logical Clifford group using lattice surgery, 1-bit teleportation, and patch reorientation  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## Relations

- _parent_: [[concepts/qec/triangle-surface]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
