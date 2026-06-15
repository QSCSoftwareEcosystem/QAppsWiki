---
type: concept
name: Quantum Gabidulin code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-true-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_gabidulin
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_gabidulin
---

# Quantum Gabidulin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_gabidulin) (`code_id: quantum_gabidulin`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A Galois-qudit stabilizer code over $n$ Galois qudits of dimension $q = 2^n $ that is useful in protecting against faults in qubit Clifford circuits acting on stacked quantum memories.
This code can be treated as a code on an $n\times n$ qubit stacked memory by decomposing each Galois qudit into a Kronecker product of $n$ qubits; see  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)) ([arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)) ([arXiv:2408.10140](https://arxiv.org/abs/2408.10140), [arXiv:2408.09254](https://arxiv.org/abs/2408.09254)).

A quantum Gabidulin code is defined using two Gabidulin codes with associated parameters $r,s$, respectively, such that $r+s = n$  ([arXiv:2411.09173](https://arxiv.org/abs/2411.09173)).

(source: raw/error-correction-zoo.md)

## Protection

The code distance is the minimum rank distance --- the rank of the field element of the lowest-rank undetectable Galois-qudit Pauli error, with the rank calculated by writing the element as an $n\times n$ binary matrix.
The code is useful in protecting against faults in $n$-qubit Clifford circuits with $n$ layers, which preserve the minimum rank distance.

## Relations

- _parent_: [[concepts/qec/galois-true-stabilizer]]
- _cousin_: [`gabidulin`](https://errorcorrectionzoo.org/c/gabidulin) — A quantum Gabidulin code is defined using two Gabidulin codes with associated parameters $r,s$, respectively, such that $r+s = n$  ([arXiv:2411.09173](https://arxiv.org/abs/2411.09173)).
- _cousin_: [`rank_metric`](https://errorcorrectionzoo.org/c/rank_metric) — Quantum Gabidulin code and (classical) rank-metric code distances are based on ranks of the matrix representations of their corresponding errors.
