---
type: concept
name: Operator-algebra QECC (OAQECC)
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-oaecc
- concepts/qec/quantum-into-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/oaecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: oaecc
---

# Operator-algebra QECC (OAQECC)

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/oaecc) (`code_id: oaecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code family that encompasses ordinary (i.e., subspace) codes, subsystem codes, classical-quantum codes, and hybrid codes using an operator-algebraic framework.

A simple example encompassing elements of all subfamilies encodes quantum information and a single classical bit into a direct sum of two subsystem codes.
A quantum subsystem code $\mathsf{A}_j\otimes\mathsf{B}_j$, with $\mathsf{A}_j$ the logical factor associated with the quantum information, and $\mathsf{B}_j$ the gauge factor, is associated with each of the two values $j\in\{1,2\}$ of the classical bit.
The corresponding decomposition of the Hilbert space $\mathsf{H}$ is
\begin{align}
  \mathsf{H}=(\mathsf{A}_{1}\otimes\mathsf{B}_{1})\oplus(\mathsf{A}_{2}\otimes\mathsf{B}_{2})\oplus\mathsf{C}^{\perp}~,
\end{align}
where $\mathsf{C}^\perp$ is the combined error space of both codes.
The above code reduces to a subsystem code when $\mathsf{A}_{2}\otimes\mathsf{B}_{2}$ is trivial, reduces to a classical-quantum code when $\mathsf{A}_{1,2}$ are both trivial, reduces to a hybrid code when $\mathsf{B}_{1,2}$ are both trivial, and reduces to an ordinary (i.e., subspace) code when $\mathsf{B}_1$ and $\mathsf{A}_{2}\otimes\mathsf{B}_{2}$ are both trivial.

In general, an OAQECC is determined by a finite dimensional $C^*$ algebra $\mathcal{A}$ of operators on $\mathsf{H}$.
This *logical algebra* induces a decomposition of the Hilbert space as
\begin{align}\mathsf{H} = \bigoplus_\gamma \mathsf{A}_\gamma \otimes \mathsf{B}_\gamma,\end{align}
with respect to which $\mathcal{A}$ takes the form
\begin{align}\mathcal{A} = \bigoplus_\gamma I_\gamma \otimes \mathcal{L}(\mathsf{B}_\gamma),\end{align}
where $\mathcal{L}(\mathsf{B}_\gamma)$ denotes the full set of linear maps on $\mathsf{B}_\gamma$.
The $\mathsf{A}_{\gamma}$ factors can be used to store quantum information, $\gamma$ indexes the block structure of the code, while $\mathsf{B}_{\gamma}$ determine its gauge structure.
Together, the above forms the most general form of an information preserving structure  ([arXiv:quant-ph/9908066](https://arxiv.org/abs/quant-ph/9908066), [arXiv:quant-ph/0402056](https://arxiv.org/abs/quant-ph/0402056), [arXiv:quant-ph/0507213](https://arxiv.org/abs/quant-ph/0507213), [arXiv:quant-ph/0603252](https://arxiv.org/abs/quant-ph/0603252), [arXiv:0705.4282](https://arxiv.org/abs/0705.4282), [arXiv:1006.1358](https://arxiv.org/abs/1006.1358)).
Logical operators form the commutant of $\mathcal{A}$ as a result of the double commutant (a.k.a. double centralizer) theorem  ([arXiv:math-ph/9807030](https://arxiv.org/abs/math-ph/9807030)).

(source: raw/error-correction-zoo.md)

## Protection

Given an error operation $\mathcal{E}$, one says that $\mathcal{A}$ is *correctable* for $\mathcal{E}$ if there exists a recovery operation $\mathcal{R}$ such that
\begin{align}\Pi_{\mathcal{A}} (\mathcal{R} \circ \mathcal{E})^\dagger(X) \Pi_{\mathcal{A}} = X\end{align} for all $X \in \mathcal{A}$, where $\Pi_{\mathcal{A}}$ is the unit projection onto $\mathcal{A}$.

Equivalently, $\mathcal{A}$ is correctable for $\mathcal{E}$ if there exists a recovery operation $\mathcal{R}$ such that for any $\gamma$ and density operators $\rho_\gamma,\sigma_\gamma$ supported on $\mathsf{A}_\gamma$ and $\mathsf{B}_\gamma$, respectively, there exists a state $\tau_\gamma$ supported on $\mathsf{A}_\gamma$ such that
\begin{align}(\mathcal{R} \circ \mathcal{E})(\rho_\gamma \otimes \sigma_\gamma) = \tau_\gamma \otimes \sigma_\gamma.\end{align}

An algebraic condition for correctability can be given in terms of the Kraus operators $E_j$ of $\mathcal{E}$.
Indeed, $\mathcal{A}$ is correctable for $\mathcal{E}$ if \begin{align}\Pi_{\mathcal{A}} E_j^\dagger E_k \Pi_{\mathcal{A}} \in \mathcal{A}'\end{align}
for all $j,k$, where $\mathcal{A}'$ is the commutant of $\mathcal{A}$.

Conversely, a *private* algebra $\mathcal{A}$ for a channel $\mathcal{E}$ is one which is completely decohered by the channel  ([arXiv:quant-ph/0403161](https://arxiv.org/abs/quant-ph/0403161)).
In other words, no information about the algebra is retained after the action of the channel.
Tradeoffs between error correction and privacy have been studied  ([arXiv:1811.10425](https://arxiv.org/abs/1811.10425)).

## Relations

- _parent_: [[concepts/qec/quantum-into-quantum]]
- _cousin_: [[concepts/qec/approximate-oaecc]] — Approximate OAQECCs correcting a noise channel exactly reduce to OAQECCs.
