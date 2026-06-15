---
type: concept
name: Machine Learning QEM
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- ML-QEM
- neural error mitigation
- NEM
- learning-based QEM
- data-driven error mitigation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/cdr
- concepts/qem/pec
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=ml-qem
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: ml-qem
---

# Machine Learning QEM

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=ml-qem) (`id: ml-qem`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Uses classical machine learning models — including linear regression, random forests, multi-layer perceptrons, and graph neural networks — to learn the mapping from noisy to ideal expectation values. Training data is generated from near-Clifford circuits (efficiently simulable) or circuits at multiple noise levels. ML-QEM dramatically reduces the runtime overhead of traditional QEM methods (2× or more reduction) without sacrificing accuracy, and has been demonstrated on quantum hardware with up to 100 qubits.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Depends on model generalization; zero if training distribution matches target |
| Sampling overhead | Low at inference; training requires running calibration circuits |
| Noise model required | Implicitly learned from data; no explicit noise characterization needed |
| Applicability | General-purpose; best when training circuits approximate target circuit structure |

## Related techniques

- [[concepts/qem/cdr]] — CDR uses linear regression on near-Clifford training data; ML-QEM generalizes to richer models
- [[concepts/qem/zne]] — ML-QEM can replace ZNE's extrapolation with learned models, reducing overhead
- [[concepts/qem/pec]] — ML-QEM achieves similar accuracy to PEC with dramatically lower sampling cost

## References

- H. Liao, D. S. Wang, I. Sitdikov, C. Salcedo, A. Seif, Z. K. Minev. *Machine Learning for Practical Quantum Error Mitigation*. Nature Machine Intelligence, 2024 [arXiv:2309.17368](https://arxiv.org/abs/2309.17368) [doi](https://doi.org/10.1038/s42256-024-00927-2)
- P. Czarnik, M. McKerns, A. T. Sornborger, L. Cincio. *Neural Error Mitigation of Near-Term Quantum Simulations*. arXiv preprint, 2022 [arXiv:2105.08086](https://arxiv.org/abs/2105.08086)
- C. Kim, K. D. Park, J.-K. K. Rhee. *Quantum Error Mitigation with Artificial Neural Network*. IEEE Access, 2020 [doi](https://doi.org/10.1109/ACCESS.2020.3031607)
- A. Strikis, D. Qin, Y. Chen, S. C. Benjamin, Y. Li. *Learning-Based Quantum Error Mitigation*. PRX Quantum, 2021 [arXiv:2005.07601](https://arxiv.org/abs/2005.07601) [doi](https://doi.org/10.1103/PRXQuantum.2.040330)
