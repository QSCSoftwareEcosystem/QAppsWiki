---
type: concept
name: Circuit Unoptimization
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- quantum circuit unoptimization
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=circuit-unoptimization
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: circuit-unoptimization
qem_catalog: noise-scaling
---

# Circuit Unoptimization

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=circuit-unoptimization) (`id: circuit-unoptimization`, catalog: noise-scaling). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Amplifies noise by iteratively transforming a circuit into an equivalent but longer circuit via a four-step procedure: (1) insert a random two-qubit gate $A$ and $A^\dagger$ between existing gates, (2) swap gates via conjugation, (3) decompose into elementary gates, (4) resynthesize. The noise scale factor is $\lambda = n(R(C))/n(C)$ where $n$ is gate count. Unlike folding, unoptimization produces structurally different circuits, enabling averaging over exponentially many variants to reduce coherent error bias. Resists server-side compiler optimization.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Scale factors | Continuous (including fractional values near 1.0) |
| Hardware requirements | None |
| Advantages | Exponentially many circuit variants for averaging; resists compiler simplification; fractional scaling |
| Disadvantages | More complex to implement; circuit structure changes significantly |

## References

- Y. Mori, H. Hakoshima, K. Sudo, T. Mori, K. Mitarai, K. Fujii. *Quantum Circuit Unoptimization*. Physical Review Research, 2025 [arXiv:2311.03805](https://arxiv.org/abs/2311.03805) [doi](https://doi.org/10.1103/PhysRevResearch.7.023139)
- E. Pelofske, V. Russo. *Digital Zero-Noise Extrapolation with Quantum Circuit Unoptimization*. arXiv preprint, 2025 [arXiv:2503.06341](https://arxiv.org/abs/2503.06341) [doi](https://doi.org/10.48550/arXiv.2503.06341)
