---
type: concept
name: Phase Flip
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Z error
- phase flip channel
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/pauli-twirling
- concepts/qem/pec
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=phase-flip
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: phase-flip
qem_catalog: noise
---

# Phase Flip

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=phase-flip) (`id: phase-flip`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Random application of the Pauli Z operator, flipping the relative phase: $|+\rangle \leftrightarrow |-\rangle$. Equivalent to a bit flip in the Hadamard basis.

(source: raw/qem-zoo.md)

## Physical origin

Fluctuating qubit frequencies; Z rotations from stray fields; dephasing events

## Effect on bloch sphere

Contraction toward the z-axis

## Kraus operators

$K_0 = \sqrt{1-p}\,I, \quad K_1 = \sqrt{p}\,Z$

## Related techniques

- [[concepts/qem/dd]] — mitigated by
- [[concepts/qem/pauli-twirling]] — mitigated by
- [[concepts/qem/pec]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
