---
type: concept
name: Three-fermion (3F) Walker-Wang model code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-bosonization
- concepts/qec/3d-stabilizer
- concepts/qec/bosonization
- concepts/qec/qldpc
- concepts/qec/spt
- concepts/qec/topological-abelian
- concepts/qec/walker-wang
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/three_fermion
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: three_fermion
---

# Three-fermion (3F) Walker-Wang model code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/three_fermion) (`code_id: three_fermion`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 3D lattice stabilizer code whose bulk realizes a 3D time-reversal SPT order  ([arXiv:1302.7072](https://arxiv.org/abs/1302.7072)) and whose gapped boundary supports the 2D three-fermion (3F) topological order.
The code can be used as a resource state for fault-tolerant MBQC  ([arXiv:2011.04693](https://arxiv.org/abs/2011.04693)).

(source: raw/error-correction-zoo.md)

## Encoders

- 3F QCA encoder  ([arXiv:1812.01625](https://arxiv.org/abs/1812.01625), [arXiv:2205.09141](https://arxiv.org/abs/2205.09141)), which can be simplified using bosonization  ([arXiv:2309.15903](https://arxiv.org/abs/2309.15903)) and can be extended to SPTs in higher dimensions based on an exact bosonization duality  ([arXiv:2407.07951](https://arxiv.org/abs/2407.07951)).

## General gates

- Clifford gates can be performed by braiding and fusing symmetry defects in the MBQC model.

## Fault tolerance

- Fault-tolerant MBQC protocol by encoding in, braiding, and fusing symmetry defects.

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/3d-stabilizer]]
- _parent_: [[concepts/qec/walker-wang]] — The Walker-Wang model code reduces to the 3F model code when the input category $\mathcal{C}=3F$  ([arXiv:2011.04693](https://arxiv.org/abs/2011.04693)). When treated as ground states of the code Hamiltonian, 3F Walker-Wang model code states realize a 3D time-reversal SPT order  ([arXiv:1302.7072](https://arxiv.org/abs/1302.7072)), while the gapped boundary supports the 3F anyon theory.
- _parent_: [[concepts/qec/spt]] — When treated as ground states of the code Hamiltonian, 3F Walker-Wang model code states realize a 3D time-reversal SPT order  ([arXiv:1302.7072](https://arxiv.org/abs/1302.7072)). The 3F Walker-Wang QCA encoder  ([arXiv:1812.01625](https://arxiv.org/abs/1812.01625), [arXiv:2205.09141](https://arxiv.org/abs/2205.09141)) can be extended to SPTs in higher dimensions based on an exact bosonization duality  ([arXiv:2407.07951](https://arxiv.org/abs/2407.07951)).
- _cousin_: [[concepts/qec/3d-bosonization]] — The 3F Walker-Wang QCA encoder  ([arXiv:1812.01625](https://arxiv.org/abs/1812.01625), [arXiv:2205.09141](https://arxiv.org/abs/2205.09141)) can be simplified using bosonization  ([arXiv:2309.15903](https://arxiv.org/abs/2309.15903)).
- _cousin_: [[concepts/qec/bosonization]] — The 3F Walker-Wang QCA encoder  ([arXiv:1812.01625](https://arxiv.org/abs/1812.01625), [arXiv:2205.09141](https://arxiv.org/abs/2205.09141)) can be extended to SPTs in higher dimensions based on an exact bosonization duality  ([arXiv:2407.07951](https://arxiv.org/abs/2407.07951)).
- _cousin_: [[concepts/qec/topological-abelian]] — The gapped boundary of the 3F Walker-Wang model supports the 3F topological order  ([arXiv:1302.7072](https://arxiv.org/abs/1302.7072), [arXiv:2011.04693](https://arxiv.org/abs/2011.04693)).
