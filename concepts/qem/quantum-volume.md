---
type: concept
name: Quantum Volume
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/measurement-error-mitigation
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=quantum-volume
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: quantum-volume
qem_catalog: applications
---

# Quantum Volume

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=quantum-volume) (`id: quantum-volume`, catalog: applications, category: benchmarking). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Quantum volume (QV) is a hardware-agnostic metric that measures the largest random circuit a quantum computer can successfully execute. Error mitigation techniques, particularly ZNE with unitary folding and dynamical decoupling, have been shown to increase the effective quantum volume beyond vendor-reported values while using the same number of samples.

(source: raw/qem-zoo.md)

## Key results

- First demonstration of increased effective QV over manufacturer benchmarks using ZNE
- Achieved on multiple IBM Quantum superconducting processors
- Achieved with the same total shot budget, split across the noise levels

## Related techniques

- [[concepts/qem/zne]] — uses
- [[concepts/qem/dd]] — uses
- [[concepts/qem/measurement-error-mitigation]] — uses

## References

- E. Pelofske, V. Russo, R. LaRose, A. Mari, D. Strano, A. Bärtschi, S. Eidenbenz, W. J. Zeng. *Increasing the Measured Effective Quantum Volume with Zero Noise Extrapolation*. ACM Transactions on Quantum Computing, 2024 [arXiv:2306.15863](https://arxiv.org/abs/2306.15863) [doi](https://doi.org/10.1145/3680290)
- R. LaRose, A. Mari, V. Russo, D. Strano, W. J. Zeng. *Error Mitigation Increases the Effective Quantum Volume of Quantum Computers*. arXiv preprint, 2022 [arXiv:2203.05489](https://arxiv.org/abs/2203.05489) [doi](https://doi.org/10.48550/arXiv.2203.05489)
- C. N. Self, M. Benedetti, D. Amaro. *Protecting Expressive Circuits with a Quantum Error Detection Code*. Nature Physics, 2024 [arXiv:2211.06703](https://arxiv.org/abs/2211.06703) [doi](https://doi.org/10.1038/s41567-023-02282-2)
