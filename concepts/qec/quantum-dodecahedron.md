---
type: concept
name: $⟦16,4,3⟧$ dodecahedral code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_dodecahedron
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_dodecahedron
---

# $⟦16,4,3⟧$ dodecahedral code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_dodecahedron) (`code_id: quantum_dodecahedron`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦16,4,3⟧$ non-CSS qubit stabilizer code whose encoder-respecting form is the graph of vertices of a dodecahedron  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).

A stabilizer tableau for the code, obtained from the graph-to-tableau map applied to the dodecahedral graph, is  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448))
\begin{align}
\begin{smallmatrix}
  I & Z & X & Z & I & I & I & I & Z & I & I & I & I & I & I & I \\
  I & I & Z & X & X & Z & I & I & I & Z & I & Z & I & I & I & I \\
  I & I & I & I & Z & X & X & Z & I & I & I & I & Z & I & Z & I \\
  Z & I & I & I & I & I & Z & X & I & I & I & I & I & I & I & Z \\
  X & Z & Z & I & I & I & I & Z & X & I & Z & I & I & I & I & I \\
  Z & X & Z & Z & I & I & I & I & I & X & I & Z & I & I & I & I \\
  I & I & Z & X & I & I & I & I & Z & Z & X & I & Z & I & I & I \\
  I & I & I & I & Z & I & I & I & I & Z & I & X & I & Z & I & I \\
  I & I & I & I & I & Z & I & I & I & I & Z & I & X & I & Z & I \\
  I & I & I & I & Z & X & I & I & I & I & I & Z & Z & X & I & Z \\
  X & Z & I & I & I & I & Z & Z & I & I & I & I & Z & I & X & I \\
  Z & X & Z & I & I & I & I & Z & I & I & I & I & I & Z & I & X
\end{smallmatrix}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

The code saturates the paper's graph degree upper bound on distance, attaining distance 3 on a degree-3 graph  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).

## Rate

The code has a rate of $1/4$, higher than that of the five-qubit perfect code.

## Encoders

- Encoding circuits of depth 5 are possible and optimal; a direct graph-based construction gives depth 6 before further optimization  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).

## Relations

- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [`dodecahedron`](https://errorcorrectionzoo.org/c/dodecahedron) — The encoder-respecting form of the $⟦16,4,3⟧$ dodecahedral code is the graph of vertices of a dodecahedron  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).
