---
type: concept
name: Sample-Based Quantum Diagonalization
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- SQD
- sample-based Krylov diagonalization
- SKQD
- SqDRIFT
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pauli-twirling
- concepts/qem/subspace-expansion
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=sqd
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: sqd
---

# Sample-Based Quantum Diagonalization

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=sqd) (`id: sqd`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Constructs a Krylov subspace by applying powers of the Hamiltonian (via time evolution) to a reference state, then uses measurement samples to build matrix representations for classical diagonalization. Unlike phase estimation, SQD avoids deep circuits by shifting computational burden to classical post-processing. The method achieves polynomial convergence guarantees while remaining practical for near-term quantum hardware.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Controlled; converges to ground state with increasing Krylov dimension |
| Sampling overhead | Moderate; requires samples from multiple Krylov states |
| Noise model required | None |
| Applicability | Ground state estimation for many-body systems; quantum chemistry |

## Related techniques

- [[concepts/qem/subspace-expansion]] — both construct subspaces for classical diagonalization; SQD uses Krylov states
- [[concepts/qem/zne]] — SqDRIFT variant uses randomized compilation similar to noise tailoring
- [[concepts/qem/pauli-twirling]] — SqDRIFT uses randomized Hamiltonian compilation

## References

- J. Yu, J. Robledo Moreno, J. T. Iosue, L. Bertels, D. Claudino, B. Fuller, P. Groszkowski, T. S. Humble, P. Jurcevic, W. Kirby, T. A. Maier, M. Motta, B. Pokharel, A. Seif, A. Shehata, K. J. Sung, M. C. Tran, V. Tripathi, A. Mezzacapo, K. Sharma. *Quantum-Centric Algorithm for Sample-Based Krylov Diagonalization*. arXiv preprint, 2025 [arXiv:2501.09702](https://arxiv.org/abs/2501.09702) [doi](https://doi.org/10.48550/arXiv.2501.09702)
- S. Piccinelli, A. Baiardi, S. Barison, M. Rossmannek, A. Carrera Vazquez, F. Tacchino, S. Mensa, E. Altamura, A. Alavi, M. Motta, J. Robledo-Moreno, W. Kirby, K. Sharma, A. Mezzacapo, I. Tavernelli. *Quantum Chemistry with Provable Convergence via Randomized Sample-Based Krylov Quantum Diagonalization*. arXiv preprint, 2025 [arXiv:2508.02578](https://arxiv.org/abs/2508.02578) [doi](https://doi.org/10.48550/arXiv.2508.02578)
