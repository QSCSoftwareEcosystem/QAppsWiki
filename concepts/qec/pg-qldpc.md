---
type: concept
name: Finite-geometry (FG) qubit QLDPC code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/multisector-hypergraph
- concepts/qec/qldpc
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/pg_qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: pg_qldpc
---

# Finite-geometry (FG) qubit QLDPC code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/pg_qldpc) (`code_id: pg_qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

CSS code constructed from linear binary codes whose parity-check or generator matrices are incidence matrices of points, hyperplanes, or other structures in finite geometries.
These codes can be interpreted as quantum versions of FG-LDPC codes, but some of them  ([arXiv:1207.0732](https://arxiv.org/abs/1207.0732), [arXiv:1512.07081](https://arxiv.org/abs/1512.07081)) are not strictly QLDPC.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qldpc]]
- _cousin_: [`pg_ldpc`](https://errorcorrectionzoo.org/c/pg_ldpc) — Quantum versions of PG-LDPC and EG-LDPC codes can be constructed via the CSS construction  ([arXiv:0712.4115](https://arxiv.org/abs/0712.4115), [arXiv:1207.0732](https://arxiv.org/abs/1207.0732)).
- _cousin_: [`projective`](https://errorcorrectionzoo.org/c/projective) — PG-QLDPC codes are constructed from linear binary codes whose parity-check or generator matrices are incidence matrices of structures in finite geometries.
- _cousin_: [[concepts/qec/multisector-hypergraph]] — Multi-dimensional homological products of PG-QLDPC codes yield families whose stabilizer-generator weights scale logarithmically with $n$  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)) ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)).
