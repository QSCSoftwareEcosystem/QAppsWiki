---
type: concept
name: Virtual Noise Scaling
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- VNS
- shifted Taylor mitigation
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=virtual-noise-scaling
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: virtual-noise-scaling
qem_catalog: extrapolation
---

# Virtual Noise Scaling

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=virtual-noise-scaling) (`id: virtual-noise-scaling`, catalog: extrapolation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Replaces the Richardson coefficients applied to noise-amplified expectation values with coefficients from a Taylor expansion recentered on the noise spectrum. Standard mitigation expands around the zero-noise point $s = 1$, which sits at the edge of the noise eigenvalue distribution rather than inside it. Rescaling the noise operator by a constant $g$ shifts the eigenvalues onto the plateau of the mitigation function, where they are mapped to 1 most accurately, cutting the runtime overhead needed to reach a given mitigated infidelity. The rescaling is post-processing: no extra circuits are run.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Data points required | Same as the underlying amplification scheme; order \(m\) uses \(m+1\) amplified circuits |
| Assumptions | Agnostic noise amplification with constant-step amplification factors (KIK, folding ZNE, PEA) |
| Bias | Set by the mitigation order; the recentering lowers the worst-case infidelity at fixed order |
| Overhead | Orders of magnitude below Richardson post-processing in the strong-noise regime |

## References

- R. Uzdin. *Orders of Magnitude Sampling Overhead Reduction in Quantum Error Mitigation*. arXiv preprint, 2026 [arXiv:2601.22785](https://arxiv.org/abs/2601.22785) [doi](https://doi.org/10.48550/arXiv.2601.22785)
