---
type: concept
name: Approximate operator-algebra QECC
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-into-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/approximate_oaecc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: approximate_oaecc
---

# Approximate operator-algebra QECC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/approximate_oaecc) (`code_id: approximate_oaecc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code encoding quantum and/or classical information that approximately corrects against noise affecting operators forming an algebra.

(source: raw/error-correction-zoo.md)

## Protection

Given an algebra $\mathcal{A}$, $\mathcal{A}$ is *$\epsilon$-correctable* under noise channel $\mathcal{N}$ if there exists some quantum channel $\mathcal{R}$ such that
\begin{align}
  ||(\mathcal{R}\circ\mathcal{N})-P_{\mathcal{A}}||_{\diamond}\leq\epsilon~,
\end{align}
where $P_{\mathcal{A}}$ is the projector onto algebra $\mathcal{A}$ and we use the diamond norm $\diamond$  ([arXiv:quant-ph/9806029](https://arxiv.org/abs/quant-ph/9806029)).

Let the minimal error for some algebra $\mathcal{A}$ under noise channel $\mathcal{N}$ be
\begin{align}
  \epsilon_{\mathcal{A}}=\min_{\mathcal{R}} ||\mathcal{R}\circ\mathcal{N}-P_{\mathcal{A}}||_{\diamond}~.
\end{align}
Let $\delta_{\mathcal{A}}=||\mathcal{N}^C-\mathcal{N}^C\circ P_{\mathcal{A}'}||_{\diamond}$
for the commutant $\mathcal{A}'$ of algebra $\mathcal{A}$ and the complementary channel $\mathcal{N}^C$ of noise channel $\mathcal{N}$. Then  ([arXiv:0907.4207](https://arxiv.org/abs/0907.4207)),
\begin{align}
  \delta_{\mathcal{A}}^2/4\leq \epsilon_{\mathcal{A}}\leq 2\delta_{\mathcal{A}}^{1/2}~.
\end{align}

\subsection{Complementary channel formulation}

Given the projector $\mathcal{P}_{\mathcal{A}}$ onto algebra $\mathcal{A}$ and a noise channel $\mathcal{N}$,
we can quantify approximate operator algebra error correction using worst-case entanglement fidelity $F$ as
\begin{align}F(R\mathcal{N},\mathcal{P}_{\mathcal{A}})\geq 1-\epsilon\end{align}
for some small $\epsilon$ and recovery channel $R$.

This is equivalent to considering the complementary channel $\mathcal{N}^C$
with projector $\mathcal{P}_{\mathcal{A}'}$ onto the commutant $\mathcal{A}'$ of $\mathcal{A}$ such that
\begin{align}
  F(\mathcal{N}^C,R'\mathcal{P}_{\mathcal{A}'})\geq 1-\epsilon
\end{align}
for that same value of $\epsilon$ and some channel $R'$.

This formulation gives a necessary and sufficient condition for approximate operator-algebra QECCs.
It implies the standard operator-algebra correctability conditions, $[A,V^{\dagger}E_i^{\dagger}E_jV]=0$ for all $A\in\mathcal{A}$, in the exact limit  ([arXiv:0907.5391](https://arxiv.org/abs/0907.5391)).
In particular, the same ideas have been extended to locality-restricted settings, where recovery operations must respect spatial or subsystem constraints (see  ([arXiv:1806.10324](https://arxiv.org/abs/1806.10324)) for the generalization).
Private algebras are correctable algebras for the complementary channel  ([arXiv:0711.3438](https://arxiv.org/abs/0711.3438)).

## Relations

- _parent_: [[concepts/qec/quantum-into-quantum]]
