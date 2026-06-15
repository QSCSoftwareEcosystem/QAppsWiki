---
type: concept
name: Fiber code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/homogeneous-space-quantum
- concepts/qec/molecular
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fiber
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fiber
---

# Fiber code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fiber) (`code_id: fiber`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Approximate quantum code that encodes a qudit in an induced representation $\text{Ind}_G^{SO(3)} \Gamma$, induced by the irrep $\Gamma$ of a subgroup $G\subset SO(3)$. Such spaces correspond to orientation state spaces of certain symmetric molecules  ([arXiv:2403.04572](https://arxiv.org/abs/2403.04572)), with the base space $SO(3)/G$ labeling the orientations and the fiber carrying the $\Gamma$-irrep encoding the logical information.

(source: raw/error-correction-zoo.md)

## Protection

A basis of noise operators is developed for general induced representations in Ref.  ([arXiv:2403.04572](https://arxiv.org/abs/2403.04572)).

## Relations

- _parent_: [[concepts/qec/homogeneous-space-quantum]] — Fiber codes are defined on an induced representation $\text{Ind}_G^{SO(3)} \Gamma$, induced by the irrep $\Gamma$ of a subgroup $G\subset SO(3)$.
- _cousin_: [[concepts/qec/molecular]] — Molecular codes encode quantum information into superpositions of multiple orientations of an asymmetric molecule  ([arXiv:1911.00099](https://arxiv.org/abs/1911.00099)), while fiber codes encode into the fiber associated with a single orientation of certain symmetric molecules  ([arXiv:2403.04572](https://arxiv.org/abs/2403.04572)).
