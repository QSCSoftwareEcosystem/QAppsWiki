---
type: concept
name: Fictitious Copy Quantum Error Mitigation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- FCQEM
- fictitious copy method
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dual-state-purification
- concepts/qem/gse
- concepts/qem/purification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=fcqem
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: fcqem
---

# Fictitious Copy Quantum Error Mitigation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=fcqem) (`id: fcqem`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

A purely classical post-processing technique that mitigates noise by squaring and renormalizing measured probability distributions, effectively approximating a first-order truncation of Virtual Distillation without any additional quantum resources. FCQEM sharpens peaked distributions to suppress noise-induced amplitudes, recovering exact eigenvalues for eigenstates of the measured operator. Particularly effective for diagonally dominant Hamiltonians and compatible with Quantum Computed Moments (QCM) for enhanced ground state energy estimation.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | State-dependent truncation error; zero for eigenstates of the observable |
| Sampling overhead | None beyond standard circuit execution; purely classical post-processing |
| Noise model required | None (model-free) |
| Applicability | Eigenvalue problems with sharply peaked distributions; diagonally dominant Hamiltonians (e.g., FCI, Ising models) |

## Related techniques

- [[concepts/qem/purification]] — FCQEM is a first-order truncation of Virtual Distillation, avoiding the need for multiple copies
- [[concepts/qem/dual-state-purification]] — both achieve purification-like effects with reduced quantum overhead
- [[concepts/qem/gse]] — GSE generalizes VD and QSE; FCQEM approximates the VD component classically

## References

- A. Karim, H. J. Vallury, M. Usman. *Fictitious Copy Quantum Error Mitigation*. arXiv preprint, 2026 [arXiv:2603.09302](https://arxiv.org/abs/2603.09302)
