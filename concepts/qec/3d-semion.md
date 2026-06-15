---
type: concept
name: Chiral semion Walker-Wang model code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-stabilizer
- concepts/qec/qudit-stabilizer
- concepts/qec/semion
- concepts/qec/tqt
- concepts/qec/walker-wang
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/3d_semion
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 3d_semion
---

# Chiral semion Walker-Wang model code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/3d_semion) (`code_id: 3d_semion`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 3D lattice modular-qudit stabilizer code with qudit dimension $q=4$ whose low-energy excitations on boundaries realize the chiral semion topological order.
The model admits 2D chiral semion topological order at one of its surfaces  ([arXiv:1907.02075](https://arxiv.org/abs/1907.02075), [arXiv:2202.05442](https://arxiv.org/abs/2202.05442)).
The corresponding phase can also be realized via a non-stabilizer Hamiltonian  ([arXiv:1208.5128](https://arxiv.org/abs/1208.5128)).

(source: raw/error-correction-zoo.md)

## Encoders

- A unitary QCA encoder applied to product state realizes the 3D chiral semion Walker-Wang model code, which in turn admits 2D chiral semion topological order if truncated at one of its surfaces  ([arXiv:1907.02075](https://arxiv.org/abs/1907.02075), [arXiv:2202.05442](https://arxiv.org/abs/2202.05442)).

## Relations

- _parent_: [[concepts/qec/qudit-stabilizer]]
- _parent_: [[concepts/qec/3d-stabilizer]]
- _parent_: [[concepts/qec/walker-wang]] — The Walker-Wang model code reduces to the chiral semion model code when the input category is $\mathcal{C}=\mathbb{Z}_{2}^{(1/2)}$, or alternatively $\mathcal{C}=\mathbb{Z}_{4}^{(1)}$ after condensing a $\mathbb{Z}_{2}$-transparent boson.
- _parent_: [[concepts/qec/tqt]] — When treated as ground states of the code Hamiltonian, the code states realize 3D double-semion topological order, a topological phase of matter that exists as the deconfined phase of the 3D twisted $\mathbb{Z}_2$ gauge theory  ([doi:10.1007/BF02096988](https://doi.org/10.1007/BF02096988)).
- _cousin_: [[concepts/qec/semion]] — A unitary QCA encoder applied to product state realizes the 3D chiral semion Walker-Wang model code, which in turn admits 2D chiral semion topological order if truncated at one of its surfaces  ([arXiv:1907.02075](https://arxiv.org/abs/1907.02075), [arXiv:2202.05442](https://arxiv.org/abs/2202.05442)).
