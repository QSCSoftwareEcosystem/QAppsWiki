---
type: concept
name: $⟦6,1,3⟧$ Six-qubit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/holographic-6-1-3
- concepts/qec/qubit-subsystem-stabilizer
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-5-1-3
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_6_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_6_1_3
---

# $⟦6,1,3⟧$ Six-qubit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_6_1_3) (`code_id: stab_6_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A degenerate, non-trivial $⟦6,1,3⟧$ stabilizer code.
It is one of two six-qubit distance-three codes that are unique up to equivalence  ([arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)), with the other code being decomposable and an extension of the five-qubit code  ([arXiv:0803.1495](https://arxiv.org/abs/0803.1495)).
The code admits fault-tolerant syndrome extraction using only one ancilla per stabilizer generator measurement.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{cccccc}
  X & I & I & I & I & Z \\
  I & X & X & Z & Z & I \\
  I & Y & I & Y & Z & Z \\
  I & X & Z & I & X & Z \\
  Z & Y & Z & Z & I & Y
\end{array}~.
\end{align}

Stabilizer generators and logical Pauli operators are presented in Refs.  ([arXiv:0803.1495](https://arxiv.org/abs/0803.1495), [arXiv:1008.0425](https://arxiv.org/abs/1008.0425)).
The code is equivalent to the graph code in Ref.  ([arXiv:2501.12072](https://arxiv.org/abs/2501.12072)).

(source: raw/error-correction-zoo.md)

## Encoders

- CNOT and Hadamard gates  ([arXiv:0803.1495](https://arxiv.org/abs/0803.1495), [arXiv:1008.0425](https://arxiv.org/abs/1008.0425)).

## Decoders

- Fault-tolerant syndrome extraction using a single ancilla  ([arXiv:2501.12072](https://arxiv.org/abs/2501.12072)).

## General gates

- Logical CNOT gate  ([arXiv:0803.1495](https://arxiv.org/abs/0803.1495), [arXiv:1008.0425](https://arxiv.org/abs/1008.0425)).

## Relations

- _parent_: [[concepts/qec/holographic-6-1-3]] — The $⟦6,1,3⟧$ six-qubit stabilizer code is the smallest six-qubit-tensor holographic code. The encoding of more general SCF holographic codes is a holographic tensor network consisting of the encoding isometry for the $⟦6,1,3⟧$ six-qubit stabilizer code.
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/qubit-subsystem-stabilizer]] — The $⟦6,1,3⟧$ six-qubit code can be converted into a $⟦6,1,1,3⟧$ subsystem code that saturates the subsystem Singleton bound while requiring only four stabilizer measurements during recovery  ([arXiv:0803.1495](https://arxiv.org/abs/0803.1495), [arXiv:1008.0425](https://arxiv.org/abs/1008.0425)).
- _cousin_: [[concepts/qec/stab-5-1-3]] — The $⟦6,1,3⟧$ six-qubit code is one of two six-qubit distance-three codes that are unique up to equivalence  ([arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)), with the other code being decomposable and an extension of the five-qubit code  ([arXiv:0803.1495](https://arxiv.org/abs/0803.1495)).
