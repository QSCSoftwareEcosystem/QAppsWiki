---
type: concept
name: QLDPC subsystem code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Sparse subsystem code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/general-qldpc
- concepts/qec/qldpc
- concepts/qec/subsystem-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/sparse_subsystem
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: sparse_subsystem
---

# QLDPC subsystem code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/sparse_subsystem) (`code_id: sparse_subsystem`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of subsystem stabilizer codes for which the number of sites participating in each gauge generator and the number of gauge generators that each site participates in are both bounded by a constant as $n\to\infty$.
The stabilizer group may contain generators of unbounded weight, distinguishing these codes from stabilizer codes with bounded-weight generators for which some logical qubits were re-assigned to be gauge qubits.

(source: raw/error-correction-zoo.md)

## Rate

There exists a family of QLDPC subsystem codes with $d = n^{1-\epsilon}$, where $\epsilon = O(1/\sqrt{\log n})$  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334)).
Spatially local subsystem codes also exist in $D\geq 2$ dimensions with $d = n^{1-\epsilon-1/D}$, where $\epsilon = O(1/\sqrt{\log n})$, nearly saturating the subsystem BT bound  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334)).

## Relations

- _parent_: [[concepts/qec/subsystem-stabilizer]]
- _cousin_: [[concepts/qec/general-qldpc]] — QLDPC subsystem codes reduce to QLDPC codes when there are no gauge degrees of freedom.
- _cousin_: [[concepts/qec/qldpc]] — Any qubit QLDPC code with stabilizer-generator weights $w_i$ can be mapped constructively to a sparse subsystem qubit code with the same number of logical qubits and distance, using $n=O(\sum_i w_i)$ physical qubits and constant-weight gauge generators  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334)).
