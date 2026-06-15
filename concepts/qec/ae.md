---
type: concept
name: Æ code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/binomial
- concepts/qec/diatomic-molecular
- concepts/qec/gnu-permutation-invariant
- concepts/qec/single-spin
- concepts/qec/spins-into-spins
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ae
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ae
---

# Æ code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ae) (`code_id: ae`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code defined in a single angular-momentum subspace that is embedded in a larger direct-sum space of different angular momenta, which can arise from combinations of spin, electronic, or rotational, or nuclear angular momenta of an atom or molecule.
A code is obtained by solving an over-constrained system of equations, and many solutions can be mapped into existing codes defined on other state spaces.

A simple example of an Æ code is the error-detecting code with codewords
\begin{align}
\begin{split}
  |\overline{0}\rangle&=\frac{1}{\sqrt{2}}\left(|_{-m}^{J}\rangle+|_{m}^{J}\rangle\right)\\|\overline{1}\rangle&=|_{0}^{J}\rangle~,
\end{split}
\end{align}
constructed out of states of total angular momentum $J$ and its projection $m$ for any $J,m\geq 2$.
This code detects a single change in $m$ or $J$.

(source: raw/error-correction-zoo.md)

## Protection

Protects against noise native to atomic and molecular platforms, such as spontaneous emission, stray electromagnetic fields, and Raman scattering.
Noise operators arising from these processes, when restricted to the angular momentum degrees of freedom, change either the total angular momentum or its projection and correspond to matrices whose elements are particular combinations of Clebsch-Gordan coefficients.

## Realizations

- Trapped ions: smallest antisymmetric code protecting against dephasing has been realized by the Du group  ([arXiv:2504.16746](https://arxiv.org/abs/2504.16746)).

## Relations

- _parent_: [[concepts/qec/spins-into-spins]] — Æ codes protect against changes in both the total angular momentum $J$ and its projection $m$, with the former type necessarily causing the information to leak out of the space of a single spin.
- _cousin_: [[concepts/qec/single-spin]] — Since Æ codes are defined in a subspace of fixed total angular momentum and protect against errors linear in the angular-momentum generators, they can also be thought of as single-spin codes.
- _cousin_: [[concepts/qec/diatomic-molecular]] — Diatomic molecular codes are supported on states with various total angular momenta, while Æ codes are supported on only one subspace of fixed total momentum. The latter codes are more practical and applicable to other spin spaces.
- _cousin_: [[concepts/qec/binomial]] — Many well-performing Æ codes can be mapped into shifted versions of binomial codes via the Holstein-Primakoff mapping.
- _cousin_: [[concepts/qec/gnu-permutation-invariant]] — Many well-performing Æ codes can be mapped into GNU codes via the Dicke state mapping.
