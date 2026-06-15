---
type: concept
name: EA FG-QLDPC code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ea-qldpc
- concepts/qec/pg-qldpc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_pg_qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_pg_qldpc
---

# EA FG-QLDPC code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_pg_qldpc) (`code_id: ea_pg_qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

One of several EA QLDPC code families constructed from finite-geometry LDPC (FG-LDPC) codes.
The construction includes families whose entanglement-consumption rate $c/n$ decreases with block length $n$  ([arXiv:0906.5532](https://arxiv.org/abs/0906.5532)).
Two such FG-based families require only one ebit ($c=1$) independent of code length  ([arXiv:0906.5532](https://arxiv.org/abs/0906.5532)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/ea-qldpc]]
- _cousin_: [`pg_ldpc`](https://errorcorrectionzoo.org/c/pg_ldpc) — EA FG-QLDPC codes are entanglement-assisted quantum analogues of finite-geometry LDPC codes.
- _cousin_: [[concepts/qec/pg-qldpc]] — EA FG-QLDPC codes are entanglement-assisted versions of FG qubit QLDPC codes.
