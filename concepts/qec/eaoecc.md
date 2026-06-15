---
type: concept
name: Entanglement-assisted (EA) operator QECC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- EA subsystem QECC
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/oecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/eaoecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: eaoecc
---

# Entanglement-assisted (EA) operator QECC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/eaoecc) (`code_id: eaoecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Subsystem QECC whose encoding and decoding utilize pre-shared entanglement between sender and receiver.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [`eaoaecc`](https://errorcorrectionzoo.org/c/eaoaecc) — An EAOA QECC that has gauge structure (e.g., gauge qubits), that has no block structure that corresponds to a classical code, and that utilizes pre-shared entanglement is an EAOQECC.
- _cousin_: [[concepts/qec/oecc]] — EAOQECCs utilize additional ancillary subsystems in a pre-shared entangled state, but reduce to subsystem QECCs when said subsystems are interpreted as noiseless physical subsystems.
