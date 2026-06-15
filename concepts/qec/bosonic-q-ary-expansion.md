---
type: concept
name: Bosonic $q$-ary expansion
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fock-state
- concepts/qec/qudits-into-qudits
- concepts/qec/single-mode
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bosonic_q-ary_expansion
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bosonic_q-ary_expansion
---

# Bosonic $q$-ary expansion

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bosonic_q-ary_expansion) (`code_id: bosonic_q-ary_expansion`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A one-to-one mapping between basis states on $n$ prime-dimensional qudits (of dimension $q=p$) and the subspace of the first $p^n$ single-mode Fock states.
While this mapping offers a way to map qudits into a single mode, noise models for the two code families induce different notions of locality and thus qualitatively different physical interpretations  ([arXiv:2111.08894](https://arxiv.org/abs/2111.08894)).

The mapping allows one to think of the Fock subspace as a tensor product of $n$ $p$-dimensional qudits by performing a $p$-ary expansion of the Fock-state labels and treating each digit as an index of a qudit basis state.
The Fock state integer label $N\geq 0$ is expanded in the $p$-ary expansion as
\begin{align}
    N=\sum_{\mu=0}^{\infty}b_{\mu}p^{\mu}~,
\end{align}
with each $p$-ary digit $b_{\mu}\in\mathbb{Z}_p$ corresponding to the basis-state label of qudit $\mu$.

In the binary case, the first qubit's $Z$-operator is the parity operator $Z_0=(-1)^{\hat{n}}$, while the second qubit's $Z$-operator is the two-photon parity $Z_1=(-1)^{\frac{1}{2}\hat{n}(\hat{n}-1)}$  ([arXiv:1106.3800](https://arxiv.org/abs/1106.3800), [arXiv:2012.06994](https://arxiv.org/abs/2012.06994)). 
These satisfy $Z_{1}aZ_{1}=aZ_{0}$.

Pauli operators for the constituent qudits can be expressed in terms of bosonic raising and lowering operators.
The modular-qudit Pauli-$Z$ operator for qudit $\mu$ is the Fock-space rotation
\begin{align}
  Z_{\mu}=\exp\left[i\frac{2\pi}{p}{\hat{n} \choose p^{\mu}}\right]~,
\end{align}
where $\hat n$ is the mode's occupation number operator.
This can be proven by Lucas's theorem.

The Pauli-$X$ operator is expressed as
\begin{align}
  X_{\mu}=\frac{1-P_{\mu}^{(p-1)}}{\sqrt{\left(\hat{n}+p^{\mu}\right)_{p^{\mu}}}}a^{p^{\mu}}+\frac{P_{\mu}^{(p-1)}}{\sqrt{\left(\hat{n}\right)_{p^{\mu}(p-1)}}}a^{\dagger p^{\mu}\left(p-1\right)}~,
\end{align}
where $\left(a\right)_{b}$ is the falling factorial, and where the qudit projector is
\begin{align}
  P_{\mu}^{(k)}=\frac{1}{p}\sum_{l\in\mathbb{Z}_{p}}Z_{\mu}^{l}e^{-i\frac{2\pi}{p}kl}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/fock-state]] — The bosonic $q$-ary expansion allows one to map between prime-dimensional qudit states and a Fock subspace of a single mode.
- _parent_: [[concepts/qec/single-mode]]
- _cousin_: [[concepts/qec/qudits-into-qudits]] — The bosonic $q$-ary expansion allows one to map between prime-dimensional qudit states and a Fock subspace of a single mode.
