---
type: concept
name: Crosstalk
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- cross-talk
- correlated errors
- ZZ coupling
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/crosstalk-mitigation
- concepts/qem/dd
- concepts/qem/noise-aware-compilation
- concepts/qem/pauli-twirling
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=crosstalk
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: crosstalk
qem_catalog: noise
---

# Crosstalk

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=crosstalk) (`id: crosstalk`, catalog: noise, category: coherent). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Unwanted interactions between qubits, causing operations on one qubit to affect neighboring qubits. Includes always-on ZZ coupling in superconducting systems and addressing errors in trapped ions.

(source: raw/qem-zoo.md)

## Physical origin

Residual qubit-qubit coupling; shared control lines; spectral crowding; electromagnetic interference

## Effect on bloch sphere

Correlated rotations across multiple qubits

## Kraus operators

Two-qubit unitary: $U = \exp(-i \theta Z \otimes Z)$ for ZZ crosstalk

## Related techniques

- [[concepts/qem/crosstalk-mitigation]] — mitigated by
- [[concepts/qem/dd]] — mitigated by
- [[concepts/qem/noise-aware-compilation]] — mitigated by
- [[concepts/qem/pauli-twirling]] — mitigated by

## References

- P. Murali, D. C. McKay, M. Martonosi, A. Javadi-Abhari. *Software Mitigation of Crosstalk on Noisy Intermediate-Scale Quantum Computers*. ASPLOS, 2020 [arXiv:2001.02826](https://arxiv.org/abs/2001.02826) [doi](https://doi.org/10.1145/3373376.3378477)
