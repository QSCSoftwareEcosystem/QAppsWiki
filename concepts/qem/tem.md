---
type: concept
name: Tensor Network Error Mitigation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- TEM
- MPO error mitigation
- matrix product operator mitigation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/nox
- concepts/qem/pec
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=tem
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: tem
---

# Tensor Network Error Mitigation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=tem) (`id: tem`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Represents the noise channel as a matrix product operator (MPO) and applies its inverse to noisy measurement outcomes to recover mitigated expectation values. The tensor network structure captures spatially and temporally correlated noise with polynomial complexity, avoiding the exponential overhead of full process tomography. The MPO inverse is computed variationally or analytically, and the method scales to large circuits while maintaining provably optimal sampling overhead.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Zero (in principle) if noise model is exact |
| Sampling overhead | Optimal among linear mitigation methods; polynomial in bond dimension |
| Noise model required | Learned MPO representation of the noise channel |
| Applicability | General-purpose; particularly effective for circuits with spatially correlated noise |

## Related techniques

- [[concepts/qem/pec]] — both invert the noise channel; TEM uses tensor network structure for efficiency
- [[concepts/qem/nox]] — both learn structured noise models; TEM uses MPO representation

## References

- Y. Guo, S. Yang. *Quantum Error Mitigation via Matrix Product Operators*. PRX Quantum, 2022 [arXiv:2201.00752](https://arxiv.org/abs/2201.00752) [doi](https://doi.org/10.1103/PRXQuantum.3.040313)
- S. Filippov, M. Leahy, M. A. C. Rossi, G. García-Pérez. *Scalable Tensor-Network Error Mitigation for Near-Term Quantum Computing*. arXiv preprint, 2023 [arXiv:2307.11740](https://arxiv.org/abs/2307.11740) [doi](https://doi.org/10.48550/arXiv.2307.11740)
