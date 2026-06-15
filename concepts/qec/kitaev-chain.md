---
type: concept
name: Kitaev chain code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Majorana repetition code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/jw
- concepts/qec/majorana-stab
- concepts/qec/mbq
- concepts/qec/quantum-repetition
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/spt
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/kitaev_chain
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: kitaev_chain
---

# Kitaev chain code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/kitaev_chain) (`code_id: kitaev_chain`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A Majorana stabilizer code obtained from the ground-state subspace of the Kitaev Majorana chain in its fermionic topological phase  ([arXiv:cond-mat/0010440](https://arxiv.org/abs/cond-mat/0010440)). Its codespace is stabilized by nearest-neighbor Majorana bilinears, while two unpaired edge Majoranas furnish one logical fermionic mode. Under parity-preserving noise, it behaves as the Majorana analogue of the repetition code  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).

At the fixed-point limit, the code Hamiltonian is proportional to $-\sum_{j=1}^{n-1} i \gamma_{2j}\gamma_{2j+1}$, so the codespace is the common $+1$ eigenspace of the stabilizers $S_j=i\gamma_{2j}\gamma_{2j+1}$. The two unpaired edge operators $\gamma_{1}$ and $\gamma_{2n}$ are the *Majorana zero modes (MZMs)* or *Majorana edge modes (MEMs)*; they commute with all stabilizers and define a logical fermionic mode $f_{\mathrm{L}}=(\gamma_{1}+i\gamma_{2n})/2$. Via the Jordan-Wigner transformation, the model maps to the 1D quantum Ising chain in its symmetry-breaking phase.
The code can be thought of as the Majorana stabilizer analogue of the quantum repetition code: parity-preserving dephasing operators $Z_j=i\gamma_{2j-1}\gamma_{2j}$ play the role of repetition-code bit flips, while the logical Majorana operators have odd weight and therefore encode a logical fermion  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).

The two basis states of a single chain have opposite fermionic parity.
Therefore, a single chain does not by itself furnish a fixed-parity qubit encoding; coherent superpositions between the two basis states are not directly accessible in an isolated fermionic system with parity superselection.
One can combine two such code blocks to form a Majorana box qubit, which is the fixed-parity subspace of the combined codespace.
Odd numbers of code blocks also contain fixed-parity logical subspaces in their codespace.

(source: raw/error-correction-zoo.md)

## Protection

In the fixed-point limit, local parity-preserving bilinears such as $Z_j=i\gamma_{2j-1}\gamma_{2j}$ anticommute with nearby stabilizers, so the chain behaves as a repetition code against dephasing or phase errors  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)). For a finite chain, the splitting between the two code states is exponentially small in the separation between the edge modes  ([arXiv:cond-mat/0010440](https://arxiv.org/abs/cond-mat/0010440)).
As a Majorana stabilizer code, however, its distance is $1$ because a single MZM is already a logical operator. The code therefore does not protect against single-Majorana, parity-violating errors such as quasiparticle poisoning.
Disorder may help with protection  ([arXiv:1108.3845](https://arxiv.org/abs/1108.3845)).

## General gates

- Braiding, $S$, and $T$ phase gates, fermion $CZ_f$, and mixed qubit-fermion $CZ_{qf}$ gates are described for logical fermions encoded in this repetition code  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).

## Decoders

- Local automaton decoder based on a self-dual cellular automaton  ([arXiv:1711.08196](https://arxiv.org/abs/1711.08196)).
- Syndrome extraction of the stabilizers $S_j=i\gamma_{2j}\gamma_{2j+1}$ can be performed by interfacing with a qubit ancilla and mixed qubit-fermion gates  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)).

## Realizations

- Photonic systems: braiding of topological Majorana modes has been simulated in a device that has a different notion of locality than a bona fide fermionic system  ([arXiv:1411.7751](https://arxiv.org/abs/1411.7751)).
- Superconducting circuits: preparation  ([arXiv:2206.00563](https://arxiv.org/abs/2206.00563)), braiding  ([arXiv:2203.15083](https://arxiv.org/abs/2203.15083)), and detection of Majorana edge modes  ([arXiv:2203.15083](https://arxiv.org/abs/2203.15083), [arXiv:2204.11372](https://arxiv.org/abs/2204.11372)) have been simulated in devices that have a different notion of locality than a bona fide fermionic system.

## Relations

- _parent_: [[concepts/qec/majorana-stab]]
- _parent_: [[concepts/qec/spt]] — The Kitaev chain is a 1D fermionic SPT (more precisely, a 1D topological superconductor) protected by fermion parity symmetry.
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/mbq]] — Majorana box qubit codes are defined to be positive-parity logical subspaces of two or more Kitaev-chain code blocks. The parameter $n$ in the MBQ code definition corresponds to the number of Kitaev chains used in the construction, and not the total number of physical Majorana modes of the chains.
- _cousin_: [[concepts/qec/quantum-repetition]] — The Kitaev chain code can be thought of as the Majorana stabilizer analogue of the quantum repetition code  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)) and is related to that code via the Jordan-Wigner transformation  ([arXiv:0904.2771](https://arxiv.org/abs/0904.2771)).
- _cousin_: [[concepts/qec/jw]] — The Kitaev chain code can be thought of as the Majorana stabilizer analogue of the quantum repetition code  ([arXiv:2411.08955](https://arxiv.org/abs/2411.08955)) and is related to that code via the Jordan-Wigner transformation  ([arXiv:0904.2771](https://arxiv.org/abs/0904.2771)).

## Notes

- See notes  ([arXiv:0904.2771](https://arxiv.org/abs/0904.2771)) for a description of this code.
