---
type: concept
name: Physics-Inspired Extrapolation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- PIE
- physics-inspired ZNE
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/emre
- concepts/qem/hemre
- concepts/qem/lre
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=pie
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: pie
---

# Physics-Inspired Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=pie) (`id: pie`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Performs zero-noise extrapolation using a theoretically motivated fitting function derived from the EMRE framework rather than heuristic polynomial or exponential models. The model $f(\lambda) = \langle O \rangle_{\text{ideal}} \cdot s^{-\lambda}$ linearizes in log-space, where the intercept gives the ideal expectation value and the slope equals the max-relative entropy between ideal and noisy circuits. This provides simultaneous error mitigation and hardware certification at no additional cost. Demonstrated on 84-qubit IBM Eagle processor.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Low; converges to zero as noise decreases. Comes from neglecting the GQPD correction term |
| Sampling overhead | Linear (~4× base circuit execution); typically requires only 4 noise-scaled data points |
| Noise model required | None; noise-agnostic like standard ZNE |
| Applicability | Shallow-to-moderate depth circuits; demonstrated at scale (84 qubits) |

## Related techniques

- [[concepts/qem/zne]] — PIE uses the same circuit folding as ZNE but with a physics-motivated fitting function
- [[concepts/qem/emre]] — PIE's fitting function is derived from EMRE's generalized quasi-probability decomposition
- [[concepts/qem/hemre]] — both build on the EMRE theoretical framework
- [[concepts/qem/lre]] — both are extrapolation-based methods; PIE uses a single global physics-motivated model

## References

- P. Diez-Valle, G. Saxena, J. S. Baker, J.-H. Lee, T. H. Kyaw. *Physics-Inspired Extrapolation for Efficient Error Mitigation and Hardware Certification*. arXiv preprint, 2025 [arXiv:2505.07977](https://arxiv.org/abs/2505.07977) [doi](https://doi.org/10.48550/arXiv.2505.07977)
- G. Saxena, T. H. Kyaw. *Error Mitigation by Restricted Evolution*. arXiv preprint, 2024 [arXiv:2409.06636](https://arxiv.org/abs/2409.06636) [doi](https://doi.org/10.48550/arXiv.2409.06636)
