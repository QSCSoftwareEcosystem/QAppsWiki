---
type: concept
name: Exponential Extrapolation
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- exponential fit
- exponential decay model
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=exponential-extrapolation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: exponential-extrapolation
qem_catalog: extrapolation
---

# Exponential Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=exponential-extrapolation) (`id: exponential-extrapolation`, catalog: extrapolation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Fits an exponential function $f(\lambda) = a \cdot e^{-b\lambda} + c$ or $f(\lambda) = a \cdot e^{b\lambda}$ to the data. Motivated by the physical intuition that expectation values often decay exponentially with circuit depth/noise. Can provide better extrapolation than polynomials when the true decay is exponential.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Data points required | Minimum 3 (for 3 parameters) |
| Assumptions | Exponential noise dependence |
| Bias | Depends on how well exponential model matches true behavior |
| Stability | Generally more stable than high-order polynomials |

## References

- T. Giurgica-Tiron, Y. Hindy, R. LaRose, A. Mari, W. J. Zeng. *Digital Zero Noise Extrapolation for Quantum Error Mitigation*. IEEE International Conference on Quantum Computing and Engineering (QCE), 2020 [arXiv:2005.10921](https://arxiv.org/abs/2005.10921) [doi](https://doi.org/10.1109/QCE49297.2020.00045)
- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
