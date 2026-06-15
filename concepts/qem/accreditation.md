---
type: concept
name: Accreditation
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- output accreditation
- accreditation protocols
- trap-based verification
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/symmetry-verification
- concepts/qem/zne
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=accreditation
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: accreditation
---

# Accreditation

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=accreditation) (`id: accreditation`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Certifies the output of a noisy quantum computation by interleaving 'trap' circuits — circuits whose ideal output is efficiently computable — alongside the target circuit. If the trap outputs pass verification, the target output is accredited with a certified error bound. The protocol provides a confidence interval on the distance between the noisy and ideal output distributions without requiring a noise model.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | None for the certification bound; target expectation value is untouched |
| Sampling overhead | Moderate; requires running additional trap circuits |
| Noise model required | None; model-free certification |
| Applicability | General-purpose; most useful when output correctness must be certified |

## Related techniques

- [[concepts/qem/symmetry-verification]] — both detect errors via post-selection or verification
- [[concepts/qem/zne]] — accreditation can certify whether ZNE output is trustworthy

## References

- S. Ferracin, T. Kapourniotis, A. Datta. *Accrediting Outputs of Noisy Intermediate-Scale Quantum Computing Devices*. New Journal of Physics, 2019 [arXiv:1811.09709](https://arxiv.org/abs/1811.09709) [doi](https://doi.org/10.1088/1367-2630/ab4fd6)
