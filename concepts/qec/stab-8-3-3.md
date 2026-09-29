---
type: concept
name: $⟦8, 3, 3⟧$ Eight-qubit Gottesman code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-hamming
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_8_3_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_8_3_3
---

# $⟦8, 3, 3⟧$ Eight-qubit Gottesman code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_8_3_3) (`code_id: stab_8_3_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Eight-qubit pure code that can be obtained from a modified CSS construction using the $[8,4,4]$ extended Hamming code and a $[8,7,2]$ even-weight code  ([arXiv:quant-ph/9605021](https://arxiv.org/abs/quant-ph/9605021)).
The modification introduces signs between the codewords.

See  ([arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)) for its stabilizer generator matrix.
A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{cccccccc}
  X & Y & Y & X & Z & I & I & Z \\
  Z & X & I & Z & X & I & Z & Z \\
  X & Z & Z & I & I & X & Z & Z \\
  Y & I & Y & Z & I & Z & X & Z \\
  Y & Z & X & I & Z & Z & I & Y
\end{array}~.
\end{align}
The code's automorphism group is $\text{A}\Gamma\text{L}(1,8)$  ([arXiv:2109.12735](https://arxiv.org/abs/2109.12735)).
It is unique for its parameters, up to equivalence  ([arXiv:0709.1780](https://arxiv.org/abs/0709.1780)) ([doi:10.1007/3-540-30731-1](https://doi.org/10.1007/3-540-30731-1)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- Permutation-based gates  ([arXiv:1302.1035](https://arxiv.org/abs/1302.1035)).
- No gates outside of the Pauli group were found in Ref.  ([arXiv:1912.10063](https://arxiv.org/abs/1912.10063)).

## General gates

- Logical Trotter circuits can be implemented via symplectic transvections  ([arXiv:2504.11444](https://arxiv.org/abs/2504.11444)), with explicit encoded parity circuits for this code given in Ref.  ([arXiv:2609.16159](https://arxiv.org/abs/2609.16159)).

## Decoders

- Weight-one lookup-table decoder built from the distinct syndromes of the 24 weight-one Pauli errors  ([arXiv:2609.16159](https://arxiv.org/abs/2609.16159)).
- Bitwise majority vote over repeated syndrome measurement rounds under phenomenological measurement noise  ([arXiv:2609.16159](https://arxiv.org/abs/2609.16159)).

## Fault tolerance

- Chao-Reichardt flagged syndrome extraction using one syndrome ancilla and one flag qubit per stabilizer generator  ([arXiv:1705.02329](https://arxiv.org/abs/1705.02329)) ([arXiv:2609.16159](https://arxiv.org/abs/2609.16159)).
- Encoded Pauli rotations built from compute-rotate-uncompute parity circuits have circuit-level distance one in the logical $Z$ sector  ([arXiv:2609.16159](https://arxiv.org/abs/2609.16159)). A single phase-type fault on the parity ancilla propagates into a logical $Z$ operator with trivial syndrome.
- Flag-conditioned recovery, $Z$-biased noise tailoring, CliNR resource verification, and flag postselection each suppress only the logical sector transverse to the rotation axis  ([arXiv:2609.16159](https://arxiv.org/abs/2609.16159)).

## Code capacity threshold

- $4\%$ pseudo-threshold under depolarizing noise with a weight-one lookup-table decoder  ([arXiv:2609.16159](https://arxiv.org/abs/2609.16159)).

## Threshold

- $1.5\times 10^{-3}$ pseudo-threshold for circuit-level depolarizing noise under one round of flagged error correction, assuming an ideal final round of weight-one correction  ([arXiv:2609.16159](https://arxiv.org/abs/2609.16159)).

## Relations

- _parent_: [[concepts/qec/quantum-hamming]]
- _cousin_: [`hamming844`](https://errorcorrectionzoo.org/c/hamming844) — The $⟦8, 3, 3⟧$ code is obtained via a modified CSS construction from the $[8,4,4]$ extended Hamming code.
