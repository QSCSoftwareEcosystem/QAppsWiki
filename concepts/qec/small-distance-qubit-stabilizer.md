---
type: concept
name: Small-distance qubit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-stabilizer
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/small_distance_qubit_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: small_distance_qubit_stabilizer
---

# Small-distance qubit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/small_distance_qubit_stabilizer) (`code_id: small_distance_qubit_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit stabilizer code that either detects or corrects errors on at most two subsystems, i.e., has distance $\leq 5$.

Criteria for the existence of single error-correcting qubit stabilizer codes have been developed  ([arXiv:0901.1968](https://arxiv.org/abs/0901.1968)). Qubit stabilizer codes for $n < 10$ have been classified  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)), all of which have small distance. Qubit stabilizer codes have been partially enumerated up to twelve qubits  ([arXiv:2009.01244](https://arxiv.org/abs/2009.01244)).
Ref.  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)) enumerates all $2.71\times10^{10}$ inequivalent CSS codes with $n\leq14$.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]] — Criteria for the existence of single error-correcting qubit stabilizer codes have been developed  ([arXiv:0901.1968](https://arxiv.org/abs/0901.1968)). Qubit stabilizer codes for $n < 10$ have been classified  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)), all of which have small distance. Qubit stabilizer codes have been partially enumerated up to twelve qubits  ([arXiv:2009.01244](https://arxiv.org/abs/2009.01244)). There are two $⟦8,1,3⟧$ self-dual non-CSS codes; see QECDB .
- _parent_: [[concepts/qec/small-distance-quantum]]
