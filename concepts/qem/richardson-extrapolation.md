---
type: concept
name: Richardson Extrapolation
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Richardson's deferred approach to the limit
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=richardson-extrapolation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: richardson-extrapolation
qem_catalog: extrapolation
---

# Richardson Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=richardson-extrapolation) (`id: richardson-extrapolation`, catalog: extrapolation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

A systematic method for improving accuracy by combining estimates at different noise levels with carefully chosen weights. For scale factors $\lambda_1, \lambda_2, \ldots, \lambda_n$, the Richardson estimator cancels leading-order error terms. Equivalent to polynomial extrapolation but with a specific choice of scale factors that simplifies the analysis.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Data points required | n for order-n Richardson |
| Assumptions | Error expansion: \(\langle O \rangle(\lambda) = \langle O \rangle_0 + \sum_k c_k \lambda^k\) |
| Bias | \(O(\lambda^n)\) for order-n Richardson |
| Optimal scale factors | Often \(\lambda_i = 2^{i-1}\) or similar geometric sequence |

## References

- K. Temme, S. Bravyi, J. M. Gambetta. *Error Mitigation for Short-Depth Quantum Circuits*. Physical Review Letters, 2017 [arXiv:1612.02058](https://arxiv.org/abs/1612.02058) [doi](https://doi.org/10.1103/PhysRevLett.119.180509)
- V. Russo, A. Mari. *Quantum Error Mitigation by Layerwise Richardson Extrapolation*. Physical Review A, 2024 [arXiv:2402.04000](https://arxiv.org/abs/2402.04000) [doi](https://doi.org/10.1103/PhysRevA.110.062420)
