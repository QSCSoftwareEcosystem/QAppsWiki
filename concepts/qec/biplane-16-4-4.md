---
type: concept
name: $⟦16,4,4⟧$ biplane code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- $⟦16,4,4⟧$ quadric code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quadric-tower
- concepts/qec/quantum-reed-muller
- concepts/qec/self-dual-css
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-16-4-4
- concepts/qec/stab-16-6-4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/biplane_16_4_4
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: biplane_16_4_4
---

# $⟦16,4,4⟧$ biplane code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/biplane_16_4_4) (`code_id: biplane_16_4_4`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Self-dual pure CSS code whose $X$- and $Z$-type stabilizer generators span the same $[16,6,6]$ binary code as the blocks of the biplane of order four.
Equivalently, the underlying classical code is $\text{RM}(1,4)$ enlarged by the indicator vector of an elliptic quadric in $\mathbb{F}_2^4$.
The code admits weight-six stabilizer generators of both types and realizes its full logical Clifford group using depth-one two-local physical circuits  ([arXiv:2608.05688](https://arxiv.org/abs/2608.05688)).

With qubits labeled by the points of $\mathbb{F}_2^{4}$ in binary order, the first five generators of each type are the affine functions spanning $\text{RM}(1,4)$.
The sixth is the zero set $\{x: Q(x)=0\}$ of the elliptic form $Q=x_1x_2+x_3+x_3x_4+x_4$.
This gives the stabilizer tableau
\begin{align}
\begin{smallmatrix}
  X & X & X & X & X & X & X & X & X & X & X & X & X & X & X & X \\
  I & X & I & X & I & X & I & X & I & X & I & X & I & X & I & X \\
  I & I & X & X & I & I & X & X & I & I & X & X & I & I & X & X \\
  I & I & I & I & X & X & X & X & I & I & I & I & X & X & X & X \\
  I & I & I & I & I & I & I & I & X & X & X & X & X & X & X & X \\
  X & X & X & I & I & I & I & X & I & I & I & X & I & I & I & X \\
  Z & Z & Z & Z & Z & Z & Z & Z & Z & Z & Z & Z & Z & Z & Z & Z \\
  I & Z & I & Z & I & Z & I & Z & I & Z & I & Z & I & Z & I & Z \\
  I & I & Z & Z & I & I & Z & Z & I & I & Z & Z & I & I & Z & Z \\
  I & I & I & I & Z & Z & Z & Z & I & I & I & I & Z & Z & Z & Z \\
  I & I & I & I & I & I & I & I & Z & Z & Z & Z & Z & Z & Z & Z \\
  Z & Z & Z & I & I & I & I & Z & I & I & I & Z & I & I & I & Z
\end{smallmatrix}~.
\end{align}
Rows 1 to 5 and 7 to 11 are the generators of the tesseract color code.
Rows 6 and 12 are the added quadric generators.
The sixteen weight-six codewords of the underlying classical code are the blocks of the biplane.
Each block contains six qubits, and each qubit lies in six blocks.
Any six linearly independent blocks form an alternative generating set consisting entirely of weight-six checks.

The permutation automorphism group of the underlying classical code is the group of affine symplectic maps $x\mapsto Mx+a$ of $\mathbb{F}_2^4$, where $M$ preserves the polar form of $Q$.
Such maps preserve $\text{RM}(1,4)$ and send $Q$ into its own coset.
There are $2^4\cdot|Sp(4,2)|=11520$ of them.

(source: raw/error-correction-zoo.md)

## Transversal gates

- CNOT gate between two blocks because the code is CSS, and transversal Hadamard because the code is self-dual.
- Transversal $S$ and $\sqrt{X}$ are valid logical gates up to Pauli corrections because every codeword of the underlying classical code has even weight.
- Fold-transversal gates built from involutions of the order-$11520$ affine symplectic automorphism group  ([arXiv:2608.05688](https://arxiv.org/abs/2608.05688)). These include the $15$ fixed-point-free translations $x\mapsto x+a$ of $\mathbb{F}_2^4$, each of which contributes a layer of eight $CZ$ gates  ([arXiv:2608.05688](https://arxiv.org/abs/2608.05688)).
- The transversal and fold-transversal gates above, all of which are depth-one two-local physical Clifford circuits, generate the full logical Clifford group $Sp(8,2)$ on the four logical qubits  ([arXiv:2608.05688](https://arxiv.org/abs/2608.05688)).

## Relations

- _parent_: [[concepts/qec/self-dual-css]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/stab-16-6-4]] — The $⟦16,4,4⟧$ biplane code is obtained from the tesseract color code by adding one $X$-type and one $Z$-type stabilizer generator supported on an elliptic quadric of $\mathbb{F}_2^4$.
This reduces the number of logical qubits from six to four.
The promoted generators are minimum-weight elements of one of the $28$ logical classes of the tesseract code, so the resulting code remains pure.
- _cousin_: [[concepts/qec/quantum-reed-muller]] — The underlying classical code of the $⟦16,4,4⟧$ biplane code is the first-order RM code $\text{RM}(1,4)$ enlarged by the indicator vector of an elliptic quadric in $\mathbb{F}_2^4$.
- _cousin_: [`nordstrom_robinson`](https://errorcorrectionzoo.org/c/nordstrom_robinson) — The underlying $[16,6,6]$ classical code of the $⟦16,4,4⟧$ biplane code is, up to a coordinate permutation, a linear subcode of the NR code. It consists of $\text{RM}(1,4)$ together with one of the seven nontrivial cosets of $\text{RM}(1,4)$ making up the NR code.
- _cousin_: [`combinatorial_design`](https://errorcorrectionzoo.org/c/combinatorial_design) — The sixteen minimum-weight codewords of the underlying $[16,6,6]$ classical code of the $⟦16,4,4⟧$ biplane code are the blocks of the biplane of order four. This biplane is the symmetric $2$-$(16,6,2)$ design, whose automorphism group is $\mathbb{Z}_{2}^{4}\rtimes Sp(4,2)$.
- _cousin_: [[concepts/qec/stab-16-4-4]] — The $⟦16,4,4⟧$ biplane code and the $⟦16,4,4⟧$ twisted color code are the two self-dual CSS gauge fixings of the $⟦16,4,2,4⟧$ tesseract subsystem code  ([arXiv:2409.04628](https://arxiv.org/abs/2409.04628)).
They are obtained by promoting the weight-six and the weight-four gauge operators, respectively.
- _cousin_: [[concepts/qec/quadric-tower]] — Both the $⟦16,4,4⟧$ biplane code and the quadric tower codes are self-dual CSS codes built from quadratic forms over $\mathbb{F}_2$. The former uses a quadric as an extra stabilizer generator, and the latter uses a quadric as the qubit set.
