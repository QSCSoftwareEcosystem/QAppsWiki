---
type: concept
name: X-cube Floquet code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/3d-surface
- concepts/qec/floquet
- concepts/qec/quantum-repetition
- concepts/qec/surface
- concepts/qec/xcube
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/floquet_xcube
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: floquet_xcube
---

# X-cube Floquet code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/floquet_xcube) (`code_id: floquet_xcube`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 3D Floquet code on the truncated cubic honeycomb, built from coupled layers of square-octagon Floquet toric codes.

Its original measurement schedule yields ISGs that are stacks of 2D surface codes or are FDLQC-equivalent to the X-cube model code  ([arXiv:2211.05784](https://arxiv.org/abs/2211.05784)).
A rewinding period-six schedule $GBRBGR$ yields only fracton ISGs: the G-round is the canonical X-cube model concatenated with four-qubit repetition codes on composite green edges, the B- and first R-rounds are FDLQC-equivalent to the product of the X-cube model, a 3D surface code, and a 3-foliated stack of 2D surface codes up to non-local stabilizers, and the second R-round is FDLQC-equivalent to the X-cube model together with a 3-foliated stack of 2D surface codes  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
A parent stabilizer code for the rewinding schedule is FDQC-equivalent to a 3-foliated stack of 2D color codes  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

(source: raw/error-correction-zoo.md)

## Rate

The original code has subextensive logical dimension  ([arXiv:2211.05784](https://arxiv.org/abs/2211.05784)); for even $L$, the rewinding schedule preserves $6L-3$ logical qubits on an $L\times L\times L$ three-torus  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

## Decoders

- Period-six measurement sequence utilizing two-qubit measurements  ([arXiv:2211.05784](https://arxiv.org/abs/2211.05784)).
- A rewinding period-six schedule $GBRBGR$ yields ISGs FDLQC-equivalent to the X-cube model together with a 3D surface-code factor and/or a 3-foliated stack of 2D surface codes  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

## Code capacity threshold

- It is argued that this code has a threshold in Ref.  ([arXiv:2211.05784](https://arxiv.org/abs/2211.05784)).

## Relations

- _parent_: [[concepts/qec/floquet]]
- _cousin_: [[concepts/qec/xcube]] — The G-round of the rewinding X-cube Floquet code is the canonical X-cube model concatenated with four-qubit repetition codes, while the other rounds remain FDLQC-equivalent to the X-cube model together with additional topological factors  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [[concepts/qec/surface]] — The rewinding schedule has rounds whose ISGs include a 3-foliated stack of 2D surface codes as an FDLQC-equivalent factor  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [[concepts/qec/3d-surface]] — The B- and first R-round ISGs of the rewinding schedule are FDLQC-equivalent to the product of the X-cube model, a 3D surface code, and a 3-foliated stack of 2D surface codes up to non-local stabilizers  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [[concepts/qec/quantum-repetition]] — The G-round of the rewinding X-cube Floquet code is exactly the canonical X-cube model concatenated with four-qubit repetition codes on composite green edges  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [[concepts/qec/2d-color]] — A parent stabilizer code for the rewinding X-cube Floquet code is FDQC-equivalent to a 3-foliated stack of 2D color codes  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
