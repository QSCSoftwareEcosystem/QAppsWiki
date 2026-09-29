---
type: concept
name: Subsystem modular-qudit CSS code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qudit-css
- concepts/qec/qudit-subsystem-stabilizer
- concepts/qec/subsystem-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_subsystem_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_subsystem_css
---

# Subsystem modular-qudit CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_subsystem_css) (`code_id: qudit_subsystem_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit subsystem stabilizer code which admits a set of gauge-group generators which consist of either all-$Z$ or all-$X$ modular-qudit Pauli strings.
This ensures that the code's stabilizer group is also CSS.

The gauge group generators can be expressed as a matrix using the symplectic representation. This matrix is of the form
\begin{align}
H=\begin{pmatrix}0 & H_{Z}\\
H_{X} & 0
\end{pmatrix}~.
\label{eq:parity}
\end{align}
The two matrix blocks, $H_{Z}$ and $H_X$, correspond to the parity-check matrices of two $q$-ary linear codes, an $[n,k_Z,d_Z]_q$ code $C_Z$ and $[n,k_X,d_X]_q$ code $C_X$, respectively.
For prime-dimensional qudits, code parameters and code basis states have been expressed in terms of data associated with only these two classical codes  ([arXiv:quant-ph/0610153](https://arxiv.org/abs/quant-ph/0610153), [arXiv:2311.18003](https://arxiv.org/abs/2311.18003)).

\begin{defterm}{Symplectic doubling}
\label{topic:symplectic-doubling}
Any $⟦n,k,r,d⟧_{\mathbb{Z}_q}$ subsystem stabilizer code can be mapped onto a $⟦2n,2k,2r,d^{\prime}⟧_{\mathbb{Z}_q}$ subsystem CSS code with $d\leq d^{\prime}\leq 2d$, with the mapping preserving geometric locality of a code up to a constant factor  ([arXiv:2311.18003](https://arxiv.org/abs/2311.18003)) (see also  ([arXiv:1212.6703](https://arxiv.org/abs/1212.6703)) ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951))).
In the modular symplectic representation, the gauge-group generator matrix of the former is mapped into that of the latter as follows,
\begin{align}
  \begin{pmatrix}G_{X} & G_{Z}\end{pmatrix}
  \to
  \begin{pmatrix}
  0     &     0 & G_{Z} & -G_{X}\\
  G_{X} & G_{Z} &     0 &      0
  \end{pmatrix}~,
\end{align}
where the first two column blocks of the latter matrix correspond to the $X$-type part of the gauge-group generator matrix of the output subsystem CSS code.
The map is linear in the rows of the generator matrix, so the double depends only on the gauge group and not on the choice of generating set.
It does depend on that group, and not merely on the code the group defines.
A local Clifford on an input qudit changes the group, and acts on the corresponding output pair by a transformation that is not itself a local Clifford, so locally equivalent codes can have inequivalent doubles.

In the case of a stabilizer code, the stabilizer generator matrix is mapped instead to yield a two-block CSS code (see  ([arXiv:1212.6703](https://arxiv.org/abs/1212.6703)) for the case of qubit stabilizer codes).
For geometrically local 2D stabilizer codes with twist defects, this mapping yields a twisted double cover of the underlying qudit geometry  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).

For qubit stabilizer codes, this map is also known as the *BLT $n\to 2n$ mapping*, and its output can be packaged as an $⟦n,k,d⟧_4$ Galois-qudit CSS code  ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)) ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).
The Galois-qudit distance is exactly $d$ because the Galois-qudit support of the image coincides with the symplectic support of the input, while splitting each Galois qudit into two qubits can double the weight of a logical operator.
Conversely, a Galois-qudit CSS code arises as a symplectic double of a qubit stabilizer code if and only if it is Hermitian self-dual  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927), [arXiv:2605.15344](https://arxiv.org/abs/2605.15344)).

*Concatenated symplectic doubling*, also known as the *BLT $n\to 4n$ mapping*, follows the above map with concatenation of each output qubit pair with the $⟦4,2,2⟧$ code along a $ZX$ duality.
This yields a $⟦4n,2k,2d⟧$ self-dual CSS code from an $⟦n,k,d⟧$ qubit stabilizer code  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)) ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)) ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).
Equivalently, one first concatenates each qubit with the tetron code to obtain a $⟦2n,k,2d⟧_{f}$ Majorana stabilizer code, and then assigns one qubit to each Majorana mode  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).
The second stage of the $n\to 4n$ mapping, applied to the $⟦n,k,d⟧_4$ packaging of the double, is the binarization-and-concatenation step used to build B\&C phantom codes  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

The two routes agree for the following reason.
Tetron concatenation assigns Majorana modes $b_j^x,b_j^y,b_j^z,c_j$ to each qubit $j$, realizing its Pauli operators as $X_j = i b_j^x c_j$, $Y_j = i b_j^y c_j$, and $Z_j = i b_j^z c_j$, and adjoining the parity operator $D_j = b_j^x b_j^y b_j^z c_j$ as a stabilizer generator  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).
Assigning one qubit to each Majorana mode then sends a Majorana monomial supported on a set $S$ to an $X$-type and a $Z$-type Pauli operator, both supported on $S$  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).
Each $D_j$ therefore becomes the pair $XXXX$ and $ZZZZ$ on the four qubits of block $j$, which generate the $⟦4,2,2⟧$ stabilizer group.
Each single-qubit Pauli of the input becomes a pair of weight-two operators of opposite type sharing a common support, up to multiplication by the $⟦4,2,2⟧$ stabilizer generators, i.e., a pair of $⟦4,2,2⟧$ logical operators exchanged by the $ZX$ duality.
The output is thus the $⟦4,2,2⟧$ code on every block of four qubits, with the symplectic double of the input code acting on the resulting logical qubits.
\end{defterm}

(source: raw/error-correction-zoo.md)

## Decoders

- Steane-type decoder utilizing data from the underlying classical codes  ([arXiv:2311.18003](https://arxiv.org/abs/2311.18003)).

## Relations

- _parent_: [[concepts/qec/qudit-subsystem-stabilizer]] — Subsystem modular-qudit CSS codes are subsystem modular-qudit stabilizer codes whose gauge groups admit a generating set of pure-$X$ and pure-$Z$ Pauli strings. Any $⟦n,k,r,d⟧_{\mathbb{Z}_q}$ subsystem stabilizer code can be mapped onto a $⟦2n,2k,2r,d^{\prime}⟧_{\mathbb{Z}_q}$ subsystem CSS code with $d\leq d^{\prime}\leq 2d$ via symplectic doubling, which preserves geometric locality of a code up to a constant factor. Every subsystem prime-qudit stabilizer code can be constructed from two nested subsystem prime-qudit CSS codes satisfying certain constraints  ([arXiv:2311.18003](https://arxiv.org/abs/2311.18003)).
- _parent_: [[concepts/qec/subsystem-css]]
- _cousin_: [[concepts/qec/qudit-css]] — Subsystem modular-qudit CSS codes reduce to (subspace) modular-qudit CSS codes when there is no gauge subsystem.
