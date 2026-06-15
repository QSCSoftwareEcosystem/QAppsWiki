---
type: concept
name: 3D DA color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-color
- concepts/qec/cubic-honeycomb-color
- concepts/qec/da
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/da_color_3d
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: da_color_3d
---

# 3D DA color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/da_color_3d) (`code_id: da_color_3d`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 3D dynamical code constructed aperiodically that utilizes measurement sequences to encode logical information with automorphisms of the 3D color code.
The code represents the first step towards universal quantum computation with dynamical automorphism codes.

The measurement sequence cycles the instantaneous stabilizer group (ISG) through different stabilizer groups, where certain measurement rounds realize the ISG of the 3D color code.
The parent topological phase underlying this dynamical code is realized by three copies of the cubic honeycomb color code  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).

(source: raw/error-correction-zoo.md)

## General gates

- A non-Clifford logical gate can be realized via adaptive two-qubit measurements  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).

## Relations

- _parent_: [[concepts/qec/da]] — The 3D DA color code is a dynamical code with an aperiodic measurement sequence realizing a non-Clifford logical gate.
- _cousin_: [[concepts/qec/cubic-honeycomb-color]] — The parent topological phase of the 3D DA color code is realized by three copies of the cubic honeycomb color code  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).
- _cousin_: [[concepts/qec/3d-color]] — At certain measurement rounds, the 3D DA color code realizes the instantaneous stabilizer group (ISG) of the 3D color code  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).
