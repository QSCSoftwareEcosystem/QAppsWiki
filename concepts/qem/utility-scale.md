---
type: concept
name: Utility-Scale Experiments
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/pauli-twirling
- concepts/qem/pea
- concepts/qem/trex
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=utility-scale
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: utility-scale
qem_catalog: applications
---

# Utility-Scale Experiments

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=utility-scale) (`id: utility-scale`, catalog: applications, category: demonstration). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Utility-scale experiments aim to demonstrate quantum computations that provide value beyond what classical computers can efficiently achieve. These experiments push the limits of qubit count, circuit depth, and accuracy, relying heavily on error mitigation to bridge the gap between raw hardware capabilities and useful results.

(source: raw/qem-zoo.md)

## Key results

- IBM's 127-qubit Eagle processor demonstrated error-mitigated results for 2800+ two-qubit gates
- Combination of Pauli twirling, PEA-based ZNE, and TREX enabled accurate expectation values
- Sparked debate on the boundary between classical simulability and quantum utility

## Related techniques

- [[concepts/qem/zne]] — uses
- [[concepts/qem/pea]] — uses
- [[concepts/qem/pauli-twirling]] — uses
- [[concepts/qem/trex]] — uses
- [[concepts/qem/dd]] — uses

## References

- Y. Kim, A. Eddins, S. Anand, K. X. Wei, E. van den Berg, S. Rosenblatt, H. Nayfeh, Y. Wu, M. Zaletel, K. Temme, A. Kandala. *Evidence for the Utility of Quantum Computing Before Fault Tolerance*. Nature, 2023 [doi](https://doi.org/10.1038/s41586-023-06096-3)
- E. van den Berg, Z. K. Minev, A. Kandala, K. Temme. *Probabilistic Error Cancellation with Sparse Pauli–Lindblad Models on Noisy Quantum Processors*. Nature Physics, 2023 [arXiv:2201.09866](https://arxiv.org/abs/2201.09866) [doi](https://doi.org/10.1038/s41567-023-02042-2)
