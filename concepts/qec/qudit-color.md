---
type: concept
name: Modular-qudit lattice color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-color
- concepts/qec/generalized-homological-product-css
- concepts/qec/qudit-css
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_color
---

# Modular-qudit lattice color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_color) (`code_id: qudit_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Extension of the color code to lattices of modular qudits.
Codes are defined analogously to qubit color codes on suitable lattices of any spatial dimension, but a directionality is required in order to make the modular-qudit stabilizers commute.
This can be done by puncturing a hyperspherical lattice  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)) or constructing a star-bipartition; see  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).
Logical dimension is determined by the genus of the underlying surface (for closed surfaces), types of boundaries (for open surfaces), and/or any twist defects present.

(source: raw/error-correction-zoo.md)

## Transversal gates

- Some modular-qudit lattice color codes on $D$-dimensional lattices can transversally implement a gate at the $(D-1)$st level of the qudit Clifford hierarchy  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).

## General gates

- Modular-qudit lattice color codes whose $X$-type stabilizers are placed on cells of dimension $\nu$ support transversal gates in the $\nu$th level of the qudit Clifford hierarchy as long as $\nu! \neq 0$ modulo the qudit dimension  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)). These codes saturate the Bravyi-Koenig bound. In particular, 3D modular-qudit color codes admit a transversal modular-qudit $T$ gate.
- For odd prime qudit dimension, charge-and-color-permuting twist defects can be used to implement generalized Clifford gates  ([arXiv:2110.08680](https://arxiv.org/abs/2110.08680)).

## Decoders

- Generalized Color Clustering (GCC) decoder  ([arXiv:1701.02335](https://arxiv.org/abs/1701.02335)).

## Relations

- _parent_: [[concepts/qec/qudit-css]]
- _parent_: [[concepts/qec/translationally-invariant-stabilizer]] — Modular-qudit lattice color codes are defined analogous to qubit color codes on suitable lattices of any spatial dimension, but a directionality is required in order to make the modular-qudit stabilizers commute  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).
- _parent_: [[concepts/qec/generalized-homological-product-css]]
- _cousin_: [[concepts/qec/generalized-color]] — The generalized color code for $G=\mathbb{Z}_q$ reduces to the 2D modular-qudit color code.
