---
type: concept
name: $⟦16,6,4⟧$ copy-cup code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-bicycle
- concepts/qec/perm-self-dual-css
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-16-6-4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/copycup_16_6_4
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: copycup_16_6_4
---

# $⟦16,6,4⟧$ copy-cup code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/copycup_16_6_4) (`code_id: copycup_16_6_4`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An even pure $⟦16,6,4⟧$ CSS code that admits a constant-depth logical $CZ$ gate between two copies and is constructed as a balanced product of two weight-four cyclic group-algebra codes over $\mathbb{F}_2[\mathbb{Z}_8]$.
It is one of two inequivalent $⟦16,6,4⟧$ codes whose complete logical Clifford group is realizable by depth-one two-local circuits, the other being the tesseract color code.

A stabilizer tableau for the code, given by cyclic shifts of the generalized bicycle rows $H_X=(A|B)$ and $H_Z=(B^T|A^T)$, is  ([arXiv:2602.23307](https://arxiv.org/abs/2602.23307))
\begin{align}
\begin{smallmatrix}
  X & X & X & X & I & I & I & I & X & X & I & X & I & I & X & I \\
  I & X & X & X & X & I & I & I & I & X & X & I & X & I & I & X \\
  I & I & X & X & X & X & I & I & X & I & X & X & I & X & I & I \\
  I & I & I & X & X & X & X & I & I & X & I & X & X & I & X & I \\
  I & I & I & I & X & X & X & X & I & I & X & I & X & X & I & X \\
  Z & I & Z & I & I & Z & I & Z & Z & I & I & I & I & Z & Z & Z \\
  Z & Z & I & Z & I & I & Z & I & Z & Z & I & I & I & I & Z & Z \\
  I & Z & Z & I & Z & I & I & Z & Z & Z & Z & I & I & I & I & Z \\
  Z & I & Z & Z & I & Z & I & I & Z & Z & Z & Z & I & I & I & I \\
  I & Z & I & Z & Z & I & Z & I & I & Z & Z & Z & Z & I & I & I
\end{smallmatrix}~,
\end{align}
where $A=a(P)$ and $B=b(P)$ are the $8\times 8$ circulants of $a(x)=1+x+x^2+x^3$ and $b(x)=1+x+x^3+x^6$, and $P$ is the length-eight cyclic shift.

(source: raw/error-correction-zoo.md)

## Transversal gates

- All logical Clifford gates can be realized as two-fold transversal gates, i.e., by depth-one circuits of two-local code-preserving physical gates  ([arXiv:2608.05688](https://arxiv.org/abs/2608.05688)).

## General gates

- Admits a constant-depth logical $CZ$ gate between two copies of the code (an inter-code gate), the 2-copy-cup gate, built from a cup product on the balanced-product cochain complex subject to a pre-orientation condition on the two classical codes  ([arXiv:2602.23307](https://arxiv.org/abs/2602.23307), [arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).

## Relations

- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _parent_: [[concepts/qec/generalized-bicycle]] — The $⟦16,6,4⟧$ copy-cup code is the generalized bicycle code $\text{GB}(a,b)$ over $\mathbb{Z}_8$ with $a(x)=1+x+x^2+x^3$ and $b(x)=1+x+x^3+x^6$, equivalently the balanced product of two weight-four cyclic group-algebra codes  ([arXiv:2602.23307](https://arxiv.org/abs/2602.23307)).
- _parent_: [[concepts/qec/perm-self-dual-css]] — The $⟦16,6,4⟧$ copy-cup code is permutationally self-dual since it is a qubit GB code. Exchanging the two blocks of eight qubits while inverting the cyclic-group index within each block exchanges the $X$- and $Z$-type stabilizer spaces  ([arXiv:2606.05044](https://arxiv.org/abs/2606.05044)).
- _cousin_: [[concepts/qec/stab-16-6-4]] — The $⟦16,6,4⟧$ copy-cup code and the $⟦16,6,4⟧$ tesseract color code are the two inequivalent $⟦16,6,4⟧$ codes whose complete logical Clifford group is realizable by depth-one two-local circuits  ([arXiv:2608.05688](https://arxiv.org/abs/2608.05688)); both are pure CSS codes whose stabilizer generators all have weight eight.
The two are inequivalent in that they have different weight enumerators, and one is even while the other is doubly-even self-dual.
