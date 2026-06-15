---
type: concept
name: 3D lattice stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/asymmetric-qecc
- concepts/qec/clifford-deformed-surface
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/3d_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 3d_stabilizer
---

# 3D lattice stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/3d_stabilizer) (`code_id: 3d_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Lattice stabilizer code in three Euclidean dimensions, using either the ordinary block notion of locality or the fermionic/Majorana notion of locality.

For translation-invariant qubit topological stabilizer models in 3D, bulk commutation data can be used to coarsely sort phases into topological quantum field theory (TQFT), foliated type-I, fractal type-I, and type-II sectors  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).
For the TQFT sector, the paper conjectures equivalence under a locality-preserving unitary to copies of the 3D surface code and/or the 3D fermionic surface code, together with trivial ancillas  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).

(source: raw/error-correction-zoo.md)

## Code capacity threshold

- Applying Clifford deformations to various 3D stabilizer codes, including the 3D surface code, 3D color code, X-cube model code, and Sierpinski prism model code, yields a $50\%$ code capacity threshold under infinitely biased Pauli noise  ([arXiv:2211.02116](https://arxiv.org/abs/2211.02116)).

## Relations

- _parent_: [[concepts/qec/translationally-invariant-stabilizer]]
- _cousin_: [[concepts/qec/clifford-deformed-surface]] — Applying Clifford deformations to various 3D stabilizer codes, including the 3D surface code, 3D color code, X-cube model code, and Sierpinski prism model code, yields a $50\%$ code capacity threshold under infinitely biased Pauli noise  ([arXiv:2211.02116](https://arxiv.org/abs/2211.02116)).
- _cousin_: [[concepts/qec/asymmetric-qecc]] — Applying Clifford deformations to various 3D stabilizer codes, including the 3D surface code, 3D color code, X-cube model code, and Sierpinski prism model code, yields a $50\%$ code capacity threshold under infinitely biased Pauli noise  ([arXiv:2211.02116](https://arxiv.org/abs/2211.02116)).
