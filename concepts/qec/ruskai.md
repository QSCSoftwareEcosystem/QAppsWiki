---
type: concept
name: $((9,2,3))$ Ruskai code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/gnu-permutation-invariant
- concepts/qec/shor-nine
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ruskai
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ruskai
---

# $((9,2,3))$ Ruskai code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ruskai) (`code_id: ruskai`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Nine-qubit PI code that protects against single-qubit errors as well as two-qubit errors arising from exchange processes.

In terms of Dicke states, the codewords are
\begin{align}
  \begin{split}
    |0_{L}\rangle&\propto|D_{0}^{9}\rangle+\sqrt{3}|D_{6}^{9}\rangle\\
    |1_{L}\rangle&\propto\sqrt{3}|D_{3}^{9}\rangle+|D_{9}^{9}\rangle~.
  \end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

Protects against all single-qubit errors as well as two-qubit errors arising from exchange processes.

## Relations

- _parent_: [[concepts/qec/gnu-permutation-invariant]] — The $((9,2,3))$ Ruskai code is a GNU PI code  ([arXiv:1302.3247](https://arxiv.org/abs/1302.3247)).
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/shor-nine]] — The $((9,2,3))$ Ruskai code results from projecting the Shor code into the PI qubit subspace  ([arXiv:quant-ph/9906114](https://arxiv.org/abs/quant-ph/9906114)).
