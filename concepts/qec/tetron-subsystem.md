---
type: concept
name: Tetron subsystem code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- BC$\mapsto$FS code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/majorana-subsystem
- concepts/qec/qubit-stabilizer
- concepts/qec/stab-5-1-3
- concepts/qec/steane
- concepts/qec/tetron
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tetron_subsystem
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tetron_subsystem
---

# Tetron subsystem code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tetron_subsystem) (`code_id: tetron_subsystem`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of Majorana subsystem stabilizer codes on $n$ tetrons obtained from an $⟦n,k_b,d_b⟧$ qubit stabilizer code and an $[n,k,d_c]$ classical binary code.
The qubit code's Pauli operators become weight-two Majorana operators on the tetrons, and the classical code's parity checks become stabilizers that are products of four-Majorana tetron parities.
A tetron parity flips only under an odd-weight (fermionic) error, so these checks detect such errors, while tetron parities not fixed by them are gauge operators rather than further stabilizer generators  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).

A *tetron* is a superconducting island hosting four Majorana zero modes $\gamma_a,\gamma_b,\gamma_c,\gamma_d$, on which only parities of two modes are measured, and it stores a qubit in the form of operator parity.
Its six weight-two Majorana operators split into two sets,
\begin{align}
  \mathcal{R} &= \{\gamma_b\gamma_c,~\gamma_a\gamma_c,~\gamma_a\gamma_b\}\\
  \mathcal{R}^{\prime} &= \{\gamma_a\gamma_d,~\gamma_d\gamma_b,~\gamma_c\gamma_d\}~,
\end{align}
identified with the Pauli operators $X,Y,Z$ and their primed counterparts, respectively  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
Corresponding operators of the two sets return the same parity under an even-weight error and opposite parities under an odd-weight error.
Comparing them therefore reveals whether an error has odd weight using only two-mode parity measurements  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).

The Pauli operators of the qubit code are mapped onto the Majorana operators of the set $\mathcal{R}$, one tetron per qubit.
Each row of the classical parity-check matrix $H$ contributes a stabilizer equal to the product of the tetron parities on its support.
A tetron parity cannot be measured directly.
Such a stabilizer is instead realized as the product of an existing stabilizer supported on those tetrons and a copy of it with the operators on those tetrons switched from $\mathcal{R}$ to $\mathcal{R}^{\prime}$.
The two codes must therefore be *compatible*: every row of $H$ has to admit a stabilizer of the qubit code supported on at least the tetrons in that row  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
Each row of the systematic generator matrix $G=[I_k|P]$ contributes two gauge operators, the tetron parity at the row's first nonzero entry and the $\gamma_d$-string supported on all of its nonzero entries.
These $2k$ operators generate a gauge group of order $2^{2k}$, yielding $k$ gauge qubits.
The output is a $⟦2n,k_b,k,d_f⟧$ Majorana subsystem code on $n$ tetrons, i.e., $2n$ fermionic modes, with $n-k_b$ stabilizers inherited from the qubit code and $n-k$ from the classical code  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
Taking the classical code to have no logical bits places every tetron parity in the stabilizer group and leaves no gauge qubits.
This recovers concatenation with the tetron code  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)) ([arXiv:2311.01779](https://arxiv.org/abs/2311.01779)).
Relative to that earlier non-subsystem construction, the subsystem code corrects both odd- and even-weight errors with fewer stabilizer generators  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).

The $⟦10,1,2,3⟧$ code is obtained from the five-qubit perfect code and the $[5,2,3]$ classical code  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
See Ref.  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)) for the instances obtained from the $⟦6,1,3⟧$ code with the $[6,1,6]$ and $[6,3,3]$ codes and from the Steane code.

(source: raw/error-correction-zoo.md)

## Protection

Protects against both errors affecting an even number of Majorana modes and *fermionic* errors affecting an odd number.
Conventional tetron encodings rely on high charging energy to suppress odd-weight errors rather than correcting them  ([arXiv:1812.08477](https://arxiv.org/abs/1812.08477)).
The fermionic distance $d_f$ is the least Majorana weight of a nontrivial dressed logical operator.
It satisfies $d_b\leq d_f\leq 2d_b$, where $d_b$ is the distance of the bosonic input code  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).

The $⟦10,1,2,3⟧$, $⟦12,1,3,3⟧$, and $⟦14,1,4,3⟧$ codes have $d_f=d_b=3$, while the $⟦12,1,1,6⟧$ code built from the $[6,1,6]$ repetition code retains $d_f=2d_b=6$  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
The least Majorana weight of the fermionic gauge operators equals the distance $d_c$ of the classical input code  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).

## Decoders

- BP-OSD decoder  ([arXiv:2005.07016](https://arxiv.org/abs/2005.07016)), run with belief propagation in the product-sum mode, ordered-statistics post-processing in combination-sweep mode, at most five iterations, and search depth $2n+1$ for $n$ tetrons  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).

## Fault tolerance

- A suitable ordering of the stabilizer measurements, with redundant measurements added where required, yields syndrome-extraction sequences tolerating one even or one odd error  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
The error can occur either at the input or at an intermediate stage.
The $⟦10,1,2,3⟧$ code admits the shortest such sequence, of length eight and using a single redundant measurement.
It attains the highest fault-tolerant pseudothreshold of the four instances.

## Relations

- _parent_: [[concepts/qec/majorana-subsystem]] — Tetron subsystem codes are Majorana subsystem stabilizer codes whose gauge group is generated by tetron parity operators together with $\gamma_d$-strings determined by a classical binary code  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
- _cousin_: [[concepts/qec/tetron]] — Tetron subsystem codes are defined on $n$ tetrons, whose parity operators serve as gauge generators. Placing these operators in the gauge group rather than fixing them by high charging energy is what exposes odd-weight errors to correction  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
- _cousin_: [[concepts/qec/qubit-stabilizer]] — The tetron subsystem construction converts an $⟦n,k_b,d_b⟧$ qubit stabilizer code, together with a compatible classical code, into a $⟦2n,k_b,k,d_f⟧$ Majorana subsystem code.
The Pauli operators of the qubit code are mapped to weight-two Majorana operators on tetrons  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — The classical input code determines the gauge sector of a tetron subsystem code.
Rows of its parity-check matrix become tetron stabilizers.
Rows of its systematic generator matrix become gauge operators, one gauge qubit per row  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
- _cousin_: [[concepts/qec/stab-5-1-3]] — The $⟦10,1,2,3⟧$ tetron subsystem code is obtained from the five-qubit perfect code together with the $[5,2,3]$ classical code  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
- _cousin_: [[concepts/qec/steane]] — The $⟦14,1,4,3⟧$ tetron subsystem code is obtained from the Steane code together with the $[7,4,3]$ Hamming code  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
- _cousin_: [`hamming`](https://errorcorrectionzoo.org/c/hamming) — The $⟦14,1,4,3⟧$ tetron subsystem code is obtained from the Steane code together with the $[7,4,3]$ Hamming code  ([doi:10.1088/1367-2630/ad4737](https://doi.org/10.1088/1367-2630/ad4737)).
