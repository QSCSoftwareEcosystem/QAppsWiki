---
type: concept
name: Subsystem Galois-qudit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Gauge Galois-qudit stabilizer code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-stabilizer
- concepts/qec/quantum-mds
- concepts/qec/subsystem-galois-into-galois
- concepts/qec/subsystem-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_subsystem_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_subsystem_stabilizer
---

# Subsystem Galois-qudit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_subsystem_stabilizer) (`code_id: galois_subsystem_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Galois-qudit generalization of a subsystem qubit stabilizer code.
Can be obtained by taking a Galois-qudit stabilizer code and assigning some of its logical qudits to be gauge qudits.

(source: raw/error-correction-zoo.md)

## Protection

There are Gilbert-Varshamov-type lower bounds, linear-programming upper bounds, and pure-code Singleton and Hamming bounds for subsystem Galois-qudit stabilizer codes  ([arXiv:quant-ph/0610153](https://arxiv.org/abs/quant-ph/0610153), [arXiv:quant-ph/0703213](https://arxiv.org/abs/quant-ph/0703213)).
A subsystem Galois-qudit stabilizer code saturating the quantum Singleton bound must have a trivial gauge subsystem, i.e., there are no $⟦n,n-2d+2,r>0,d⟧_q$ codes  ([arXiv:quant-ph/0610153](https://arxiv.org/abs/quant-ph/0610153)).

## Relations

- _parent_: [[concepts/qec/subsystem-galois-into-galois]]
- _parent_: [[concepts/qec/subsystem-stabilizer]]
- _cousin_: [[concepts/qec/galois-stabilizer]] — Subsystem Galois-qudit stabilizer codes reduce to Galois-qudit stabilizer codes when there are no gauge qudits.
- _cousin_: [[concepts/qec/quantum-mds]] — A subsystem Galois-qudit stabilizer code saturating the quantum Singleton bound must have a trivial gauge subsystem, i.e., there are no $⟦n,n-2d+2,r>0,d⟧_q$ codes  ([arXiv:quant-ph/0610153](https://arxiv.org/abs/quant-ph/0610153)). More generally, all pure MDS subsystem stabilizer codes are derived from MDS stabilizer codes  ([arXiv:0712.4321](https://arxiv.org/abs/0712.4321)).
