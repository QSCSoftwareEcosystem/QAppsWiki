---
type: concept
name: Stellated surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stellated_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stellated_surface
---

# Stellated surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stellated_surface) (`code_id: stellated_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A twist-defect surface-code family parameterized by a rotational symmetry order $s$, with a central toric-code twist connected to the boundary by a domain wall.
The $s=3$ member is the triangular surface code  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

In the plaquette construction of Ref.  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)), qubits lie on vertices, each plaquette hosts one stabilizer, and plaquettes along the central domain wall act in mixed Pauli bases.

(source: raw/error-correction-zoo.md)

## Rate

Stellated surface codes have $c=2-\frac{2}{s}$ for odd $s$ and $c=2-\frac{4}{s}$ for even $s$, both approaching $2$ as $s$ grows  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).

## Relations

- _parent_: [[concepts/qec/twist-defect-surface]]
