---
type: concept
name: Truncated trihexagonal (4.6.12) color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/4612_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 4612_color
---

# Truncated trihexagonal (4.6.12) color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/4612_color) (`code_id: 4612_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

2D color code defined on a (typically triangular) patch of the 4.6.12 (truncated trihexagonal or square-hexagon-dodecagon) tiling.

Stabilizer generators are shown in \ref{figure:4.6.12-operators}.

(source: raw/error-correction-zoo.md)

## Protection

For triangular patches, there is a $⟦(3d^2+5)/2-3d, 1, d⟧$ code family  ([arXiv:1108.5738](https://arxiv.org/abs/1108.5738)).

## Transversal gates

- CNOT gate because the code is CSS.
- Hadamard gates for any qubit geometry which yields a self-dual CSS code.

## Relations

- _parent_: [[concepts/qec/2d-color]]
- _cousin_: [`honeycomb`](https://errorcorrectionzoo.org/c/honeycomb) — The 4.6.12 (truncated trihexagonal or square-hexagon-dodecagon) tiling is obtained by applying a fattening procedure to the honeycomb tiling  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).
