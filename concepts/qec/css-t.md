---
type: concept
name: CSS-T code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-reed-muller
- concepts/qec/weakly-divisible-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/css-t
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: css-t
---

# CSS-T code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/css-t) (`code_id: css-t`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CSS code for which a physical transversal $T$ gate is either the identity (up to a global phase) or a logical gate.
CSS-T codes are constructed from a pair of linear binary codes via the CSS construction, with the pair satisfying certain conditions  ([arXiv:2312.17518](https://arxiv.org/abs/2312.17518)).

(source: raw/error-correction-zoo.md)

## Rate

Asymptotically good CSS-T codes exist  ([arXiv:2412.08586](https://arxiv.org/abs/2412.08586)).

## Transversal gates

- A physical transversal $T$ gate is either the identity (up to a global phase) or a logical gate  ([arXiv:1910.09333](https://arxiv.org/abs/1910.09333)).

## Relations

- _parent_: [[concepts/qec/weakly-divisible-css]] — CSS-T codes are weakly eight-divisible CSS codes that satisfy the stronger coset-divisibility condition at $\Delta=8$.
A strongly transversal $T$ gate preserves the code space if and only if $\operatorname{wt}(x)-2\operatorname{wt}(x*z)\equiv0\pmod 8$ for every $x\in C_2$ and every $z\in C_1+y$  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).
Here $*$ is the entrywise product and $y$ is the character vector.
The identity $\operatorname{wt}(x+z)-\operatorname{wt}(z)=\operatorname{wt}(x)-2\operatorname{wt}(x*z)$ makes this coset divisibility at $\Delta=8$.
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — CSS-T codes are constructed from a pair of linear binary codes via the CSS construction, with the pair satisfying certain conditions  ([arXiv:2312.17518](https://arxiv.org/abs/2312.17518)).
- _cousin_: [`binary_cyclic`](https://errorcorrectionzoo.org/c/binary_cyclic) — Binary cyclic and extended cyclic codes can be used to construct CSS-T codes via the CSS construction  ([arXiv:2312.17518](https://arxiv.org/abs/2312.17518)).
- _cousin_: [[concepts/qec/quantum-reed-muller]] — Certain quantum RM codes are CSS-T codes  ([arXiv:2305.06423](https://arxiv.org/abs/2305.06423), [arXiv:2310.16504](https://arxiv.org/abs/2310.16504), [arXiv:2312.17518](https://arxiv.org/abs/2312.17518)).

## Notes

- A database of CSS-T codes is available in QECDB .
