---
type: concept
name: Quantum Approximate Optimization Algorithm
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/measurement-error-mitigation
- concepts/qem/pauli-twirling
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=qaoa
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: qaoa
qem_catalog: applications
---

# Quantum Approximate Optimization Algorithm

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=qaoa) (`id: qaoa`, catalog: applications, category: optimization). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

QAOA is a variational algorithm for combinatorial optimization problems like MaxCut and portfolio optimization. Noise degrades the quality of approximate solutions, making error mitigation essential for demonstrating quantum advantage. ZNE and measurement error mitigation are commonly applied.

(source: raw/qem-zoo.md)

## Key results

- Error-mitigated QAOA improves approximation ratios on optimization benchmarks
- Demonstrated on problems including MaxCut, graph partitioning, and scheduling
- Combination of ZNE with dynamical decoupling provides compounding benefits

## Related techniques

- [[concepts/qem/zne]] — uses
- [[concepts/qem/measurement-error-mitigation]] — uses
- [[concepts/qem/dd]] — uses
- [[concepts/qem/pauli-twirling]] — uses

## References

- M. P. Harrigan, K. J. Sung, M. Neeley, et al.. *Quantum Approximate Optimization of Non-Planar Graph Problems on a Planar Superconducting Processor*. Nature Physics, 2021 [arXiv:2004.04197](https://arxiv.org/abs/2004.04197) [doi](https://doi.org/10.1038/s41567-020-01105-y)
- J. Weidenfeller, L. C. Valor, J. Gacon, C. Tornow, L. Bello, S. Woerner, D. J. Egger. *Scaling of the Quantum Approximate Optimization Algorithm on Superconducting Qubit Based Hardware*. Quantum, 2022 [arXiv:2202.03459](https://arxiv.org/abs/2202.03459) [doi](https://doi.org/10.22331/q-2022-12-07-870)
