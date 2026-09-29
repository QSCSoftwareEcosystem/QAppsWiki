---
type: concept
name: Identity Insertion
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- identity scaling
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=identity-insertion
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: identity-insertion
qem_catalog: noise-scaling
---

# Identity Insertion

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=identity-insertion) (`id: identity-insertion`, catalog: noise-scaling). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Amplifies noise by inserting identity operations between circuit gates, extending circuit duration and exposing qubits to more decoherence. Unlike folding ($G \to GG^\dagger G$), identity insertion focuses on passive decoherence rather than gate noise, making it effective when T1/T2 errors dominate.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Scale factors | Discrete (ratio of scaled to original depth) |
| Hardware requirements | None |
| Advantages | Simple; effective for decoherence-dominated noise |
| Disadvantages | Primarily scales idle noise, not gate noise; coarse control |

## References

- T. Giurgica-Tiron, Y. Hindy, R. LaRose, A. Mari, W. J. Zeng. *Digital Zero Noise Extrapolation for Quantum Error Mitigation*. IEEE International Conference on Quantum Computing and Engineering (QCE), 2020 [arXiv:2005.10921](https://arxiv.org/abs/2005.10921) [doi](https://doi.org/10.1109/QCE49297.2020.00045)
