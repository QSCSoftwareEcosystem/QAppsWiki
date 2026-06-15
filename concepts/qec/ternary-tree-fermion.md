---
type: concept
name: Ternary-tree fermion-into-qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fermions-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ternary_tree_fermion
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ternary_tree_fermion
---

# Ternary-tree fermion-into-qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ternary_tree_fermion) (`code_id: ternary_tree_fermion`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A fermion-into-qubit encoding defined on ternary trees that maps Majorana operators into Pauli strings of weight $\lceil \log_3 (2n+1) \rceil$.

(source: raw/error-correction-zoo.md)

## General gates

- Fermion permutations on $N$ modes can be done with a circuit of depth order $O(\log^2 N)$  ([arXiv:2510.05099](https://arxiv.org/abs/2510.05099)).

## Relations

- _parent_: [[concepts/qec/fermions-into-qubits]]
