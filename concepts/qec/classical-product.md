---
type: concept
name: Classical-product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qldpc
- concepts/qec/quantum-tanner
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/classical_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: classical_product
---

# Classical-product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/classical_product) (`code_id: classical_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A QLDPC qubit CSS code constructed by separately constructing the $X$ and $Z$ check matrices using product constructions from classical codes. A particular $⟦512,174,8⟧$ code performed well  ([arXiv:2209.13474](https://arxiv.org/abs/2209.13474)) against erasure and depolarizing noise when compared to other notable CSS codes, such as the asymptotically good quantum Tanner codes. These codes have been generalized to the *intersecting subset code* family  ([arXiv:2306.06056](https://arxiv.org/abs/2306.06056)).

For example, letting $H_i^x$ and $H_i^z$ be the $X$- and $Z$-check matrices of CSS codes $C_i$ with $i\in\{1,2,3,4\}$, the 2-fold symmetric classical product code is given by
\begin{align}
H_{\otimes}^x &:=\left(\begin{array}{c}
H_1^x \otimes H_2^x \otimes I \otimes I \\
I \otimes I \otimes H_3^x \otimes H_4^x
\end{array}\right) \\
H_{\otimes}^z &:=\left(\begin{array}{c}
H_1^z \otimes I \otimes H_3^z \otimes I \\
I \otimes H_2^z \otimes I \otimes H_4^z
\end{array}\right)~.
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qldpc]]
- _cousin_: [[concepts/qec/quantum-tanner]] — A $⟦512,174,8⟧$ classical-product code performed well  ([arXiv:2209.13474](https://arxiv.org/abs/2209.13474)) against erasure and depolarizing noise when compared to a member of an asymptotically good quantum Tanner code family.
- _cousin_: [`parity_check`](https://errorcorrectionzoo.org/c/parity_check) — SPC codes are used as component codes in classical-product code constructions.
- _cousin_: [`tensor`](https://errorcorrectionzoo.org/c/tensor) — Tensor-product codes are utilized in classical-product code constructions.
