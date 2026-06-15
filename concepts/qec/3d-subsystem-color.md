---
type: concept
name: 3D subsystem color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- 3D gauge color code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-color
- concepts/qec/3d-surface
- concepts/qec/rbh
- concepts/qec/single-shot
- concepts/qec/spt
- concepts/qec/subsystem-color
- concepts/qec/symmetry-protected-self-correct
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/3d_subsystem_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 3d_subsystem_color
---

# 3D subsystem color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/3d_subsystem_color) (`code_id: 3d_subsystem_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A subsystem version of the 3D color code defined on a 3-colex.

In the tetrahedral subsystem family introduced in  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)), qubits live on tetrahedra, boundary triangles, boundary edges, and boundary vertices of a colored tetrahedron, and the code encodes one logical qubit.
Gauge generators can be chosen to have weight four or six, while the corresponding stabilizer generators can be much larger.

(source: raw/error-correction-zoo.md)

## Transversal gates

- For the $(1,1)$ member, $CNOT$ and Hadamard are transversal; gauge fixing to the $(1,2)$ code enables a transversal $R_3$ gate, yielding a universal gate set without encoded ancillas  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).

## Fault tolerance

- In the tetrahedral subsystem family, syndrome extraction can use 4- or 6-qubit gauge checks instead of directly measuring larger stabilizers, and gauge fixing uses only local quantum operations plus classical processing  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).

## Threshold

- Phenomenological noise: $0.31\%$ under clustering decoder  ([arXiv:1503.08217](https://arxiv.org/abs/1503.08217)).

## Relations

- _parent_: [[concepts/qec/subsystem-color]]
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _cousin_: [[concepts/qec/3d-color]] — On a fixed 3D lattice, the 3D subsystem color code is gauge-related to the 3D color code; switching between the $(1,1)$ and $(1,2)$ members yields transversal $CNOT$, $H$, and $R_3$ gates  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).
- _cousin_: [[concepts/qec/single-shot]] — The 3D subsystem color code defined on the cube-truncated rhombic dodecahedral honeycomb, i.e., a tessellation of cubes and chamfered cubes (a.k.a. tetratruncated rhombic dodecahedra)  ([arXiv:1503.08217](https://arxiv.org/abs/1503.08217)), is a single-shot code  ([arXiv:1404.5504](https://arxiv.org/abs/1404.5504), [arXiv:1503.08217](https://arxiv.org/abs/1503.08217)).
- _cousin_: [[concepts/qec/symmetry-protected-self-correct]] — A particular gauge-fixed version of a subsystem code on a 3D lattice yields a self-correcting memory protected by one-form symmetries  ([arXiv:1805.01474](https://arxiv.org/abs/1805.01474)) ([arXiv:1805.01836](https://arxiv.org/abs/1805.01836)).
The symmetric energy barrier grows linearly with the length of a side of the lattice. When the system is coupled locally to a thermal bath respecting the symmetry and below a critical temperature, the memory time grows exponentially with the side length.
The subsystem color code is not a self-correcting quantum memory if symmetry protection is removed  ([arXiv:2305.06389](https://arxiv.org/abs/2305.06389)).
- _cousin_: [[concepts/qec/3d-surface]] — The 3D subsystem color code can be ungauged  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) to obtain six copies of $\mathbb{Z}_2$ gauge theory with one-form symmetries  ([arXiv:1805.01836](https://arxiv.org/abs/1805.01836)).
- _cousin_: [[concepts/qec/spt]] — Ungauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) different stabilizer Hamiltonians of the 3D subsystem color code yields distinct SPT phases; in particular, one ungauges to three decoupled copies of the RBH model  ([arXiv:1805.01836](https://arxiv.org/abs/1805.01836)).
- _cousin_: [[concepts/qec/rbh]] — Different stabilizer Hamiltonians of the 3D subsystem color code correspond to distinct SPT phases; one ungauges to three decoupled copies of the RBH model  ([arXiv:1805.01836](https://arxiv.org/abs/1805.01836)).
The RBH code for a certain boundary Hamiltonian is dual to the 3D subsystem color code  ([arXiv:1805.01474](https://arxiv.org/abs/1805.01474)).
