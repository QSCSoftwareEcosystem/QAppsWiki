---
type: concept
name: Galois-qudit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $\mathbb{F}_q$-qudit code
- $\mathbb{F}_q$-qudit code
- Galois-qudit subspace code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-quantum
- concepts/qec/group-quantum
- concepts/qec/qecc-finite
- concepts/qec/qudits-into-qudits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_into_galois
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_into_galois
---

# Galois-qudit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_into_galois) (`code_id: galois_into_galois`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes $K$-dimensional Hilbert space into a $q^n$-dimensional ($n$-qudit) Hilbert space, with canonical qudit states $|k\rangle$ labeled by elements $k$ of the *Galois field* $\mathbb{F}_q$ and with $q$ being a power of a prime $p$.

Codes can be denoted as $((n,K))_q$ or $((n,K,d))_q$, whenever the code's distance $d$ is defined.
This notation differentiates between Galois-qudit and $((n,K,d))_{\mathbb{Z}_q}$ modular-qudit codes, although the same notation is usually used for both.

There exists an analogue of the Wigner function for Galois qudits  ([arXiv:quant-ph/0401155](https://arxiv.org/abs/quant-ph/0401155), [arXiv:quant-ph/0410117](https://arxiv.org/abs/quant-ph/0410117)).

(source: raw/error-correction-zoo.md)

## Protection

An $((n,K,d))_q$ code with distance $d$ detects errors acting on up to $d-1$ Galois qudits, corrects erasure errors on up to $d-1$ Galois qudits, or corrects errors acting on up to $\lfloor (d-1)/2 \rfloor$ Galois qudits.

\subsection{Galois-qudit Pauli-string error basis}
A convenient and often considered error set is the Galois-qudit analogue of the Pauli string set for qubit codes.

\begin{defterm}{Galois-qudit Pauli strings}
\label{topic:galois-pauli}
For a single Galois qudit, this set consists of products of $X$-type and $Z$-type operators labeled by elements $\beta \in \mathbb{F}_q$, which act on computational basis states $|\gamma\rangle$ for $\gamma\in \mathbb{F}_q$ as
\begin{align}
  X_{\beta}\left|\gamma\right\rangle =\left|\gamma+\beta\right\rangle \,\,\text{ and }\,\,Z_{\beta}\left|\gamma\right\rangle =e^{i\frac{2\pi}{p}\text{tr}(\beta\gamma)}\left|\gamma\right\rangle~,
\end{align}
where $\text{tr}$ is the field trace.
For multiple Galois qudits, error set elements are tensor products of elements of the single-qudit error set.
Tensor products of $X$ ($Z$) Galois-qudit Paulis acting on different qudits are called $X$*-type* ($Z$*-type*) Galois-qudit Pauli strings.
Combining the $X$-type and $Z$-type strings with a $p$th root of unity forms a group called the *Galois-qudit Pauli group* on $n$ Galois qudits.
\end{defterm}

The Galois-qudit Pauli error set is a unitary basis for linear operators on the multi-qudit Hilbert space that is orthonormal under the Hilbert-Schmidt inner product; it is a nice error basis. The distance associated with this set is often the minimum weight of a Galois qudit Pauli string that implements a nontrivial logical operation in the code.

## General gates

- The normalizer of the Galois-qudit Pauli group  is the Galois-qudit Clifford group  ([arXiv:quant-ph/0211014](https://arxiv.org/abs/quant-ph/0211014)) ([doi:10.1007/978-3-319-44906-7](https://doi.org/10.1007/978-3-319-44906-7)).

## Decoders

- For few-qudit codes ($n$ is small), decoding can be based on a lookup table. For infinite code families, the size of such a table scales exponentially with $n$, so approximate decoding algorithms scaling polynomially with $n$ have to be used. The decoder determining the most likely error given a noise channel is called the *maximum-likelihood* (ML) decoder.
- RL-on-Greedy decoder based on reinforcement learning  ([arXiv:2506.03397](https://arxiv.org/abs/2506.03397)).

## Relations

- _parent_: [[concepts/qec/block-quantum]] — Galois-qudit codes are block quantum codes with $\Sigma=\mathbb{F}_q$.
- _parent_: [[concepts/qec/qecc-finite]]
- _parent_: [[concepts/qec/group-quantum]] — A Galois qudit for $q=p^m$ can be decomposed into a Kronecker product of $m$ modular qudits  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)); see  ([arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)).
Interpreted this way, Galois-qudit codes are group quantum codes whose physical spaces are constructed using Galois fields $\mathbb{F}_q$ as groups. More general versions of such qudits can be valued in a Galois ring  ([arXiv:2501.18968](https://arxiv.org/abs/2501.18968)), over which there also exists a Fourier transform  ([arXiv:0904.2560](https://arxiv.org/abs/0904.2560)).
- _cousin_: [[concepts/qec/qudits-into-qudits]] — A Galois qudit for $q=p^m$ can be decomposed into a Kronecker product of $m$ modular qudits; see  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)) ([arXiv:quant-ph/0501074](https://arxiv.org/abs/quant-ph/0501074)) ([arXiv:2408.10140](https://arxiv.org/abs/2408.10140), [arXiv:2408.09254](https://arxiv.org/abs/2408.09254)).
The two coincide when $q$ is prime, and reduce to qubits when $q=2$.
However, Pauli matrices for the two types of qudits are defined differently.
See  ([doi:10.1007/978-3-319-44906-7](https://doi.org/10.1007/978-3-319-44906-7)) for a side-by-side introduction to modular and Galois qudits.

## Notes

- Introduction to Galois qudits by [Gottesman](https://www.qec14.ethz.ch/slides/DanielGottesman.pdf).
- CodingTheory Julia software library .
- See  ([doi:10.1007/978-3-319-44906-7](https://doi.org/10.1007/978-3-319-44906-7)) for a side-by-side introduction to modular and Galois qudits.
