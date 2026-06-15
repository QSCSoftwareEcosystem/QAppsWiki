---
type: concept
name: Modular-qudit 3D surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-stabilizer
- concepts/qec/generalized-homological-product-css
- concepts/qec/quantum-triple
- concepts/qec/qudit-css
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_3d_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_3d_surface
---

# Modular-qudit 3D surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_3d_surface) (`code_id: qudit_3d_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A generalization of the 3D surface code to modular qudits.
Qudits are placed on edges, $Z$-type stabilizer generators are placed on square plaquettes oriented in all three directions, and $X$-type stabilizers are placed on the six edges neighboring every vertex  ([arXiv:1404.4618](https://arxiv.org/abs/1404.4618)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qudit-css]]
- _parent_: [[concepts/qec/quantum-triple]] — A quantum triple model for the group $G=\mathbb{Z}_q$ is a modular-qudit 3D surface code.
- _parent_: [[concepts/qec/generalized-homological-product-css]]
- _parent_: [[concepts/qec/3d-stabilizer]]
- _parent_: [[concepts/qec/topological-abelian]] — The modular-qudit 3D surface code realizes 3D $\mathbb{Z}_q$ gauge theory with bosonic charge and loop excitations (BcBl).
