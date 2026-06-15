---
type: concept
name: Clifford Data Regression
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- CDR
- variable-noise CDR
- vnCDR
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/ml-qem
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=cdr
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: cdr
---

# Clifford Data Regression

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=cdr) (`id: cdr`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Trains a regression model using circuits that are close to Clifford (and thus efficiently simulable) to learn the relationship between noisy and ideal expectation values. The learned model is then applied to correct the noisy output of the target non-Clifford circuit. Because near-Clifford circuits can be simulated classically, CDR generates its own training labels without requiring a noise-free quantum device.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Depends on similarity between training and target circuits |
| Sampling overhead | Low at inference; training requires running near-Clifford circuits |
| Noise model required | Implicitly learned from data; no explicit noise model needed |
| Applicability | General-purpose; works best when near-Clifford training circuits approximate target noise profile |

## Related techniques

- [[concepts/qem/zne]] — vnCDR combines CDR with variable noise scaling
- [[concepts/qem/ml-qem]] — ML-QEM generalizes CDR's linear regression to richer ML models

## References

- P. Czarnik, A. Arrasmith, P. J. Coles, L. Cincio. *Error Mitigation with Clifford Quantum-Circuit Data*. Quantum, 2021 [arXiv:2005.10189](https://arxiv.org/abs/2005.10189) [doi](https://doi.org/10.22331/q-2021-11-26-592)
- A. Lowe, M. H. Gordon, P. Czarnik, A. Arrasmith, P. J. Coles, L. Cincio. *Unified Approach to Data-Driven Quantum Error Mitigation*. Physical Review Research, 2021 [arXiv:2011.01157](https://arxiv.org/abs/2011.01157) [doi](https://doi.org/10.1103/PhysRevResearch.3.033098)
- A. Strikis, D. Qin, Y. Chen, S. C. Benjamin, Y. Li. *Learning-Based Quantum Error Mitigation*. PRX Quantum, 2021 [arXiv:2005.07601](https://arxiv.org/abs/2005.07601) [doi](https://doi.org/10.1103/PRXQuantum.2.040330)
