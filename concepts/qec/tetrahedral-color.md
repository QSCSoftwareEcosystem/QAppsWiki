---
type: concept
name: Tetrahedral color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-color
- concepts/qec/3d-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tetrahedral_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tetrahedral_color
---

# Tetrahedral color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tetrahedral_color) (`code_id: tetrahedral_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 3D color code defined on a colored tetrahedron cut from a suitably colored BCC lattice  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).
Qubits are placed on tetrahedra, on the triangles covering the tetrahedron faces, on the edges along the tetrahedron edges, and on the tetrahedron vertices.
The code has both string-like and sheet-like logical operators  ([arXiv:1708.07131](https://arxiv.org/abs/1708.07131)).

(source: raw/error-correction-zoo.md)

## Rate

The tetrahedral family with linear size parameter $L$ has $n=1+4L+6L^2+4L^3$ physical qubits and encodes one logical qubit  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).

## Transversal gates

- A $⟦5d^3-12d^2+16,3,d⟧$ close relative of this code admits a logical $CCZ$ gate via single-qubit rotations; for this family, stabilizers remain asymptotically constant-weight and can be gauge-reduced to weight at most six  ([arXiv:2404.19005](https://arxiv.org/abs/2404.19005)).

## Threshold

- $0.46\%$ with clustering decoder  ([arXiv:1708.07131](https://arxiv.org/abs/1708.07131)).
- $1.9\%$ for 1D string-like logical operators and $27.6\%$ for 2D sheet-like operators for 3D codes with noise models using optimal decoding and perfect measurements  ([arXiv:1708.07131](https://arxiv.org/abs/1708.07131)).

## Fault tolerance

- Fault-tolerant quantum computation designed for a 2D architecture  ([arXiv:1810.09571](https://arxiv.org/abs/1810.09571)).

## Relations

- _parent_: [[concepts/qec/3d-color]]
- _cousin_: [`bcc`](https://errorcorrectionzoo.org/c/bcc) — The tetrahedral color code is defined on a lattice of tetrahedra carved out of a suitably colored BCC lattice  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).
- _cousin_: [[concepts/qec/3d-surface]] — A tetrahedral 3D color code with four differently colored boundaries is equivalent, via a local Clifford circuit, to three 3D surface codes attached along one boundary, with condensation of a composite electric charge on that attached boundary  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065)).
