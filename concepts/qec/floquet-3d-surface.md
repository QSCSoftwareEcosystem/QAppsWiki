---
type: concept
name: Floquet 3D surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/3d-subsystem-surface
- concepts/qec/3d-surface
- concepts/qec/checkerboard
- concepts/qec/floquet
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/floquet_3d_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: floquet_3d_surface
---

# Floquet 3D surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/floquet_3d_surface) (`code_id: floquet_3d_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 3D Floquet code on a truncated cubic honeycomb with pairs of physical qubits on vertices.
It is constructed from three stacks of square-octagon Floquet toric codes, coupled by interlayer $YY$ measurements in a coupled-layer construction  ([arXiv:1701.00747](https://arxiv.org/abs/1701.00747), [arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

The rewinding schedule $GBRBGR$ yields ISGs that are FDLQC-equivalent either to the 3D surface code or to two copies of the 3D surface code up to non-local stabilizers.
A parent stabilizer code for this Floquet code is FDQC-equivalent to a 3-foliated stack of 2D color codes  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

(source: raw/error-correction-zoo.md)

## Rate

On a three-torus of linear size $L$, the Floquet code preserves three logical qubits  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

## General gates

- A planar Floquet 3D surface code stacked with two planar 3D subsystem surface codes prepares an instantaneous state equivalent to a 3D surface code stacked with two checkerboard model codes, enabling a logical $CCZ$ gate  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

## Relations

- _parent_: [[concepts/qec/floquet]]
- _cousin_: [[concepts/qec/3d-surface]] — The G-round ISG is FDLQC-equivalent to the 3D surface code, while the other rounds are FDLQC-equivalent to two copies of the 3D surface code up to non-local stabilizers  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [[concepts/qec/2d-color]] — A parent stabilizer code for the Floquet 3D surface code is FDQC-equivalent to a 3-foliated stack of 2D color codes  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [[concepts/qec/3d-subsystem-surface]] — A planar Floquet 3D surface code stacked with two planar 3D subsystem surface codes prepares an instantaneous state equivalent to a 3D surface code stacked with two checkerboard model codes, enabling a logical $CCZ$ gate  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [[concepts/qec/checkerboard]] — A planar Floquet 3D surface code stacked with two planar 3D subsystem surface codes prepares an instantaneous state equivalent to a 3D surface code stacked with two checkerboard model codes, enabling a logical $CCZ$ gate  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
