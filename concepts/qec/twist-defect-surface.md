---
type: concept
name: Twist-defect surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Surface code with a twist
- Genon surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/qldpc
- concepts/qec/qudit-surface
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/twist_defect_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: twist_defect_surface
---

# Twist-defect surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/twist_defect_surface) (`code_id: twist_defect_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A non-CSS extension of the 2D surface-code construction whose non-CSS stabilizer generators are associated with twist defects of the associated lattice.
A related construction  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)) doubles the number of qubits in the lattice via symplectic doubling.

For lattices with dislocations and rotational disclinations, twist-defect stabilizer generators are placed at the location of the dislocations to yield a stabilizer code whose logical dimension depends on the defects.
Logical dimension is determined by the genus of the underlying surface (for closed surfaces), types of boundaries (for open surfaces), and any twist defects present.

A simple example is a surface code on a lattice with a single lattice dislocation which hosts a weight-five non-CSS twist-defect stabilizer generator  ([arXiv:1004.1838](https://arxiv.org/abs/1004.1838)).
More generally, given a graph embedded in a 2D manifold, qubits are placed on vertices, stabilizers on faces, and twist defects are associated to odd-degree vertices.

(source: raw/error-correction-zoo.md)

## Protection

Code properties depend on the number and size of the twist defects.

## Rate

Twist-defect surface codes have negative curvature around their defects, and thus circumvent the BPT bound for codes on Euclidean lattices.

## General gates

- Clifford gates can be implemented via twist-based lattice surgery  ([arXiv:2201.05678](https://arxiv.org/abs/2201.05678)) or braiding twist defects
 ([arXiv:0704.2540](https://arxiv.org/abs/0704.2540), [arXiv:1004.1838](https://arxiv.org/abs/1004.1838), [arXiv:1104.5047](https://arxiv.org/abs/1104.5047), [arXiv:1208.0928](https://arxiv.org/abs/1208.0928), [arXiv:1508.04166](https://arxiv.org/abs/1508.04166), [arXiv:1609.04673](https://arxiv.org/abs/1609.04673), [arXiv:2103.08381](https://arxiv.org/abs/2103.08381)).
- State injection protocols yield arbitrary logical rotations  ([arXiv:1408.3379](https://arxiv.org/abs/1408.3379)).
- Symplectic doubles of codes yield fault-tolerant Clifford gates performed via Dehn twists  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).

## Fault tolerance

- Fault-tolerant measurement of defects  ([arXiv:1408.3379](https://arxiv.org/abs/1408.3379)).
- Twisted double covers of codes yield fault-tolerant Clifford gates performed via Dehn twists  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).

## Realizations

- Ground state of the toric code has been implemented with and without twists, and the non-Abelian braiding behavior of the twists, which realize Ising anyons, has been demonstrated  ([arXiv:2211.09802](https://arxiv.org/abs/2211.09802)).
- Logical Clifford gates arising from a $⟦4,1,2⟧$ twist-defect surface-code protocol, together with lifted gates on its $⟦8,2,2⟧$ and $⟦10,2,3⟧$ double covers, were realized on a trapped-ion device by Quantinuum  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/2d-stabilizer]]
- _cousin_: [[concepts/qec/topological-abelian]] — Twist-defect surface codes realize $\mathbb{Z}_2$ topological order with twist defects.
- _cousin_: [[concepts/qec/qudit-surface]] — Twist-defect surface codes have been extended to prime-dimensional qudits  ([doi:10.1103/PhysRevA.102.042616](https://doi.org/10.1103/PhysRevA.102.042616)).
