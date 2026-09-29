---
type: concept
name: Coherent Errors
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- unitary errors
- over-rotation
- under-rotation
- systematic errors
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/echo-verification
- concepts/qem/noise-aware-compilation
- concepts/qem/pauli-twirling
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=coherent-errors
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: coherent-errors
qem_catalog: noise
---

# Coherent Errors

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=coherent-errors) (`id: coherent-errors`, catalog: noise, category: coherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Deterministic, unitary deviations from the intended gate operation. Examples include over/under-rotation angles and axis tilts. Coherent errors can accumulate constructively, potentially causing worse scaling than incoherent errors.

(source: raw/qem-zoo.md)

## Physical origin

Miscalibrated pulse amplitudes or durations; frequency drift; crosstalk

## Effect on bloch sphere

Rotation to wrong location (deterministic, reversible)

## Kraus operators

Single unitary: $K_0 = U_{\text{error}}$ where $U_{\text{error}} \neq U_{\text{ideal}}$

## Related techniques

- [[concepts/qem/pauli-twirling]] — mitigated by
- [[concepts/qem/dd]] — mitigated by
- [[concepts/qem/echo-verification]] — mitigated by
- [[concepts/qem/noise-aware-compilation]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
