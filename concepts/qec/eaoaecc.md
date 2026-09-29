---
type: concept
name: Entanglement-assisted operator-algebra QECC (EAOA QECC)
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/oaecc
- concepts/qec/quantum-into-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/eaoaecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: eaoaecc
---

# Entanglement-assisted operator-algebra QECC (EAOA QECC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/eaoaecc) (`code_id: eaoaecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code family that encompasses ordinary (i.e., subspace) codes, subsystem codes, classical-quantum codes, hybrid codes, and their entanglement-assisted counterparts using an operator-algebraic framework.
In the EAOAQEC framework, the original EAQEC, EAOQEC, and EACQ formalisms appear as special cases, and the operator-algebra perspective also yields EA hybrid subspace and EA subsystem codes beyond those earlier settings  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).

(source: raw/error-correction-zoo.md)

## Protection

For Pauli noise with noiseless receiver ebits, the EAOAQEC framework gives a unified error-correction criterion and an associated distance notion that specialize to the corresponding conditions for EAQEC, EAOQEC, and EACQ codes  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).

## Relations

- _parent_: [[concepts/qec/quantum-into-quantum]]
- _cousin_: [[concepts/qec/oaecc]] — EAOA QECCs use pre-shared entangled ancillary subsystems, while OAQECCs recover the same operator-algebraic structures when those ancillary subsystems are instead treated as noiseless physical subsystems.
