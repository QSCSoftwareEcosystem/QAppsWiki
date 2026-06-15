---
type: concept
name: $⟦9,1,3⟧$ Shor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cluster-state
- concepts/qec/qecc
- concepts/qec/quantum-parity
- concepts/qec/quantum-repetition
- concepts/qec/qubit-concatenated
- concepts/qec/real-projective-plane
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-9-1-3
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/shor_nine
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: shor_nine
---

# $⟦9,1,3⟧$ Shor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/shor_nine) (`code_id: shor_nine`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Nine-qubit CSS code that is the first quantum error-correcting code .
Among indecomposable $⟦9,1,3⟧$ CSS codes, the Shor code has the largest automorphism group  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).

A set of logical codewords is
\begin{align}
\begin{split}
|\overline{0}\rangle&=\frac{1}{2\sqrt{2}}\left(|000\rangle+|111\rangle\right)^{\otimes3}\\
|\overline{1}\rangle&=\frac{1}{2\sqrt{2}}\left(|000\rangle-|111\rangle\right)^{\otimes3}~.
\end{split}
\end{align}
A stabilizer tableau for the code is
\begin{align}
\begin{array}{ccccccccc}
  Z & Z & I & I & I & I & I & I & I \\
  I & Z & Z & I & I & I & I & I & I \\
  I & I & I & Z & Z & I & I & I & I \\
  I & I & I & I & Z & Z & I & I & I \\
  I & I & I & I & I & I & Z & Z & I \\
  I & I & I & I & I & I & I & Z & Z \\
  X & X & X & X & X & X & I & I & I \\
  I & I & I & X & X & X & X & X & X
\end{array}~.
\end{align}
The encoder-respecting form of the Shor code is a star-shaped tree graph  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).
The code works by concatenating each qubit of a phase-flip repetition code with a bit-flip repetition code. Therefore, the code can correct both types of errors simultaneously.
The code is degenerate: for example, two $Z$ errors in the same three-qubit block act identically on all codewords .

(source: raw/error-correction-zoo.md)

## Protection

The code detects two-qubit errors or corrects an arbitrary single-qubit error. Since it corrects the single-qubit Pauli errors, linearity implies that it corrects arbitrary single-qubit errors and corresponding single-qubit error channels . It also corrects two-qubit AD errors  ([arXiv:1001.2356](https://arxiv.org/abs/1001.2356)).

## Encoders

- Fault-tolerant logical zero and logical plus state preparation using reinforcement learning  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).
- Fault-tolerant measurement-free logical-zero state preparation  ([arXiv:2303.17211](https://arxiv.org/abs/2303.17211)).

## Decoders

- Bit- and phase-flip circuits utilize CNOT and Hadamard gates  ([doi:10.1201/9781420012293](https://doi.org/10.1201/9781420012293)).

## Fault tolerance

- Fault-tolerant logical zero and logical plus state preparation using reinforcement learning  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).
- Fault-tolerant measurement-free logical-zero state preparation  ([arXiv:2303.17211](https://arxiv.org/abs/2303.17211)).

## Realizations

- Trapped-ion qubits: state preparation with 98.8(1)\% and 98.5(1)\% fidelity for state $|\overline{0}\rangle$ and $|\overline{1}\rangle$, respectively, by N. Linke group  ([arXiv:2104.01205](https://arxiv.org/abs/2104.01205)). Variants of the code to handle coherent noise studied and realized by K. Brown and C. Monroe groups  ([arXiv:2105.05068](https://arxiv.org/abs/2105.05068)).
- Optical systems: quantum teleportation of information implemented by J.-W. Pan group on a maximally entangled pair of one physical and one logical qubit with a fidelity of up to 78.6\%  ([arXiv:2009.06242](https://arxiv.org/abs/2009.06242)). All-photonic quantum repeater architecture tested on the same code  ([arXiv:2203.07979](https://arxiv.org/abs/2203.07979)).

## Relations

- _parent_: [[concepts/qec/quantum-parity]] — The Shor code is part of the sub-family of $⟦m^2,1,m⟧$ QPCs.
- _parent_: [[concepts/qec/real-projective-plane]] — The Shor code is one of the nine-qubit surface codes defined on the projective plane  ([arXiv:quant-ph/9810055](https://arxiv.org/abs/quant-ph/9810055)) ([arXiv:quant-ph/0605094](https://arxiv.org/abs/quant-ph/0605094)).
- _parent_: [[concepts/qec/stab-9-1-3]] — The $⟦9,1,3⟧_{\mathbb{Z}_q}$ modular-qudit code for $q=2$ reduces to the $⟦9,1,3⟧$ Shor code.
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/quantum-repetition]] — The Shor code is a concatenation of a three-qubit bit-flip with a three-qubit phase-flip repetition code.
- _cousin_: [[concepts/qec/qubit-concatenated]] — The Shor code is a concatenation of a three-qubit bit-flip with a three-qubit phase-flip repetition code.
- _cousin_: [[concepts/qec/qecc]] — The Shor code is the first quantum error-correcting code.
- _cousin_: [[concepts/qec/cluster-state]] — The Shor code admits a codeword that is the cluster state of a particular nine-vertex graph  ([arXiv:1511.05647](https://arxiv.org/abs/1511.05647)).
