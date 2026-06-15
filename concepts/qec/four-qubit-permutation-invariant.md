---
type: concept
name: $((4,2,2))$ Four-qubit single-deletion code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/binomial
- concepts/qec/combinatorial-permutation-invariant
- concepts/qec/gnu-permutation-invariant
- concepts/qec/stab-4-2-2
- concepts/qec/unentangled-permutation-invariant
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/four_qubit_permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: four_qubit_permutation_invariant
---

# $((4,2,2))$ Four-qubit single-deletion code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/four_qubit_permutation_invariant) (`code_id: four_qubit_permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Four-qubit PI code that is the smallest qubit code to correct one deletion error.

In terms of Dicke states, a basis of logical codewords is
\begin{align}
\begin{split}
  |0_{L}\rangle&=\frac{1}{\sqrt{2}}\left(|D_{0}^{4}\rangle+|D_{4}^{4}\rangle\right)\\
  |1_{L}\rangle&=|D_{2}^{4}\rangle~.
\end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

The smallest qubit PI code to correct one deletion error.

## Relations

- _parent_: [[concepts/qec/gnu-permutation-invariant]] — The four-qubit single-deletion code is a GNU code for $g=m=2$  ([arXiv:2102.02494](https://arxiv.org/abs/2102.02494)).
- _parent_: [[concepts/qec/unentangled-permutation-invariant]] — The Bravyi-Lee-Li-Yoshida code reduces to the four-qubit single-deletion code for $n=4$.
- _cousin_: [[concepts/qec/binomial]] — The four-qubit single-deletion code can be obtained from the "0-2-4" single-mode binomial code by substituting Fock states with Dicke states.
- _cousin_: [[concepts/qec/stab-4-2-2]] — Projecting the four-qubit code into the PI subspace yields the four-qubit single-deletion code. A basis of codewords for the four-qubit single-deletion code consists of the $|\overline{00}\rangle$ and $|\overline{01}\rangle+|\overline{10}\rangle+|\overline{11}\rangle$ states of the four-qubit code.
- _cousin_: [[concepts/qec/combinatorial-permutation-invariant]] — The combinatorial PI code $Q_{1,1,1,-}$ is another example of a four-qubit code correcting a single deletion error  ([arXiv:2310.05358](https://arxiv.org/abs/2310.05358)).
