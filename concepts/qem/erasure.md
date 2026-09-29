---
type: concept
name: Erasure
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- erasure channel
- loss
- leakage to detectable state
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/qed
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=erasure
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: erasure
qem_catalog: noise
---

# Erasure

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=erasure) (`id: erasure`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

The qubit is lost or transitions to a detectable non-computational state. Unlike other errors, erasure locations are known (heralded), making them easier to correct. Common in photonic and neutral atom systems.

(source: raw/qem-zoo.md)

## Physical origin

Photon loss in optical systems; atom loss in neutral atom arrays; leakage to non-computational levels

## Effect on bloch sphere

Qubit leaves the Bloch sphere entirely (flagged as lost)

## Kraus operators

$K_0 = \sqrt{1-p}\,I, \quad K_1 = \sqrt{p}\,|e\rangle\langle 0|, \quad K_2 = \sqrt{p}\,|e\rangle\langle 1|$

## Related techniques

- [[concepts/qem/qed]] — mitigated by
- [[concepts/qem/symmetry-verification]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
