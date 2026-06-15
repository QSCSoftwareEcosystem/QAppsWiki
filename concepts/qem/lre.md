---
type: concept
name: Layerwise Richardson Extrapolation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- LRE
- multivariate Richardson extrapolation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=lre
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: lre
---

# Layerwise Richardson Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=lre) (`id: lre`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Generalizes zero-noise extrapolation by scaling noise independently at each layer of a quantum circuit rather than uniformly across the entire circuit. This multivariate approach constructs a higher-dimensional extrapolation in the space of per-layer noise rates, enabling more accurate extrapolation to the zero-noise limit. The number of circuit variations scales polynomially with circuit depth $d$ for a fixed extrapolation order.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced compared to global ZNE at the same extrapolation order |
| Sampling overhead | \(\binom{d + k - 1}{k}\) circuit variations for depth \(d\) and order \(k\); exponential in order |
| Noise model required | Minimal; requires ability to scale noise at each layer independently |
| Applicability | Layered circuits (e.g., variational ansatze, Trotterized evolution) |

## Related techniques

- [[concepts/qem/zne]] — LRE is a multivariate generalization of ZNE

## References

- V. Russo, A. Mari. *Quantum Error Mitigation by Layerwise Richardson Extrapolation*. Physical Review A, 2024 [arXiv:2402.04000](https://arxiv.org/abs/2402.04000) [doi](https://doi.org/10.1103/PhysRevA.110.062420)
