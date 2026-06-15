---
type: concept
name: $⟦2^r-1, 2^r-2r-1, 3⟧$ quantum Hamming code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-reed-muller
- concepts/qec/qubit-concatenated
- concepts/qec/qudit-hamming-css
- concepts/qec/self-dual-css
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-4-2-2
- concepts/qec/stab-6-2-2
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_hamming_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_hamming_css
---

# $⟦2^r-1, 2^r-2r-1, 3⟧$ quantum Hamming code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_hamming_css) (`code_id: quantum_hamming_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of self-dual CSS codes constructed from $[2^r-1,2^r-r-1,3]=C_X=C_Z$ Hamming codes and their duals, the simplex codes.
The code's stabilizer generator matrix blocks $H_{X}$ and $H_{Z}$ are both the generator matrix for a simplex code.
The weight of each stabilizer generator is $2^{r-1}$.

(source: raw/error-correction-zoo.md)

## Protection

Protects against any single qubit error.

## Transversal gates

- Pauli, Hadamard, and CNOT gates.

## Decoders

- Efficient decoder  ([arXiv:2207.08826](https://arxiv.org/abs/2207.08826)).

## Fault tolerance

- Syndrome measurement can be done with two ancillary flag qubits  ([arXiv:1705.02329](https://arxiv.org/abs/1705.02329)).
- Concatenating a growing sequence of quantum Hamming codes yields fault-tolerant quantum computation with constant space overhead and quasi-polylogarithmic time overhead  ([arXiv:2207.08826](https://arxiv.org/abs/2207.08826)).
- Concatenating quantum Hamming codes on top of the $⟦4,2,2⟧$ and $C_6$ codes yields fault-tolerant quantum computation with constant space and quasi-polylogarithmic time overheads  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)). In the optimized protocol of Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), a level-five $C_4/C_6$ code underlies concatenated quantum Hamming codes $\mathcal{Q}_5,\mathcal{Q}_6,\mathcal{Q}_7,\mathcal{Q}_7$, yielding a $2.5\%$ threshold and space overheads $162$ and $373$ physical qubits per logical qubit at physical error rate $0.1\%$ for logical CNOT error rates $10^{-10}$ and $10^{-24}$, respectively.
- A modified tower of interleaved quantum Hamming codes with reserved qubits and recursive hookless Pauli-product measurements yields fault-tolerant quantum computation on a 1D nearest-neighbor qubit line with asymptotic rate above $5\%$, constant space overhead, quasi-polylogarithmic time overhead, and a threshold  ([arXiv:2502.16132](https://arxiv.org/abs/2502.16132)).

## Threshold

- Concatenated threshold requiring constant-space and quasi-polylogarithmic time overhead  ([arXiv:2207.08826](https://arxiv.org/abs/2207.08826)).

## Relations

- _parent_: [[concepts/qec/quantum-reed-muller]] — $⟦2^r-1, 2^r-2r-1, 3⟧$ quantum Hamming codes are quantum RM codes because Hamming and simplex codes are both punctured RM codes.
- _parent_: [[concepts/qec/qudit-hamming-css]] — $⟦2^r-1, 2^r-2r-1, 3⟧_p$ prime-qudit CSS codes for $p=2$ reduce to $⟦2^r-1, 2^r-2r-1, 3⟧$ quantum Hamming codes.
- _parent_: [[concepts/qec/self-dual-css]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [`hamming`](https://errorcorrectionzoo.org/c/hamming) — Quantum Hamming codes result from applying the CSS construction to Hamming codes and their duals the simplex codes.
- _cousin_: [`simplex`](https://errorcorrectionzoo.org/c/simplex) — Quantum Hamming codes result from applying the CSS construction to Hamming codes and their duals the simplex codes.
- _cousin_: [[concepts/qec/qubit-concatenated]] — Concatenating a growing sequence of quantum Hamming codes yields fault-tolerant quantum computation with constant space overhead and quasi-polylogarithmic time overhead  ([arXiv:2207.08826](https://arxiv.org/abs/2207.08826)).
Concatenating quantum Hamming codes on top of the $⟦4,2,2⟧$ and $C_6$ codes yields fault-tolerant quantum computation with constant space and quasi-polylogarithmic time overheads  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)). In the optimized protocol of Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), a level-five $C_4/C_6$ code underlies concatenated quantum Hamming codes $\mathcal{Q}_5,\mathcal{Q}_6,\mathcal{Q}_7,\mathcal{Q}_7$, yielding a $2.5\%$ threshold and space overheads $162$ and $373$ physical qubits per logical qubit at physical error rate $0.1\%$ for logical CNOT error rates $10^{-10}$ and $10^{-24}$, respectively.
A modified tower of interleaved quantum Hamming codes with reserved qubits and recursive hookless Pauli-product measurements yields fault-tolerant quantum computation on a 1D nearest-neighbor qubit line with asymptotic rate above $5\%$, constant space overhead, quasi-polylogarithmic time overhead, and a threshold  ([arXiv:2502.16132](https://arxiv.org/abs/2502.16132)).
Quantum Hamming codes can also be concatenated with surface codes  ([arXiv:2407.16176](https://arxiv.org/abs/2407.16176)).
- _cousin_: [[concepts/qec/stab-4-2-2]] — Concatenating quantum Hamming codes on top of the $⟦4,2,2⟧$ and $C_6$ codes yields fault-tolerant quantum computation with constant space and quasi-polylogarithmic time overheads  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)). In the optimized protocol of Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), a level-five $C_4/C_6$ code underlies concatenated quantum Hamming codes $\mathcal{Q}_5,\mathcal{Q}_6,\mathcal{Q}_7,\mathcal{Q}_7$, yielding a $2.5\%$ threshold and space overheads $162$ and $373$ physical qubits per logical qubit at physical error rate $0.1\%$ for logical CNOT error rates $10^{-10}$ and $10^{-24}$, respectively.
- _cousin_: [[concepts/qec/stab-6-2-2]] — Concatenating quantum Hamming codes on top of the $⟦4,2,2⟧$ and $C_6$ codes yields fault-tolerant quantum computation with constant space and quasi-polylogarithmic time overheads  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)). In the optimized protocol of Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), a level-five $C_4/C_6$ code underlies concatenated quantum Hamming codes $\mathcal{Q}_5,\mathcal{Q}_6,\mathcal{Q}_7,\mathcal{Q}_7$, yielding a $2.5\%$ threshold and space overheads $162$ and $373$ physical qubits per logical qubit at physical error rate $0.1\%$ for logical CNOT error rates $10^{-10}$ and $10^{-24}$, respectively.
- _cousin_: [[concepts/qec/surface]] — Quantum Hamming codes can be concatenated with surface codes  ([arXiv:2407.16176](https://arxiv.org/abs/2407.16176)). In a unified logical-CNOT comparison under circuit-level depolarizing noise, using the surface code as the underlying code gives a $0.31\%$ threshold and requires space overhead $4.5\times 10^3$ at physical error rate $0.1\%$ to achieve logical CNOT error rate $10^{-24}$, compared to $3.7\times 10^2$ for the optimized $C_4/C_6$/Hamming construction  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)).
