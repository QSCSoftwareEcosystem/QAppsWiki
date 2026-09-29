---
type: concept
name: Noiseless Output eXtrapolation
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- NOX
- noise-learned output extrapolation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pauli-twirling
- concepts/qem/pea
- concepts/qem/pec
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=nox
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: nox
qem_catalog: techniques
---

# Noiseless Output eXtrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=nox) (`id: nox`, catalog: techniques, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Combines efficient noise reconstruction (e.g., cycle benchmarking) with noise amplification and extrapolation to the zero-noise limit. Unlike standard ZNE, which uses heuristic noise-scaling methods, NOX learns a detailed noise model per cycle of gates and uses it to perform accurate, targeted noise amplification. This allows it to handle non-local and gate-dependent noise processes that violate the assumptions of simpler extrapolation methods. The protocol was validated on a four-qubit superconducting processor on W-state preparation, quantum phase estimation, and pseudo-random circuits.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | First-order mitigation; does not cancel second-order noise terms |
| Sampling overhead | Moderate; noise-learning calibration plus multiple noise-scaled circuit executions |
| Noise model required | Learned via efficient noise reconstruction (cycle benchmarking); handles non-local and gate-dependent noise |
| Applicability | General-purpose; demonstrated on superconducting hardware for circuits with up to 11 noisy cycles |

## Related techniques

- [[concepts/qem/zne]] — NOX is a more principled version of ZNE using a learned noise model for amplification
- [[concepts/qem/pec]] — NOX combines noise reconstruction from PEC with extrapolation from ZNE
- [[concepts/qem/pea]] — both use learned noise models for accurate noise amplification within ZNE
- [[concepts/qem/pauli-twirling]] — NOX operates on twirled noise channels via randomized compiling

## References

- S. Ferracin, A. Hashim, J.-L. Ville, R. Naik, A. Carignan-Dugas, H. Qassim, A. Morvan, D. I. Santiago, I. Siddiqi, J. J. Wallman. *Efficiently Improving the Performance of Noisy Quantum Computers*. Quantum, 2024 [arXiv:2201.10672](https://arxiv.org/abs/2201.10672) [doi](https://doi.org/10.22331/q-2024-07-15-1410)
