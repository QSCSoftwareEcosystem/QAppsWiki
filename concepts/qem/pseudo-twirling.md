---
type: concept
name: Pseudo Twirling
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- pseudo-Pauli twirling
- non-Clifford twirling
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/kik
- concepts/qem/pauli-twirling
- concepts/qem/symmetric-clifford-twirling
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=pseudo-twirling
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: pseudo-twirling
---

# Pseudo Twirling

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=pseudo-twirling) (`id: pseudo-twirling`, category: suppression). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Extends Pauli twirling to mitigate coherent errors in non-Clifford gates, where standard twirling fails. For gates like partial CPhase rotations (small-angle ZZ interactions), pseudo twirling applies approximate twirling operations that convert coherent errors into quasi-stochastic noise while preserving the gate's action. Can be combined with Adaptive KIK to simultaneously address both coherent and incoherent errors. Experimentally validated on native gate implementations.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Small residual from imperfect twirling of non-Clifford gates |
| Sampling overhead | Similar to Pauli twirling; requires averaging over randomized circuits |
| Noise model required | None |
| Applicability | Non-Clifford gates (partial rotations, native entangling gates); addresses calibration imperfections and crosstalk |

## Related techniques

- [[concepts/qem/pauli-twirling]] — pseudo twirling extends Pauli twirling to non-Clifford gates
- [[concepts/qem/kik]] — can be combined with KIK to address both coherent and incoherent errors
- [[concepts/qem/symmetric-clifford-twirling]] — both extend standard twirling to broader gate classes

## References

- J. P. Santos, B. Bar, R. Uzdin. *Pseudo Twirling Mitigation of Coherent Errors in non-Clifford Gates*. npj Quantum Information, 2024 [arXiv:2401.09040](https://arxiv.org/abs/2401.09040) [doi](https://doi.org/10.1038/s41534-024-00889-8)
