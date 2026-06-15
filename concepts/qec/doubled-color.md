---
type: concept
name: Doubled color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-subsystem-color
- concepts/qec/quantum-divisible
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/doubled_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: doubled_color
---

# Doubled color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/doubled_color) (`code_id: doubled_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Family of $⟦2t^3+8t^2+6t-1,1,2t+1⟧$ subsystem color codes (with $t\geq 1$), constructed using a generalization of the doubling transformation  ([arXiv:1012.4134](https://arxiv.org/abs/1012.4134)), that admit a Clifford + $T$ transversal gate set using gauge fixing.

The family is embedded into a 2D honeycomb lattice with two qubits per site; the $C$-code has spatially local face-supported gauge generators, and the $T$-code is reached by local gauge fixing using edge-supported stabilizer measurements  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- Doubled color codes are triply even, so they yield a transversal $T$ gate  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)). Using gauge fixing, the codes admit a Clifford + $T$ transversal gate set.

## Decoders

- ML decoder that can utilize a history of syndromes, based on the Walsh-Hadamard transform  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)).

## Relations

- _parent_: [[concepts/qec/2d-subsystem-color]]
- _cousin_: [[concepts/qec/quantum-divisible]] — Doubled color codes are subsystem codes constructed using a generalization of the doubling transformation  ([arXiv:1012.4134](https://arxiv.org/abs/1012.4134)) that combines doubly even linear binary codes to make triply even codes.
The doubling transformation is a special case of level lifting (from two to three)  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
