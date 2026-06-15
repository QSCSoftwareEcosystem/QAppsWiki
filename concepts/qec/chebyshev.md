---
type: concept
name: Chebyshev code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/binomial
- concepts/qec/metopt
- concepts/qec/single-mode
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/chebyshev
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: chebyshev
---

# Chebyshev code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/chebyshev) (`code_id: chebyshev`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Single-mode bosonic Fock-state code that can be used for error-corrected sensing of a signal Hamiltonian ${\hat n}^s$, where ${\hat n}$ is the occupation number operator. 

Codewords for the $s$th-order Chebyshev code are
\begin{align}
\begin{split}
\ket{\overline 0} &=\sum_{k \text{~even}}^{[0,s]} \tilde{c}_k \Ket{\left\lfloor M\sin^2\left( k\pi/{2s}\right) \right\rfloor},\\
\ket{\overline 1} &= \sum_{k \text{~odd}}^{[0,s]} \tilde{c}_k \Ket{\left\lfloor M\sin^2 \left(k\pi/{2s}\right) \right\rfloor},
\end{split}
\end{align}
where $\tilde{c}_k>0$ can be obtained by solving a system of order $O(s^2)$ linear equations, and where $\lfloor x \rfloor$ is the floor function. The code approaches optimality for sensing the signal Hamiltonian as $M$ increases.

(source: raw/error-correction-zoo.md)

## Protection

The $s$th-order code corrects errors from the set $\{I,a,a^{\dagger},{\hat n},{\hat n}^2,\cdots,{\hat n}^{s-1}\}$.

## Relations

- _parent_: [[concepts/qec/single-mode]]
- _parent_: [[concepts/qec/metopt]]
- _cousin_: [[concepts/qec/binomial]] — Chebyshev codes resemble binomial codes, and a class of binomial codes have similar error-correcting properties  ([arXiv:1811.01450](https://arxiv.org/abs/1811.01450)).
