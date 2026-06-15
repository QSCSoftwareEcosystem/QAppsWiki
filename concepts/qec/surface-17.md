---
type: concept
name: $⟦9,1,3⟧$ Surface-17 code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $⟦9,1,3⟧$ rotated surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/rotated-surface
- concepts/qec/shor-nine
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stellated-dodecahedron-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/surface-17
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: surface-17
---

# $⟦9,1,3⟧$ Surface-17 code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/surface-17) (`code_id: surface-17`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦9,1,3⟧$ rotated surface code named for the sum of its 9 data qubits and 8 syndrome qubits.
It is one of the four inequivalent CSS gauge fixings of the nine-qubit Bacon-Shor code  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
It uses the smallest number of qubits to perform fault-tolerant error correction on a surface code with parallel syndrome extraction.

A stabilizer tableau for the code is given by .
\begin{align}
\begin{array}{ccccccccc}
  I & X & I & I & I & I & I & X & I \\
  I & I & I & X & X & I & I & I & I \\
  I & I & X & I & I & X & X & X & I \\
  X & I & I & X & I & X & I & I & X \\
  Z & I & I & I & I & I & I & I & Z \\
  I & I & Z & I & I & I & Z & I & I \\
  I & I & I & Z & Z & Z & Z & I & I \\
  I & Z & I & I & I & Z & I & Z & Z
\end{array}~.
\end{align}
The code is depicted in \ref{figure:surface-17}.

(source: raw/error-correction-zoo.md)

## Protection

Independent correction of single-qubit $X$ and $Z$ errors. Correction for some two-qubit $X$ and $Z$ errors.
Admits pseudo-thresholds of $\approx 10^{-4}$ under depolarizing noise.

## Encoders

- Measurement-free fault-tolerant logical zero state preparation in nearest-neighbor qubit connectivity  ([arXiv:2303.17211](https://arxiv.org/abs/2303.17211)).
- Fault-tolerant logical zero and logical plus state preparation in all-to-all connectivity, and fault-tolerant logical zero state preparation on 2D grids, with flag qubits  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).

## Transversal gates

- Pauli gates, CNOT gate, and $H$ gate (with relabeling).

## Decoders

- Lookup table  ([arXiv:1404.3747](https://arxiv.org/abs/1404.3747)).
- Syndrome extraction using Toffoli gates and qubit reset  ([arXiv:1708.08683](https://arxiv.org/abs/1708.08683)).

## Fault tolerance

- Measurement-free fault-tolerant logical zero state preparation in nearest-neighbor qubit connectivity  ([arXiv:2303.17211](https://arxiv.org/abs/2303.17211)).
- Fault-tolerant logical zero and logical plus state preparation in all-to-all connectivity, and fault-tolerant logical zero state preparation on 2D grids, with flag qubits  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).

## Realizations

- Implemented at ETH Zurich by the Wallraff group
 ([arXiv:2112.03708](https://arxiv.org/abs/2112.03708)) and on the Zuchongzhi 2.1 superconducting quantum processor  ([arXiv:2112.13505](https://arxiv.org/abs/2112.13505)).
Both experimental error rates are above the pseudo-threshold for this code relative to a single qubit; see Physics viewpoint for a summary  ([doi:10.1103/Physics.15.103](https://doi.org/10.1103/Physics.15.103)).
Magic states have been created on the latter processor  ([arXiv:2305.15972](https://arxiv.org/abs/2305.15972)).
Lattice surgery on the surface-17 code has been realized by splitting the code into two repetition codes by the Wallraff group  ([arXiv:2501.04612](https://arxiv.org/abs/2501.04612)).
The device noise can be used to develop a decoder without relying on a theoretical noise model  ([arXiv:2502.17722](https://arxiv.org/abs/2502.17722)).

## Relations

- _parent_: [[concepts/qec/rotated-surface]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/shor-nine]] — Both Shor's code and surface-17 are $⟦9,1,3⟧$ codes, but they are distinct (e.g., they have different quantum weight enumerators).
- _cousin_: [[concepts/qec/stellated-dodecahedron-css]] — Bring's code and the surface-17 code have been compared numerically  ([arXiv:1712.07666](https://arxiv.org/abs/1712.07666)).

## Notes

- Subject of various numerical studies examining the code under noise models and architectures specific to trapped ions  ([arXiv:1404.3747](https://arxiv.org/abs/1404.3747), [arXiv:1710.01378](https://arxiv.org/abs/1710.01378), [arXiv:1910.08495](https://arxiv.org/abs/1910.08495)) and superconducting circuits  ([arXiv:1612.08208](https://arxiv.org/abs/1612.08208), [arXiv:1703.04136](https://arxiv.org/abs/1703.04136), [arXiv:2002.07119](https://arxiv.org/abs/2002.07119)).
