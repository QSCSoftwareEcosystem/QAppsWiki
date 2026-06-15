---
type: concept
name: N-Representability Constraints
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- fermionic constraints
- reduced density matrix constraints
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/subspace-expansion
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=n-representability
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: n-representability
---

# N-Representability Constraints

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=n-representability) (`id: n-representability`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Leverages known constraints from quantum chemistry and many-body physics on reduced density matrices (RDMs). Physical RDMs must satisfy $N$-representability conditions (e.g., the 2-RDM must be derivable from a valid $N$-particle state). By projecting noisy estimates of RDMs onto the set of $N$-representable matrices, unphysical noise artifacts are removed.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced; projection removes unphysical contributions |
| Sampling overhead | Minimal (classical post-processing only) |
| Noise model required | None; uses physical constraints |
| Applicability | Primarily fermionic/quantum chemistry problems |

## Related techniques

- [[concepts/qem/symmetry-verification]] — both exploit physical constraints to remove noise
- [[concepts/qem/subspace-expansion]] — both are post-processing methods for variational algorithms

## References

- N. C. Rubin, R. Babbush, J. R. McClean. *Application of Fermionic Marginal Constraints to Hybrid Quantum Algorithms*. New Journal of Physics, 2018 [arXiv:1801.03524](https://arxiv.org/abs/1801.03524) [doi](https://doi.org/10.1088/1367-2630/aab919)
- J. R. McClean, M. E. Kimchi-Schwartz, J. Carter, W. A. de Jong. *Hybrid Quantum-Classical Hierarchy for Mitigation of Decoherence and Determination of Excited States*. Physical Review A, 2017 [arXiv:1603.05681](https://arxiv.org/abs/1603.05681) [doi](https://doi.org/10.1103/PhysRevA.95.042308)
