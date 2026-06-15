---
type: concept
name: W-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/covariant
- concepts/qec/eth
- concepts/qec/permutation-invariant
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/w_state
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: w_state
---

# W-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/w_state) (`code_id: w_state`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Approximate block quantum code whose encoding resembles the structure of the
W state~ ([arXiv:quant-ph/0005115](https://arxiv.org/abs/quant-ph/0005115)).
This code enables universal quantum computation with transversal gates.

The encoding is of a $d_L$-dimensional Hilbert space into $n$ physical quantum systems, each associated with a Hilbert space
of dimension $d_L+1$:
\begin{align}
  \ket\psi
  \to \frac{1}{\sqrt{n}}\bigl(\ket{\psi\perp\perp\ldots}
  + \ket{\perp\psi\perp\ldots} + \cdots
  + \ket{\perp\perp\ldots\psi}\bigr)\ ,
\end{align}
where on each physical system, $\ket\perp$ denotes the $(d_L+1)$-th basis state,
and $\ket\psi$ is encoded using the first $d_L$ basis states.

Indeed, to apply any logical unitary $U$ it suffices to apply $U$ on each physical system,
where the unitary is taken to act nontrivially only on the first $d_L$ basis states
of each system.  Universal computation with transversal gates does not violate the
Eastin-Knill theorem because this code is an approximate error-correcting
code~ ([arXiv:1709.04471](https://arxiv.org/abs/1709.04471), [arXiv:1902.07714](https://arxiv.org/abs/1902.07714)) rather than an exact error-correcting
code.

(source: raw/error-correction-zoo.md)

## Protection

The W state code is an approximate error-correcting code.  Intuitively, if a
subsystem is lost to the environment, the environment only gains access to
$\ket\psi$ with probability of order $O(1/n)$. Under a single located erasure,
the worst-case entanglement infidelity of the W state code can be upper bounded as
\begin{align}
  \epsilon_{\mathrm{worst}} \leq \frac{\sqrt{2} + d_L}{\sqrt{n}}\ .
\end{align}

In contrast to the \ref{code:eth}, the W state code does not saturate the scaling
$1/n$ in worst-case entanglement infidelity which is known to be
optimal for covariant approximate error-correcting codes~ ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714)).

## Encoders

- There are complexity-theoretic bounds on $W$-state preparation  ([arXiv:2510.04453](https://arxiv.org/abs/2510.04453)).

## Transversal gates

- All logical gates can be implemented transversally. The logical unitary $U_L$ can be performed with the physical unitary $U_L\otimes U_L\otimes\cdots\otimes U_L$, where on the physical space $U_L$ is taken to act trivially on $\ket\perp$, i.e., $ U_L\ket\perp = \ket\perp$.

## Relations

- _parent_: [[concepts/qec/covariant]] — The W-state code approximately protects against a single erasure while allowing for a universal transversal set of gates.
- _parent_: [[concepts/qec/permutation-invariant]]
- _parent_: [[concepts/qec/approximate-qecc]] — The W-state code approximately protects against a single erasure while allowing for a universal transversal set of gates.
- _cousin_: [[concepts/qec/eth]] — The W-state is not a unique ground state of any local Hamiltonian  ([arXiv:2310.10716](https://arxiv.org/abs/2310.10716)).
