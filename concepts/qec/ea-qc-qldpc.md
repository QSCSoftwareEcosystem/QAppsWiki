---
type: concept
name: EA QC-QLDPC code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ea-qldpc
- concepts/qec/quasi-cyclic-qldpc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_qc_qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_qc_qldpc
---

# EA QC-QLDPC code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_qc_qldpc) (`code_id: ea_qc_qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

One of several EA QLDPC code families constructed from classical QC-LDPC codes with girth at least six.
The entanglement assistance removes the dual-containing constraint in the CSS construction, avoiding many 4-cycles while retaining SPA decoding  ([arXiv:0803.0100](https://arxiv.org/abs/0803.0100)).

(source: raw/error-correction-zoo.md)

## Decoders

- Sum-product algorithm (SPA) decoder  ([arXiv:0906.5532](https://arxiv.org/abs/0906.5532)).

## Relations

- _parent_: [[concepts/qec/ea-qldpc]]
- _cousin_: [`qc_ldpc`](https://errorcorrectionzoo.org/c/qc_ldpc) — EA QC-QLDPC codes are entanglement-assisted quantum analogues of QC-LDPC codes.
- _cousin_: [[concepts/qec/quasi-cyclic-qldpc]] — EA QC-QLDPC codes are entanglement-assisted versions of QC-QLDPC codes.
