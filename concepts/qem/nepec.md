---
type: concept
name: Noise-Extended Probabilistic Error Cancellation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- NEPEC
- noise-scaled PEC
- extended PEC
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pea
- concepts/qem/pec
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=nepec
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: nepec
---

# Noise-Extended Probabilistic Error Cancellation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=nepec) (`id: nepec`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Combines probabilistic error cancellation (PEC) with zero-noise extrapolation (ZNE) by extending the quasi-probability decomposition to include noise-scaled operations. Standard PEC requires expressing ideal gates as combinations of noisy implementable operations, but this decomposition may not exist or may have prohibitive overhead. NEPEC overcomes this by first scaling noise to higher levels where decompositions are possible, then extrapolating to the zero-noise limit. The framework also enables 'gate extrapolation' — performing PEC without knowing the noise model by extrapolating from multiple noise levels.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Zero in principle (unbiased PEC combined with extrapolation) |
| Sampling overhead | Reduced compared to pure PEC; combines quasi-probability sampling with extrapolation |
| Noise model required | Partial or none; can use gate extrapolation to avoid explicit noise characterization |
| Applicability | General-purpose; especially useful when standard PEC decomposition is unavailable or expensive |

## Related techniques

- [[concepts/qem/pec]] — NEPEC extends PEC by incorporating noise scaling
- [[concepts/qem/zne]] — NEPEC uses extrapolation to the zero-noise limit
- [[concepts/qem/pea]] — both combine noise scaling with other QEM techniques

## References

- A. Mari, N. Shammah, W. J. Zeng. *Extending Quantum Probabilistic Error Cancellation by Noise Scaling*. Physical Review A, 2021 [arXiv:2108.02237](https://arxiv.org/abs/2108.02237) [doi](https://doi.org/10.1103/PhysRevA.104.052607)
