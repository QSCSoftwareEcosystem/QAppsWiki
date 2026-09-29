---
type: concept
name: Hamiltonian Simulation
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/pauli-twirling
- concepts/qem/pea
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=hamiltonian-simulation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: hamiltonian-simulation
qem_catalog: applications
---

# Hamiltonian Simulation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=hamiltonian-simulation) (`id: hamiltonian-simulation`, catalog: applications, category: simulation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Simulating the time evolution of quantum many-body systems is a natural application for quantum computers. Error mitigation enables accurate simulation of dynamics for longer times and larger systems than raw hardware would allow. The IBM 127-qubit Ising model demonstration used PEA-based ZNE to achieve results beyond classical brute-force simulation.

(source: raw/qem-zoo.md)

## Key results

- 127-qubit kicked Ising model simulation with 60 layers of two-qubit gates
- ZNE with probabilistic error amplification (PEA) enabled accurate observable estimation
- Results verified against tensor network methods where tractable

## Related techniques

- [[concepts/qem/zne]] — uses
- [[concepts/qem/pea]] — uses
- [[concepts/qem/pauli-twirling]] — uses
- [[concepts/qem/dd]] — uses

## References

- Y. Kim, A. Eddins, S. Anand, K. X. Wei, E. van den Berg, S. Rosenblatt, H. Nayfeh, Y. Wu, M. Zaletel, K. Temme, A. Kandala. *Evidence for the Utility of Quantum Computing Before Fault Tolerance*. Nature, 2023 [doi](https://doi.org/10.1038/s41586-023-06096-3)
- M. Urbanek, B. Nachman, V. R. Pascuzzi, A. He, C. W. Bauer, W. A. de Jong. *Mitigating Depolarizing Noise on Quantum Computers with Noise-Estimation Circuits*. Physical Review Letters, 2021 [arXiv:2103.08591](https://arxiv.org/abs/2103.08591) [doi](https://doi.org/10.1103/PhysRevLett.127.270502)
