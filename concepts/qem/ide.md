---
type: concept
name: Infinite Distance Extrapolation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- IDE
- distance extrapolation
- code distance extrapolation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/lre
- concepts/qem/qed
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=ide
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: ide
---

# Infinite Distance Extrapolation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=ide) (`id: ide`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Adapts zero-noise extrapolation to the quantum error correction setting by using code distance as the extrapolation parameter. Since increasing code distance decreases the logical error rate analogously to decreasing physical noise, expectation values measured at several code distances can be extrapolated to the infinite-distance limit. The ansatz $y(d) = A + B e^{-Cd}$ is motivated by the analytical scaling of logical error rates from the threshold theorem, providing a more principled extrapolation than heuristic ZNE fitting models. Evaluated on the rotated surface code under circuit-level noise.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced compared to fixed-distance QEC; depends on ansatz quality and number of distances used |
| Sampling overhead | Requires running the computation at multiple code distances; parallelizable on a single device |
| Noise model required | None beyond a QEC decoder; ansatz is analytically motivated |
| Applicability | Early fault-tolerant regime; requires physical error rate below the code threshold |

## Related techniques

- [[concepts/qem/zne]] — IDE applies ZNE's extrapolation framework with code distance replacing the noise parameter
- [[concepts/qem/lre]] — both generalize ZNE by changing the extrapolation parameter space
- [[concepts/qem/qed]] — IDE uses quantum error-detecting/correcting codes as a subroutine within the QEM framework

## References

- G. Umbrarescu, O. Higgott, D. E. Browne. *Infinite Distance Extrapolation: How error mitigation can enhance quantum error correction*. arXiv preprint, 2026 [arXiv:2603.11285](https://arxiv.org/abs/2603.11285)
