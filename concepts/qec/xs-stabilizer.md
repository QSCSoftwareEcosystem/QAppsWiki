---
type: concept
name: XS stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/tqd-abelian
- concepts/qec/xp-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/xs_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: xs_stabilizer
---

# XS stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/xs_stabilizer) (`code_id: xs_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A type of stabilizer code where stabilizer generators are elements of the group $ \{\alpha I, X, \sqrt{Z}\}^{\otimes n} $, with $ S = \sqrt{Z} = \text{diag} (1, i)$. The codespace is a joint $+1$ eigenspace of a set of stabilizer generators, which need not commute to define a valid codespace.

The phases in the qubit-basis expansion of an XS stabilizer state are polynomials of degree three or below  ([arXiv:1404.5327](https://arxiv.org/abs/1404.5327)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/xp-stabilizer]] — The XP stabilizer formalism reduces to the XS formalism at $N=4$.
- _cousin_: [[concepts/qec/tqd-abelian]] — Abelian TQD models for the groups $\mathbb{Z}_2^k$ can be realized as XS stabilizer codes  ([arXiv:1404.5327](https://arxiv.org/abs/1404.5327)). Upon gauging some symmetries  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)), a Type-III $\mathbb{Z}_2^3$ TQD realizes the same topological order as the $G=D_4$ quantum double model  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195), [arXiv:1508.03468](https://arxiv.org/abs/1508.03468)).
