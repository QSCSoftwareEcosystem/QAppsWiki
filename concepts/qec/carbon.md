---
type: concept
name: $⟦12,2,4⟧$ carbon code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $C_{12}$ code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bc-phantom
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-4-2-2
- concepts/qec/stab-6-2-2
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/carbon
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: carbon
---

# $⟦12,2,4⟧$ carbon code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/carbon) (`code_id: carbon`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Twelve-qubit CSS code based on Knill's $C_4/C_6$ scheme  ([arXiv:2404.02280](https://arxiv.org/abs/2404.02280)).
Using the concatenation convention of the Zoo, the carbon code can be viewed as a block concatenation with inner code $⟦4,2,2⟧$ and outer code $C_6$: three inner $⟦4,2,2⟧$ blocks encode six intermediate qubits, which are then encoded into two logical qubits by the outer $⟦6,2,2⟧$ code.

A stabilizer tableau for the code is given by  ([arXiv:2404.02280](https://arxiv.org/abs/2404.02280))
\begin{align}
\begin{array}{cccccccccccc}
  X & X & X & X & I & I & I & I & I & I & I & I \\
  Z & Z & Z & Z & I & I & I & I & I & I & I & I \\
  I & I & I & I & X & X & X & X & I & I & I & I \\
  I & I & I & I & Z & Z & Z & Z & I & I & I & I \\
  I & I & I & I & I & I & I & I & X & X & X & X \\
  I & I & I & I & I & I & I & I & Z & Z & Z & Z \\
  X & X & I & I & I & X & I & X & X & I & I & X \\
  X & I & I & X & X & X & I & I & I & X & I & X \\
  Z & I & Z & I & I & I & Z & Z & Z & I & I & Z \\
  Z & I & I & Z & Z & I & Z & I & I & I & Z & Z
\end{array}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Encoders

- Simplified fault-tolerant state preparation circuits for the $00$ and $++$ states  ([arXiv:2404.02280](https://arxiv.org/abs/2404.02280)).

## Transversal gates

- Two-block CNOT gates are transversal because the code is CSS.
- Automorphism groups of the underlying classical codes can yield transversal Clifford gates when combined with qubit permutations  ([arXiv:1302.1035](https://arxiv.org/abs/1302.1035)). In particular, logical Hadamard is realized by a transversal physical Hadamard followed by a qubit permutation, and a logical one-block CNOT is implemented by a qubit permutation  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199), [arXiv:2404.02280](https://arxiv.org/abs/2404.02280)).

## Decoders

- Syndrome extraction circuit based on Knill error correction (a.k.a. telecorrection  ([arXiv:quant-ph/0601066](https://arxiv.org/abs/quant-ph/0601066))), but using only one ancillary code block instead of two  ([arXiv:2404.02280](https://arxiv.org/abs/2404.02280)).

## Realizations

- Trapped-ion devices: Three rounds of error correction and post-selected fault-tolerant logical Bell-state preparation with logical error rates at least 5 times lower than physical rate on a quantum charge-coupled device (QCCD)  ([arXiv:2305.03828](https://arxiv.org/abs/2305.03828)) by Microsoft and Quantinuum  ([arXiv:2404.02280](https://arxiv.org/abs/2404.02280)).

## Relations

- _parent_: [[concepts/qec/bc-phantom]] — The carbon code is the B\&C phantom code obtained from the $⟦3,1,2⟧_4$ Galois-qudit code  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/stab-4-2-2]] — The carbon code is a concatenation of the $⟦4,2,2⟧$ code and the $C_6$ code.
- _cousin_: [[concepts/qec/stab-6-2-2]] — The carbon code is a concatenation of the $⟦4,2,2⟧$ code and the $C_6$ code.
