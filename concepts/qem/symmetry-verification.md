---
type: concept
name: Symmetry Verification
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- SV
- symmetry-based post-selection
- symmetry constraints
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/measurement-error-mitigation
- concepts/qem/n-representability
- concepts/qem/subspace-expansion
- concepts/qem/symmetry-adjusted-shadows
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=symmetry-verification
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: symmetry-verification
---

# Symmetry Verification

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=symmetry-verification) (`id: symmetry-verification`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Exploits known symmetries of the target quantum system (e.g., particle number conservation, parity, or spin symmetry) to detect and discard erroneous measurement outcomes. If the ideal output state is known to lie in a particular symmetry sector, any measurement result that violates this symmetry is post-selected away. A post-processing variant projects expectation values onto the symmetric subspace without discarding data.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced (post-selection) or adjustable (post-processing) |
| Sampling overhead | Inverse of pass rate (post-selection); inverse squared (post-processing) |
| Noise model required | None; requires knowledge of system symmetries |
| Applicability | Systems with known conserved quantities (chemistry, condensed matter, lattice gauge theories) |

## Related techniques

- [[concepts/qem/n-representability]] — both exploit physical constraints
- [[concepts/qem/subspace-expansion]] — symmetry constraints can define subspaces
- [[concepts/qem/measurement-error-mitigation]] — both can detect measurement-stage errors
- [[concepts/qem/symmetry-adjusted-shadows]] — SAS uses symmetry to adjust shadow inversion rather than post-select

## References

- S. McArdle, X. Yuan, S. Benjamin. *Error-Mitigated Digital Quantum Simulation*. Physical Review Letters, 2019 [arXiv:1807.02467](https://arxiv.org/abs/1807.02467) [doi](https://doi.org/10.1103/PhysRevLett.122.180501)
- X. Bonet-Monroig, R. Sagastizabal, M. Singh, T. E. O'Brien. *Low-Cost Error Mitigation by Symmetry Verification*. Physical Review A, 2018 [arXiv:1807.10050](https://arxiv.org/abs/1807.10050) [doi](https://doi.org/10.1103/PhysRevA.98.062339)
- Z. Cai. *Quantum Error Mitigation Using Symmetry Expansion*. Quantum, 2021 [arXiv:2101.03151](https://arxiv.org/abs/2101.03151) [doi](https://doi.org/10.22331/q-2021-09-21-548)
