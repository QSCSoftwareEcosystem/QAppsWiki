---
type: concept
name: PI qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/permutation-invariant
- concepts/qec/qubit-stabilizer
- concepts/qec/qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_permutation_invariant
---

# PI qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_permutation_invariant) (`code_id: qubit_permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Block quantum code defined on two-dimensional subsystems such that any permutation of the subsystems leaves any codeword invariant.

\begin{defterm}{Dicke states}
\label{topic:dicke}
For $n$-qubit block codes, an often used basis for the $n+1$-dimensional PI subspace consists of the Dicke states $|D^n_w\rangle$ -- normalized PI states of $w$ excitations, i.e., a normalized sum over all binary-string basis elements with $w$ ones and $n - w$ zeroes.
For example, the single-excitation Dicke state, known as a $W$ *state*, on three qubits is
\begin{align}
  |D_{1}^{3}\rangle=\frac{1}{\sqrt{3}}\left(|001\rangle+|010\rangle+|100\rangle\right)~.
\end{align}
The $n+1$-dimensional PI space can be thought of as a standalone spin-$n/2$ quantum system, yielding a way to convert between PI qubit codes and $SU(2)$ spin codes.
A single-spin code for the $SU(2)$ group correcting spherical tensors can be mapped into a PI qubit code with an analogous distance  ([arXiv:2304.08611](https://arxiv.org/abs/2304.08611)) ([arXiv:2310.17652](https://arxiv.org/abs/2310.17652)).
\end{defterm}

(source: raw/error-correction-zoo.md)

## Protection

Permutation invariant qubit codes of distance $d$ can protect against $d-1$ deletion errors  ([arXiv:2001.08405](https://arxiv.org/abs/2001.08405), [arXiv:2004.00814](https://arxiv.org/abs/2004.00814)), i.e., erasures of subsystems at unknown locations.
There are also simplified conditions on insertion errors  ([arXiv:2602.08780](https://arxiv.org/abs/2602.08780)).

## Encoders

- With quantum harmonic oscillators (superconducting charge qubits in an ultrastrong coupling regime) in $O(N)$ as in  ([doi:10.1103/PhysRevA.99.012335](https://doi.org/10.1103/PhysRevA.99.012335)). Can be done in $O(N^2)$ steps using quantum circuits  ([arXiv:1904.07358](https://arxiv.org/abs/1904.07358)), or using geometric phase gates in $O(N)$  ([arXiv:1908.01120](https://arxiv.org/abs/1908.01120)).
- Finite-depth quantum circuits with LOCC for Dicke states  ([arXiv:2307.14840](https://arxiv.org/abs/2307.14840), [arXiv:2403.07604](https://arxiv.org/abs/2403.07604), [arXiv:2411.03428](https://arxiv.org/abs/2411.03428)).
- Preparation of sparse Dicke states using the combinatorial number system  ([arXiv:2510.10967](https://arxiv.org/abs/2510.10967)).

## General gates

- There is a measurement-free code-switching protocol between a qubit stabilizer code and a PI qubit code  ([arXiv:2411.13142](https://arxiv.org/abs/2411.13142)).

## Decoders

- Schur-Weyl-transform based decoder  ([arXiv:2212.06285](https://arxiv.org/abs/2212.06285)). Here, one first measures nested total angular momenta, i.e., that of the first qubit, the first and second, followed by the first, second, and third, etc. Then, for codes with spacing, one measures the projection of the angular momentum modulo the spacing. Recovery can be performed by applying geometric phase gates  ([arXiv:quant-ph/0111017](https://arxiv.org/abs/quant-ph/0111017)) or the quantum Schur transform. This decoder has been generalized to work with insertion errors  ([arXiv:2509.03413](https://arxiv.org/abs/2509.03413)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/permutation-invariant]]
- _cousin_: [[concepts/qec/qubit-stabilizer]] — There is a measurement-free code-switching protocol between a qubit stabilizer code and a PI qubit code  ([arXiv:2411.13142](https://arxiv.org/abs/2411.13142)).
