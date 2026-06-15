---
type: concept
name: Partial Pauli Twirling
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- PPT
- subset Pauli twirling
- optimized twirling
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/pauli-twirling
- concepts/qem/pec
- concepts/qem/qed
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=partial-pauli-twirling
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: partial-pauli-twirling
---

# Partial Pauli Twirling

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=partial-pauli-twirling) (`id: partial-pauli-twirling`, category: suppression). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Modifies standard Pauli twirling by using only a strategically selected subset of Pauli gates rather than the full group. The subset is optimized to align errors with the detectable error space of a quantum error-detecting code, enabling synergistic combination with QED. This reduces sampling overhead and can avoid error-prone gates (e.g., Y gates on certain hardware) at the cost of incomplete noise diagonalization.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Slightly higher than full twirling; does not fully diagonalize noise |
| Sampling overhead | Lower than full Pauli twirling; fewer circuit variants needed |
| Noise model required | None; optimization uses target error space from QED code |
| Applicability | Hybrid QED + error mitigation pipelines; hardware with biased gate errors |

## Related techniques

- [[concepts/qem/pauli-twirling]] — PPT is a resource-efficient variant of full Pauli twirling
- [[concepts/qem/qed]] — PPT is designed to synergize with quantum error detection codes
- [[concepts/qem/pec]] — PPT can be used as preprocessing before PEC in hybrid protocols

## References

- R. Majumdar, P. Rivero, F. Metz, A. Hasan, D. S. Wang. *Combining Error Detection and Mitigation: A Hybrid Protocol for Near-Term Quantum Simulation*. arXiv preprint, 2025 [arXiv:2510.01181](https://arxiv.org/abs/2510.01181) [doi](https://doi.org/10.48550/arXiv.2510.01181)
