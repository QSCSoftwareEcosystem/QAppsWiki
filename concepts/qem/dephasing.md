---
type: concept
name: Dephasing
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- phase damping
- T2 decay
- pure dephasing
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/echo-verification
- concepts/qem/emre
- concepts/qem/hemre
- concepts/qem/pauli-twirling
- concepts/qem/pie
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=dephasing
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: dephasing
qem_catalog: noise
---

# Dephasing

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=dephasing) (`id: dephasing`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Loss of quantum phase information without energy exchange. Off-diagonal elements of the density matrix decay exponentially with time constant $T_2$. The qubit retains its population but loses coherence.

(source: raw/qem-zoo.md)

## Physical origin

Fluctuating magnetic fields; low-frequency noise in control electronics; T2 relaxation processes

## Effect on bloch sphere

Contraction toward the z-axis (poles preserved, equator shrinks)

## Kraus operators

$K_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\lambda} \end{pmatrix}, \quad K_1 = \begin{pmatrix} 0 & 0 \\ 0 & \sqrt{\lambda} \end{pmatrix}$

## Related techniques

- [[concepts/qem/dd]] — mitigated by
- [[concepts/qem/pauli-twirling]] — mitigated by
- [[concepts/qem/zne]] — mitigated by
- [[concepts/qem/echo-verification]] — mitigated by
- [[concepts/qem/emre]] — mitigated by
- [[concepts/qem/hemre]] — mitigated by
- [[concepts/qem/pie]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
