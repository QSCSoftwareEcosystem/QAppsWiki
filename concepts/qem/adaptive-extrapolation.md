---
type: concept
name: Adaptive Extrapolation
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- model selection
- cross-validated extrapolation
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=adaptive-extrapolation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: adaptive-extrapolation
qem_catalog: extrapolation
---

# Adaptive Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=adaptive-extrapolation) (`id: adaptive-extrapolation`, catalog: extrapolation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Automatically selects the best extrapolation model (linear, polynomial, exponential, etc.) based on the data using cross-validation or information criteria (AIC, BIC). Reduces bias from choosing an inappropriate model while controlling for overfitting.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Data points required | Enough for cross-validation (typically ≥5) |
| Assumptions | True model is among the candidates |
| Bias | Adapts to data; generally lower than fixed model |
| Complexity | Higher computational cost; automated model selection |

## References

- T. Giurgica-Tiron, Y. Hindy, R. LaRose, A. Mari, W. J. Zeng. *Digital Zero Noise Extrapolation for Quantum Error Mitigation*. IEEE International Conference on Quantum Computing and Engineering (QCE), 2020 [arXiv:2005.10921](https://arxiv.org/abs/2005.10921) [doi](https://doi.org/10.1109/QCE49297.2020.00045)
- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
