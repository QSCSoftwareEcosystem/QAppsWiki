---
type: concept
name: Error Mitigation by Restricted Evolution
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- EMRE
- restricted evolution mitigation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/hemre
- concepts/qem/pec
- concepts/qem/pie
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=emre
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: emre
---

# Error Mitigation by Restricted Evolution

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=emre) (`id: emre`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Trades unbiasedness for constant sampling overhead by retaining only the positive (implementable) part of the quasi-probability decomposition used in PEC. For each ideal gate, EMRE finds the closest implementable operation in the semidefinite ordering sense and a scaling factor (the generalized robustness $R^+$) that quantifies the distance. The resulting estimator has finite bias that depends on the generalized robustness, but its sample complexity is constant — independent of noise rate and circuit depth.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Finite; bounded by \(s - 1\) where \(s = \prod_i (1 + R^+_i)\) grows with circuit depth |
| Sampling overhead | Constant: \(M = \frac{2}{c^2} \ln(2/p_{\text{fail}})\), independent of noise and depth |
| Noise model required | Full characterization of gate noise to compute the generalized quasi-probability decomposition |
| Applicability | High-fidelity hardware (gate fidelity ≥ 99.7%); shallow-to-moderate depth circuits |

## Related techniques

- [[concepts/qem/pec]] — EMRE uses the same quasi-probability framework as PEC but discards the negative correction terms
- [[concepts/qem/hemre]] — HEMRE is a hybrid protocol interpolating between EMRE and PEC
- [[concepts/qem/pie]] — PIE derives its extrapolation model from EMRE's theoretical framework
- [[concepts/qem/zne]] — EMRE avoids the heuristic extrapolation model assumptions of ZNE

## References

- G. Saxena, T. H. Kyaw. *Error Mitigation by Restricted Evolution*. arXiv preprint, 2024 [arXiv:2409.06636](https://arxiv.org/abs/2409.06636) [doi](https://doi.org/10.48550/arXiv.2409.06636)
