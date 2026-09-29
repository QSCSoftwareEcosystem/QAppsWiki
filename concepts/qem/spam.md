---
type: concept
name: SPAM Errors
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- state preparation and measurement errors
- readout errors
- initialization errors
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/measurement-error-mitigation
- concepts/qem/robust-shadows
- concepts/qem/trex
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=spam
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: spam
qem_catalog: noise
---

# SPAM Errors

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=spam) (`id: spam`, catalog: noise, category: incoherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Errors in preparing the initial state or measuring the final state. Readout errors cause $|0\rangle$ to be measured as 1 (and vice versa). SPAM errors are independent of circuit depth but can dominate for shallow circuits.

(source: raw/qem-zoo.md)

## Physical origin

Thermal population; measurement discrimination errors; T1 decay during readout; insufficient reset

## Effect on bloch sphere

Misidentification of final Bloch sphere location

## Kraus operators

Confusion (assignment) matrix: $A = \begin{pmatrix} 1-p_0 & p_1 \\ p_0 & 1-p_1 \end{pmatrix}$ (classical, not a quantum channel)

## Related techniques

- [[concepts/qem/measurement-error-mitigation]] — mitigated by
- [[concepts/qem/trex]] — mitigated by
- [[concepts/qem/robust-shadows]] — mitigated by

## References

- S. Bravyi, S. Sheldon, A. Kandala, D. C. McKay, J. M. Gambetta. *Mitigating Measurement Errors in Multi-Qubit Experiments*. Physical Review A, 2021 [arXiv:2006.14044](https://arxiv.org/abs/2006.14044) [doi](https://doi.org/10.1103/PhysRevA.103.042605)
- E. van den Berg, Z. K. Minev, K. Temme. *Model-Free Readout-Error Mitigation for Quantum Expectation Values*. Physical Review A, 2022 [arXiv:2012.09738](https://arxiv.org/abs/2012.09738) [doi](https://doi.org/10.1103/PhysRevA.105.032620)
