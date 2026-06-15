---
type: concept
name: Echo Verification
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- EV
- computational echo
- mirror verification
- self-mitigation
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/cdr
- concepts/qem/purification
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=echo-verification
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: echo-verification
---

# Echo Verification

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=echo-verification) (`id: echo-verification`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Detects errors by running the target circuit forward and then its inverse (the 'echo'), so that the ideal output should return to the initial state. Deviations from the initial state signal that errors occurred. An ancilla qubit can be used to condition on successful verification, or ancilla-free variants measure the overlap directly. Echo verification effectively performs a purity-based check that amplifies the signal from the dominant eigenvector of the noisy density matrix.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced; errors that survive the echo are suppressed exponentially |
| Sampling overhead | Roughly doubles circuit depth (forward + inverse); post-selection reduces effective sample size |
| Noise model required | None (model-free) |
| Applicability | General-purpose; especially effective for coherent errors and short-to-moderate depth circuits |

## Related techniques

- [[concepts/qem/purification]] — both exploit purity to suppress noise; EV uses time-reversal instead of copies
- [[concepts/qem/symmetry-verification]] — both use post-selection to discard erroneous runs
- [[concepts/qem/cdr]] — EV+CDR is a powerful combined technique demonstrated in recent experiments

## References

- Z. Cai. *Resource-Efficient Purification-Based Quantum Error Mitigation*. arXiv preprint, 2021 [arXiv:2107.07279](https://arxiv.org/abs/2107.07279) [doi](https://doi.org/10.48550/arXiv.2107.07279)
- S. A. Rahman, R. Lewis, E. Mendicelli, S. Powell. *Self-Mitigating Trotter Circuits for SU(2) Lattice Gauge Theory*. Physical Review D, 2022 [arXiv:2205.09247](https://arxiv.org/abs/2205.09247) [doi](https://doi.org/10.1103/PhysRevD.106.074502)
