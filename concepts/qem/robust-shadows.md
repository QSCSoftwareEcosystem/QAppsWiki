---
type: concept
name: Robust Shadow Estimation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- RSE
- error-mitigated classical shadows
- noise-resilient shadows
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/logical-shadow-tomography
- concepts/qem/measurement-error-mitigation
- concepts/qem/symmetry-adjusted-shadows
- concepts/qem/trex
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=robust-shadows
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: robust-shadows
---

# Robust Shadow Estimation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=robust-shadows) (`id: robust-shadows`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Extends the classical shadow estimation protocol to be robust against noise by adding a calibration stage. Instead of assuming ideal measurement channels, the protocol characterizes the noisy measurement channel and uses the calibrated inverse to construct unbiased classical shadows. This enables sample-efficient estimation of many observables simultaneously while being resilient to gate and measurement errors, with only minimal assumptions on the noise.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Zero (unbiased estimator with calibrated inverse) |
| Sampling overhead | Same as standard shadows up to a noise-dependent multiplicative factor |
| Noise model required | Calibration via a small set of known input states; no explicit noise model |
| Applicability | Any observable estimation task; especially useful for tomographic and many-observable settings |

## Related techniques

- [[concepts/qem/measurement-error-mitigation]] — both calibrate the measurement channel; RSE generalizes to full shadow framework
- [[concepts/qem/trex]] — both mitigate measurement-stage noise with calibration
- [[concepts/qem/logical-shadow-tomography]] — both use shadow tomography; LST adds codespace projection for error mitigation
- [[concepts/qem/symmetry-adjusted-shadows]] — both extend classical shadows; SAS uses symmetry structure instead of calibration

## References

- S. Chen, W. Yu, P. Zeng, S. T. Flammia. *Robust Shadow Estimation*. PRX Quantum, 2021 [arXiv:2011.09636](https://arxiv.org/abs/2011.09636) [doi](https://doi.org/10.1103/PRXQuantum.2.030348)
