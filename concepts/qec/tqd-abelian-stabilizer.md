---
type: concept
name: Abelian TQD stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/qudit-stabilizer
- concepts/qec/spt
- concepts/qec/topological-abelian
- concepts/qec/tqd-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tqd_abelian_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tqd_abelian_stabilizer
---

# Abelian TQD stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tqd_abelian_stabilizer) (`code_id: tqd_abelian_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit stabilizer code whose codewords realize a 2D Abelian twisted-quantum-double topological order on composite-dimensional qudits.
For every finite Abelian group $G=\prod_i \mathbb{Z}_{N_i}$ and every product of Type-I and Type-II cocycles, there is a Pauli stabilizer Hamiltonian realizing the corresponding Abelian TQD  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).
Equivalently, these codes exhaust the 2D Abelian topological orders that admit gapped boundaries  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394), [arXiv:2107.13091](https://arxiv.org/abs/2107.13091)).

(source: raw/error-correction-zoo.md)

## Rate

On a torus, the ground-state Hilbert-space dimension is $|G|^2$ for underlying group $G=\prod_i \mathbb{Z}_{N_i}$  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).

## Relations

- _parent_: [[concepts/qec/qudit-stabilizer]]
- _parent_: [[concepts/qec/2d-stabilizer]] — For every finite Abelian group $G=\prod_i \mathbb{Z}_{N_i}$ and every product of Type-I and Type-II cocycles, there is a 2D modular-qudit Pauli stabilizer Hamiltonian on composite-dimensional qudits realizing the corresponding Abelian TQD  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).
- _parent_: [[concepts/qec/tqd-abelian]] — Every Abelian TQD code with Type-I and -II cocycles can be realized as a modular-qudit Pauli stabilizer code by starting from a stack of Abelian quantum double models (it suffices to take $\prod_i \mathbb{Z}_{N_i^2}$ toric codes) and condensing certain bosonic anyons  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).
- _parent_: [[concepts/qec/topological-abelian]] — Every Abelian TQD code with Type-I and -II cocycles can be realized as a modular-qudit Pauli stabilizer code by starting from a stack of Abelian quantum double models (it suffices to take $\prod_i \mathbb{Z}_{N_i^2}$ toric codes) and condensing certain bosonic anyons  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).
- _cousin_: [[concepts/qec/spt]] — Gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) the $1$-form symmetries associated with gauge charges of Abelian TQD stabilizer codes yields Pauli stabilizer models of SPT phases classified by products of Type-I and Type-II cocycles  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).
