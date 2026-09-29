---
type: concept
name: Bit Flip
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- X error
- bit flip channel
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pec
- concepts/qem/qed
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=bit-flip
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: bit-flip
qem_catalog: noise
---

# Bit Flip

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=bit-flip) (`id: bit-flip`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Random application of the Pauli X operator, flipping $|0\rangle \leftrightarrow |1\rangle$ with probability $p$. The simplest non-trivial noise model, analogous to classical bit errors.

(source: raw/qem-zoo.md)

## Physical origin

Spurious X rotations; readout errors; crosstalk inducing unintended flips

## Effect on bloch sphere

Contraction toward the x-axis

## Kraus operators

$K_0 = \sqrt{1-p}\,I, \quad K_1 = \sqrt{p}\,X$

## Related techniques

- [[concepts/qem/pec]] — mitigated by
- [[concepts/qem/qed]] — mitigated by
- [[concepts/qem/symmetry-verification]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
