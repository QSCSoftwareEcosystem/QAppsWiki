---
type: concept
name: Leakage
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- leakage errors
- non-computational state transitions
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=leakage
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: leakage
qem_catalog: noise
---

# Leakage

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=leakage) (`id: leakage`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Transition from the computational subspace ($|0\rangle, |1\rangle$) to higher energy levels ($|2\rangle, |3\rangle, ...$). Unlike erasure, leakage is typically not heralded and can propagate through subsequent gates.

(source: raw/qem-zoo.md)

## Physical origin

Off-resonant driving in transmons; multi-photon transitions; insufficient anharmonicity

## Effect on bloch sphere

Qubit leaves the Bloch sphere (enters higher-dimensional space)

## Kraus operators

Depends on specific leakage pathway; generally non-Pauli

## Related techniques

- [[concepts/qem/dd]] — mitigated by
- [[concepts/qem/symmetry-verification]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
