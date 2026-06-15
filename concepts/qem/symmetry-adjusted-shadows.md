---
type: concept
name: Symmetry-Adjusted Classical Shadows
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- SAS
- group-theoretic error mitigation
- symmetry-adjusted shadows
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/logical-shadow-tomography
- concepts/qem/robust-shadows
- concepts/qem/symmetry-verification
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=symmetry-adjusted-shadows
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: symmetry-adjusted-shadows
---

# Symmetry-Adjusted Classical Shadows

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=symmetry-adjusted-shadows) (`id: symmetry-adjusted-shadows`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Adjusts classical shadow tomography based on how device errors corrupt known symmetries of the quantum system. Unlike standard symmetry verification (which post-selects), this technique uses group-theoretic structure to modify the shadow inversion itself, correcting estimates without discarding data. No calibration experiments are needed — the symmetry information alone enables error mitigation across the full circuit, not just readout errors.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Reduced; uses symmetry structure to correct estimates |
| Sampling overhead | Low; no calibration experiments required |
| Noise model required | None; only requires knowledge of preserved symmetries |
| Applicability | Systems with known symmetries (U(1), particle number, magnetization); fermionic and spin systems |

## Related techniques

- [[concepts/qem/symmetry-verification]] — both use symmetries; SV post-selects while SAS adjusts the shadow inversion
- [[concepts/qem/robust-shadows]] — both extend classical shadows for error mitigation; RSE uses calibration, SAS uses symmetry
- [[concepts/qem/logical-shadow-tomography]] — both use shadow tomography with additional structure for error mitigation

## References

- A. Zhao, A. Miyake. *Group-Theoretic Error Mitigation Enabled by Classical Shadows and Symmetries*. npj Quantum Information, 2024 [arXiv:2310.03071](https://arxiv.org/abs/2310.03071) [doi](https://doi.org/10.1038/s41534-024-00854-5)
