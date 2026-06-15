---
type: concept
name: Probabilistic Error Cancellation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- PEC
- quasi-probability decomposition
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/emre
- concepts/qem/hemre
- concepts/qem/measurement-error-mitigation
- concepts/qem/pauli-twirling
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=pec
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: pec
---

# Probabilistic Error Cancellation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=pec) (`id: pec`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Decomposes each ideal (noiseless) gate operation into a linear combination of noisy implementable operations with real (possibly negative) quasi-probability coefficients. By randomly sampling from this decomposition and weighting results by the sign of the coefficient, the noise-free expectation value is recovered exactly in the limit of infinite samples.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Zero (unbiased estimator) |
| Sampling overhead | Exponential: scales as \(\gamma^2\) where \(\gamma = \prod_i C_i\) is the total one-norm of the quasi-probability decomposition |
| Noise model required | Full characterization of local gate noise (e.g., via gate set tomography) |
| Scalability | Overhead grows exponentially with circuit depth and noise rate |

## Related techniques

- [[concepts/qem/pauli-twirling]] — Pauli twirling simplifies noise model for PEC
- [[concepts/qem/zne]] — both are foundational QEM techniques
- [[concepts/qem/measurement-error-mitigation]] — PEC can be combined with REM for full-circuit mitigation
- [[concepts/qem/emre]] — EMRE retains only the positive part of PEC's quasi-probability decomposition
- [[concepts/qem/hemre]] — HEMRE interpolates between PEC and EMRE

## References

- K. Temme, S. Bravyi, J. M. Gambetta. *Error Mitigation for Short-Depth Quantum Circuits*. Physical Review Letters, 2017 [arXiv:1612.02058](https://arxiv.org/abs/1612.02058) [doi](https://doi.org/10.1103/PhysRevLett.119.180509)
- S. Endo, S. C. Benjamin, Y. Li. *Practical Quantum Error Mitigation for Near-Future Applications*. Physical Review X, 2018 [arXiv:1712.09271](https://arxiv.org/abs/1712.09271) [doi](https://doi.org/10.1103/PhysRevX.8.031027)
- E. van den Berg, Z. K. Minev, A. Kandala, K. Temme. *Probabilistic Error Cancellation with Sparse Pauli–Lindblad Models on Noisy Quantum Processors*. Nature Physics, 2023 [arXiv:2201.09866](https://arxiv.org/abs/2201.09866) [doi](https://doi.org/10.1038/s41567-023-02042-2)
- C. Piveteau, D. Sutter, S. Woerner. *Quasiprobability Decompositions with Reduced Sampling Overhead*. npj Quantum Information, 2022 [arXiv:2101.09290](https://arxiv.org/abs/2101.09290) [doi](https://doi.org/10.1038/s41534-022-00517-3)
