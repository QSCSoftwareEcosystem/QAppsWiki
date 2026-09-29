---
type: concept
name: Poly-Exponential Extrapolation
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- polyexp
- polynomial-exponential
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=poly-exponential
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: poly-exponential
qem_catalog: extrapolation
---

# Poly-Exponential Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=poly-exponential) (`id: poly-exponential`, catalog: extrapolation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Combines polynomial and exponential models: $f(\lambda) = (a_0 + a_1\lambda + \cdots) \cdot e^{-b\lambda}$. Captures both the polynomial correction terms and the overall exponential decay. Often provides better fits than pure polynomial or pure exponential models.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Data points required | Depends on polynomial order + exponential parameters |
| Assumptions | Poly-exponential noise dependence |
| Bias | Can be lower than pure polynomial or exponential |
| Complexity | More parameters to fit; risk of overfitting |

## References

- T. Giurgica-Tiron, Y. Hindy, R. LaRose, A. Mari, W. J. Zeng. *Digital Zero Noise Extrapolation for Quantum Error Mitigation*. IEEE International Conference on Quantum Computing and Engineering (QCE), 2020 [arXiv:2005.10921](https://arxiv.org/abs/2005.10921) [doi](https://doi.org/10.1109/QCE49297.2020.00045)
