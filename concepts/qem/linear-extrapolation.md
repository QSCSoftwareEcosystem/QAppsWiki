---
type: concept
name: Linear Extrapolation
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- first-order extrapolation
- linear fit
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=linear-extrapolation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: linear-extrapolation
qem_catalog: extrapolation
---

# Linear Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=linear-extrapolation) (`id: linear-extrapolation`, catalog: extrapolation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Fits a linear function $f(\lambda) = a + b\lambda$ to expectation values measured at multiple noise levels and extrapolates to $\lambda = 0$. The simplest extrapolation method, requiring only two noise levels. Works well when the noise dependence is approximately linear, but introduces systematic bias for nonlinear noise scaling.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Data points required | Minimum 2 |
| Assumptions | Linear noise dependence: \(\langle O \rangle(\lambda) \approx a + b\lambda\) |
| Bias | \(O(\lambda^2)\) for nonlinear noise dependence |
| Variance | Low (fewest parameters to fit) |

## References

- K. Temme, S. Bravyi, J. M. Gambetta. *Error Mitigation for Short-Depth Quantum Circuits*. Physical Review Letters, 2017 [arXiv:1612.02058](https://arxiv.org/abs/1612.02058) [doi](https://doi.org/10.1103/PhysRevLett.119.180509)
- Y. Li, S. C. Benjamin. *Efficient Variational Quantum Simulator Incorporating Active Error Minimization*. Physical Review X, 2017 [arXiv:1611.09301](https://arxiv.org/abs/1611.09301) [doi](https://doi.org/10.1103/PhysRevX.7.021050)
