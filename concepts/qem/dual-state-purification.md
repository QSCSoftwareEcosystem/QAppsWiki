---
type: concept
name: Dual-State Purification
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- DSP
- dual-map purification
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/echo-verification
- concepts/qem/purification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=dual-state-purification
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: dual-state-purification
---

# Dual-State Purification

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=dual-state-purification) (`id: dual-state-purification`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Purifies a noisy quantum state by combining it with a 'dual state' prepared by running the inverse circuit through the dual (conjugate) noise channel. The overlap between the noisy state and its dual provides an estimate equivalent to virtual distillation but without requiring multiple copies of the state or ancilla qubits. Combined with tomography purification, the method ensures the final estimate is obtained from an effectively pure state, with error reduction that improves for larger circuits.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced; purification suppresses off-diagonal noise contributions |
| Sampling overhead | Roughly doubles circuit executions (forward + dual); no qubit overhead |
| Noise model required | None (model-free); relies on structure of the noise channel |
| Applicability | Variational algorithms; demonstrated on cloud quantum computers with VQE |

## Related techniques

- [[concepts/qem/purification]] — both perform virtual purification; DSP avoids multi-copy overhead
- [[concepts/qem/echo-verification]] — both use forward and inverse circuits; DSP extracts purified expectation values

## References

- M. Huo, Y. Li. *Dual-State Purification for Practical Quantum Error Mitigation*. Physical Review A, 2022 [arXiv:2105.01239](https://arxiv.org/abs/2105.01239) [doi](https://doi.org/10.1103/PhysRevA.105.022427)
