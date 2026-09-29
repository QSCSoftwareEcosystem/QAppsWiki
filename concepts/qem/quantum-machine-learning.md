---
type: concept
name: Quantum Machine Learning
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/cdr
- concepts/qem/dd
- concepts/qem/measurement-error-mitigation
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=quantum-machine-learning
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: quantum-machine-learning
qem_catalog: applications
---

# Quantum Machine Learning

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=quantum-machine-learning) (`id: quantum-machine-learning`, catalog: applications, category: machine-learning). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Quantum machine learning algorithms, including variational classifiers and quantum kernel methods, are sensitive to noise that can destroy the quantum advantage. Error mitigation helps preserve the expressibility of parameterized quantum circuits and the quality of learned models.

(source: raw/qem-zoo.md)

## Key results

- Noise-induced barren plateaus flatten the cost landscape exponentially in circuit depth, so mitigating noise is a prerequisite for trainability rather than a refinement
- ZNE and CDR correct the systematic bias in the expectation values used for both training and inference
- Measurement error mitigation matters most where readout dominates, as in classification with many output classes

## Related techniques

- [[concepts/qem/zne]] — uses
- [[concepts/qem/measurement-error-mitigation]] — uses
- [[concepts/qem/cdr]] — uses
- [[concepts/qem/dd]] — uses

## References

- S. Wang, E. Fontana, M. Cerezo, K. Sharma, A. Sone, L. Cincio, P. J. Coles. *Noise-Induced Barren Plateaus in Variational Quantum Algorithms*. Nature Communications, 2021 [arXiv:2007.14384](https://arxiv.org/abs/2007.14384) [doi](https://doi.org/10.1038/s41467-021-27045-6)
- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
