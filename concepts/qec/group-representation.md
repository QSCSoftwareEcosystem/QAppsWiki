---
type: concept
name: Group-representation code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/covariant
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/group_representation
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: group_representation
---

# Group-representation code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/group_representation) (`code_id: group_representation`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose projector is onto an irreducible representation of a subgroup $G$ of a group of canonical or distinguished unitary operations, e.g., transversal gates in the case of block quantum codes, Gaussian operations in the case of bosonic codes, or $SU(2)$ operations in the case of single-spin codes.

(source: raw/error-correction-zoo.md)

## Protection

Error correction ability is not guaranteed, but can be sought in the multiplicity space of the irrep in case there is more than one copy present.

## Encoders

- General encoding map  ([arXiv:2306.11621](https://arxiv.org/abs/2306.11621)).

## General gates

- By definition, a group $G$ of gates can be realized on the code using the unitary operations used to define the code.

## Relations

- _parent_: [[concepts/qec/covariant]] — Group-representation code projections are onto a single irrep of a subgroup of canonical or distinguished unitary operations on a Hilbert space. This makes them covariant w.r.t. that subgroup. More general covariant codes need not be projections onto a single irrep. Removing the restriction to distinguished operations and allowing all operations, every code projection on an $N$-dim Hilbert space can be expressed as a projection onto the irrep formed by the code-preserving subgroup of $U(N)$. The same idea holds when $N$ is taken to infinity. In other words, while all codes are covariant w.r.t. some group, group-representation codes are covariant w.r.t. a canonical or distinguished subgroup.
- _cousin_: [[concepts/qec/small-distance-quantum]] — See Ref.  ([arXiv:2403.08999](https://arxiv.org/abs/2403.08999)) for tables of distance-two codes with various families of transversal gates.
