---
type: concept
name: Conformal-field theory (CFT) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/hamiltonian
- concepts/qec/holographic
- concepts/qec/qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cft
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cft
---

# Conformal-field theory (CFT) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cft) (`code_id: cft`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Approximate code whose codewords lie in the low-energy subspace of a conformal field theory, e.g., the quantum Ising model at its critical point  ([arXiv:1611.07528](https://arxiv.org/abs/1611.07528), [arXiv:2406.09555](https://arxiv.org/abs/2406.09555)).
Its encoding is argued to perform source coding (i.e., compression) as well as channel coding (i.e., error correction)  ([arXiv:1611.07528](https://arxiv.org/abs/1611.07528)).

(source: raw/error-correction-zoo.md)

## Protection

Code performance is quantified by a lower bound on the entanglement fidelity in terms of the conditional mutual information  ([arXiv:1611.07528](https://arxiv.org/abs/1611.07528)); see also  ([arXiv:1801.07271](https://arxiv.org/abs/1801.07271)).
Certain CFT codes have indefinite codespace complexity, and their protection depends on the minimum scaling dimension of the underlying CFT  ([arXiv:2310.04710](https://arxiv.org/abs/2310.04710)).
The coherent information of a combined noise and recovery channel can be perturbatively expanded  ([arXiv:2406.09555](https://arxiv.org/abs/2406.09555)).

## Code capacity threshold

- Threshold under dephasing depends on the structure of the conformal field theory, with the 1D critical Ising model admitting a finite threshold against certain dephasing noise  ([arXiv:2406.09555](https://arxiv.org/abs/2406.09555)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/hamiltonian]] — CFT codewords lie in the low-energy subspace of a conformal field theory (CFT), e.g., the quantum Ising model at its critical point.
- _parent_: [[concepts/qec/approximate-qecc]]
- _parent_: [[concepts/qec/holographic]] — CFT codewords lie in the low-energy subspace of a conformal field theory (CFT), e.g., the quantum Ising model at its critical point.
