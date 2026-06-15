---
type: concept
name: Benchmarked-Noise Zero-Noise Extrapolation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- bnZNE
- benchmarked-noise ZNE
- benchmark-calibrated ZNE
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/accreditation
- concepts/qem/cdr
- concepts/qem/odr
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=bnzne
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: bnzne
---

# Benchmarked-Noise Zero-Noise Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=bnzne) (`id: bnzne`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Improves zero-noise extrapolation by replacing nominal noise-scaling factors with empirically measured error rates derived from verifiable benchmark circuits. The benchmark circuits mirror the application circuit's native-gate structure but have classically computable outputs, enabling accurate quantification of the actual noise at each ZNE level. Also introduces a general bias-mitigation framework where dividing the QEM estimate by the benchmark's QEM estimate cancels leading-order bias. Demonstrated up to 15% fidelity improvement over standard ZNE on 100-qubit experiments on IBM superconducting hardware.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced compared to standard ZNE; leading-order bias cancels via benchmark calibration |
| Sampling overhead | Approximately 2x standard ZNE (application + benchmark circuits at each noise level) |
| Noise model required | None; benchmark circuits empirically characterize the noise |
| Applicability | Any biased QEM method (general bias-mitigation framework); demonstrated at utility scale (100 qubits, up to 2000 entangling gates) |

## Related techniques

- [[concepts/qem/zne]] — bnZNE improves ZNE's extrapolation by using benchmark-calibrated noise levels
- [[concepts/qem/cdr]] — both use classically verifiable circuits to calibrate error mitigation
- [[concepts/qem/odr]] — both use calibration circuits with known outputs to estimate noise effects
- [[concepts/qem/accreditation]] — both use verifiable circuits to assess or improve QEM output quality

## References

- J. Harris, K. Lively, P. K. Schuhmacher. *Reducing Quantum Error Mitigation Bias Using Verifiable Benchmark Circuits*. arXiv preprint, 2026 [arXiv:2603.10224](https://arxiv.org/abs/2603.10224)
