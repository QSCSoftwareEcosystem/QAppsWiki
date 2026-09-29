---
type: concept
name: Unitary Folding
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- gate folding
- circuit folding
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=unitary-folding
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: unitary-folding
qem_catalog: noise-scaling
---

# Unitary Folding

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=unitary-folding) (`id: unitary-folding`, catalog: noise-scaling). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Amplifies noise by inserting identity-equivalent gate pairs $G G^\dagger$ into the circuit. For a scale factor $\lambda$, gates are replaced with $G (G^\dagger G)^{(\lambda-1)/2}$. Can be applied globally (to the whole circuit) or locally (to individual gates). Simple to implement but requires integer or odd-integer scale factors for exact folding.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Scale factors | Odd-integer multiples (1, 3, 5, ...); fractional via partial folding |
| Hardware requirements | None beyond standard gate set |
| Advantages | Simple, no pulse-level access needed, widely supported |
| Disadvantages | Large stretch factors needed for deep circuits; folded gates may have different noise than original |

## References

- T. Giurgica-Tiron, Y. Hindy, R. LaRose, A. Mari, W. J. Zeng. *Digital Zero Noise Extrapolation for Quantum Error Mitigation*. IEEE International Conference on Quantum Computing and Engineering (QCE), 2020 [arXiv:2005.10921](https://arxiv.org/abs/2005.10921) [doi](https://doi.org/10.1109/QCE49297.2020.00045)
- A. He, B. Nachman, W. A. de Jong, C. W. Bauer. *Zero-Noise Extrapolation for Quantum-Gate Error Mitigation with Identity Insertions*. Physical Review A, 2020 [arXiv:2003.04941](https://arxiv.org/abs/2003.04941) [doi](https://doi.org/10.1103/PhysRevA.102.012426)
