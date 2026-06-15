---
type: concept
name: Subsystem Galois-qudit CSS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Euclidean construction subsystem code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-css
- concepts/qec/galois-subsystem-stabilizer
- concepts/qec/subsystem-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_subsystem_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_subsystem_css
---

# Subsystem Galois-qudit CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_subsystem_css) (`code_id: galois_subsystem_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Galois-qudit subsystem stabilizer code which admits a set of gauge-group generators which consist of either all-$Z$ or all-$X$ Galois-qudit Pauli strings.

These codes can be constructed from classical codes via a subsystem generalization of the CSS construction or the Hermitian construction  ([arXiv:quant-ph/0604161](https://arxiv.org/abs/quant-ph/0604161), [arXiv:quant-ph/0610153](https://arxiv.org/abs/quant-ph/0610153)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/galois-subsystem-stabilizer]]
- _parent_: [[concepts/qec/subsystem-css]]
- _cousin_: [[concepts/qec/galois-css]] — Subsystem Galois-qudit CSS codes reduce to (subspace) Galois-qudit CSS codes when there is no gauge subsystem.
