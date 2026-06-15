---
type: concept
name: X-cube model code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-surface
- concepts/qec/double-semion
- concepts/qec/qldpc
- concepts/qec/qubit-css
- concepts/qec/qudit-xcube
- concepts/qec/string-net
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/xcube
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: xcube
---

# X-cube model code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/xcube) (`code_id: xcube`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A foliated type-I fracton CSS code on a cubic lattice with qubits on edges, cube stabilizers, and three cross-shaped vertex stabilizers for each vertex  ([arXiv:1603.04442](https://arxiv.org/abs/1603.04442)).
It supports a subextensive number of logical qubits.

In the generalized lattice-gauge-theory construction of Ref.  ([arXiv:1603.04442](https://arxiv.org/abs/1603.04442)), the X-cube model is the quantum dual of the 3D plaquette Ising model in a transverse field.
Its fundamental excitations include immobile fractons created at the corners of membrane operators and dimension-1 quasiparticles, i.e., lineons in later terminology, created at the ends of straight Wilson lines  ([arXiv:1603.04442](https://arxiv.org/abs/1603.04442)).
On an $L_x\times L_y\times L_z$ three-torus, the ground-state degeneracy is $2^{2L_x+2L_y+2L_z-3}$, reflecting the model's subextensive encoding rate  ([arXiv:1603.04442](https://arxiv.org/abs/1603.04442)).

Variants include several generalized X-cube models  ([arXiv:2402.16831](https://arxiv.org/abs/2402.16831)).
A non-stabilizer commuting-projector code constructed by stacking layers of the double-semion string-net model, called the semionic X-cube model  ([arXiv:1701.00747](https://arxiv.org/abs/1701.00747)), is equivalent to the X-cube model  ([arXiv:1806.08625](https://arxiv.org/abs/1806.08625)) (see also Refs.  ([arXiv:1904.01111](https://arxiv.org/abs/1904.01111), [arXiv:1903.11625](https://arxiv.org/abs/1903.11625))).

(source: raw/error-correction-zoo.md)

## Decoders

- Parallelized matching decoder  ([arXiv:1901.08061](https://arxiv.org/abs/1901.08061)).

## Code capacity threshold

- Independent $X,Z$ noise: minimum threshold $\approx 7.5\%$, higher than those reported for the 3D surface code and color code  ([arXiv:2112.05122](https://arxiv.org/abs/2112.05122)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/qudit-xcube]] — The qudit X-cube model code reduces to the X-cube model code for $q=2$. The X-cube model is a foliated type-I fracton code  ([arXiv:1803.10426](https://arxiv.org/abs/1803.10426), [arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).
- _cousin_: [`quantum_inspired`](https://errorcorrectionzoo.org/c/quantum_inspired) — According to Ref.  ([arXiv:2002.11738](https://arxiv.org/abs/2002.11738)), a classical analogue of the X-cube model is the eight-vertex model  ([doi:10.1063/1.1665111](https://doi.org/10.1063/1.1665111), [doi:10.1103/PhysRevLett.26.832](https://doi.org/10.1103/PhysRevLett.26.832), [doi:10.1016/0003-4916(72)90335-1](https://doi.org/10.1016/0003-4916(72)90335-1)).
- _cousin_: [[concepts/qec/double-semion]] — A non-stabilizer commuting-projector code constructed by stacking layers of the double-semion string-net model, called the semionic X-cube model  ([arXiv:1701.00747](https://arxiv.org/abs/1701.00747)), is equivalent to the X-cube model  ([arXiv:1806.08625](https://arxiv.org/abs/1806.08625)) (see also Refs.  ([arXiv:1904.01111](https://arxiv.org/abs/1904.01111), [arXiv:1903.11625](https://arxiv.org/abs/1903.11625))).
- _cousin_: [[concepts/qec/string-net]] — A non-stabilizer commuting-projector code constructed by stacking layers of the double-semion string-net model, called the semionic X-cube model  ([arXiv:1701.00747](https://arxiv.org/abs/1701.00747)), is equivalent to the X-cube model  ([arXiv:1806.08625](https://arxiv.org/abs/1806.08625)) (see also Refs.  ([arXiv:1904.01111](https://arxiv.org/abs/1904.01111), [arXiv:1903.11625](https://arxiv.org/abs/1903.11625))).
- _cousin_: [[concepts/qec/surface]] — The X-cube model can be constructed by coupling layers of the surface code  ([arXiv:1701.00747](https://arxiv.org/abs/1701.00747), [arXiv:2112.14717](https://arxiv.org/abs/2112.14717)).
- _cousin_: [[concepts/qec/3d-surface]] — The X-cube model admits a topological defect network construction out of 3D surface codes  ([arXiv:2002.05166](https://arxiv.org/abs/2002.05166)).
