---
type: concept
name: Amplitude Damping
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- T1 decay
- energy relaxation
- spontaneous emission
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pec
- concepts/qem/purification
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=amplitude-damping
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: amplitude-damping
qem_catalog: noise
---

# Amplitude Damping

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=amplitude-damping) (`id: amplitude-damping`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Irreversible decay from the excited state $|1\rangle$ to the ground state $|0\rangle$. Models energy loss to the environment with time constant $T_1$. Breaks the symmetry between computational basis states.

(source: raw/qem-zoo.md)

## Physical origin

Spontaneous emission; energy relaxation to thermal equilibrium; T1 processes in superconducting qubits

## Effect on bloch sphere

Contraction and drift toward the north pole (|0⟩ state)

## Kraus operators

$K_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-\gamma} \end{pmatrix}, \quad K_1 = \begin{pmatrix} 0 & \sqrt{\gamma} \\ 0 & 0 \end{pmatrix}$

## Related techniques

- [[concepts/qem/zne]] — mitigated by
- [[concepts/qem/pec]] — mitigated by
- [[concepts/qem/purification]] — mitigated by

## References

- Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, T. E. O'Brien. *Quantum Error Mitigation*. Reviews of Modern Physics, 2023 [arXiv:2210.00921](https://arxiv.org/abs/2210.00921) [doi](https://doi.org/10.1103/RevModPhys.95.045005)
