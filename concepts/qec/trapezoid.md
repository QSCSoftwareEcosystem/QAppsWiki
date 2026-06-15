---
type: concept
name: Trapezoid subsystem code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bravyi-bacon-shor
- concepts/qec/goy
- concepts/qec/iceberg
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/trapezoid
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: trapezoid
---

# Trapezoid subsystem code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/trapezoid) (`code_id: trapezoid`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of a family of BBS codes with weight-two (two-body) gauge generators designed to suppress errors in adiabatic quantum computation.

The family consists of odd-$m$ codes with $m=2k+1$ and parameters $⟦4k+2l,2k,2k+2l-2,2⟧$, together with even-$m$ codes with $m=2k$ and parameters $⟦4k+2l-2,2k-1,2k+2l-3,2⟧$, where $1 \leq l \leq k$  ([arXiv:2412.06744](https://arxiv.org/abs/2412.06744)).

(source: raw/error-correction-zoo.md)

## Protection

These are distance-two subsystem codes, so they detect arbitrary single-qubit errors. In the energy-penalty setting of Hamiltonian quantum computation, the $l=1$ subfamily maximizes the code rate and has the largest penalty gap within the trapezoid family  ([arXiv:2412.06744](https://arxiv.org/abs/2412.06744)).

## General gates

- Single-qubit dressed logical operators are two-local, and products of two dressed logical operators of the same Pauli type can also be implemented using two-local physical interactions up to gauge operators  ([arXiv:1911.01354](https://arxiv.org/abs/1911.01354), [arXiv:2412.06744](https://arxiv.org/abs/2412.06744)).

## Relations

- _parent_: [[concepts/qec/bravyi-bacon-shor]]
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _cousin_: [[concepts/qec/iceberg]] — The trapezoid code family can be obtained from the $⟦2m,2m-2,2⟧$ error-detecting code by using some logical qubits as gauge qubits and imposing a two-dimensional qubit geometry  ([arXiv:2412.06744](https://arxiv.org/abs/2412.06744)).
- _cousin_: [[concepts/qec/goy]] — The odd-$m$ trapezoid family at $l=k$ has parameters $⟦6k,2k,4k,2⟧$ and reproduces the two-local subsystem construction used for universal Hamiltonian quantum computation in  ([arXiv:1911.01354](https://arxiv.org/abs/1911.01354)); this is a subsystem analogue of the $⟦6k,2k,2⟧$ Ganti-Onunkwo-Young family.
- _cousin_: [[concepts/qec/small-distance-qubit-stabilizer]]
