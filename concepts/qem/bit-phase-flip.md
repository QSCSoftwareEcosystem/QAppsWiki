---
type: concept
name: Bit-Phase Flip
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Y error
- bit-phase flip channel
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pauli-twirling
- concepts/qem/pec
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=bit-phase-flip
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: bit-phase-flip
qem_catalog: noise
---

# Bit-Phase Flip

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=bit-phase-flip) (`id: bit-phase-flip`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Random application of the Pauli Y operator, which combines a bit flip and a phase flip: $Y = iXZ$. Flips both the computational basis and introduces a phase, mapping $|0\rangle \to i|1\rangle$ and $|1\rangle \to -i|0\rangle$.

(source: raw/qem-zoo.md)

## Physical origin

Combined bit and phase errors; certain types of crosstalk; composite noise processes

## Effect on bloch sphere

Contraction toward the y-axis

## Kraus operators

$K_0 = \sqrt{1-p}\,I, \quad K_1 = \sqrt{p}\,Y$

## Related techniques

- [[concepts/qem/pec]] — mitigated by
- [[concepts/qem/pauli-twirling]] — mitigated by
- [[concepts/qem/symmetry-verification]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
