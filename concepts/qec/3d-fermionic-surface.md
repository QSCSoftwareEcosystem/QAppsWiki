---
type: concept
name: 3D fermionic surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- 3D toric code with emergent fermion
- Levin-Wen fermion model
- Fermionic-charge bosonic-loop (FcBl) surface code
- Twisted surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-bosonization
- concepts/qec/3d-stabilizer
- concepts/qec/3d-surface
- concepts/qec/kitaev-chain
- concepts/qec/qldpc
- concepts/qec/topological-abelian
- concepts/qec/walker-wang
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/3d_fermionic_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 3d_fermionic_surface
---

# 3D fermionic surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/3d_fermionic_surface) (`code_id: 3d_fermionic_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A non-CSS variant of the 3D Kitaev surface code that realizes $\mathbb{Z}_2$ gauge theory with an emergent fermion, i.e., the fermionic-charge bosonic-loop (FcBl) phase  ([arXiv:2110.14654](https://arxiv.org/abs/2110.14654)).
The model can be defined on a cubic lattice in several ways  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).
Realizations on other lattices also exist  ([arXiv:0811.2036](https://arxiv.org/abs/0811.2036)), and the phase of this code also exists in the 3D Kitaev honeycomb model  ([arXiv:0801.0229](https://arxiv.org/abs/0801.0229)).

*3D fermionic toric code* often either refers to the construction on the three-dimensional torus or is an alternative name for the general construction.
The construction on surfaces with boundaries is often called the
*3D fermionic surface code*.
However, unlike the 3D surface code, an open (a.k.a. rough) boundary is not possible.
Twist defects in the form of Kitaev chains can be introduced as in the 2D surface code to store additional logicals  ([arXiv:1906.01045](https://arxiv.org/abs/1906.01045), [arXiv:2208.07367](https://arxiv.org/abs/2208.07367)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- $CCZ$ and $CS$ gates can be obtained for the fermionic 3D surface code on certain manifolds by circuits that can be interpreted as moving and spreading lattice realizations of Kitaev chain and $p+ip$ defects  ([arXiv:2311.05674](https://arxiv.org/abs/2311.05674)).

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/3d-stabilizer]]
- _parent_: [[concepts/qec/topological-abelian]] — The 3D fermionic surface code realizes 3D $\mathbb{Z}_2$ gauge theory with fermionic charge and bosonic loop excitations (FcBl), i.e., with an emergent fermion. The fermionic excitations endow the code with an anomalous two-form symmetry, which is argued to induce a non-trivial finite-temperature topological order  ([arXiv:2503.02928](https://arxiv.org/abs/2503.02928)).
- _parent_: [[concepts/qec/walker-wang]] — The 3D fermionic surface code is a Walker-Wang model code with premodular input category $\mathcal{C} = \text{sVec}$ consisting of a trivial anyon and a fermion.
- _cousin_: [[concepts/qec/3d-surface]] — The 3D (fermionic) surface code is a CSS (non-CSS) code which realizes a $\mathbb{Z}_2$ gauge theory in 3D (with an emergent fermion). Two copies of the 3D fermionic surface code are equivalent to a copy of the 3D surface code and a copy of the 3D fermionic surface code via anyon relabeling: the two incoming fermions, $f_1$ and $f_2$, can be re-organized into a boson $f_1 f_2$ and fermion $f_2$.
- _cousin_: [[concepts/qec/kitaev-chain]] — The 3D fermionic surface code is the result of applying the 3D bosonization mapping to a trivial fermionic theory  ([arXiv:2208.07367](https://arxiv.org/abs/2208.07367)). Twist defects in the 3D fermionic surface code take the form of Kitaev chains after the mapping  ([arXiv:1906.01045](https://arxiv.org/abs/1906.01045), [arXiv:2208.07367](https://arxiv.org/abs/2208.07367)).
- _cousin_: [[concepts/qec/3d-bosonization]] — The 3D fermionic surface code is the result of applying the 3D bosonization mapping to a trivial fermionic theory  ([arXiv:2208.07367](https://arxiv.org/abs/2208.07367)). Twist defects in the 3D fermionic surface code take the form of Kitaev chains after the mapping  ([arXiv:1906.01045](https://arxiv.org/abs/1906.01045), [arXiv:2208.07367](https://arxiv.org/abs/2208.07367)).
