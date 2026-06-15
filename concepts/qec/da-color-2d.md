---
type: concept
name: 2D DA color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/da
- concepts/qec/surface
- concepts/qec/triangular-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/da_color_2d
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: da_color_2d
---

# 2D DA color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/da_color_2d) (`code_id: da_color_2d`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 2D dynamical code constructed aperiodically that utilizes measurement sequences to encode logical information with automorphisms of the 2D color code.
The code is assembled from short measurement sequences that can realize all 72 automorphisms of the 2D color code.
On a stack of $N$ triangular patches with a Pauli boundary, the code encodes $N$ logical qubits.

The measurement sequence cycles the instantaneous stabilizer group (ISG) through different stabilizer groups, where certain measurement rounds realize the ISG of the 2D color code.
The parent topological phase underlying this dynamical code is realized by two copies of the 6.6.6 (honeycomb) color code  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).

(source: raw/error-correction-zoo.md)

## General gates

- On $N$ layers of triangular patches (which encodes $N$ logical qubits) with a *Pauli boundary*, the measurement sequences can implement all Clifford logical gates via a sequence of two- and three-qubit Pauli measurements  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).

## Relations

- _parent_: [[concepts/qec/da]] — The 2D DA color code is a dynamical code with an aperiodic measurement sequence realizing Clifford logical gates.
- _cousin_: [[concepts/qec/triangular-color]] — The parent topological phase of the 2D DA color code is realized by two copies of the 6.6.6 color code  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).
- _cousin_: [[concepts/qec/2d-color]] — At certain measurement rounds, the 2D DA color code realizes the instantaneous stabilizer group (ISG) of the 2D color code  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).
- _cousin_: [[concepts/qec/surface]] — One of the instantaneous stabilizer groups of the 2D DA color code is that of stacks of surface codes  ([arXiv:2307.10353](https://arxiv.org/abs/2307.10353)).
