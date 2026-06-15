---
type: concept
name: Group-based cluster-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-quantum
- concepts/qec/hopf-cluster-state
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/group_cluster_state
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: group_cluster_state
---

# Group-based cluster-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/group_cluster_state) (`code_id: group_cluster_state`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code based on a group-based cluster state for a group $G$  ([arXiv:1408.6237](https://arxiv.org/abs/1408.6237)).
Such cluster states can be defined using a graph and conditional group multiplication operations.
A group-based cluster state for $G=\mathbb{F}_q$ for prime-power $q$ is called a *Galois-qudit cluster state*, while the state for $G=\mathbb{Z}_q$ for positive $q$ is called a modular-qudit cluster state.

(source: raw/error-correction-zoo.md)

## General gates

- 1D group-based cluster states for certain non-Abelian groups  ([arXiv:2312.09272](https://arxiv.org/abs/2312.09272)) are resources for universal MBQC.

## Relations

- _parent_: [[concepts/qec/group-quantum]] — Group-based cluster states are stabilized by group-based right- and left-multiplication error operators  ([arXiv:1408.6237](https://arxiv.org/abs/1408.6237), [arXiv:2312.09272](https://arxiv.org/abs/2312.09272)).
- _cousin_: [[concepts/qec/hopf-cluster-state]] — Hopf-algebra cluster-state codes reduce to group-based cluster-state codes for finite groups when the Hopf algebra reduces to a finite group.
