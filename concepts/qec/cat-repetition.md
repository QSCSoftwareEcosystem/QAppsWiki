---
type: concept
name: Cat-repetition code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cat-concatenated
- concepts/qec/quantum-repetition
- concepts/qec/self-correct
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/cat_repetition
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: cat_repetition
---

# Cat-repetition code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/cat_repetition) (`code_id: cat_repetition`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A concatenated qubit-into-$n$-mode code obtained by encoding each qubit of a quantum repetition code into a two-component cat code in its cat-state basis.

A basis of codewords for the two-component case is
\begin{align}
  |\overline{\pm}\rangle\propto\left(\left|\alpha\right\rangle \pm\left|-\alpha\right\rangle \right)^{\otimes n}
\end{align}
for any complex $\alpha$.

(source: raw/error-correction-zoo.md)

## Protection

The code can detect arbitrary losses in up to $n/2$ modes.  
The cat-repetition code on a 2D mode lattice is a candidate for a memory that may be self-correcting, but only in the limit of infinite energy per mode  ([arXiv:2205.09767](https://arxiv.org/abs/2205.09767)).

## General gates

- Fault-tolerant logical $X$, CNOT, and Toffoli gates and a logical Hadamard synthesized from state preparation and measurement in the dual basis, without magic-state preparation or distillation  ([arXiv:1904.09474](https://arxiv.org/abs/1904.09474)).
- Using a physical bias-preserving CX between cat qubits, the logical $\overline{\mathrm{CX}}$ gadget can be implemented transversally between repetition-code blocks; magic-state preparation using transversal $ZZ(\theta)$ gates was also analyzed  ([arXiv:1905.00450](https://arxiv.org/abs/1905.00450)).

## Decoders

- A measurement-code decoder for the repetition layer yields a $\overline{\mathrm{CX}}$-gadget threshold of about $6\times 10^{-3}$ for $n=5$; reaching a comparable threshold with naive repeated-syndrome decoding requires $n=11$ and $r=5$  ([arXiv:1905.00450](https://arxiv.org/abs/1905.00450)).

## Fault tolerance

- Fault-tolerant logical $X$, CNOT, and Toffoli gates and a logical Hadamard synthesized from state preparation and measurement in the dual basis, without magic-state preparation or distillation  ([arXiv:1904.09474](https://arxiv.org/abs/1904.09474)).

## Threshold

- For dephasing bias $\eta=10^4$, the cat-based logical $\overline{\mathrm{CX}}$ gadget has threshold $7.5\times 10^{-3}$, compared with $3.55\times 10^{-3}$ for an earlier scheme; at $\varepsilon=2.5\times 10^{-3}$, its circuit volume is about five times smaller  ([arXiv:1905.00450](https://arxiv.org/abs/1905.00450)).

## Realizations

- Superconducting circuit devices: a repetition code out of two-component cat qubits has been realized for distances 3 and 5  ([arXiv:2409.13025](https://arxiv.org/abs/2409.13025)).

## Relations

- _parent_: [[concepts/qec/cat-concatenated]] — The cat-repetition code is a concatenation whose outer code is the cat code in its cat-state basis.
- _cousin_: [[concepts/qec/quantum-repetition]] — The cat-repetition code is obtained by encoding each qubit of a quantum repetition code into a two-component cat code in its cat-state basis  ([arXiv:1904.09474](https://arxiv.org/abs/1904.09474), [arXiv:1905.00450](https://arxiv.org/abs/1905.00450), [arXiv:2009.10756](https://arxiv.org/abs/2009.10756), [arXiv:2012.04108](https://arxiv.org/abs/2012.04108), [arXiv:2212.11927](https://arxiv.org/abs/2212.11927)).
- _cousin_: [[concepts/qec/self-correct]] — The cat-repetition code on a 2D mode lattice is a candidate for a memory that may be self-correcting, but only in the limit of infinite energy per mode  ([arXiv:2205.09767](https://arxiv.org/abs/2205.09767)).
