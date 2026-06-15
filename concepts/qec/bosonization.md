---
type: concept
name: Bosonization code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fermions-into-qubits
- concepts/qec/fibonacci-fractal-liquid
- concepts/qec/haah-cubic
- concepts/qec/qldpc
- concepts/qec/translationally-invariant-stabilizer
- concepts/qec/xcube
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bosonization
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bosonization
---

# Bosonization code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bosonization) (`code_id: bosonization`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A mapping that maps a $D$-dimensional lattice quadratic Hamiltonian of Majorana modes into a lattice of qubits.
The resulting qubit code can realize various topological phases, depending on the initial Majorana-mode Hamiltonian and its symmetries.

A general mapping for quadratic Hamiltonians was constructed in Ref.  ([arXiv:1911.00017](https://arxiv.org/abs/1911.00017)), while others considered higher-order products of Majorana modes that correspond to symmetry constraints  ([arXiv:2002.12026](https://arxiv.org/abs/2002.12026), [arXiv:2002.11345](https://arxiv.org/abs/2002.11345)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/fermions-into-qubits]]
- _parent_: [[concepts/qec/qldpc]] — The $D$-dimensional bosonization code encodes fermionic modes into a $D$-dimensional qubit stabilizer code.
- _parent_: [[concepts/qec/translationally-invariant-stabilizer]] — The $D$-dimensional bosonization code encodes fermionic modes into a $D$-dimensional qubit stabilizer code.
- _cousin_: [[concepts/qec/haah-cubic]] — Bosonization can be used to realize a Haah cubic code with an emergent fermion from a Majorana stabilizer code  ([arXiv:2002.11345](https://arxiv.org/abs/2002.11345)). This code is shown to be distinct from the original code  ([arXiv:2304.00028](https://arxiv.org/abs/2304.00028)).
- _cousin_: [[concepts/qec/fibonacci-fractal-liquid]] — Bosonization can be used to realize a Fibonacci fractal spin-liquid code with an emergent fermion from a Majorana stabilizer code  ([arXiv:2002.11345](https://arxiv.org/abs/2002.11345)). This code is shown to be distinct from the original code  ([arXiv:2304.00028](https://arxiv.org/abs/2304.00028)).
- _cousin_: [[concepts/qec/xcube]] — Bosonization can be used to realize an X-cube model code with an emergent fermion from a Majorana stabilizer code  ([arXiv:2002.11345](https://arxiv.org/abs/2002.11345)), but this model has the same stabilizer group as the original X-cube model  ([arXiv:2002.12026](https://arxiv.org/abs/2002.12026)).
