---
type: concept
name: Zero-pi qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/gkp
- concepts/qec/homological-rotor
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/zero_pi
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: zero_pi
---

# Zero-pi qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/zero_pi) (`code_id: zero_pi`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦2,(0,2),(2,1)⟧_{\mathbb{Z}}$ homological rotor code on the smallest tiling of the projective plane $\mathbb{R}P^2$.
The ideal code can be obtained from a four-rotor Josephson-junction  ([doi:10.1093/acprof:oso/9780199681181.003.0003](https://doi.org/10.1093/acprof:oso/9780199681181.003.0003)) system after a choice of grounding  ([arXiv:2303.13723](https://arxiv.org/abs/2303.13723)).

Logical codewords can be expressed in the basis of angular momentum states as
\begin{align}
\begin{split}
  |\overline{0}\rangle&=\sum_{\ell\in\mathbb{Z}}\left|2\ell,-2\ell\right\rangle \\|\overline{1}\rangle&=\sum_{\ell\in\mathbb{Z}}\left|2\ell+1,-2\ell-1\right\rangle~.
\end{split}
\end{align}
An alternative codeword basis in terms of angular position states is
\begin{align}
\begin{split}
  |\overline{+}\rangle&=\intop_{U(1)}\textnormal{d}\phi\left|\phi,\phi\right\rangle \\|\overline{-}\rangle&=\intop_{U(1)}\textnormal{d}\phi\left|\phi,\phi+\pi\right\rangle~.
\end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

Protection in the context of superconducting circuits was investigated in Ref.  ([arXiv:1708.02886](https://arxiv.org/abs/1708.02886)).

## General gates

- One- and two-qubit phase gates utilizing ancillary oscillators in GKP states  ([arXiv:cond-mat/0609441](https://arxiv.org/abs/cond-mat/0609441), [arXiv:1302.4122](https://arxiv.org/abs/1302.4122)).
- Protected phase gate  ([arXiv:2503.14634](https://arxiv.org/abs/2503.14634)).

## Fault tolerance

- One- and two-qubit phase gate errors can be suppressed  ([arXiv:1302.4122](https://arxiv.org/abs/1302.4122)).

## Realizations

- A related superconducting circuit has been realized by the Houck group  ([arXiv:1910.07542](https://arxiv.org/abs/1910.07542)).

## Relations

- _parent_: [[concepts/qec/homological-rotor]]
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/gkp]] — Zero-pi code phase gates utilize ancillary oscillators in square-lattice GKP states  ([arXiv:cond-mat/0609441](https://arxiv.org/abs/cond-mat/0609441), [arXiv:1302.4122](https://arxiv.org/abs/1302.4122)).

## Notes

- The zero-pi qubit is based on earlier blueprints for protected subspaces using superconducting circuits  ([arXiv:cond-mat/0202115](https://arxiv.org/abs/cond-mat/0202115), [arXiv:cond-mat/0205186](https://arxiv.org/abs/cond-mat/0205186)).
