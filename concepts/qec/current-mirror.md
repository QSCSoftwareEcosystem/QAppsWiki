---
type: concept
name: Kitaev current-mirror qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/1d-stabilizer
- concepts/qec/gkp
- concepts/qec/homological-rotor
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/current_mirror
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: current_mirror
---

# Kitaev current-mirror qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/current_mirror) (`code_id: current_mirror`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of the family of $⟦2n,(0,2),(2,n)⟧_{\mathbb{Z}}$ homological rotor codes storing a logical qubit on a thin Möbius strip.
The ideal code can be obtained from a Josephson-junction  ([doi:10.1093/acprof:oso/9780199681181.003.0003](https://doi.org/10.1093/acprof:oso/9780199681181.003.0003)) system  ([arXiv:2303.13723](https://arxiv.org/abs/2303.13723)).

Logical codewords can be expressed in the basis of angular momentum states as
\begin{align}
\begin{split}
  |\overline{0}\rangle&=\sum_{\overset{\ell_{1},\dots,\ell_{n}\in\mathbb{Z}}{\sum_{k=1}^{n}\ell_{k}=\mathrm{even}}}\left|\ell_{1},\dots,\ell_{n},-\ell_{1},\dots,-\ell_{n}\right\rangle \\|\overline{1}\rangle&=\sum_{\overset{\ell_{1},\dots,\ell_{n}\in\mathbb{Z}}{\sum_{k=1}^{n}\ell_{k}=\mathrm{odd}}}\left|\ell_{1},\dots,\ell_{n},-\ell_{1},\dots,-\ell_{n}\right\rangle~.
\end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

Protection in the context of superconducting circuits investigated in Ref.  ([arXiv:1908.04615](https://arxiv.org/abs/1908.04615)).

## General gates

- One- and two-qubit phase gates utilizing ancillary oscillators in GKP states  ([arXiv:cond-mat/0609441](https://arxiv.org/abs/cond-mat/0609441)).

## Relations

- _parent_: [[concepts/qec/homological-rotor]]
- _parent_: [[concepts/qec/1d-stabilizer]]
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/gkp]] — Current-mirror code phase gates utilize ancillary oscillators in square-lattice GKP states  ([arXiv:cond-mat/0609441](https://arxiv.org/abs/cond-mat/0609441), [arXiv:1302.4122](https://arxiv.org/abs/1302.4122)).
