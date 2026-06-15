---
type: concept
name: Group-based quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/category-quantum
- concepts/qec/homogeneous-space-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/group_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: group_quantum
---

# Group-based quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/group_quantum) (`code_id: group_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes a *logical* Hilbert space, finite- or infinite-dimensional, into a *physical* Hilbert space of $L^2$-normalizable functions on a second-countable unimodular group $G$, i.e., a $G$*-valued qudit* or $G$-qudit.
In other words, a group-valued qudit is a vector space whose canonical basis states $|g\rangle$ are labeled by elements $g$ of a group $G$.
For $K$-dimensional logical subspace and for block codes defined on groups $G^{n}$, can be denoted as $((n,K))_G$.
When the logical subspace is the Hilbert space of $L^2$-normalizable functions on $G^{ k}$, can be denoted as $⟦n,k⟧_G$.
Ideal codewords may not be normalizable, depending on whether $G$ is continuous and/or noncompact, so approximate versions have to be constructed in practice.

A notion of Gaussian states and Hudson's theorem have been developed for arbitrary locally compact Abelian $G$  ([arXiv:2204.08162](https://arxiv.org/abs/2204.08162)).
A Wigner function formalism has also been developed  ([arXiv:2004.13860](https://arxiv.org/abs/2004.13860)).

(source: raw/error-correction-zoo.md)

## Protection

\subsection{Group-based error basis}
A convenient error set is the group-based analogue of the Pauli string set for qubit codes.
For a single group-valued qudit, this set consists of products of $X$-type operators labeled by group elements $g$, and $Z$-type operators labeled by matrix elements of $G$-irreps $\lambda$  ([arXiv:1408.6237](https://arxiv.org/abs/1408.6237), [arXiv:1911.00099](https://arxiv.org/abs/1911.00099), [arXiv:2111.12096](https://arxiv.org/abs/2111.12096)).
The outline below is for finite groups, but can be extended to compact unimodular groups or to oscillators and rotors by substituting the sum over the group with a group integral.

\begin{defterm}{Group-based error basis}
\label{topic:group-pauli}
There are two types of $X$-type operators, corresponding to left and right group multiplication.
These act on computational basis states $|h\rangle$ as
\begin{align}
  \overrightarrow{X}_{g}|h\rangle&=|gh\rangle\\
  \overleftarrow{X}_{g}|h\rangle&=|hg^{-1}\rangle
\end{align}
for any group elements $h,g$.
The $Z$-type operators can be thought of as matrix-product operators (MPOs)  ([arXiv:2312.09272](https://arxiv.org/abs/2312.09272)) whose virtual dimension is the dimension $d_{\lambda}$ of their corresponding irrep.
They are diagonal in the group-valued basis, yielding the $d_{\lambda}$-dimensional irrep matrix $Z_{\lambda}(g)$ evaluated at the given group element,
\begin{align}
  \hat{Z}_{\lambda}\otimes|g\rangle=Z_{\lambda}(g)\otimes|g\rangle~.
\end{align}
Each matrix element of this irrep matrix is a generally non-unitary operator on the group-valued qudit.
For 1D irreps, the matrix reduces to a single unitary $Z$-type operator, and the direct-product symbol is no longer needed.
For special cases of Abelian $G$ being $\mathbb{Z}_2$, $\mathbb{Z}_q$, $\mathbb{F}_q$, $U(1)\cong \mathbb{Z}$, or $\mathbb{R}$, the group-based error basis reduces to the familiar qubit Pauli, qudit Pauli, Galois-qudit Pauli, rotor generalized Pauli, or oscillator displacement error basis, respectively.
\end{defterm}

Products of either left- or right-multiplication $X$-type operators with all $Z$-type operators form a basis for linear operators on the group-valued qudit space that is complete and orthonormal under the Hilbert-Schmidt inner product  ([arXiv:1911.00099](https://arxiv.org/abs/1911.00099)).
In particular,
\begin{align}
  \text{tr}(\overrightarrow{X}_{g}^{\dagger}\overrightarrow{X}_{h})=\delta_{g,h}^{G}~,
\end{align}
where the group Kronecker delta function $\delta^{G}_{g,h}=1$ if $g=h$ and zero otherwise.

## General gates

- Various gates for a single $G$-valued qudit include the Fourier gate (which is a re-expression of the group basis in terms of $G$-irreps), the $g \to g^{-1}$ inversion gate, conditional multiplication gates, and conditional multiplication gates in the irrep basis  ([arXiv:1408.6237](https://arxiv.org/abs/1408.6237), [arXiv:1911.00099](https://arxiv.org/abs/1911.00099), [arXiv:1903.08807](https://arxiv.org/abs/1903.08807), [arXiv:2208.12309](https://arxiv.org/abs/2208.12309), [arXiv:2402.16780](https://arxiv.org/abs/2402.16780)).
- The \term{Clifford hierarchy} can be extended to arbitrary Abelian $G$  ([arXiv:quant-ph/9908010](https://arxiv.org/abs/quant-ph/9908010), [arXiv:1503.08800](https://arxiv.org/abs/1503.08800), [arXiv:1509.03626](https://arxiv.org/abs/1509.03626)).

## Relations

- _parent_: [[concepts/qec/homogeneous-space-quantum]] — Homogeneous spaces $G/H$ for trivial $H$ reduce to group spaces. A group-$G$ space can also be thought of as a multiplicity-free homogeneous space $(G\times G) / G$ .
- _parent_: [[concepts/qec/category-quantum]] — Finite-group-based quantum codes, whose basis states are parameterized by a finite group, correspond to category-based codes for the fusion category $Vec G$. Extensions of such categories to Lie groups can also be done  ([arXiv:2106.12577](https://arxiv.org/abs/2106.12577)),arxiv:2503.14596} (see also  ([arXiv:gr-qc/0303060](https://arxiv.org/abs/gr-qc/0303060))).

## Notes

- See Refs.  ([arXiv:1601.03843](https://arxiv.org/abs/1601.03843), [arXiv:1709.04460](https://arxiv.org/abs/1709.04460)) for introductions to Hilbert spaces for Abelian groups.
- Group-based $Z$-type operators correspond to group-valued fields in the continuum limit  ([arXiv:2111.12096](https://arxiv.org/abs/2111.12096)) and Wilson link operators in lattice gauge theory  ([arXiv:2108.11402](https://arxiv.org/abs/2108.11402)).
