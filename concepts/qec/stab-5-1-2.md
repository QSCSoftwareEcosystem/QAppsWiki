---
type: concept
name: $⟦5,1,2⟧$ rotated surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $⟦5,1,2⟧$ morphed Steane code
- $⟦5,1,2⟧$ rotated toric code
- $⟦5,1,2⟧$ genon code
- $⟦5,1,2⟧$ holographic code
- $⟦5,1,2⟧$ planar-perfect code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-perfect
- concepts/qec/holographic-5-1-2
- concepts/qec/morphed-diagonal-clifford
- concepts/qec/rotated-surface
- concepts/qec/stab-4-2-2
- concepts/qec/steane
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_5_1_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_5_1_2
---

# $⟦5,1,2⟧$ rotated surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_5_1_2) (`code_id: stab_5_1_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A rotated surface code on one rung of a ladder, with one qubit on the rung, and four qubits surrounding it. This is the smallest code that implements a fault-tolerant logical $S$ gate using a diagonal depth-one Clifford circuit .

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{ccccc}
  Z & Z & I & Z & I \\
  I & I & Z & Z & Z \\
  I & X & X & X & I \\
  X & I & I & X & X
\end{array}~.
\end{align}
The code is depicted in \ref{figure:512-operators}.



A non-CSS genon-code form of the same stabilizer group, local Clifford equivalent to the above via Hadamard on the four corner qubits, is  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951))
\begin{align}
\begin{array}{ccccc}
  X & X & I & Z & I \\
  I & I & X & Z & X \\
  I & Z & Z & X & I \\
  Z & I & I & X & Z
\end{array}~.
\end{align}
The missing external stabilizer $YYYIY$ (product of all four generators) forms the back face when the code is viewed as a genon code on a sphere.

(source: raw/error-correction-zoo.md)

## General gates

- In the qubit order of the stabilizer tableau above, the physical action $S_0 S_2 S_3^{\dagger} CZ_{1,4}$ implements the logical gate $\bar{S}$  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
- Fault-tolerant implementation of the single-qubit Clifford group  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).

## Fault tolerance

- Fault-tolerant implementation of the single-qubit Clifford group  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).

## Relations

- _parent_: [[concepts/qec/rotated-surface]]
- _parent_: [[concepts/qec/morphed-diagonal-clifford]] — The $⟦5,1,2⟧$ code is a specific instance of the $⟦2^r+r-1,1,2⟧$ morphed simplex codes with $r=2$  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
- _parent_: [[concepts/qec/holographic-5-1-2]] — The $⟦5,1,2⟧$ rotated surface code is the smallest SCF holographic code  ([arXiv:2008.10206](https://arxiv.org/abs/2008.10206)). The encoding of more general SCF holographic codes is a holographic tensor network consisting of the encoding isometry for the $⟦5,1,2⟧$ rotated surface code, which is a planar-perfect tensor.
- _parent_: [[concepts/qec/block-perfect]] — The $⟦5,1,2⟧$ rotated surface code is the smallest SCF holographic code  ([arXiv:2008.10206](https://arxiv.org/abs/2008.10206)). The encoding of more general SCF holographic codes is a holographic tensor network consisting of the encoding isometry for the $⟦5,1,2⟧$ rotated surface code, which is a planar-perfect tensor.
- _cousin_: [[concepts/qec/twist-defect-surface]] — The $⟦5,1,2⟧$ rotated surface code is a genon code on a sphere, with the missing external $Y$-type stabilizer forming the back of the sphere. More generally, any surface code with a single boundary component can be interpreted this way  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).
- _cousin_: [[concepts/qec/steane]] — The $⟦5,1,2⟧$ morphed Steane code is obtained by morphing the Steane code on a region whose child code is a $⟦4,2,2⟧$ code  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
- _cousin_: [[concepts/qec/stab-4-2-2]] — The $⟦5,1,2⟧$ morphed Steane code is obtained by morphing the Steane code on a region whose child code is a $⟦4,2,2⟧$ code  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
