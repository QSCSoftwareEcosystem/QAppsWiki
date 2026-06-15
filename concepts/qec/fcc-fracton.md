---
type: concept
name: Four Color Cube (FCC) fracton model code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fracton
- concepts/qec/qldpc
- concepts/qec/qubit-css
- concepts/qec/xcube
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fcc_fracton
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fcc_fracton
---

# Four Color Cube (FCC) fracton model code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fcc_fracton) (`code_id: fcc_fracton`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A fracton code obtained from four coupled X-cube models using p-membrane condensation.
A modular-qudit generalization has been proposed  ([arXiv:2412.14320](https://arxiv.org/abs/2412.14320)).

(source: raw/error-correction-zoo.md)

## Rate

The logical space on a cubic lattice of length $L$ with periodic boundary conditions is $32L - 24$ qubits.

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/fracton]]
- _cousin_: [[concepts/qec/xcube]] — The FCC fracton model code is obtained from four coupled X-cube models using p-membrane condensation.  ([arXiv:1701.00747](https://arxiv.org/abs/1701.00747)).
