---
type: concept
name: Sparse Pauli-Lindblad Learning
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Pauli-Lindblad noise model
- SPL
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=sparse-pauli-lindblad
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: sparse-pauli-lindblad
qem_catalog: noise-learning
---

# Sparse Pauli-Lindblad Learning

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=sparse-pauli-lindblad) (`id: sparse-pauli-lindblad`, catalog: noise-learning). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Learns a sparse noise model by representing errors as low-weight Pauli operators in a Lindblad master equation. The sparsity assumption (weight $\leq 2$, geometrically local) reduces parameters from $O(4^{2n})$ to $O(n \cdot 4^w)$, enabling scalable learning and inversion. Captures correlated noise including crosstalk. Used in the 127-qubit utility demonstration.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Scalability | Demonstrated on 100+ qubits |
| Noise captured | Local Pauli errors, nearest-neighbor correlations, crosstalk |
| Learning method | Calibration circuits (randomized benchmarking style) |
| Enables | Scalable PEC, accurate PEA noise amplification |

## References

- E. van den Berg, Z. K. Minev, A. Kandala, K. Temme. *Probabilistic Error Cancellation with Sparse Pauli–Lindblad Models on Noisy Quantum Processors*. Nature Physics, 2023 [arXiv:2201.09866](https://arxiv.org/abs/2201.09866) [doi](https://doi.org/10.1038/s41567-023-02042-2)
- Y. Kim, A. Eddins, S. Anand, K. X. Wei, E. van den Berg, S. Rosenblatt, H. Nayfeh, Y. Wu, M. Zaletel, K. Temme, A. Kandala. *Evidence for the Utility of Quantum Computing Before Fault Tolerance*. Nature, 2023 [doi](https://doi.org/10.1038/s41586-023-06096-3)
