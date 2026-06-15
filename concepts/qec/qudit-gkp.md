---
type: concept
name: Modular-qudit GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Shift-resistant code
- Pre-GKP code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/gkp
- concepts/qec/quantum-perfect
- concepts/qec/qudit-css
- concepts/qec/rotor-gkp
- concepts/qec/single-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_gkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_gkp
---

# Modular-qudit GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_gkp) (`code_id: qudit_gkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit analogue of the GKP code.
Encodes a qudit into a larger qudit and protects against Pauli shifts up to some maximum value.

The simplest example requires an 18-dimensional qudit and admits stabilizer generators $Z^6$ and $X^6$.
A set of logical codewords is
\begin{align}
\begin{split}
|\overline{0}\rangle&=\frac{1}{\sqrt{3}}\left(|0\rangle+|6\rangle+|12\rangle\right)\\|\overline{1}\rangle&=\frac{1}{\sqrt{3}}\left(|3\rangle+|9\rangle+|15\rangle\right)~, \end{split}
\end{align}
and logical operators are $Z^3$ and $X^3$.

More generally, for qudit dimension $q = r_1 r_2 K$ for some positive integers $r_1$, $r_2$, and logical dimension $K$, the stabilizer generators are $Z^{r_1 K}$ and $X^{r_2 K}$.

(source: raw/error-correction-zoo.md)

## Protection

The above simple code corrects any Pauli string $X^{a}Z^{b}$ with $|a|,|b|\leq 1$.
A general code protects against any shift errors for which $|a| < r_1/2$ and $|b| < r_2/2$.

## General gates

- Not all logical Clifford gates can be realized using $q$-dimensional modular-qudit Clifford gates for certain values of $r_1,r_2$  ([arXiv:1307.5087](https://arxiv.org/abs/1307.5087)).

## Relations

- _parent_: [[concepts/qec/qudit-css]]
- _parent_: [[concepts/qec/single-subsystem]]
- _cousin_: [[concepts/qec/gkp]] — The square-lattice GKP code can be obtained from the modular-qudit code by taking the physical qudit dimension to be infinite  ([arXiv:quant-ph/0008040](https://arxiv.org/abs/quant-ph/0008040)).
- _cousin_: [[concepts/qec/quantum-perfect]] — The modular-qudit GKP code is not a block code, but it is perfect in the sense that each correctable error maps the logical space into a distinct error space.
- _cousin_: [[concepts/qec/rotor-gkp]] — The rotor GKP code can be thought of as a concatenation of a homological rotor code and a modular-qudit GKP code  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).
