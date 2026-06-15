---
type: concept
name: Rotor cluster-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/graph-quantum
- concepts/qec/rotor-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rotor_cluster
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rotor_cluster
---

# Rotor cluster-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rotor_cluster) (`code_id: rotor_cluster`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Rotor analogue of the qubit and analog cluster-state codes.
The exact rotor cluster state is non-normalizable, so approximate constructions have to be considered.
Defined from a real-valued weighted adjacency matrix of a graph  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/rotor-stabilizer]] — Rotor cluster-state codes are particular rotor stabilizer codes.
- _parent_: [[concepts/qec/graph-quantum]] — Graph quantum codes for $G=\mathbb{Z}$ reduce to rotor cluster-state codes.
- _cousin_: [[concepts/qec/ame]] — Rotor AME cluster states exist for any number of modes  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).
