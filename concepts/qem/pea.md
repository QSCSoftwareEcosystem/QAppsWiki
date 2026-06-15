---
type: concept
name: Probabilistic Error Amplification
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- PEA
- learned noise amplification
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pauli-twirling
- concepts/qem/pec
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=pea
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: pea
---

# Probabilistic Error Amplification

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=pea) (`id: pea`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

A noise-amplification strategy for zero-noise extrapolation that first learns the twirled noise model of each layer of entangling gates (e.g., via a sparse Pauli–Lindblad model) and then probabilistically injects single-qubit noise proportional to the learned model to achieve controlled, accurate noise scaling. Unlike pulse stretching (which assumes noise scales with gate duration) or gate folding (which requires large stretch factors), PEA provides precise amplification factors without additional calibration, making it practical for utility-scale circuits.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Inherits from ZNE extrapolation model; amplification itself is accurate |
| Sampling overhead | Low per noise level (no exponential overhead unlike PEC); requires multiple noise levels for extrapolation |
| Noise model required | Learned sparse Pauli–Lindblad model of per-layer noise |
| Applicability | Utility-scale circuits; demonstrated on 127 qubits with 60 layers of two-qubit gates |

## Related techniques

- [[concepts/qem/zne]] — PEA is a noise amplification method used within ZNE
- [[concepts/qem/pec]] — PEA uses the same learned noise model as PEC but avoids exponential sampling overhead
- [[concepts/qem/pauli-twirling]] — PEA operates on twirled (Pauli) noise channels

## References

- Y. Kim, A. Eddins, S. Anand, K. X. Wei, E. van den Berg, S. Rosenblatt, H. Nayfeh, Y. Wu, M. Zaletel, K. Temme, A. Kandala. *Evidence for the Utility of Quantum Computing Before Fault Tolerance*. Nature, 2023 [doi](https://doi.org/10.1038/s41586-023-06096-3)
- E. van den Berg, Z. K. Minev, A. Kandala, K. Temme. *Probabilistic Error Cancellation with Sparse Pauli–Lindblad Models on Noisy Quantum Processors*. Nature Physics, 2023 [arXiv:2201.09866](https://arxiv.org/abs/2201.09866) [doi](https://doi.org/10.1038/s41567-023-02042-2)
