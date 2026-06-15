---
type: concept
name: Homological rotor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/css
- concepts/qec/rotor-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/homological_rotor
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: homological_rotor
---

# Homological rotor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/homological_rotor) (`code_id: homological_rotor`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CSS rotor code stabilized by a group of rotor $X$-type and $Z$-type generalized Pauli operators.
Codes are formulated using an extension of the qubit CSS-to-homology correspondence to rotors.
The homology group of the logical operators has a torsion component because the chain complexes are defined over the ring of integers, which yields codes with finite logical dimension, i.e., encoding logical qudits instead of only logical rotors.

A homological rotor code encoding $k$ logical rotors and a $q$-dimensional logical qudit is denoted as $⟦n,(k,q)⟧_{\mathbb{Z}}$ or $⟦n,(k,q),(d_X,\delta_Z)⟧_{\mathbb{Z}}$, where $d_X$ and $\delta_Z$ are the code's $X$ and $Z$ distances, respectively.
The subscript $\mathbb{Z}$ refers to the label used for the rotor's angular momentum, but shifts in the dual angular position degree of freedom are also used to construct stabilizers (the alternative subscript $U(1)$ is used in some cases).

The stabilizer group is defined using two integer matrices $H_X\in\mathbb{Z}^{r_X\times n}$ and $H_Z\in\mathbb{Z}^{r_Z\times n}$ which are such that
\begin{align}
      H_XH_Z^T = 0.\label{eq:commutation}
\end{align}
The stabilizer is then defined as
\begin{align}
  \mathsf{S}=\left\langle e^{-i\boldsymbol{s}H_{X}\cdot\hat{\boldsymbol{L}}}e^{i\boldsymbol{\varphi}H_{Z}\cdot\hat{\boldsymbol{\phi}}}\middle\vert\forall\boldsymbol{s}\in\mathbb{Z}^{r_{X}},\forall\boldsymbol{\varphi}\in U(1)^{r_{Z}}\right\rangle .\label{eq:stabilizer}
\end{align}
The condition \eqref{eq:commutation} ensures that $\mathsf{S}$ has a common +1 eigenspace.

As with CSS codes, there is a natural connection to a length-3 integer chain complex,
\begin{align}
  \mathcal{A}:~\mathbb{Z}^{r_X} \xrightarrow{H_X} \mathbb{Z}^n \xrightarrow{H_Z^T} \mathbb{Z}^{r_Z}~,
\end{align}
whose middle homology group describes the logical $X$ operators of the code.
The logical $Z$ operators are defined by the middle cohomology group where the cohomology is taken with phase coefficients, $\mathbb{T} = \mathbb{R}/2\pi\mathbb{Z}$,
\begin{align}
  \mathcal{A}^*:~\mathbb{T}^{r_X} \xleftarrow{H_X^T} \mathbb{T}^n \xleftarrow{H_Z} \mathbb{T}^{r_Z}.
\end{align}

The logical subspace can contain logical rotors as well as logical qudits.
The former correspond to the so-called free part of the homology group while the latter correspond to the torsion part,
\begin{align}
  H_1(\mathcal{A},\mathbb{Z}) = \mathbb{Z}^{k^\prime}\oplus\mathbb{Z}_{d_1}\oplus\cdots\oplus\mathbb{Z}_{d_{k^{\prime\prime}}}.
\end{align}
Stabilizer generator matrices equivalent under CSS rotor Clifford group transformations are classified by distinct Smith normal forms  ([arXiv:2303.13723](https://arxiv.org/abs/2303.13723), [arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).

(source: raw/error-correction-zoo.md)

## Protection

The $X$ distance $d_X$ of a code is the (slightly generalized notion of) weight of the smallest logical operator constructed out of angular position shifts.
The $Z$ distance $\delta_Z$ depends on whether or not the code encodes logical rotors, but a similar notion exists in the case of only a logical qudit encoding.
One can extend the idea of disjointness  ([arXiv:1710.07256](https://arxiv.org/abs/1710.07256)) to rotors to obtain distance bounds  ([arXiv:2303.13723](https://arxiv.org/abs/2303.13723)).

## Transversal gates

- All generalized Pauli gates are realized transversally.

## General gates

- Some logical gates come from the rotor Clifford group  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).

## Relations

- _parent_: [[concepts/qec/rotor-stabilizer]] — Homological rotor codes are rotor CSS codes constructed from chain complexes over the integers in an extension of the qubit CSS-to-homology correspondence to rotors.
- _parent_: [[concepts/qec/css]] — Homological rotor codes are rotor CSS codes constructed from chain complexes over the integers in an extension of the qubit CSS-to-homology correspondence to rotors. The homology group of the logical operators has a torsion component because the chain complexes are defined over the ring of integers, which yields codes with finite logical dimension. Products of chain complexes can also yield rotor codes.

## Notes

- A [Sage notebook](https://github.com/cianibegood/quantum-rotor-codes) of small examples.
