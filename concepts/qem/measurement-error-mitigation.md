---
type: concept
name: Readout Error Mitigation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- REM
- measurement error mitigation
- MEM
- assignment matrix inversion
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=measurement-error-mitigation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: measurement-error-mitigation
---

# Readout Error Mitigation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=measurement-error-mitigation) (`id: measurement-error-mitigation`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Corrects for errors occurring during the final measurement (readout) stage of a quantum computation. The key idea is to characterize the measurement channel by preparing known computational basis states and recording the assignment probabilities, forming a confusion matrix $A$. The inverse $A^{-1}$ is then applied to raw measurement results to recover corrected expectation values.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Zero (in principle) if the assignment matrix is exact |
| Sampling overhead | Grows exponentially with measurement fault rate |
| Noise model required | Measurement-only; characterized via \(2^n\) calibration circuits (or fewer with tensor product approximation) |
| Scalability | Full matrix inversion is \(O(2^n)\); tensor product or correlated subsets used in practice |

## Related techniques

- [[concepts/qem/symmetry-verification]] — both can detect/correct measurement-stage errors

## References

- F. B. Maciejewski, Z. Zimborás, M. Oszmaniec. *Mitigation of Readout Noise in Near-Term Quantum Devices by Classical Post-Processing Based on Detector Tomography*. Quantum, 2020 [arXiv:1907.08518](https://arxiv.org/abs/1907.08518) [doi](https://doi.org/10.22331/q-2020-04-24-257)
- S. Bravyi, S. Sheldon, A. Kandala, D. C. McKay, J. M. Gambetta. *Mitigating Measurement Errors in Multi-Qubit Experiments*. Physical Review A, 2021 [arXiv:2006.14044](https://arxiv.org/abs/2006.14044) [doi](https://doi.org/10.1103/PhysRevA.103.042605)
- P. Nation, H. Kang, N. Sundaresan, J. M. Gambetta. *Scalable Mitigation of Measurement Errors on Quantum Computers*. PRX Quantum, 2021 [arXiv:2108.12518](https://arxiv.org/abs/2108.12518) [doi](https://doi.org/10.1103/PRXQuantum.2.040326)
