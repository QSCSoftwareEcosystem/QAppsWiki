---
type: concept
name: Homogeneous-space quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Coset-space quantum code
- $G/H$ quantum code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/homogeneous_space_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: homogeneous_space_quantum
---

# Homogeneous-space quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/homogeneous_space_quantum) (`code_id: homogeneous_space_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes a *logical* Hilbert space, finite- or infinite-dimensional, into a *physical* Hilbert space of $L^2$-normalizable functions on a homogeneous space $G/H$ or, more generally, induced representations whose base space is $G/H$  ([doi:10.2307/1969423](https://doi.org/10.2307/1969423), [doi:10.1016/B978-1-4832-3188-4.50009-0](https://doi.org/10.1016/B978-1-4832-3188-4.50009-0), [doi:10.1016/0550-3213(91)90609-2](https://doi.org/10.1016/0550-3213(91)90609-2), [arXiv:1304.3366](https://arxiv.org/abs/1304.3366)). Here, $G$ is a second-countable unimodular group, and $H$ is a closed subgroup of $G$.

(source: raw/error-correction-zoo.md)

## Protection

Quantum weight enumerators, linear programming bounds, and Rains shadow enumerators have been extended to quantum codes defined on multiplicity-free two-point homogeneous spaces  ([arXiv:2502.14165](https://arxiv.org/abs/2502.14165)).
In this multiplicity-free setting (the analogue of a Gelfand-pair decomposition), irreducible-representation labels entirely parameterize the Fourier basis useful for these bounds.

## Relations

- _parent_: [[concepts/qec/qecc]]
- _cousin_: [`homogeneous_space_classical`](https://errorcorrectionzoo.org/c/homogeneous_space_classical) — Homogeneous-space quantum codes are quantum counterparts of homogeneous-space codes.
