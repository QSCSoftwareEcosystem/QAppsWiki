---
type: concept
name: Twirled Readout Error eXtinction
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- TREX
- measurement twirling
- twirled readout mitigation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/measurement-error-mitigation
- concepts/qem/pauli-twirling
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=trex
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: trex
---

# Twirled Readout Error eXtinction

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=trex) (`id: trex`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Mitigates readout errors by randomly applying Pauli-X bit flips before measurement and tracking the flips classically. This twirling diagonalizes an arbitrary readout-noise channel into a single multiplicative factor per Pauli observable, which can be estimated and divided out. The method is model-free — it does not require characterizing the full assignment matrix — and avoids the exponential overhead of full matrix inversion.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Zero (in principle); multiplicative correction is exact if calibration factor is accurate |
| Sampling overhead | Moderate; increases with readout error rate but avoids exponential matrix inversion |
| Noise model required | None (model-free); only requires ability to insert bit flips before measurement |
| Applicability | General-purpose readout error mitigation; used as resilience level 1 in Qiskit Runtime |

## Related techniques

- [[concepts/qem/measurement-error-mitigation]] — both address readout errors; TREX avoids explicit confusion-matrix inversion
- [[concepts/qem/pauli-twirling]] — both use Pauli randomization to simplify noise structure

## References

- E. van den Berg, Z. K. Minev, K. Temme. *Model-Free Readout-Error Mitigation for Quantum Expectation Values*. Physical Review A, 2022 [arXiv:2012.09738](https://arxiv.org/abs/2012.09738) [doi](https://doi.org/10.1103/PhysRevA.105.032620)
