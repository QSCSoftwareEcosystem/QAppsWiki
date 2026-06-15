---
type: concept
name: $⟦7,2,2⟧$ QETC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bare-7-1-3
- concepts/qec/qetc
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qetc_7_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qetc_7_2
---

# $⟦7,2,2⟧$ QETC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qetc_7_2) (`code_id: qetc_7_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Seven-qubit pure QETC that transmutes all single-qubit Pauli errors to logical phase errors.

A stabilizer tableau for the code is given by  ([arXiv:2310.10278](https://arxiv.org/abs/2310.10278))
\begin{align}
\begin{array}{ccccccc}
  X & X & Y & Y & Z & I & Z \\
  I & Z & X & Y & Y & X & Y \\
  I & I & I & I & I & Z & Z \\
  Z & Z & I & I & Z & I & Z \\
  Z & Z & Z & Z & I & I & I
\end{array}~.
\end{align}
The above stabilizer tableau is equivalent to  by applying $H$ to qubits 1 and 2 and $SH$ (with $H$ applied first) to qubits 3 and 4, followed by the qubit relabeling $(1,2,3,4,5,6,7)\to(5,6,1,3,7,2,4)$.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _parent_: [[concepts/qec/qetc]]
- _cousin_: [[concepts/qec/bare-7-1-3]] — The stabilizer group of the $⟦7,2,2⟧$ QETC, together with the logical-$Z$ operator on the first logical qubit, generates the stabilizer group of a $⟦7,1,3⟧$ code  ([arXiv:2310.10278](https://arxiv.org/abs/2310.10278)) equivalent to the bare $⟦7,1,3⟧$ code .
