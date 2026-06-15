---
type: concept
name: Quantum pin code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-k-orthogonal
- concepts/qec/quantum-rainbow
- concepts/qec/qubit-generalized-homological-product-css
- concepts/qec/subsystem-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_pin
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_pin
---

# Quantum pin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_pin) (`code_id: quantum_pin`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of CSS codes that encompasses both quantum RM and color codes and that is defined using intersections of pinned sets.

(source: raw/error-correction-zoo.md)

## Magic scaling exponent

A family of punctured pin codes admits $\gamma \approx 1.6$  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).

## Relations

- _parent_: [[concepts/qec/quantum-rainbow]] — Quantum pin codes are a special case of quantum rainbow codes  ([arXiv:2408.13130](https://arxiv.org/abs/2408.13130)).
- _parent_: [[concepts/qec/quantum-k-orthogonal]] — Quantum pin codes are $\ell$-orthogonal, i.e., the overlap between any $\ell$ stabilizers is even  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).
- _cousin_: [[concepts/qec/subsystem-color]] — Quantum pin codes have a subsystem version that can be viewed as a generalization of subsystem color codes  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).
- _cousin_: [[concepts/qec/qubit-generalized-homological-product-css]] — One can construct quantum pin codes from any chain complex  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).
