---
type: concept
name: Icosahedral spin code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/j-gross
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/icosahedral_spin
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: icosahedral_spin
---

# Icosahedral spin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/icosahedral_spin) (`code_id: icosahedral_spin`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A spin-$7/2$ single-spin code designed to realize the binary icosahedral group $2I$ using $SU(2)$ rotations  ([arXiv:2005.10910](https://arxiv.org/abs/2005.10910)).
The codespace is a two-dimensional irrep subspace obtained by restricting the spin-$7/2$ representation of $SU(2)$ to the subgroup $2I$.
Under the Dicke-state mapping, this code is equivalent to the $((7,2,3))$ Pollatsek-Ruskai permutation-invariant code  ([arXiv:2005.10910](https://arxiv.org/abs/2005.10910), [arXiv:2305.07023](https://arxiv.org/abs/2305.07023)).

The code has unnormalized logical states
\begin{align}
  \begin{split}
    |0_{L}\rangle&\propto\sqrt{3}|_{7/2}^{7/2}\rangle+\sqrt{7}|_{-3/2}^{7/2}\rangle\\
    |1_{L}\rangle&\propto\sqrt{7}|_{3/2}^{7/2}\rangle-\sqrt{3}|_{-7/2}^{7/2}\rangle\,.
  \end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/j-gross]] — The icosahedral spin code is the $2I$ example of a Clifford-group spin code  ([arXiv:2005.10910](https://arxiv.org/abs/2005.10910)).
