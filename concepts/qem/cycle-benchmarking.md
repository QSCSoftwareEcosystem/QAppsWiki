---
type: concept
name: Cycle Benchmarking
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- CB
- per-cycle noise learning
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=cycle-benchmarking
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: cycle-benchmarking
qem_catalog: noise-learning
---

# Cycle Benchmarking

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=cycle-benchmarking) (`id: cycle-benchmarking`, catalog: noise-learning). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Efficiently characterizes noise on a per-cycle basis by running circuits with varying numbers of repeated gate cycles and fitting the decay of fidelity. Provides Pauli error rates for each cycle of gates without requiring full process tomography. Used by NOX and other learned-noise methods.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Scalability | Polynomial in qubit count |
| Noise captured | Per-cycle Pauli error rates |
| Learning method | Decay fitting from repeated cycles |
| Enables | NOX, learned noise amplification |

## References

- A. Erhard, J. J. Wallman, L. Postler, M. Meth, R. Stricker, E. A. Martinez, P. Schindler, T. Monz, J. Emerson, R. Blatt. *Characterizing Large-Scale Quantum Computers via Cycle Benchmarking*. Nature Communications, 2019 [arXiv:1902.08543](https://arxiv.org/abs/1902.08543) [doi](https://doi.org/10.1038/s41467-019-13068-7)
- S. Ferracin, A. Hashim, J.-L. Ville, R. Naik, A. Carignan-Dugas, H. Qassim, A. Morvan, D. I. Santiago, I. Siddiqi, J. J. Wallman. *Efficiently Improving the Performance of Noisy Quantum Computers*. Quantum, 2024 [arXiv:2201.10672](https://arxiv.org/abs/2201.10672) [doi](https://doi.org/10.22331/q-2024-07-15-1410)
