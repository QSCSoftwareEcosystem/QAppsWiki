---
type: concept
name: Crosstalk-Adaptive Scheduling
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- CAS
- XtalkSched
- crosstalk-aware compilation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/noise-aware-compilation
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=crosstalk-mitigation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: crosstalk-mitigation
---

# Crosstalk-Adaptive Scheduling

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=crosstalk-mitigation) (`id: crosstalk-mitigation`, category: suppression). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Suppresses crosstalk errors by intelligently scheduling gate operations to avoid simultaneous execution on qubit pairs with high crosstalk. The method first characterizes crosstalk via simultaneous randomized benchmarking, then formulates gate scheduling as an optimization problem that balances serialization (to avoid crosstalk) against parallelism (to minimize decoherence from extended circuit duration). Demonstrated up to 5.6x error reduction on 20-qubit IBM systems.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced; avoids crosstalk-induced coherent errors |
| Sampling overhead | None (same number of shots); may increase circuit duration from serialization |
| Noise model required | Crosstalk characterization via simultaneous randomized benchmarking |
| Applicability | Multi-qubit circuits on hardware with significant crosstalk (e.g., superconducting processors) |

## Related techniques

- [[concepts/qem/dd]] — both are suppression techniques; DD handles idle noise, CAS handles crosstalk
- [[concepts/qem/noise-aware-compilation]] — both use hardware calibration data to improve circuit execution

## References

- P. Murali, D. C. McKay, M. Martonosi, A. Javadi-Abhari. *Software Mitigation of Crosstalk on Noisy Intermediate-Scale Quantum Computers*. ASPLOS, 2020 [arXiv:2001.02826](https://arxiv.org/abs/2001.02826) [doi](https://doi.org/10.1145/3373376.3378477)
