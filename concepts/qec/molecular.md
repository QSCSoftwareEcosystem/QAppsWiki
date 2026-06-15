---
type: concept
name: Molecular code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-gkp
- concepts/qec/single-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/molecular
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: molecular
---

# Molecular code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/molecular) (`code_id: molecular`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Approximate quantum code that encodes a finite-dimensional logical space into the Hilbert space of $L^2$-normalizable functions on $SO(3)$, i.e., rotational states of an asymmetric rigid body such as a polyatomic molecule.

Construction is based on nested finite subgroups $H\subset K \subset SO(3)$.
The $|K|/|H|$-dimensional logical subspace is spanned by basis states that are uniform superpositions of elements of cosets of $H$ in $K$.
Examples discussed in the original work include cyclic, dihedral, tetrahedral-octahedral, and tetrahedral-icosahedral subgroup embeddings.

(source: raw/error-correction-zoo.md)

## Protection

Protects against generalized bit-flip errors $g\in SO(3)$ that are inside the fundamental domain of $SO(3)/K$.
In the cyclic $Z_N\subset Z_{dN}$ family, the code corrects sufficiently small rigid-body rotations about any axis and angular-momentum kicks with $\delta\ell<N/2$.
Protection against phase-flip and more general momentum-kick errors is determined by the branching rules of irreps of $SO(3)$ into those of $K$, and further into those of $H$.

## Relations

- _parent_: [[concepts/qec/group-gkp]]
- _parent_: [[concepts/qec/single-subsystem]]

## Notes

- Physical space characterizes orientations of a rigid body in 3D, which correspond to rotational states of an asymmetric molecule. See APS Physics Synopsis  ([doi:10.1103/Physics.13.s111](https://doi.org/10.1103/Physics.13.s111)) and [Physical Review Journal club](https://www.youtube.com/watch?v=gjBbMMZ3L1k) discussing molecular applications.
- Each ideal molecular code has a parent Hamiltonian whose ground space is the codespace, and normalizable approximate codewords can be obtained by damping in total angular momentum.
