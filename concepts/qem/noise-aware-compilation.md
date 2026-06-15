---
type: concept
name: Noise-Aware Compilation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- NAC
- noise-aware routing
- hardware-aware transpilation
- calibration-aware compilation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/crosstalk-mitigation
- concepts/qem/dd
- concepts/qem/pauli-twirling
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=noise-aware-compilation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: noise-aware-compilation
---

# Noise-Aware Compilation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=noise-aware-compilation) (`id: noise-aware-compilation`, category: suppression). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Suppresses errors at the compilation stage by using up-to-date hardware calibration data (gate error rates, coherence times, crosstalk maps) to make routing, qubit mapping, and gate scheduling decisions. This includes selecting low-error qubit subgraphs, routing SWAP operations through high-fidelity paths, and timing gate execution to avoid decoherence and crosstalk. Modern implementations recover up to 40% of missing fidelity compared to noise-unaware compilation.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced by avoiding high-error hardware resources |
| Sampling overhead | None; purely a compilation-stage optimization |
| Noise model required | Hardware calibration data (gate errors, T1/T2 times, crosstalk tables) |
| Applicability | Any quantum circuit; most impactful on hardware with non-uniform error rates |

## Related techniques

- [[concepts/qem/crosstalk-mitigation]] — CAS is a specific form of noise-aware compilation targeting crosstalk
- [[concepts/qem/dd]] — both are suppression techniques; NAC optimizes layout, DD optimizes idle periods
- [[concepts/qem/pauli-twirling]] — both are preprocessing steps that improve downstream mitigation

## References

- P. Murali, D. C. McKay, M. Martonosi, A. Javadi-Abhari. *Software Mitigation of Crosstalk on Noisy Intermediate-Scale Quantum Computers*. ASPLOS, 2020 [arXiv:2001.02826](https://arxiv.org/abs/2001.02826) [doi](https://doi.org/10.1145/3373376.3378477)
- S. Nishio, Y. Pan, T. Satoh, H. Amano, R. Van Meter. *Extracting Success from IBM's 20-Qubit Machines Using Error-Aware Compilation*. ACM Journal on Emerging Technologies in Computing Systems, 2020 [arXiv:1903.10963](https://arxiv.org/abs/1903.10963) [doi](https://doi.org/10.1145/3386162)
