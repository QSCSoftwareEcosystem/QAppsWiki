---
type: concept
name: Floquet 3D fermionic surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-fermionic-surface
- concepts/qec/3d-kitaev-honeycomb
- concepts/qec/floquet
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/floquet_3d_fermionic_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: floquet_3d_fermionic_surface
---

# Floquet 3D fermionic surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/floquet_3d_fermionic_surface) (`code_id: floquet_3d_fermionic_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 3D Floquet code on a trivalent lattice whose weight-two checks are the $XX$, $YY$, and $ZZ$ edge terms of the 3D Kitaev honeycomb model  ([arXiv:0801.0229](https://arxiv.org/abs/0801.0229), [arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

A rewinding sixteen-round schedule yields ISGs that are FDLQC-equivalent to the 3D fermionic surface code.
The rewinding avoids measuring all non-contractible-loop logical operators, so on periodic boundaries the Floquet code preserves a single logical qubit even though the static 3D fermionic surface code has three  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

(source: raw/error-correction-zoo.md)

## Rate

With periodic boundary conditions, the rewinding schedule preserves a single logical qubit because two logical operators are inferred during the cycle  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

## Relations

- _parent_: [[concepts/qec/floquet]]
- _cousin_: [[concepts/qec/3d-fermionic-surface]] — Each ISG of the Floquet 3D fermionic surface code is FDLQC-equivalent to the 3D fermionic surface code  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [[concepts/qec/3d-kitaev-honeycomb]] — The weight-two check operators of the Floquet 3D fermionic surface code are those of the 3D Kitaev honeycomb model  ([arXiv:0801.0229](https://arxiv.org/abs/0801.0229), [arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
