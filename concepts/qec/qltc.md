---
type: concept
name: Quantum locally testable code (QLTC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-quantum
- concepts/qec/commuting-projector
- concepts/qec/distance-balanced
- concepts/qec/frustration-free
- concepts/qec/general-qldpc
- concepts/qec/qecc-finite
- concepts/qec/qubit-css
- concepts/qec/self-correct
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qltc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qltc
---

# Quantum locally testable code (QLTC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qltc) (`code_id: qltc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A local commuting-projector Hamiltonian-based block quantum code which has a nonzero average-energy penalty for creating large errors. Informally, states that are far away from the codespace of a QLTC have to be excited states of a number of the code's local projectors that scales linearly with $n$.

The average-energy penalty is quantified by the code's *soundness* $R$. Typically, one looks at how $R$ scales with increasing code size for infinite families of codes, defining QLTC families as those for which the soundness is asymptotically constant. QLTC families that also have asymptotically constant distance, rate, and weight of local projectors are called $c^3$*-QLTCs*; none have been found so far.

More technically, a QLTC is a code $\mathsf{C}$ defined as the ground-state space of a commuting-projector Hamiltonian $H$ consisting of a sum of $r$ local projectors (where $r$ typically scales linearly with $n$), each of which acts on exactly $u$ qubits (for some constant $u$). Such a code is a $(u,R)$-QLTC with soundness function $R(\delta)\in[0,1]$ if
\begin{align}
\label{eq:qltc}
  \forall \delta > 0,|\psi\rangle~:~\text{dist}(|\psi\rangle,C) \geq \delta n \Rightarrow \frac{1}{r}\langle\psi|H|\psi\rangle\geq R(\delta)~,
\end{align}
where $\text{dist}(|\psi\rangle,\mathsf{C})$ is a particular distance function between the state $|\psi\rangle$ and the codespace $\mathsf{C}$  ([arXiv:1310.5664](https://arxiv.org/abs/1310.5664)). The locality parameter $u$ is called the *query complexity* of the code.

A qubit, modular-qudit, or Galois-qudit stabilizer code that is locally testable is called a *stabilizer locally testable code (SLTC)*. In other words, the code admits a set of $r$ $u$-local stabilizer generators $S_i$ whose corresponding code Hamiltonian $H=\frac{1}{2}\sum_{i=1}^r (I-S_i)$ satisfies the requirement of being a QLTC.

For example, the $⟦n=2L^2,k=2,d=L⟧$ toric code on an $L\times L$ lattice is *not* a QLTC because of the following argument. Let $|\psi\rangle$ be a ground state that is excited by $L/3$ Pauli strings, each of length $L/2$. In order to fit on the lattice, such strings can, e.g., be horizontal and aligned next to each other in the vertical direction. The distance function $\text{dist}(|\psi\rangle,\mathsf{C})$ is the weight of the smallest Pauli string that multiplies $|\psi\rangle$ to yield a state in the codespace. In this case, that weight is the same as the weight of the perturbing string, i.e., $L^2/6$, requiring $\delta = 1/12$ to satisfy \eqref{eq:qltc}. There are $2L/3$ violated Hamiltonian terms because each of the $L/3$ strings violates only two stabilizer generators. However, there are $r = 2(L^2-1)$ stabilizer generators, so the implication of \eqref{eq:qltc} is not satisfied for nonzero soundness as $L\to\infty$ because $\frac{1}{r}\langle\psi|H|\psi\rangle = \frac{2L/3}{2(L^2-1)}\to 0$.

(source: raw/error-correction-zoo.md)

## Protection

Distance balancing and weight reduction are useful for constructing QLTCs.
For CSS code families with $w_X,w_Z,q_X,q_Z=O(\log n)$, Hastings' weight-reduction construction yields a QLDPC family whose soundness parameters $\epsilon_X,\epsilon_Z$ deteriorate by at most polylogarithmic factors  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790)).
Analogous scaling for a generalized distance-balancing scheme  ([arXiv:2004.07935](https://arxiv.org/abs/2004.07935)) is proven in  ([arXiv:2305.00689](https://arxiv.org/abs/2305.00689)).
Weight reduction can be used to construct codes of constant locality out of CSS QLTCs  ([arXiv:2309.05541](https://arxiv.org/abs/2309.05541)).

*Soundness amplification*  ([arXiv:2309.05541](https://arxiv.org/abs/2309.05541)) can be used to obtain a constant-soundness (i.e., $R = \Omega(1)$) QLTC family from a CSS family with a sub-constant value, with the former's locality being at most polynomial in $1/R$.

AEL distance amplification  ([doi:10.1109/SFCS.1995.492581](https://doi.org/10.1109/SFCS.1995.492581), [doi:10.1109/18.556669](https://doi.org/10.1109/18.556669)) can be used to convert an $⟦n^{\prime},k,d,w⟧$ soundness-$R$ CSS LTC family into one with the same dimension, linear distance, and block length differing by at most a constant factor, with $w$ and $R$ differing by at most a polynomial factor in $w$ and $n/d$  ([arXiv:2309.05541](https://arxiv.org/abs/2309.05541)).

## Relations

- _parent_: [[concepts/qec/block-quantum]]
- _parent_: [[concepts/qec/qecc-finite]]
- _parent_: [[concepts/qec/commuting-projector]] — Quantum LTC codespaces are ground-state spaces of $u$-local frustration-free commuting-projector Hamiltonians.
- _parent_: [[concepts/qec/frustration-free]] — Quantum LTC codespaces are ground-state spaces of $u$-local frustration-free commuting-projector Hamiltonians.
- _cousin_: [[concepts/qec/general-qldpc]] — Stabilizer LTCs are QLDPC. More general QLTCs are not defined using Pauli strings, but the codespace is the ground-state subspace of a local Hamiltonian. In this sense, QLTCs are QLDPC codes.
- _cousin_: [[concepts/qec/self-correct]] — The notion of an energy barrier in a self-correcting memory is intimately related to the soundness of a QLTC.
- _cousin_: [[concepts/qec/qubit-css]] — A qubit CSS code defined by $H_{Z}$ and $H_{X}$ is locally testable with some soundness iff the constituent codes $\ker H_{Z}$ and $\ker H_{X}$ are locally testable with the same soundness  ([arXiv:1510.02082](https://arxiv.org/abs/1510.02082)).
- _cousin_: [[concepts/qec/distance-balanced]] — Distance balancing and weight reduction are useful for constructing QLTCs  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790), [arXiv:2305.00689](https://arxiv.org/abs/2305.00689), [arXiv:2309.05541](https://arxiv.org/abs/2309.05541)).

## Notes

- It was shown in Ref.  ([arXiv:1510.02082](https://arxiv.org/abs/1510.02082)) that existence of a QLTC with constant parameters would imply resolution of the *No low-energy trivial states* (NLTS) conjecture  ([arXiv:1301.1363](https://arxiv.org/abs/1301.1363)) (see also  ([arXiv:2311.09503](https://arxiv.org/abs/2311.09503))). QLTCs are believed to also be useful for solving the quantum PCP conjecture  ([arXiv:1309.7495](https://arxiv.org/abs/1309.7495)).
