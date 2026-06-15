---
type: concept
name: Circuit-to-Hamiltonian approximate code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/frustration-free
- concepts/qec/nonlocal-lowdepth
- concepts/qec/qlwc
- concepts/qec/qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/circuit_to_hamiltonian
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: circuit_to_hamiltonian
---

# Circuit-to-Hamiltonian approximate code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/circuit_to_hamiltonian) (`code_id: circuit_to_hamiltonian`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Approximate qubit block code that forms the ground-state space of a frustration-free Hamiltonian with non-commuting terms.
Its distance and logical-qubit number are both of order $\Omega(n/\log^5 n)$  ([arXiv:1811.00277](https://arxiv.org/abs/1811.00277)).
The code is an approximate non-stabilizer QLWC code since the Hamiltonian consists of non-commuting 9-local non-Pauli projectors, with each qubit acted on by order $O( \text{polylog}(n) )$ projectors.

The code is constructed by converting the encoding circuit of a Brown-Fawzi random Clifford-circuit code into a Hamiltonian using the spacetime circuit-to-Hamiltonian construction  ([arXiv:quant-ph/0609067](https://arxiv.org/abs/quant-ph/0609067), [arXiv:1311.6101](https://arxiv.org/abs/1311.6101)) (a generalization of the Feynman-Kitaev clock construction  ([doi:10.1090/gsm/047](https://doi.org/10.1090/gsm/047))).
The ground-state subspace of this Hamiltonian is the $\epsilon$-approximate code with infidelity of recovery $\epsilon = O( 1/\text{polylog}(n) )$.

Using Markov-chain techniques, the gap of the Hamiltonian can be proven to be of order $\Omega(D^{-2}n^{-3.09}\log^{-6} n)$ for an $n$-qubit input circuit of depth $D$.

(source: raw/error-correction-zoo.md)

## Protection

Circuit-to-Hamiltonian approximate codes have nontrivial codespace complexity  ([arXiv:2310.04710](https://arxiv.org/abs/2310.04710)).

## Encoders

- There exists a circuit of size polynomial in $n$ whose terms act on at most $\log (n)+2$ qubits  ([arXiv:1811.00277](https://arxiv.org/abs/1811.00277)).

## Decoders

- Local detection of Pauli errors can be done using circuits of depth of order $O( \text{polylog}(n) )$ based on exact decoders for the Brown-Fawzi code  ([arXiv:1811.00277](https://arxiv.org/abs/1811.00277)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/approximate-qecc]]
- _parent_: [[concepts/qec/frustration-free]] — Circuit-to-Hamiltonian approximate codes form the ground-state space of a frustration-free non-commuting projector Hamiltonian whose projectors are constant weight, but such that each physical qubit is acted on by order $O( \text{polylog}(n) )$ projectors.
- _cousin_: [[concepts/qec/qlwc]] — The circuit-to-Hamiltonian code construction yields approximate codes whose distance and logical-qubit number are both of order $\Omega(n/\log^5 n)$  ([arXiv:1811.00277](https://arxiv.org/abs/1811.00277)).
These codes are approximate non-stabilizer QLWC codes since the Hamiltonian consists of non-commuting 9-local non-Pauli projectors, with each qubit acted on by order $O( \text{polylog}(n) )$ projectors.
- _cousin_: [[concepts/qec/nonlocal-lowdepth]] — Circuit-to-Hamiltonian approximate codes are constructed by converting the encoding circuit of a Brown-Fawzi random Clifford-circuit code into a Hamiltonian using the spacetime circuit-to-Hamiltonian construction  ([arXiv:quant-ph/0609067](https://arxiv.org/abs/quant-ph/0609067), [arXiv:1311.6101](https://arxiv.org/abs/1311.6101)).
