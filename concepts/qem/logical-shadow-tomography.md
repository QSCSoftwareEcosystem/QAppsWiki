---
type: concept
name: Logical Shadow Tomography
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- LST
- logical shadows
- codespace shadow tomography
domains:
- quantum-error-correction
related_concepts:
- concepts/qem/purification
- concepts/qem/qed
- concepts/qem/robust-shadows
- concepts/qem/subspace-expansion
sources:
- raw/qem-zoo.md
- https://qemzoo.com/technique.html?id=logical-shadow-tomography
provenance_status: needs-verification
imported_from: qem-zoo
imported_id: logical-shadow-tomography
---

# Logical Shadow Tomography

> **Imported by `qappswiki import-zoo qemzoo`** from the [QEM Zoo](https://qemzoo.com/technique.html?id=logical-shadow-tomography) (`id: logical-shadow-tomography`, category: mitigation). Public domain (The Unlicense); cited as the QEM Zoo (qemzoo.com), public domain (The Unlicense). This is a `needs-verification` page — confirm against the references below.

## Summary

Performs shadow tomography on encoded logical states and uses classical post-processing to project noisy measurement data into the error-correction codespace. This filters out noise-induced errors without requiring mid-circuit syndrome measurements. LST unifies subspace expansion and virtual distillation as special cases, achieving sample complexity that scales with logical qubits $k$ rather than physical qubits $n$.

(source: raw/qem-zoo.md)

## Properties

| Property | Value |
|---|---|
| Bias | Low; codespace projection filters detectable errors |
| Sampling overhead | \(O(4^k)\) for \(k\) logical qubits; much better than \(O(2^n)\) for subspace expansion |
| Noise model required | None; uses code structure |
| Applicability | Encoded logical qubits; efficient estimation of logical Pauli observables |

## Related techniques

- [[concepts/qem/robust-shadows]] — both use shadow tomography; RSE calibrates measurement noise, LST projects onto codespace
- [[concepts/qem/subspace-expansion]] — QSE is a special case of the LST framework
- [[concepts/qem/purification]] — virtual distillation is a special case of the LST framework
- [[concepts/qem/qed]] — both use quantum error-detecting codes; LST applies codespace projection classically

## References

- H.-Y. Hu, R. LaRose, Y.-Z. You, E. Rieffel, Z. Wang. *Logical Shadow Tomography: Efficient Estimation of Error-Mitigated Observables*. arXiv preprint, 2022 [arXiv:2203.07263](https://arxiv.org/abs/2203.07263) [doi](https://doi.org/10.48550/arXiv.2203.07263)
