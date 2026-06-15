---
type: concept
name: 2D bosonization code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/bosonization
- concepts/qec/jw
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/2d_bosonization
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 2d_bosonization
---

# 2D bosonization code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/2d_bosonization) (`code_id: 2d_bosonization`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A mapping between a 2D lattice quadratic Hamiltonian of Majorana modes and a 2D lattice of qubits.
The original exact 2D bosonization code  ([arXiv:1711.00515](https://arxiv.org/abs/1711.00515)) is a stabilizer code whose generators are products of plaquettes and stars of the surface code, with gauge constraints that project onto a toric-code-like subspace with emergent fermions  ([arXiv:1711.00515](https://arxiv.org/abs/1711.00515), [arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).
Finite-depth generalized local unitary Clifford circuits generate a family of equivalent local encodings with qubit-to-fermion ratio $r = 1 + \frac{1}{2k}$ for any positive integer $k$; the square-lattice compact encoding with $r=1.5$ and the super-compact encoding with $r=1.25$ are explicit examples  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).

(source: raw/error-correction-zoo.md)

## Protection

The original code  ([arXiv:1711.00515](https://arxiv.org/abs/1711.00515)) can be converted via Clifford operations into codes whose distance runs up to $7$ while preserving the code rate  ([arXiv:2210.08411](https://arxiv.org/abs/2210.08411)).

## Encoders

- Tensor-network realization  ([arXiv:1909.10552](https://arxiv.org/abs/1909.10552)), extended to periodic boundary conditions and sectors of odd fermionic charge  ([arXiv:2404.07727](https://arxiv.org/abs/2404.07727)).

## Relations

- _parent_: [[concepts/qec/bosonization]]
- _parent_: [[concepts/qec/2d-stabilizer]] — The 2D bosonization code encodes fermionic modes into a 2D qubit stabilizer code.
- _cousin_: [[concepts/qec/jw]] — The exact 2D bosonization code can be converted by a linear-depth Clifford circuit into a Jordan-Wigner ordering path on the 2D lattice  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).
- _cousin_: [[concepts/qec/surface]] — The original 2D bosonization code  ([arXiv:1711.00515](https://arxiv.org/abs/1711.00515)) is a stabilizer code whose generators are products of plaquettes and stars of the surface code.
