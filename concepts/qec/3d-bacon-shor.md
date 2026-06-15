---
type: concept
name: 3D Bacon-Shor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bravyi-bacon-shor
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/3d_bacon_shor
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 3d_bacon_shor
---

# 3D Bacon-Shor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/3d_bacon_shor) (`code_id: 3d_bacon_shor`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Generalization of the Bacon-Shor code to three dimensions that was conjectured to be a self-correcting memory.
It is defined on a cubic lattice and admits sheet-like stabilizer generators.

(source: raw/error-correction-zoo.md)

## Protection

On an $L\times L\times L$ cubic lattice, the symmetric family has parameters $⟦L^3,1,L⟧$  ([arXiv:quant-ph/0506023](https://arxiv.org/abs/quant-ph/0506023)).

## Transversal gates

- Logical $CCZ$ gates on three code blocks of different orientations  ([arXiv:1705.01686](https://arxiv.org/abs/1705.01686)).

## Threshold

- The 3D Bacon-Shor code has two entanglement transitions  ([arXiv:2405.14927](https://arxiv.org/abs/2405.14927)).

## Relations

- _parent_: [[concepts/qec/bravyi-bacon-shor]]
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _cousin_: [`hypercubic`](https://errorcorrectionzoo.org/c/hypercubic) — 3D Bacon-Shor codes are defined on a hypercubic lattice.
