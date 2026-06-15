---
type: concept
name: Subsystem Galois-qudit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Gauge Galois-qudit code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-into-galois
- concepts/qec/subsystem-group-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_galois_into_galois
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_galois_into_galois
---

# Subsystem Galois-qudit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_galois_into_galois) (`code_id: subsystem_galois_into_galois`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Subsystem QECC encoding into a $q^n$-dimensional Hilbert space consisting of $n$ Galois qudits.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/subsystem-group-quantum]] — A Galois qudit for $q=p^m$ can be decomposed into a Kronecker product of $m$ modular qudits  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)); see  ([arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)).
Interpreted this way, subsystem Galois-qudit codes are subsystem group quantum codes whose physical spaces are constructed using Galois fields $\mathbb{F}_q$ as groups. More general versions of such qudits can be valued in a Galois ring  ([arXiv:2501.18968](https://arxiv.org/abs/2501.18968)), over which there also exists a Fourier transform  ([arXiv:0904.2560](https://arxiv.org/abs/0904.2560)).
- _cousin_: [[concepts/qec/galois-into-galois]] — Subsystem Galois-qudit codes reduce to (subspace) Galois-qudit codes when there is no gauge subsystem.
