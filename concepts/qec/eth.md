---
type: concept
name: Eigenstate thermalization hypothesis (ETH) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Thermodynamic code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/frustration-free
- concepts/qec/hamiltonian
- concepts/qec/qubit-permutation-invariant
- concepts/qec/qubits-into-qubits
- concepts/qec/spins-into-spins
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/eth
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: eth
---

# Eigenstate thermalization hypothesis (ETH) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/eth) (`code_id: eth`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $n$-qubit approximate code whose codespace is formed by eigenstates of a translationally-invariant quantum many-body system which satisfies the Eigenstate Thermalization Hypothesis (ETH).
ETH ensures that codewords cannot be locally distinguished in the thermodynamic limit.
Relevant many-body systems include 1D non-interacting spin chains or frustration-free systems such as Motzkin chains and Heisenberg models.

ETH requires that for ordered energy eigenstates $|E_l\rangle$ and any local observable $O$,
\begin{align}
|\langle E_l|O|E_l\rangle-\langle E_{l+1}|O|E_{l+1}\rangle|\leq\exp(-cn)
\end{align}
for a constant $c$.
This implies that energy eigenstates around some energy $\bar E$ are approximately locally indistinguishable from one another, as their reduced density matrices on any subsystem are both approximately thermal at energy $\bar E$.
In this way, global information is protected from local measurements by the environment as $n\to\infty$.

(source: raw/error-correction-zoo.md)

## Protection

Approximately protects against erasure errors at known locations. Translation invariance alone is sufficient for good approximate error-correcting properties in a many-body spectrum, including in integrable models  ([arXiv:1710.04631](https://arxiv.org/abs/1710.04631)). The ETH code generated from the spectrum of the translation-invariant 1D Heisenberg spin chain  ([arXiv:1710.04631](https://arxiv.org/abs/1710.04631)) has recovery infidelity against the erasure of a constant number of sites scaling as $\epsilon_\text{worst}=O(1/n)$  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714)).

The ETH code defined on a Heisenberg spin chain has unbounded codespace complexity  ([arXiv:2310.04710](https://arxiv.org/abs/2310.04710)).

## Decoders

- An explicit universal recovery channel for the ETH code is given in  ([arXiv:1906.03669](https://arxiv.org/abs/1906.03669)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]] — ETH codewords are eigenstates of a local Hamiltonian whose eigenstates satisfy ETH.
- _parent_: [[concepts/qec/hamiltonian]] — ETH codewords are eigenstates of a local Hamiltonian whose eigenstates satisfy ETH, and many example codes are eigenstates of frustration-free Hamiltonians.
- _parent_: [[concepts/qec/approximate-qecc]] — ETH codes approximately protect against erasures in the thermodynamic limit. There is a link between ETH and approximate QEC, with fluctuations of the infinite-time average of certain observables expressible in terms of code error  ([arXiv:2510.26758](https://arxiv.org/abs/2510.26758)).
- _cousin_: [[concepts/qec/topological]] — ETH codewords, like topological codewords, are locally indistinguishable.
- _cousin_: [[concepts/qec/qubit-permutation-invariant]] — Several instances of ETH codes contain PI qubit codewords.
- _cousin_: [[concepts/qec/spins-into-spins]] — Relevant many-body systems housing ETH codes include 1D non-interacting spin chains or frustration-free systems such as Motzkin chains and Heisenberg models.
- _cousin_: [[concepts/qec/frustration-free]] — ETH codewords are eigenstates of a local Hamiltonian whose eigenstates satisfy ETH, and many example codes are eigenstates of frustration-free Hamiltonians.
