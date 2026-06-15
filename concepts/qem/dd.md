---
type: concept
name: Dynamical Decoupling
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- DD
- spin echo
- CPMG
- Uhrig dynamical decoupling
- XY-4
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pauli-twirling
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=dd
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: dd
---

# Dynamical Decoupling

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=dd) (`id: dd`, category: suppression). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Suppresses unwanted system-environment interactions by applying sequences of fast control pulses during idle periods in a quantum circuit. The pulse sequences are designed so that the net effect of the environment averages to zero over the decoupling cycle. Common sequences include spin echo, CPMG, XY-4, and Uhrig DD, each optimized for different noise spectra.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Residual errors from finite pulse width and higher-order terms |
| Sampling overhead | None (same number of shots); adds gate overhead |
| Noise model required | None, though knowledge of noise spectrum helps choose optimal sequence |
| Applicability | Idle qubits during circuit execution; most effective against low-frequency noise |

## Related techniques

- [[concepts/qem/pauli-twirling]] — both are suppression techniques applied at the gate level

## References

- L. Viola, E. Knill, S. Lloyd. *Dynamical Decoupling of Open Quantum Systems*. Physical Review Letters, 1999 [arXiv:quant-ph/9809071](https://arxiv.org/abs/quant-ph/9809071) [doi](https://doi.org/10.1103/PhysRevLett.82.2417)
- A. M. Souza, G. A. Álvarez, D. Suter. *Robust Dynamical Decoupling*. Philosophical Transactions of the Royal Society A, 2012 [arXiv:1110.6334](https://arxiv.org/abs/1110.6334) [doi](https://doi.org/10.1098/rsta.2011.0355)
