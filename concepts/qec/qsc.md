---
type: concept
name: Quantum spherical code (QSC)
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ampdamp
- concepts/qec/coherent-constellation
- concepts/qec/group-representation
- concepts/qec/single-spin
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qsc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qsc
---

# Quantum spherical code (QSC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qsc) (`code_id: qsc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose codewords are superpositions of points on an $n$-dimensional real or complex sphere.
Such codes can in principle be defined on any configuration space housing a sphere, but the focus of this entry is on QSCs constructed out of coherent-state constellations.

More technically, a QSC is a collection $\{\mathcal{C}_k\}_{k=1}^K$ of *logical constellations*, each of which yields a codeword by taking a quantum superposition of all points $\mathbf{x}\in \mathcal{C}_k$.
Taken together, the logical constellations yield the *code constellation*, $\mathcal{C}=\bigcup_{k=1}^{K}\mathcal{C}_{k}$.

Codewords of coherent-state QSCs of uniform superposition are defined as
\begin{align}
  |\mathcal{C}_{k}\rangle\sim\frac{1}{\sqrt{|{\mathcal{C}}_{k}|}}\sum_{\boldsymbol{\alpha}\in\mathcal{C}_{k}}|\sqrt{\bar{N}}\boldsymbol{\alpha}\rangle~,
\end{align}
where $ |\boldsymbol{\alpha} \rangle = |\alpha_1,\alpha_2,...\alpha_n \rangle $ is an $n$-mode coherent state.
This asymptotic expression is valid in the limit of large energy $\bar{N}\to\infty$.

Coherent-state QSCs on $n$ modes are denoted by
$((n,K,d_E,\langle t_{\downarrow},d_{\updownarrow},d_{\downarrow}\rangle))$,
where $K$ is codespace dimension, $d_E$ is the *squared minimum distance*, i.e., the smallest Euclidean distance between pairs of distinct points across all codewords, and $ t_{\downarrow},d_{\updownarrow},d_{\downarrow} $ are the number of *correctable* losses (plus 1), the degree distance, and the number of *detectable* losses (plus 1), respectively.

(source: raw/error-correction-zoo.md)

## Protection

The *resolution* $d_E$ of the code is defined as
  \begin{align}
    d_E = \min_{\boldsymbol{\alpha},\boldsymbol{\beta}\in\mathcal{C}} \Vert\boldsymbol{\alpha}-\boldsymbol{\beta}\Vert^2~.
  \end{align}
The code protects against passive Gaussian transformations, which manifest as rotations on the sphere, $ |\boldsymbol{\alpha}\rangle \rightarrow |\mathbf{R}\boldsymbol{\alpha}\rangle $ for all $\mathbf{R}$.
Detectable transformations correspond to rotations for which
  \begin{align}
    \Vert \mathbf{R}\boldsymbol{\alpha} - \boldsymbol{\alpha}\Vert^2 < d_E~,
  \end{align}
in the large $\bar{N}$ limit.

The code also protects against general ladder errors, which are defined as
\begin{align}
  \mathbf{a}^{\dagger\mathbf{p}}\mathbf{a}^{\mathbf{q}}=\prod_{j=1}^{n}a_{j}^{\dagger p_{j}}a_{j}^{q_{j}}~.
\end{align}
Any AD ladder error $\mathbf{a}^{\mathbf{q}}$ with $|\mathbf{q}|<d_{\downarrow}$ is detectable.
Any ladder error $\mathbf{a}^{\dagger\mathbf{p}}\mathbf{a}^{\mathbf{q}}$ with $|\mathbf{p}|,|\mathbf{q}|<t_{\downarrow}$ is detectable, implying that up to $t_{\downarrow}-1$ losses are correctable.
Any ladder error with degree $|\mathbf{p}+\mathbf{q}|<d_{\updownarrow}$ is detectable.

## Decoders

- Lindbladian scheme stabilizing all points in the constellation and protecting from the AD operator $E_{0}^{\otimes n}$  ([arXiv:2302.11593](https://arxiv.org/abs/2302.11593)).

## Relations

- _parent_: [[concepts/qec/coherent-constellation]] — Coherent-state QSCs are coherent-state constellation codes constrained to lie on a sphere.
- _parent_: [[concepts/qec/ampdamp]] — QSC codewords are superpositions of coherent states with the same energy, but coherent states are not eigenstates of the energy Hamiltonian. The AD Kraus operator $E_{0}^{\otimes n}$ acts identically on each coherent state by shrinking the radius of the QSC's sphere.
- _cousin_: [[concepts/qec/group-representation]] — QSCs should be able to be formulated as group-representation codes whose group is that formed by the permutation representation of the code polytope symmetry group, but this representation may be reducible.
- _cousin_: [`points_into_spheres`](https://errorcorrectionzoo.org/c/points_into_spheres) — QSCs are quantum counterparts of spherical and constant-energy codes because they store information in quantum superpositions of points on a sphere in quantum phase space.
- _cousin_: [`spherical`](https://errorcorrectionzoo.org/c/spherical) — QSCs are quantum counterparts of spherical and constant-energy codes because they store information in quantum superpositions of points on a sphere in quantum phase space.
- _cousin_: [[concepts/qec/single-spin]] — Single-spin codes whose codewords are expressed in terms of discrete sets of spin-coherent states may also be interpreted as QSCs.
- _cousin_: [`polytope`](https://errorcorrectionzoo.org/c/polytope) — QSCs can be constructed by using vertices of polytopes for logical constellations. The logical constellations form the vertices of the code constellation, a polytope compound.
