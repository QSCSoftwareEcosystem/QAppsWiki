---
type: concept
name: Floquet color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- CSS Floquet toric code
- $\mathbb{Z}_2$ Floquet code
- CSS honeycomb code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/floquet
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/floquet_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: floquet_color
---

# Floquet color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/floquet_color) (`code_id: floquet_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

2D Floquet code on a trivalent 2D lattice whose parent topological phase is the $\mathbb{Z}_2\times\mathbb{Z}_2$ 2D color-code phase and whose measurements cycle logical quantum information between the nine $\mathbb{Z}_2$ surface-code condensed phases of the parent phase.
The code's ISG is the stabilizer group of one of the nine surface codes.

This older use of the term *Floquet color code* refers to the CSS/honeycomb construction of Refs.  ([arXiv:2210.02468](https://arxiv.org/abs/2210.02468), [arXiv:2212.00042](https://arxiv.org/abs/2212.00042)), and is distinct from the ruby-lattice Floquet color code of Ref.  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

(source: raw/error-correction-zoo.md)

## Decoders

- Period-six measurement sequence utilizing two-qubit measurements  ([arXiv:2210.02468](https://arxiv.org/abs/2210.02468)).

## Fault tolerance

- Fault-tolerant measurement-based computation can be realized using the foliated Floquet color code  ([arXiv:2212.06775](https://arxiv.org/abs/2212.06775)).

## Realizations

- Plaquette stabilizer measurement realized on the IBM Falcon superconducting-qubit device  ([arXiv:2210.13154](https://arxiv.org/abs/2210.13154))

## Relations

- _parent_: [[concepts/qec/floquet]]
- _cousin_: [[concepts/qec/2d-color]] — The parent topological phase of the Floquet color code is the $\mathbb{Z}_2\times\mathbb{Z}_2$ 2D color-code phase.
- _cousin_: [[concepts/qec/surface]] — The ISG of the Floquet color code is the stabilizer group of one of nine realizations of the $\mathbb{Z}_2$ 2D surface code.
