---
type: concept
name: Commuting-projector Hamiltonian code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bravyi-bacon-shor
- concepts/qec/hamiltonian
- concepts/qec/qubit-stabilizer
- concepts/qec/qubit-subsystem-stabilizer
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/commuting_projector
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: commuting_projector
---

# Commuting-projector Hamiltonian code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/commuting_projector) (`code_id: commuting_projector`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Hamiltonian-based code whose Hamiltonian terms can be expressed as orthogonal projectors (i.e., Hermitian operators with eigenvalues 0 or 1) that commute with each other.

(source: raw/error-correction-zoo.md)

## Protection

Geometrically local commuting-projector code Hamiltonians on Euclidean manifolds are stable with respect to small perturbations when they satisfy the TQO conditions, meaning that a notion of a phase can be defined  ([arXiv:1001.4363](https://arxiv.org/abs/1001.4363), [arXiv:1001.0344](https://arxiv.org/abs/1001.0344), [arXiv:1810.02428](https://arxiv.org/abs/1810.02428), [arXiv:2010.15337](https://arxiv.org/abs/2010.15337)).
This notion can be extended to semi-hyperbolic manifolds  ([arXiv:2405.19412](https://arxiv.org/abs/2405.19412)) and non-geometrically local QLDPC codes exhibiting check soundness  ([arXiv:2411.01002](https://arxiv.org/abs/2411.01002)) (see also  ([arXiv:2411.02384](https://arxiv.org/abs/2411.02384))).
Hamiltonians satisfying a Peierls condition are stable to off-diagonal perturbations  ([arXiv:quant-ph/0111035](https://arxiv.org/abs/quant-ph/0111035)).

2D topological order on qubit manifolds requires weight-four (four-body) commuting-projector Hamiltonian terms, i.e., it cannot be stabilized via weight-two (two-body) or weight-three (three-body) terms on nearly Euclidean geometries of qubits or qutrits  ([arXiv:quant-ph/0308021](https://arxiv.org/abs/quant-ph/0308021), [arXiv:1102.0770](https://arxiv.org/abs/1102.0770), [arXiv:1803.02213](https://arxiv.org/abs/1803.02213)).

Ground-state spaces of commuting-projector Hamiltonians with weight-two (two-body) terms cannot be used to suppress errors in adiabatic quantum computation  ([arXiv:1410.5487](https://arxiv.org/abs/1410.5487)), but this can be circumvented with excited-state subspaces  ([arXiv:2412.07764](https://arxiv.org/abs/2412.07764)) or ground-state subspaces of subsystem code Hamiltonians, e.g., using BBS codes  ([arXiv:1511.01997](https://arxiv.org/abs/1511.01997), [arXiv:1606.03795](https://arxiv.org/abs/1606.03795)).
No eigenspace of a weight-two commuting-projector Hamiltonian can simultaneously have $d > 2$ and dimension greater than 1  ([arXiv:2412.07764](https://arxiv.org/abs/2412.07764)).

## Relations

- _parent_: [[concepts/qec/hamiltonian]] — Geometrically local commuting-projector code Hamiltonians on Euclidean manifolds are stable with respect to small perturbations when they satisfy the TQO conditions, meaning that a notion of a phase can be defined  ([arXiv:1001.4363](https://arxiv.org/abs/1001.4363), [arXiv:1001.0344](https://arxiv.org/abs/1001.0344), [arXiv:1810.02428](https://arxiv.org/abs/1810.02428), [arXiv:2010.15337](https://arxiv.org/abs/2010.15337)). This notion can be extended to semi-hyperbolic manifolds  ([arXiv:2405.19412](https://arxiv.org/abs/2405.19412)) and non-geometrically local QLDPC codes exhibiting check soundness  ([arXiv:2411.01002](https://arxiv.org/abs/2411.01002)) (see also  ([arXiv:2411.02384](https://arxiv.org/abs/2411.02384))). Hamiltonians admitting a Peierls condition are stable to off-diagonal perturbations  ([arXiv:quant-ph/0111035](https://arxiv.org/abs/quant-ph/0111035)).
- _cousin_: [[concepts/qec/topological]] — Geometrically local commuting-projector code Hamiltonians on Euclidean manifolds are stable with respect to small perturbations when they satisfy the TQO conditions, meaning that a notion of a phase can be defined  ([arXiv:1001.4363](https://arxiv.org/abs/1001.4363), [arXiv:1001.0344](https://arxiv.org/abs/1001.0344), [arXiv:1810.02428](https://arxiv.org/abs/1810.02428), [arXiv:2010.15337](https://arxiv.org/abs/2010.15337)). This notion can be extended to semi-hyperbolic manifolds  ([arXiv:2405.19412](https://arxiv.org/abs/2405.19412)) and non-geometrically local QLDPC codes exhibiting check soundness  ([arXiv:2411.01002](https://arxiv.org/abs/2411.01002)) (see also  ([arXiv:2411.02384](https://arxiv.org/abs/2411.02384))). Hamiltonians admitting a Peierls condition are stable to off-diagonal perturbations  ([arXiv:quant-ph/0111035](https://arxiv.org/abs/quant-ph/0111035)). 2D states admitting strict area-law entanglement necessarily have commuting-projector Hamiltonians  ([arXiv:2404.05867](https://arxiv.org/abs/2404.05867)). 2D topological order on qubit manifolds requires weight-four (four-body) commuting-projector Hamiltonian terms, i.e., it cannot be stabilized via weight-two (two-body) or weight-three (three-body) terms on nearly Euclidean geometries of qubits or qutrits  ([arXiv:quant-ph/0308021](https://arxiv.org/abs/quant-ph/0308021), [arXiv:1102.0770](https://arxiv.org/abs/1102.0770), [arXiv:1803.02213](https://arxiv.org/abs/1803.02213)).
- _cousin_: [[concepts/qec/qubit-stabilizer]] — Qubit stabilizer codes are *infectious*: if the ground-state subspace of an $\ell$-local commuting projector Hamiltonian contains a state close to a stabilizer state, then the entire ground-state space is close to a stabilizer code  ([arXiv:2503.04566](https://arxiv.org/abs/2503.04566), [arXiv:2504.19966](https://arxiv.org/abs/2504.19966)).
- _cousin_: [[concepts/qec/qubit-subsystem-stabilizer]] — Ground-state spaces of qubit commuting-projector Hamiltonians with weight-two (two-body) terms cannot be used to suppress errors in adiabatic quantum computation  ([arXiv:1410.5487](https://arxiv.org/abs/1410.5487)), but this can be circumvented with excited-state subspaces  ([arXiv:2412.07764](https://arxiv.org/abs/2412.07764)) or ground-state subspaces of subsystem code Hamiltonians, e.g., using BBS codes  ([arXiv:1511.01997](https://arxiv.org/abs/1511.01997), [arXiv:1606.03795](https://arxiv.org/abs/1606.03795)).
- _cousin_: [[concepts/qec/bravyi-bacon-shor]] — Ground-state spaces of qubit commuting-projector Hamiltonians with weight-two (two-body) terms cannot be used to suppress errors in adiabatic quantum computation  ([arXiv:1410.5487](https://arxiv.org/abs/1410.5487)), but this can be circumvented with excited-state subspaces  ([arXiv:2412.07764](https://arxiv.org/abs/2412.07764)) or ground-state subspaces of subsystem code Hamiltonians, e.g., using BBS codes  ([arXiv:1511.01997](https://arxiv.org/abs/1511.01997), [arXiv:1606.03795](https://arxiv.org/abs/1606.03795)).
