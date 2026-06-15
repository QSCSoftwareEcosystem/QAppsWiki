---
type: concept
name: Permutation-invariant (PI) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/constant-excitation
- concepts/qec/fock-state
- concepts/qec/quantum-cyclic
- concepts/qec/single-spin
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: permutation_invariant
---

# Permutation-invariant (PI) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/permutation_invariant) (`code_id: permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Block quantum code such that any permutation of the subsystems leaves any codeword invariant.
In other words, the automorphism group of the code contains the symmetric group $S_n$.

There is a notion of Wigner functions for PI subspaces  ([arXiv:2507.14866](https://arxiv.org/abs/2507.14866)). 

\subsection{Qudit Dicke states and the discrete simplex mapping}

For $n$-modular-qudit block codes with qudit dimension $q$, an often used basis for the PI subspace consists of the qudit Dicke states. 

\begin{defterm}{Qudit Dicke states}
\label{topic:qudit-dicke}
A qudit Dicke state is an equal superposition of all qudit basis elements whose labels have the same composition,
\begin{align}
  |D_{\mathbf{c}}\rangle=\frac{1}{\sqrt{\binom{n}{\mathbf{c}}}}\sum_{\substack{\mathbf{n}\in\mathbb{Z}_{q}^{n}\\ C(\mathbf{n})=\mathbf{c} } }|\mathbf{n}\rangle\,,
\end{align}  
where $\binom{n}{\mathbf{c}}$ is the multinomial coefficient.
Above, the *composition* $C$ of a qudit basis label $\mathbf{n}$ tabulates the number of each type of element present in the label. For example, the label $\mathbf{n}=(0313)$ has composition $C(\mathbf{n})=(1102)$, whose coordinates denote the number of zeroes (one), number of ones (one), number of twos (zero), and number of threes (two) present in the label.  
The $q=2$ case reduces to the Dicke-state mapping.
\end{defterm}

Qudit Dicke states are in one-to-one correspondence with points on the discrete simplex $\Delta_{q,n}$, which houses the totally symmetric irrep of $SU(q)$  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
The same simplex labels define constant-excitation Fock-state codes and single-spin codes on the completely symmetric $SU(q)$ irrep.
Applying the simplex mapping to a qudit PI code yields Fock-state and spin codes with the same distance  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
Wigner functions are also interconvertible between the Fock-state and single-spin spaces  ([arXiv:2510.21476](https://arxiv.org/abs/2510.21476)).

(source: raw/error-correction-zoo.md)

## Protection

Noise models can be categorized as those that cause the state to leave the maximally symmetric subspace and those that do not.
PI codes of distance $d$ can protect against $d-1$ deletion errors  ([arXiv:2001.08405](https://arxiv.org/abs/2001.08405), [arXiv:2004.00814](https://arxiv.org/abs/2004.00814), [arXiv:2102.02494](https://arxiv.org/abs/2102.02494), [arXiv:2102.03015](https://arxiv.org/abs/2102.03015)), i.e., erasures of subsystems at unknown locations.

Other protection depends on the code family.
The GNU PI family (parameterized by $t$) protects against arbitrary weight $t$ qubit errors and approximately corrects spontaneous decay errors  ([arXiv:1302.3247](https://arxiv.org/abs/1302.3247), [arXiv:1512.02469](https://arxiv.org/abs/1512.02469)).
Other related codes protect against AD  ([arXiv:1809.09801](https://arxiv.org/abs/1809.09801)) while admitting a constant number of excitations.

## Encoders

- State preparation of qudit Dicke states  ([arXiv:2301.04989](https://arxiv.org/abs/2301.04989)).

## Rate

For every $K,t \geq 2$, there are explicitly constructible PI codes with $q=N=(K-1)t(t+1)$, length $N$, and distance $t+1$; there also exist families with logical dimension $K = o(2^N)$ and distance of order $o(N/\log N)$  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).

## Transversal gates

- Qudit Dicke states are in one-to-one correspondence with points on the discrete simplex $\Delta_{q,n}$, which houses the totally symmetric irrep of $SU(q)$  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)). Any transversal gates of the form $U^{\otimes N}$, with $U \in SU(q)$, will implement logical operations in a subgroup of $SU(q)$.

## Relations

- _parent_: [[concepts/qec/quantum-cyclic]] — The cyclic group of these codes is a subgroup of the $S_n$ symmetric group used in permutation invariant codes.
- _cousin_: [`simplex_discrete`](https://errorcorrectionzoo.org/c/simplex_discrete) — Simplex integer-based codes can be partitioned into qudit PI codewords whose error-correction is guaranteed by the Tverberg theorem  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
- _cousin_: [[concepts/qec/constant-excitation]] — Modular-qudit PI codes can be converted to constant-excitation Fock-state codes via the simplex mapping  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)). Any transversal gates are mapped to Gaussian gates on the Fock-state codes  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
- _cousin_: [[concepts/qec/fock-state]] — Modular-qudit PI codes can be converted to constant-excitation Fock-state codes via the simplex mapping  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)). Any transversal gates are mapped to Gaussian gates on the Fock-state codes  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
- _cousin_: [[concepts/qec/single-spin]] — Modular-qudit PI codes can be converted to spin codes defined on the completely symmetric irrep of $SU(q)$ via the simplex mapping  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)). Any transversal gates are mapped to $SU(q)$ gates on the spin codes  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).

## Notes

- PI codes can be constructed using real polynomials for high-dimensional qudit spaces  ([arXiv:1604.07925](https://arxiv.org/abs/1604.07925)).
- Qubit and qudit PI codes obtained from numerical optimization routines are useful for entanglement distillation  ([arXiv:2105.13233](https://arxiv.org/abs/2105.13233)).
- Qudit Dicke state preparation  ([arXiv:2507.13308](https://arxiv.org/abs/2507.13308)).
