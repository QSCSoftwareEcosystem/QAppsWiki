---
type: concept
name: Capped color code (CCC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/subsystem-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/capped_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: capped_color
---

# Capped color code (CCC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/capped_color) (`code_id: capped_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A non-geometrically local subsystem color code consisting of two layers of 2D color code stacked together and topped (or capped) by a single qubit.
Gauge fixing yields two types of codes, capped color codes in H or T form.
Layers of 2D color codes can also be stacked together in a recursive construction, yielding *recursive capped color codes* (RCCCs).

(source: raw/error-correction-zoo.md)

## Transversal gates

- Capped color codes in H (T) form admit a transversal Hadamard (T) gate.

## Fault tolerance

- Fault-tolerant syndrome extraction and error correction for capped color codes in H form  ([arXiv:2106.02649](https://arxiv.org/abs/2106.02649)).
- Fault-tolerant T gate implementation  ([arXiv:2106.02649](https://arxiv.org/abs/2106.02649)).

## Relations

- _parent_: [[concepts/qec/subsystem-color]]
