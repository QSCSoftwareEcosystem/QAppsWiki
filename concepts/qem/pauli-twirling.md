---
type: concept
name: Pauli Twirling
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- PT
- Pauli-frame randomization
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/dd
- concepts/qem/partial-pauli-twirling
- concepts/qem/pec
- concepts/qem/pseudo-twirling
- concepts/qem/symmetric-clifford-twirling
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=pauli-twirling
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: pauli-twirling
---

# Pauli Twirling

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=pauli-twirling) (`id: pauli-twirling`, category: suppression). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Converts coherent (systematic) gate errors into stochastic Pauli noise by randomly conjugating each gate with Pauli operators drawn from the Pauli group, choosing pairs that preserve the gate's action up to a tracked phase. Over many randomized circuit instances, off-diagonal terms in the error channel average out, leaving a Pauli channel. This tailored noise is easier to analyze and mitigate with downstream techniques such as PEC or ZNE.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Converts coherent errors to stochastic; does not remove noise on its own |
| Sampling overhead | Minimal; requires averaging over random Pauli insertions |
| Noise model required | None |
| Applicability | General-purpose; especially useful as a preprocessing step before PEC or ZNE |

## Related techniques

- [[concepts/qem/pec]] — Pauli twirling simplifies noise for PEC
- [[concepts/qem/zne]] — Pauli twirling simplifies noise for ZNE
- [[concepts/qem/dd]] — both are suppression techniques applied at the gate level
- [[concepts/qem/partial-pauli-twirling]] — PPT uses a subset of Pauli gates optimized for error-detecting codes
- [[concepts/qem/pseudo-twirling]] — pseudo twirling extends Pauli twirling to non-Clifford gates
- [[concepts/qem/symmetric-clifford-twirling]] — SCT uses symmetric Cliffords for structure-preserving noise scrambling

## References

- J. J. Wallman, J. Emerson. *Noise Tailoring for Scalable Quantum Computation via Randomized Compiling*. Physical Review A, 2016 [arXiv:1512.01098](https://arxiv.org/abs/1512.01098) [doi](https://doi.org/10.1103/PhysRevA.94.052325)
- M. Ware, G. Ribeill, D. Ristè, C. A. Ryan, B. Johnson, M. P. da Silva. *Experimental Demonstration of Pauli-Frame Randomization on a Superconducting Qubit*. Physical Review A, 2021 [arXiv:1803.01818](https://arxiv.org/abs/1803.01818) [doi](https://doi.org/10.1103/PhysRevA.103.042604)
- A. Hashim, R. K. Naik, A. Morvan, J.-L. Ville, B. Mitchell, J. M. Kreikebaum, M. Davis, E. Smith, C. Iancu, K. P. O'Brien, I. Hincks, J. J. Wallman, J. Emerson, I. Siddiqi. *Randomized Compiling for Scalable Quantum Computing on a Noisy Superconducting Quantum Processor*. Physical Review X, 2021 [arXiv:2010.00215](https://arxiv.org/abs/2010.00215) [doi](https://doi.org/10.1103/PhysRevX.11.041039)
- A. A. Saki, A. Katabarwa, S. Resch, G. Umbrarescu. *Hypothesis Testing for Error Mitigation: How to Evaluate Error Mitigation*. arXiv preprint, 2023 [arXiv:2301.02690](https://arxiv.org/abs/2301.02690) [doi](https://doi.org/10.48550/arXiv.2301.02690)
