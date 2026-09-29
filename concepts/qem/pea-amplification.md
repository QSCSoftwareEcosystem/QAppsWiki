---
type: concept
name: Probabilistic Error Amplification
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- learned noise injection
- PEA
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=pea-amplification
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: pea-amplification
qem_catalog: noise-scaling
---

# Probabilistic Error Amplification

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=pea-amplification) (`id: pea-amplification`, catalog: noise-scaling). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Amplifies noise by learning the per-layer noise model (via sparse Pauli–Lindblad tomography) and probabilistically injecting additional Pauli errors proportional to the learned rates. Provides accurate, targeted amplification without the assumptions of pulse stretching or the discrete steps of folding.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Scale factors | Continuous |
| Hardware requirements | Noise characterization (Pauli–Lindblad learning) |
| Advantages | Accurate amplification using learned noise model; no pulse access needed |
| Disadvantages | Requires upfront noise learning; noise model may drift |

## References

- Y. Kim, A. Eddins, S. Anand, K. X. Wei, E. van den Berg, S. Rosenblatt, H. Nayfeh, Y. Wu, M. Zaletel, K. Temme, A. Kandala. *Evidence for the Utility of Quantum Computing Before Fault Tolerance*. Nature, 2023 [doi](https://doi.org/10.1038/s41586-023-06096-3)
- E. van den Berg, Z. K. Minev, A. Kandala, K. Temme. *Probabilistic Error Cancellation with Sparse Pauli–Lindblad Models on Noisy Quantum Processors*. Nature Physics, 2023 [arXiv:2201.09866](https://arxiv.org/abs/2201.09866) [doi](https://doi.org/10.1038/s41567-023-02042-2)
