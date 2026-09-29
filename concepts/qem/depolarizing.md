---
type: concept
name: Depolarizing
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- depolarizing channel
- white noise
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/emre
- concepts/qem/hemre
- concepts/qem/pauli-twirling
- concepts/qem/pec
- concepts/qem/pie
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=depolarizing
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: depolarizing
qem_catalog: noise
---

# Depolarizing

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=depolarizing) (`id: depolarizing`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Symmetric noise that randomly applies Pauli X, Y, or Z errors with equal probability. The qubit state decays toward the maximally mixed state $I/2$, losing both phase and amplitude information. Often used as a worst-case noise model.

(source: raw/qem-zoo.md)

## Physical origin

Interaction with a high-temperature environment; aggregate effect of many unknown error sources

## Effect on bloch sphere

Uniform contraction toward the center (origin)

## Kraus operators

$K_0 = \sqrt{1-p}\,I, \quad K_1 = \sqrt{p/3}\,X, \quad K_2 = \sqrt{p/3}\,Y, \quad K_3 = \sqrt{p/3}\,Z$

## Related techniques

- [[concepts/qem/pec]] — mitigated by
- [[concepts/qem/zne]] — mitigated by
- [[concepts/qem/pauli-twirling]] — mitigated by
- [[concepts/qem/dd]] — mitigated by
- [[concepts/qem/emre]] — mitigated by
- [[concepts/qem/hemre]] — mitigated by
- [[concepts/qem/pie]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
