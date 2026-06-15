---
type: concept
name: Zero-Noise Extrapolation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- ZNE
- noise scaling and extrapolation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/bnzne
- concepts/qem/cdr
- concepts/qem/ide
- concepts/qem/lre
- concepts/qem/pauli-twirling
- concepts/qem/pec
- concepts/qem/pie
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=zne
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: zne
---

# Zero-Noise Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=zne) (`id: zne`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Intentionally increases the noise level of a quantum circuit (e.g., by stretching pulses, inserting identity-gate pairs, or rescaling error rates) to collect expectation values at multiple noise levels. These data points are then extrapolated to the hypothetical zero-noise limit using polynomial, exponential, or other fitting models.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Approximately \(O(\lambda^n)\) where \(n\) is the number of noise levels used for extrapolation and \(\lambda\) is the noise rate |
| Sampling overhead | Exponential in number of data points \(M\) (for Richardson); moderate for linear extrapolation |
| Noise model required | Minimal; only requires ability to scale noise controllably |
| Scalability | Demonstrated on up to 127 qubits; widely used in practice |

## Related techniques

- [[concepts/qem/lre]] — LRE is a multivariate generalization of ZNE
- [[concepts/qem/pec]] — both are foundational QEM techniques
- [[concepts/qem/pauli-twirling]] — Pauli twirling simplifies noise for ZNE
- [[concepts/qem/cdr]] — vnCDR combines CDR with noise scaling from ZNE
- [[concepts/qem/pie]] — PIE replaces ZNE's heuristic fitting models with a physics-motivated function
- [[concepts/qem/ide]] — IDE adapts ZNE to the QEC setting by extrapolating over code distance instead of noise level
- [[concepts/qem/bnzne]] — bnZNE replaces nominal noise-scaling factors with empirically calibrated error rates from benchmark circuits

## References

- K. Temme, S. Bravyi, J. M. Gambetta. *Error Mitigation for Short-Depth Quantum Circuits*. Physical Review Letters, 2017 [arXiv:1612.02058](https://arxiv.org/abs/1612.02058) [doi](https://doi.org/10.1103/PhysRevLett.119.180509)
- Y. Li, S. C. Benjamin. *Efficient Variational Quantum Simulator Incorporating Active Error Minimisation*. Physical Review X, 2017 [arXiv:1611.09301](https://arxiv.org/abs/1611.09301) [doi](https://doi.org/10.1103/PhysRevX.7.021050)
- S. Endo, S. C. Benjamin, Y. Li. *Practical Quantum Error Mitigation for Near-Future Applications*. Physical Review X, 2018 [arXiv:1712.09271](https://arxiv.org/abs/1712.09271) [doi](https://doi.org/10.1103/PhysRevX.8.031027)
- Y. Kim, A. Eddins, S. Anand, K. X. Wei, E. van den Berg, S. Rosenblatt, H. Nayfeh, Y. Wu, M. Zaletel, K. Temme, A. Kandala. *Evidence for the Utility of Quantum Computing Before Fault Tolerance*. Nature, 2023 [doi](https://doi.org/10.1038/s41586-023-06096-3)
- R. Majumdar, P. Rivero, F. Metz, A. Hasan, D. S. Wang. *Best Practices for Quantum Error Mitigation with Digital Zero-Noise Extrapolation*. IEEE International Conference on Quantum Computing and Engineering (QCE), 2023 [arXiv:2307.05203](https://arxiv.org/abs/2307.05203) [doi](https://doi.org/10.1109/QCE57702.2023.00102)
- J. Harris, K. Lively, P. K. Schuhmacher. *Reducing Quantum Error Mitigation Bias Using Verifiable Benchmark Circuits*. arXiv preprint, 2026 [arXiv:2603.10224](https://arxiv.org/abs/2603.10224)
- G. Umbrarescu, O. Higgott, D. E. Browne. *Infinite Distance Extrapolation: How error mitigation can enhance quantum error correction*. arXiv preprint, 2026 [arXiv:2603.11285](https://arxiv.org/abs/2603.11285)
