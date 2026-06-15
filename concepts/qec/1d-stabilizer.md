---
type: concept
name: 1D lattice stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-cyclic
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/1d_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 1d_stabilizer
---

# 1D lattice stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/1d_stabilizer) (`code_id: 1d_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Lattice stabilizer code in one Euclidean dimension, using either the ordinary block notion of locality or the fermionic/Majorana notion of locality.

Any modular-qudit code can be converted to several copies of the 1D repetition code along with some trivial codes via a local constant-depth Clifford circuit  ([arXiv:1607.01387](https://arxiv.org/abs/1607.01387)).
There is no 1D bosonic topological order at nonzero temperature  ([arXiv:1804.05457](https://arxiv.org/abs/1804.05457), [arXiv:2511.14699](https://arxiv.org/abs/2511.14699), [arXiv:2602.13386](https://arxiv.org/abs/2602.13386)).

(source: raw/error-correction-zoo.md)

## Fault tolerance

- A fault-tolerant quantum computation scheme on a 1D nearest-neighbor qubit line can be built from a modified tower of interleaved quantum Hamming codes. It achieves coding rate above $5\%$, constant space overhead, quasi-polylogarithmic time overhead, and a threshold  ([arXiv:2502.16132](https://arxiv.org/abs/2502.16132)).

## Relations

- _parent_: [[concepts/qec/translationally-invariant-stabilizer]]
- _cousin_: [[concepts/qec/quantum-cyclic]] — A 1D lattice stabilizer code with periodic boundary conditions is a quantum cyclic code.
