---
type: concept
name: Qutrit-Pauli tessellation code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-representation
- concepts/qec/multimodegkp
- concepts/qec/oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qutrit_pauli_gkp_subcode
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qutrit_pauli_gkp_subcode
---

# Qutrit-Pauli tessellation code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qutrit_pauli_gkp_subcode) (`code_id: qutrit_pauli_gkp_subcode`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Euclidean-plane tessellation code whose projection is onto a copy of an irreducible representation of the single-qutrit Pauli group, realized by the $\{3,3,3\}$ tessellation  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).
The code is a subcode of a two-mode GKP code and has GKP-like stabilizers. Logical $X$, $Z$, and $(ZX)^{-1}$ are implemented by $2\pi/3$ rotations around tessellation vertices, while only a GKP-like logical $Z$ is available via real-space displacement.

(source: raw/error-correction-zoo.md)

## Protection

The code corrects translation errors of Euclidean norm less than $\sqrt{3}/2$.
It also corrects momentum errors in any direction with $|\vec{k}| < 2\pi/9$  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).

## Relations

- _parent_: [[concepts/qec/oscillators]]
- _parent_: [[concepts/qec/group-representation]] — The qutrit-Pauli tessellation code is a group-representation code with $G$ being the single-qutrit Pauli group.
- _cousin_: [[concepts/qec/multimodegkp]] — The qutrit-Pauli tessellation code is a subcode of a two-mode GKP code with GKP-like stabilizers  ([arXiv:2410.18713](https://arxiv.org/abs/2410.18713)).
