---
type: concept
name: Quantum Hermitian AG code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-ag
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_hermitian_ag
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_hermitian_ag
---

# Quantum Hermitian AG code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_hermitian_ag) (`code_id: quantum_hermitian_ag`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Quantum AG code constructed from Hermitian AG codes via the Galois-qudit Hermitian construction or the Galois-qudit CSS construction.
The underlying classical codes can be constructed from one-point  ([doi:10.1007/11617983_13](https://doi.org/10.1007/11617983_13)) or two-point  ([arXiv:1102.3605](https://arxiv.org/abs/1102.3605)) Hermitian codes on Hermitian curves (see also Ref.  ([arXiv:2110.00769](https://arxiv.org/abs/2110.00769))).
In parameter ranges where two-point Hermitian codes improve on one-point codes, the resulting quantum codes can also have improved parameters  ([arXiv:1102.3605](https://arxiv.org/abs/1102.3605)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/quantum-ag]]
- _cousin_: [`hermitian`](https://errorcorrectionzoo.org/c/hermitian) — Quantum Hermitian AG codes are quantum analogues of Hermitian codes.
