---
type: concept
name: Virtual Distillation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- VD
- purification-based methods
- error suppression by derangement
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dual-state-purification
- concepts/qem/fcqem
- concepts/qem/gse
- concepts/qem/logical-shadow-tomography
- concepts/qem/subspace-expansion
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=purification
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: purification
---

# Virtual Distillation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=purification) (`id: purification`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Exploits the fact that noise makes a pure quantum state mixed. By preparing $M$ independent copies of the noisy state and measuring collective observables (e.g., via a derangement or cyclic-shift operator), the contribution of the dominant eigenvector of the density matrix is amplified exponentially in $M$, effectively purifying the state.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Exponentially suppressed: \(O((\lambda_2/\lambda_1)^M)\) where \(\lambda_1, \lambda_2\) are the two largest eigenvalues |
| Sampling overhead | Polynomial in \(M\); requires \(M\) copies of the circuit |
| Noise model required | None (model-free) |
| Hardware requirements | \(M\) copies of the state; entangling measurements across copies or classical shadows |

## Related techniques

- [[concepts/qem/subspace-expansion]] — both use multiple quantum states to improve estimates
- [[concepts/qem/symmetry-verification]] — purity is itself a constraint that can be verified
- [[concepts/qem/logical-shadow-tomography]] — virtual distillation is a special case of the LST framework
- [[concepts/qem/dual-state-purification]] — DSP achieves similar purification without multi-copy overhead
- [[concepts/qem/gse]] — GSE generalizes virtual distillation and QSE into a unified framework
- [[concepts/qem/fcqem]] — FCQEM approximates first-order VD using only classical post-processing of probabilities

## References

- W. J. Huggins, S. McArdle, T. E. O'Brien, J. Lee, N. C. Rubin, S. Boixo, K. B. Whaley, R. Babbush, J. R. McClean. *Virtual Distillation for Quantum Error Mitigation*. Physical Review X, 2021 [arXiv:2011.07064](https://arxiv.org/abs/2011.07064) [doi](https://doi.org/10.1103/PhysRevX.11.041036)
- B. Koczor. *Exponential Error Suppression for Near-Term Quantum Devices*. Physical Review X, 2021 [arXiv:2011.05942](https://arxiv.org/abs/2011.05942) [doi](https://doi.org/10.1103/PhysRevX.11.031057)
- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
