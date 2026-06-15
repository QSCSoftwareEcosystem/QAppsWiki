---
type: concept
name: Operator Decoherence Renormalization
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- ODR
- noise renormalization
- noise-estimation circuits
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/cdr
- concepts/qem/trex
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=odr
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: odr
---

# Operator Decoherence Renormalization

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=odr) (`id: odr`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Estimates the effective decoherence rate acting on a target observable by running short 'noise-estimation circuits' — circuits structurally similar to the target but with known ideal outputs. The measured decay rate is then used to renormalize (rescale) the noisy expectation value of the target observable, dividing out the noise-induced suppression factor. The method is simple, requires no detailed noise model, and is particularly effective for depolarizing-like noise.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Residual bias if noise on estimation circuits differs from target circuit |
| Sampling overhead | Low; requires running a small number of additional calibration circuits |
| Noise model required | Minimal; assumes noise acts as a multiplicative suppression on observables |
| Applicability | Expectation value estimation; demonstrated in quantum simulation and Fourier moment computation |

## Related techniques

- [[concepts/qem/trex]] — both correct multiplicative noise factors via calibration
- [[concepts/qem/zne]] — both address systematic noise bias; ODR uses direct rescaling instead of extrapolation
- [[concepts/qem/cdr]] — both use classically simulable calibration circuits to learn noise effects

## References

- M. Urbanek, B. Nachman, V. R. Pascuzzi, A. He, C. W. Bauer, W. A. de Jong. *Mitigating Depolarizing Noise on Quantum Computers with Noise-Estimation Circuits*. Physical Review Letters, 2021 [arXiv:2103.08591](https://arxiv.org/abs/2103.08591) [doi](https://doi.org/10.1103/PhysRevLett.127.270502)
