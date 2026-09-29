---
type: concept
name: Polynomial Extrapolation
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- polynomial fit
- quadratic extrapolation
- higher-order polynomial
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=polynomial-extrapolation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: polynomial-extrapolation
qem_catalog: extrapolation
---

# Polynomial Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=polynomial-extrapolation) (`id: polynomial-extrapolation`, catalog: extrapolation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Fits a polynomial $f(\lambda) = a_0 + a_1\lambda + a_2\lambda^2 + \cdots + a_n\lambda^n$ to measured data and extrapolates to $\lambda = 0$. Higher-order polynomials can capture nonlinear noise dependence but require more data points and may suffer from overfitting or numerical instability.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Data points required | n+1 for degree-n polynomial |
| Assumptions | Noise dependence is well-approximated by a polynomial |
| Bias | \(O(\lambda^{n+1})\) for degree-n polynomial |
| Variance | Increases with polynomial degree |

## References

- K. Temme, S. Bravyi, J. M. Gambetta. *Error Mitigation for Short-Depth Quantum Circuits*. Physical Review Letters, 2017 [arXiv:1612.02058](https://arxiv.org/abs/1612.02058) [doi](https://doi.org/10.1103/PhysRevLett.119.180509)
- T. Giurgica-Tiron, Y. Hindy, R. LaRose, A. Mari, W. J. Zeng. *Digital Zero Noise Extrapolation for Quantum Error Mitigation*. IEEE International Conference on Quantum Computing and Engineering (QCE), 2020 [arXiv:2005.10921](https://arxiv.org/abs/2005.10921) [doi](https://doi.org/10.1109/QCE49297.2020.00045)
