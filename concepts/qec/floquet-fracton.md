---
type: concept
name: Fracton Floquet code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/checkerboard
- concepts/qec/floquet
- concepts/qec/floquet-color
- concepts/qec/xcube
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/floquet_fracton
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: floquet_fracton
---

# Fracton Floquet code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/floquet_fracton) (`code_id: floquet_fracton`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

3D Floquet code whose qubits are placed on vertices of a truncated cubic honeycomb.
Its weight-two check operators are placed on edges of each truncated cube, while weight-three check operators are placed on each triangle.
Its ISG can be that of the X-cube model code or the checkerboard model code.
On a three-torus of size $L_x \times L_y \times L_z$, the code consists of $n= 48L_xL_yL_z$ physical qubits and encodes $k= 2(L_x+L_y+L_z)-6$ logical qubits.

(source: raw/error-correction-zoo.md)

## Decoders

- Period-six measurement sequence utilizing two- and three-qubit measurements  ([arXiv:2210.02468](https://arxiv.org/abs/2210.02468)).

## Relations

- _parent_: [[concepts/qec/floquet]]
- _cousin_: [[concepts/qec/xcube]] — The ISG of the Fracton Floquet code can be that of the X-cube model code or the checkerboard model code.
- _cousin_: [[concepts/qec/checkerboard]] — The ISG of the Fracton Floquet code can be that of the X-cube model code or the checkerboard model code.
- _cousin_: [[concepts/qec/floquet-color]] — The fracton Floquet code is obtained via a 3D generalization of the construction used in the Floquet color code  ([arXiv:2210.02468](https://arxiv.org/abs/2210.02468)).
