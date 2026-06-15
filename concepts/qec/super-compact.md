---
type: concept
name: Super-compact fermion-to-qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Super-compact encoding
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-bosonization
- concepts/qec/derby-klassen
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/super_compact
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: super_compact
---

# Super-compact fermion-to-qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/super_compact) (`code_id: super_compact`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 2D fermion-into-qubit encoding on the square lattice obtained from exact 2D bosonization by a finite-depth generalized local unitary Clifford circuit, followed by re-pairing of Majorana modes and a slight lattice deformation.
The code uses $1.25$ qubits per fermion, improving on the square-lattice compact encoding with ratio $r=1.5$.
Its fermion-parity, hopping, and stabilizer operators have weights $1$-$2$, $2$-$6$, and $12$, respectively  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/2d-bosonization]] — The super-compact code is obtained from exact 2D bosonization by finite-depth generalized local unitaries  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).
- _cousin_: [[concepts/qec/derby-klassen]] — On the square lattice, the super-compact code is obtained by further transforming the $r=1.5$ compact/DK construction to a qubit-to-fermion ratio of $1.25$  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).
