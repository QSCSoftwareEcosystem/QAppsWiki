---
type: concept
name: $⟦7,1,3⟧$ bare code
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
- https://errorcorrectionzoo.org/c/bare_7_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bare_7_1_3
---

# $⟦7,1,3⟧$ bare code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bare_7_1_3) (`code_id: bare_7_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦7,1,3⟧$ code that admits fault-tolerant syndrome extraction using only one ancilla per stabilizer generator measurement.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{ccccccc}
  X & I & I & I & Z & I & I \\
  I & X & I & I & Z & I & I \\
  I & I & X & I & I & Z & I \\
  I & I & I & X & I & I & Z \\
  I & I & Z & Z & I & Y & Y \\
  Z & Z & Z & I & X & X & Z
\end{array}~.
\end{align}
It is one of sixteen distinct indecomposable $⟦7,1,3⟧$ codes  ([arXiv:0709.1780](https://arxiv.org/abs/0709.1780)).

(source: raw/error-correction-zoo.md)

## Decoders

- Fault-tolerant syndrome extraction using a single ancilla  ([arXiv:1702.01155](https://arxiv.org/abs/1702.01155)).

## Relations

- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
