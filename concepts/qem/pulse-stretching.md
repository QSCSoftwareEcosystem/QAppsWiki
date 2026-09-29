---
type: concept
name: Pulse Stretching
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- time stretching
- pulse scaling
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=pulse-stretching
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: pulse-stretching
qem_catalog: noise-scaling
---

# Pulse Stretching

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=pulse-stretching) (`id: pulse-stretching`, catalog: noise-scaling). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Amplifies noise by stretching the duration of control pulses while maintaining their area (so the unitary is unchanged). Assumes that noise scales linearly with gate duration, which holds for some but not all noise sources. Requires pulse-level control of the quantum hardware.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Scale factors | Continuous (any \(\lambda \geq 1\)) |
| Hardware requirements | Pulse-level access (e.g., OpenPulse on IBM systems) |
| Advantages | Continuous scale factors; no additional gates |
| Disadvantages | Assumes noise ∝ duration (often inaccurate); requires pulse calibration; not available on all platforms |

## References

- K. Temme, S. Bravyi, J. M. Gambetta. *Error Mitigation for Short-Depth Quantum Circuits*. Physical Review Letters, 2017 [arXiv:1612.02058](https://arxiv.org/abs/1612.02058) [doi](https://doi.org/10.1103/PhysRevLett.119.180509)
- A. Kandala, K. Temme, A. D. Córcoles, A. Mezzacapo, J. M. Chow, J. M. Gambetta. *Error Mitigation Extends the Computational Reach of a Noisy Quantum Processor*. Nature, 2019 [arXiv:1805.04492](https://arxiv.org/abs/1805.04492) [doi](https://doi.org/10.1038/s41586-019-1040-7)
