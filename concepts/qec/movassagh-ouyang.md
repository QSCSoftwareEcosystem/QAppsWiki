---
type: concept
name: Movassagh-Ouyang Hamiltonian code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/frustration-free
- concepts/qec/hamiltonian
- concepts/qec/qubit-stabilizer
- concepts/qec/qubits-into-qubits
- concepts/qec/spins-into-spins
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/movassagh_ouyang
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: movassagh_ouyang
---

# Movassagh-Ouyang Hamiltonian code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/movassagh_ouyang) (`code_id: movassagh_ouyang`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

This is a family of codes derived via an algorithm that takes as input *any* binary classical code and outputs a quantum code (note that this framework can be extended to $q$-ary codes).  
The algorithm is probabilistic but succeeds almost surely if the classical code is random. 
An explicit code construction does exist for linear distance codes encoding one logical qubit using Radon's theorem  ([doi:10.1007/BF01464231](https://doi.org/10.1007/BF01464231), [doi:10.1007/978-1-4613-0039-7](https://doi.org/10.1007/978-1-4613-0039-7)). 
For finite rate codes, there is no rigorous proof that the construction algorithm succeeds, and approximate constructions are described instead.

This family strictly generalizes CSS codes (because CSS codes come only from linear or self-orthogonal classical codes). These codes can be shown to be realized as a subspace of the ground space of a (geometrically) local Hamiltonian.

(source: raw/error-correction-zoo.md)

## Protection

Let $C \subset \{0,1,\dots,q-1\}^n$ be a classical code with distance $d_x$. Let $d_z$ satisfy $q^n > 2 V_q(d_z-1) -1$, where $V_q(r)$ is the volume of the $q$-ary Hamming ball of radius $r$. Then the algorithm produces a quantum code with distance $d = \min(d_x,d_z)$. Asymptotically, the distance scales linearly with $n$.

## Rate

The rate depends on the classical code, but distance can scale linearly with $n$.

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/hamiltonian]] — Movassagh-Ouyang codes reside in the ground space of a Hamiltonian. Justesen codes can be used to build a family of $n$-qubit Movassagh-Ouyang Hamiltonian spin codes encoding one logical qubit with linear distance. These codes form the ground-state subspace of a frustration-free geometrically local Hamiltonian  ([arXiv:2012.01453](https://arxiv.org/abs/2012.01453)).
- _cousin_: [[concepts/qec/qubit-stabilizer]] — Many, but not all, Movassagh-Ouyang codes are stabilizer codes.
- _cousin_: [`bits_into_bits`](https://errorcorrectionzoo.org/c/bits_into_bits) — Movassagh-Ouyang codes are constructed from classical binary codes.
- _cousin_: [`justesen`](https://errorcorrectionzoo.org/c/justesen) — Justesen codes can be used to build a family of $n$-qubit Movassagh-Ouyang Hamiltonian spin codes encoding one logical qubit with linear distance. These codes form the ground-state subspace of a frustration-free geometrically local Hamiltonian  ([arXiv:2012.01453](https://arxiv.org/abs/2012.01453)).
- _cousin_: [[concepts/qec/spins-into-spins]] — Justesen codes can be used to build a family of $n$-qubit Movassagh-Ouyang Hamiltonian spin codes encoding one logical qubit with linear distance. These codes form the ground-state subspace of a frustration-free geometrically local Hamiltonian  ([arXiv:2012.01453](https://arxiv.org/abs/2012.01453)).
- _cousin_: [[concepts/qec/frustration-free]] — Movassagh-Ouyang codes reside in the ground space of a Hamiltonian. Justesen codes can be used to build a family of $n$-qubit Movassagh-Ouyang Hamiltonian spin codes encoding one logical qubit with linear distance. These codes form the ground-state subspace of a frustration-free geometrically local Hamiltonian  ([arXiv:2012.01453](https://arxiv.org/abs/2012.01453)).
