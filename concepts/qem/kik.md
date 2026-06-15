---
type: concept
name: K-Inverse-K (KIK)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- adaptive KIK
- pulse-based inverse evolution
- layered KIK
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/echo-verification
- concepts/qem/pauli-twirling
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=kik
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: kik
---

# K-Inverse-K (KIK)

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=kik) (`id: kik`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Mitigates errors by combining noisy circuit outputs with outputs from pulse-based inverse evolutions, using adaptive coefficients tuned to the device noise level. Unlike gate-level folding (ZNE) or echo verification, KIK constructs the inverse at the pulse level by reversing pulse amplitudes and time ordering, enabling more accurate noise cancellation. The method adapts to moderate-to-strong noise regimes and integrates with randomized compiling to handle both coherent and incoherent noise.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Low; first-order noise cancellation with adaptive coefficients |
| Sampling overhead | Low; number of circuits is independent of system size |
| Noise model required | None; no tomography or machine learning required |
| Applicability | General-purpose; handles moderate-to-strong noise, time-dependent noise, and spatially correlated errors |

## Related techniques

- [[concepts/qem/echo-verification]] — both use forward and inverse circuits; KIK operates at pulse level with adaptive coefficients
- [[concepts/qem/zne]] — KIK outperforms circuit folding ZNE by using pulse-based inverses and adaptive coefficients
- [[concepts/qem/pauli-twirling]] — KIK integrates with randomized compiling to handle coherent noise
- [[concepts/qem/dd]] — both operate at the pulse level to suppress noise

## References

- L. Botelho, A. Glos, A. Kundu, J. A. Miszczak, Ö. Salehi, Z. Zimborás. *Adaptive Quantum Error Mitigation Using Pulse-Based Inverse Evolutions*. npj Quantum Information, 2023 [arXiv:2303.05001](https://arxiv.org/abs/2303.05001) [doi](https://doi.org/10.1038/s41534-023-00785-7)
- L. Botelho, A. Glos, A. Kundu, Ö. Salehi, Z. Zimborás. *Layered KIK Quantum Error Mitigation for Dynamic Circuits and Error Correction*. arXiv preprint, 2025 [arXiv:2504.12457](https://arxiv.org/abs/2504.12457) [doi](https://doi.org/10.48550/arXiv.2504.12457)
