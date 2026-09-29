---
type: concept
name: Randomized Benchmarking
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- RB
- Clifford RB
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=randomized-benchmarking
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: randomized-benchmarking
qem_catalog: noise-learning
---

# Randomized Benchmarking

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=randomized-benchmarking) (`id: randomized-benchmarking`, catalog: noise-learning). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Estimates average gate fidelity by running random sequences of Clifford gates followed by an inverting gate. The decay of success probability with sequence length gives the average error per Clifford. Efficient and robust to SPAM errors, but provides only aggregate fidelity, not detailed noise structure.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Scalability | Scales to many qubits |
| Noise captured | Average error rate per gate (not detailed structure) |
| Learning method | Exponential decay fitting |
| Enables | Fidelity benchmarking, rough noise estimates |

## References

- E. Magesan, J. M. Gambetta, J. Emerson. *Scalable and Robust Randomized Benchmarking of Quantum Processes*. Physical Review Letters, 2011 [arXiv:1009.3639](https://arxiv.org/abs/1009.3639) [doi](https://doi.org/10.1103/PhysRevLett.106.180504)
