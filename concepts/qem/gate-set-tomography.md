---
type: concept
name: Gate Set Tomography
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- GST
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=gate-set-tomography
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: gate-set-tomography
qem_catalog: noise-learning
---

# Gate Set Tomography

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=gate-set-tomography) (`id: gate-set-tomography`, catalog: noise-learning). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Self-consistent characterization of an entire gate set including state preparation, measurement, and gates. Provides complete process matrices for all operations but scales poorly with qubit count. The gold standard for detailed noise characterization on small systems.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Scalability | Limited to ~2-3 qubits in practice |
| Noise captured | Complete process matrices for all operations |
| Learning method | Long sequence experiments with maximum likelihood estimation |
| Enables | Detailed noise analysis, PEC on small systems |

## References

- E. Nielsen, J. K. Gamble, K. Rudinger, T. Scholten, K. Young, R. Blume-Kohout. *Gate Set Tomography*. Quantum, 2021 [arXiv:2009.07301](https://arxiv.org/abs/2009.07301) [doi](https://doi.org/10.22331/q-2021-10-05-557)
