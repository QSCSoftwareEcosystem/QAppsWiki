---
type: concept
name: $(1,3)$ 4D toric code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/4d-stabilizer
- concepts/qec/dijkgraaf-witten
- concepts/qec/higher-dimensional-surface
- concepts/qec/multisector-hypergraph
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/4d_13_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 4d_13_surface
---

# $(1,3)$ 4D toric code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/4d_13_surface) (`code_id: 4d_13_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A generalization of the Kitaev surface code defined on a 4D lattice.
The code is called a $(1,3)$ toric code because it admits 1D $Z$-type and 3D $X$-type logical operators.
In the hypercubic lattice version, qubits are placed on edges, each $Z$-type stabilizer generator is supported on cubes on the boundary of a hypercube, and $X$-type stabilizers are placed on the edges neighboring every vertex  ([arXiv:2010.02238](https://arxiv.org/abs/2010.02238)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- Logical $CCCZ$ gate on a hyper-diamond lattice  ([arXiv:2010.02238](https://arxiv.org/abs/2010.02238)).

## Relations

- _parent_: [[concepts/qec/higher-dimensional-surface]] — The $(1,3)$ 4D toric code realizes 4D $\mathbb{Z}_2$ gauge theory with 1D $Z$-type and 3D $X$-type logical operators.
- _parent_: [[concepts/qec/4d-stabilizer]]
- _parent_: [[concepts/qec/topological-abelian]] — The $(1,3)$ 4D toric code realizes 4D $\mathbb{Z}_2$ gauge theory with 1D $Z$-type and 3D $X$-type logical operators.
- _parent_: [[concepts/qec/dijkgraaf-witten]] — An untwisted Dijkgraaf-Witten theory in 4D for the group $G=\mathbb{Z}_2$ is a $(1,3)$ 4D toric code.
- _cousin_: [`dfour`](https://errorcorrectionzoo.org/c/dfour) — The $(1,3)$ 4D toric code on a hyper-diamond lattice admits a transversal logical $CCCZ$ gate  ([arXiv:2010.02238](https://arxiv.org/abs/2010.02238)).
- _cousin_: [[concepts/qec/multisector-hypergraph]] — The 4D $(1,3)$ planar (toric) code on a hypercubic lattice can be obtained from a particular choice of chain complex from a hypergraph product of four repetition codes  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The 4D $(1,3)$ planar (toric) code on a hypercubic lattice can be obtained from a particular choice of chain complex from a hypergraph product of four repetition codes  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).
