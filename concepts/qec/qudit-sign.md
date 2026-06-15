---
type: concept
name: Modular-qudit shift-resistant code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-perfect
- concepts/qec/quantum-repetition
- concepts/qec/qudit-css
- concepts/qec/qudit-gkp
- concepts/qec/single-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_sign
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_sign
---

# Modular-qudit shift-resistant code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_sign) (`code_id: qudit_sign`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Monolithic code encoding a qubit into a single modular qudit and protecting against either $Z$-type or $X$-type modular-qudit Pauli shifts.

The simplest example requires a 6-dimensional qudit.
The bit-flip version admits codewords $|0\rangle$ and $|3\rangle$ and corrects a single $X$-type shift.
The phase-flip version admits codewords 
\begin{align}
\begin{split}
|\overline{0}\rangle&=\frac{1}{\sqrt{6}}\sum_{j=0}^{5}|j\rangle\\|\overline{1}\rangle&=\frac{1}{\sqrt{6}}\sum_{j=0}^{5}(-1)^{j}|j\rangle\,.
\end{split}
\end{align}
Both codes are modular-qudit CSS codes with stabilizer generators $Z^2$ and $X^2$, respectively.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qudit-css]]
- _parent_: [[concepts/qec/single-subsystem]]
- _cousin_: [[concepts/qec/qudit-gkp]] — The modular-qudit shift-resistant code requires a smaller physical qudit dimension but protects against only one type of error  ([arXiv:0705.1099](https://arxiv.org/abs/0705.1099)).
- _cousin_: [[concepts/qec/quantum-perfect]] — The modular-qudit shift-resistant code is not a block code, but it is perfect in the sense that each correctable error maps the logical space into a distinct error space  ([arXiv:0705.1099](https://arxiv.org/abs/0705.1099)).
- _cousin_: [[concepts/qec/quantum-repetition]] — Both the quantum repetition and modular-qudit shift-resistant codes protect against only one type of noise.
