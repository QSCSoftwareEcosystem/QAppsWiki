---
type: concept
name: $⟦8,2,3⟧$ Hermitian code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-concatenated
- concepts/qec/self-dual-css
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-4-2-2
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_8_2_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_8_2_3
---

# $⟦8,2,3⟧$ Hermitian code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_8_2_3) (`code_id: stab_8_2_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A non-CSS Hermitian eight-qubit stabilizer code that is the only Hermitian code and that has the largest automorphism group among the 20 inequivalent $⟦8,2,3⟧$ codes  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
The code has an exceptionally short fault-tolerant syndrome measurement sequence  ([arXiv:2008.05051](https://arxiv.org/abs/2008.05051), [arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).

A stabilizer tableau for the code is  ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344))
\begin{align}
\begin{array}{cccccccc}
  X & X & X & X & I & I & I & I \\
  Z & Z & Z & Z & I & I & I & I \\
  I & I & I & I & X & X & X & X \\
  I & I & I & I & Z & Z & Z & Z \\
  I & X & Y & Z & I & X & Y & Z \\
  I & Z & X & Y & I & Z & X & Y
\end{array}~,
\end{align}
which is equivalent to .

(source: raw/error-correction-zoo.md)

## Decoders

- Short Shor-style syndrome extraction circuits can be used for syndrome-based decoding  ([arXiv:2008.05051](https://arxiv.org/abs/2008.05051)).

## Fault tolerance

- Short Shor-style syndrome extraction circuits can be used for syndrome-based decoding  ([arXiv:2008.05051](https://arxiv.org/abs/2008.05051)).

## Relations

- _parent_: [[concepts/qec/stabilizer-over-gf4]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/qubit-concatenated]] — Applying the BLT mapping to the $⟦8,2,3⟧$ Hermitian code and concatenating each qubit pair with the $⟦4,2,2⟧$ code yields a $⟦32,4,6⟧$ self-dual CSS code  ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)).
- _cousin_: [[concepts/qec/self-dual-css]] — Applying the BLT mapping to the $⟦8,2,3⟧$ Hermitian code and concatenating each qubit pair with the $⟦4,2,2⟧$ code yields a $⟦32,4,6⟧$ self-dual CSS code  ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)).
- _cousin_: [[concepts/qec/stab-4-2-2]] — Applying the BLT mapping to the $⟦8,2,3⟧$ Hermitian code and concatenating each qubit pair with the $⟦4,2,2⟧$ code yields a $⟦32,4,6⟧$ self-dual CSS code  ([arXiv:2605.15344](https://arxiv.org/abs/2605.15344)).
