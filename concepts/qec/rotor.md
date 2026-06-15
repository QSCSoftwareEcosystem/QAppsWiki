---
type: concept
name: Rotor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Angle-number code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rotor
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rotor
---

# Rotor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rotor) (`code_id: rotor`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes a *logical* Hilbert space, finite- or infinite-dimensional, into a *physical* Hilbert space of $L^2$-normalizable functions on either the integers $\mathbb Z$ or the circle group $U(1)$.
This space is colloquially referred to as a (planar) rotor.
Ideal codewords may not be normalizable because the space is infinite-dimensional, so approximate versions have to be constructed in practice.

(source: raw/error-correction-zoo.md)

## Protection

\subsection{Rotor generalized Pauli error basis}
A rotor analogue of the Pauli string basis for qubit codes consists of rotor *generalized Pauli operators*.

\begin{defterm}{Rotor generalized Pauli strings}
\label{topic:rotor-pauli}
For a single rotor, its elements are products of exponentials of the rotor's angular position ($\hat\phi$) and angular momentum ($\hat L$) operators, acting on the rotor's angular position states $|\phi\rangle$ for $\phi\in U(1)$ as
\begin{align}
  e^{-i\varphi\hat{L}}\left|\phi\right\rangle =\left|\phi+\varphi\right\rangle \,\,\text{ and }\,\,e^{i\ell\hat{\phi}}\left|\phi\right\rangle =e^{i\ell\phi}\left|\phi\right\rangle ~,
\end{align}
where $\varphi\in U(1)$ and $\ell\in\mathbb{Z}$.
For multiple rotors, error set elements are tensor products of elements of the single-rotor error set, characterized by vectors of angle and integer coefficients multiplying vectors of angular momentum $\hat{\boldsymbol{L}}$ and angular position $\hat{\boldsymbol{\phi}}$ operators.
These satisfy the usual Weyl-type commutation relations but do not violate the Stone-von Neumann theorem because $\ell$ is restricted to be an integer (cf.  ([doi:10.1007/978-1-4614-7116-5](https://doi.org/10.1007/978-1-4614-7116-5))).
\end{defterm}

## General gates

- The normalizer of the rotor Pauli group is the $n$-*rotor Clifford group*  ([arXiv:1409.3208](https://arxiv.org/abs/1409.3208), [arXiv:1911.00099](https://arxiv.org/abs/1911.00099)). The rotor Clifford group permutes rotor Pauli operators amongst themselves, and, up to any phases, is equivalent to $U(1)^{n(n+1)/2} \rtimes GL(n,\mathbb{Z})$  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).

## Relations

- _parent_: [[concepts/qec/group-quantum]] — Group quantum codes whose physical spaces are constructed using either the group of the integers $\mathbb{Z}$ or the circle group $U(1)$ are rotor codes.

## Notes

- See Refs.  ([arXiv:1601.03843](https://arxiv.org/abs/1601.03843), [arXiv:1709.04460](https://arxiv.org/abs/1709.04460)) ([arXiv:1911.00099](https://arxiv.org/abs/1911.00099)) for introductions to rotor Hilbert spaces.
