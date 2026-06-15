---
type: concept
name: Hybrid Error Mitigation by Restricted Evolution
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- HEMRE
- hybrid EMRE
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/emre
- concepts/qem/pec
- concepts/qem/pie
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=hemre
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: hemre
---

# Hybrid Error Mitigation by Restricted Evolution

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=hemre) (`id: hemre`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Interpolates continuously between PEC and EMRE by introducing an adjustable bias tolerance parameter $\Delta_{\text{fixed}}$. Gates whose generalized robustness is below the threshold receive the EMRE approximation (biased but cheap), while remaining gates receive full PEC treatment (unbiased but expensive). At $\Delta_{\text{fixed}} = 0$ HEMRE reduces to PEC; as $\Delta_{\text{fixed}} \to \infty$ it reduces to EMRE.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Tunable; bounded by user-specified \(\Delta_{\text{fixed}}\) |
| Sampling overhead | Intermediate between PEC (exponential) and EMRE (constant); depends on gate partition |
| Noise model required | Full characterization of gate noise for both EMRE and PEC decompositions |
| Applicability | Moderate-noise regimes (0.1%–1% error rates) where neither pure EMRE nor pure PEC is optimal |

## Related techniques

- [[concepts/qem/pec]] — HEMRE reduces to PEC when the bias tolerance is zero
- [[concepts/qem/emre]] — HEMRE reduces to EMRE when the bias tolerance is unlimited
- [[concepts/qem/pie]] — both build on the EMRE theoretical framework
- [[concepts/qem/zne]] — HEMRE avoids model-dependent extrapolation

## References

- G. Saxena, T. H. Kyaw. *Error Mitigation by Restricted Evolution*. arXiv preprint, 2024 [arXiv:2409.06636](https://arxiv.org/abs/2409.06636) [doi](https://doi.org/10.48550/arXiv.2409.06636)
