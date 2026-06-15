---
type: concept
name: $((3,2,2))_3$ Three-qutrit single-deletion code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/four-qubit-permutation-invariant
- concepts/qec/permutation-invariant
- concepts/qec/qudits-into-qudits
- concepts/qec/small-distance-quantum
- concepts/qec/wasilewski-banaszek
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/three_qutrit_permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: three_qutrit_permutation_invariant
---

# $((3,2,2))_3$ Three-qutrit single-deletion code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/three_qutrit_permutation_invariant) (`code_id: three_qutrit_permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Three-qutrit PI code that is the smallest qutrit PI code to correct one deletion error.

The code admits the following logical codewords:
\begin{align}
  |\overline{0}\rangle &\propto|000\rangle+|111\rangle+|222\rangle\\
  |\overline{1}\rangle &\propto|012\rangle+|021\rangle+|102\rangle+|120\rangle+|201\rangle+|210\rangle~.
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

The smallest qutrit PI code to correct one deletion error.

## Relations

- _parent_: [[concepts/qec/qudits-into-qudits]]
- _parent_: [[concepts/qec/permutation-invariant]]
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/four-qubit-permutation-invariant]] — The four-qubit (three-qutrit) single-deletion code is the smallest PI qubit (qutrit) code to correct one deletion error.
- _cousin_: [[concepts/qec/wasilewski-banaszek]] — The three-qutrit single-deletion code maps to the Wasilewski-Banaszek code via the simplex mapping  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).
