---
type: concept
name: Decoherence
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- quantum decoherence
- T1/T2 decay
- environmental decoherence
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/echo-verification
- concepts/qem/pec
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=decoherence
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: decoherence
qem_catalog: noise
---

# Decoherence

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=decoherence) (`id: decoherence`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

The general loss of quantum coherence due to interaction with the environment, encompassing both energy relaxation ($T_1$) and phase randomization ($T_2$). The fundamental relationship $1/T_2 = 1/(2T_1) + 1/T_2^*$ connects these processes, where $T_2^*$ is pure dephasing.

(source: raw/qem-zoo.md)

## Physical origin

Unavoidable coupling between qubit and environment; thermal fluctuations; electromagnetic noise; material defects

## Effect on bloch sphere

Combined contraction toward z-axis (T2) and drift toward |0⟩ (T1); state evolves toward thermal equilibrium

## Kraus operators

Composite of amplitude damping and dephasing channels (see individual entries)

## Related techniques

- [[concepts/qem/dd]] — mitigated by
- [[concepts/qem/zne]] — mitigated by
- [[concepts/qem/pec]] — mitigated by
- [[concepts/qem/echo-verification]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
