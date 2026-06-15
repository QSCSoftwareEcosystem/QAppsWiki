---
type: concept
name: $⟦8,1,2⟧$ Shen-Wang-Cao code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-lego
- concepts/qec/qubit-css
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-15-1-3
- concepts/qec/xp-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_8_1_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_8_1_2
---

# $⟦8,1,2⟧$ Shen-Wang-Cao code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_8_1_2) (`code_id: stab_8_1_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A stabilizer code that admits a logical $T$ gate via application of physical $T$ gates and a $CZ$-like gate.

A stabilizer tableau for the code is given by .
\begin{align}
\begin{array}{cccccccc}
  X & X & I & I & X & X & I & I \\
  I & I & X & X & X & X & I & I \\
  I & I & I & I & I & I & X & X \\
  Z & I & I & Z & I & Z & Z & Z \\
  I & Z & I & Z & I & Z & Z & Z \\
  I & I & Z & Z & I & I & I & I \\
  I & I & I & I & Z & Z & I & I
\end{array}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Transversal gates

- Logical $T$ gate $\bar{T}=T^{\otimes 6}\otimes K$ via physical $T$ gates on the first six qubits and the two-qubit gate $K\propto\cos(\pi/8)(I\otimes I)-i\sin(\pi/8)(Z\otimes Z)\propto\mathrm{diag}(1,e^{i\pi/4},e^{i\pi/4},1)$ on qubits 7 and 8  ([arXiv:2310.19538](https://arxiv.org/abs/2310.19538)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/xp-stabilizer]] — The $⟦8,1,2⟧$ code is an XP-regular code that can be obtained via the XP stabilizer formalism applied to the $⟦15,1,3⟧$ Reed-Muller code  ([arXiv:2310.19538](https://arxiv.org/abs/2310.19538)).
- _cousin_: [[concepts/qec/stab-15-1-3]] — The $⟦8,1,2⟧$ code is an XP-regular code that can be obtained via the XP stabilizer formalism applied to the $⟦15,1,3⟧$ Reed-Muller code  ([arXiv:2310.19538](https://arxiv.org/abs/2310.19538)).
- _cousin_: [[concepts/qec/quantum-lego]] — The $⟦8,1,2⟧$ code is an XP-regular code that can be obtained via the XP stabilizer formalism applied to the $⟦15,1,3⟧$ Reed-Muller code  ([arXiv:2310.19538](https://arxiv.org/abs/2310.19538)).
