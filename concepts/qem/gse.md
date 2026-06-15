---
type: concept
name: Generalized Subspace Expansion
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- GSE
- generalized quantum subspace expansion
- power subspace method
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dual-state-purification
- concepts/qem/logical-shadow-tomography
- concepts/qem/purification
- concepts/qem/subspace-expansion
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=gse
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: gse
---

# Generalized Subspace Expansion

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=gse) (`id: gse`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

A unified error mitigation framework that handles stochastic, coherent, and algorithmic errors simultaneously by constructing an expanded subspace from powers of the noisy density matrix ($\rho^m$) or error-boosted states. GSE generalizes both quantum subspace expansion and virtual distillation, inheriting advantages of both while overcoming their individual limitations. The method is noise-agnostic and can suppress errors by orders of magnitude without requiring knowledge of the noise model.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Suppressed exponentially with subspace dimension |
| Sampling overhead | Moderate; requires measuring matrix elements in expanded subspace |
| Noise model required | None (noise-agnostic) |
| Applicability | General-purpose; particularly effective for variational algorithms and Hamiltonian simulation |

## Related techniques

- [[concepts/qem/subspace-expansion]] — QSE is a special case of GSE
- [[concepts/qem/purification]] — virtual distillation is a special case of GSE
- [[concepts/qem/dual-state-purification]] — Dual-GSE combines GSE with dual-state purification for resource efficiency
- [[concepts/qem/logical-shadow-tomography]] — both provide unified frameworks for multiple QEM techniques

## References

- N. Yoshioka, H. Hakoshima, Y. Matsuzaki, Y. Tokunaga, Y. Suzuki, S. Endo. *Generalized Quantum Subspace Expansion*. Physical Review Letters, 2022 [arXiv:2107.02611](https://arxiv.org/abs/2107.02611) [doi](https://doi.org/10.1103/PhysRevLett.129.020502)
