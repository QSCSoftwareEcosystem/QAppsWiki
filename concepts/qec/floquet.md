---
type: concept
name: Hastings-Haah Floquet code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Periodic Floquet code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/da
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/floquet
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: floquet
---

# Hastings-Haah Floquet code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/floquet) (`code_id: floquet`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Dynamical code whose sequence of check-operator measurements is periodic.
The original Hastings-Haah construction introduced periodic measurement schedules that dynamically generate logical qubits even when the underlying subsystem code has fewer or no logical qubits  ([arXiv:2107.02194](https://arxiv.org/abs/2107.02194)).
Its basic examples are the 2D honeycomb Floquet code and the 1D ladder Floquet code.

(source: raw/error-correction-zoo.md)

## Protection

In the original Hastings-Haah examples, periodic measurements protect against single-qubit Pauli faults and measurement faults: the honeycomb Floquet code on a torus stores two logical qubits with distance proportional to linear size, while the ladder Floquet code is an error-detecting toy model  ([arXiv:2107.02194](https://arxiv.org/abs/2107.02194)). Spacetime errors for periodic Floquet codes have been studied in Ref.  ([arXiv:2510.05549](https://arxiv.org/abs/2510.05549)).

## Fault tolerance

- Periodic Floquet codes on tri-colorable lattices can be made fault-tolerant in the presence of dead qubits  ([arXiv:2307.03715](https://arxiv.org/abs/2307.03715), [arXiv:2405.15854](https://arxiv.org/abs/2405.15854)).

## Relations

- _parent_: [[concepts/qec/da]] — Periodic Floquet codes are dynamical codes with periodic measurement sequences.
