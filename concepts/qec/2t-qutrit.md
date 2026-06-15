---
type: concept
name: 2T-qutrit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qsc
- concepts/qec/two-mode-binomial
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/2t_qutrit
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 2t_qutrit
---

# 2T-qutrit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/2t_qutrit) (`code_id: 2t_qutrit`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Two-mode qutrit code constructed out of superpositions of coherent states whose amplitudes make up the binary tetrahedral group $2T$, a.k.a. the 24-cell.

The codespace is a particular three-dimensional subspace of the 24-dimensional two-mode coherent-state subspace,
\begin{align}
  \mathrm{Span}( \{|\sqrt{2} e^{i (2k+1) \pi/4} \alpha\rangle |0\rangle,  |0\rangle |\sqrt{2} e^{i (2k+1) \pi/4} \alpha\rangle, |e^{i k\pi/2} \alpha\rangle |e^{i \ell \pi/2} \alpha\rangle \: : \: 0\leq  k, \ell \leq 3\})
\end{align}
for any $\alpha \geq 0$.
A basis can be constructed whose elements are uniform superpositions of coherent states whose amplitudes make up cosets of the quaternion subgroup $Q$ in $2T$.

(source: raw/error-correction-zoo.md)

## General gates

- Logical phase-flip can be implemented using an excitation-preserving Gaussian transformation. Degree-four polynomial in the lowering operators of the two modes serves as a non-unitary logical bit-flip. Rotations of either mode by $\pi/4$ are logical gates that swap two logical codewords.

## Relations

- _parent_: [[concepts/qec/qsc]] — The $2T$-qutrit is a QSC on the two-dimensional complex sphere whose code constellation is the $4\{3\}4$ complex polytope.
- _cousin_: [[concepts/qec/two-mode-binomial]] — The $2T$-qutrit code reduces to the two-mode "0-2-4" binomial code as $\alpha\to 0$.
- _cousin_: [`24cell`](https://errorcorrectionzoo.org/c/24cell) — The $2T$-qutrit code is constructed out of superpositions of coherent states whose amplitudes make up the binary tetrahedral group $2T$, a.k.a. the 24-cell.
