---
type: concept
name: Quasi-cyclic QLDPC (QC-QLDPC) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/general-qldpc
- concepts/qec/quantum-quasi-cyclic
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quasi_cyclic_qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quasi_cyclic_qldpc
---

# Quasi-cyclic QLDPC (QC-QLDPC) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quasi_cyclic_qldpc) (`code_id: quasi_cyclic_qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A QLDPC code such that cyclic shifts of the subsystems by a fixed $\ell\geq 1$ leave the codespace invariant.
Stabilizer generator matrices of such codes can be put into block form, where each nonzero block is a circulant matrix  ([arXiv:quant-ph/0701020](https://arxiv.org/abs/quant-ph/0701020), [arXiv:1007.1778](https://arxiv.org/abs/1007.1778)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/general-qldpc]]
- _parent_: [[concepts/qec/quantum-quasi-cyclic]]
- _cousin_: [`qc_ldpc`](https://errorcorrectionzoo.org/c/qc_ldpc) — QC-QLDPC codes are quantum counterparts of QC-LDPC codes. QC-LDPC codes can be used to make qubit QLDPC codes using various non-CSS constructions  ([doi:10.1109/TIT.2009.2034794](https://doi.org/10.1109/TIT.2009.2034794)). There exist explicit constructions of both whose parity-check (stabilizer generator) matrices have column weight 2 and girth 12  ([arXiv:2501.13444](https://arxiv.org/abs/2501.13444)).
