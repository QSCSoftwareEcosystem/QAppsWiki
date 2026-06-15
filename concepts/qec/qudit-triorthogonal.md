---
type: concept
name: Prime-qudit triorthogonal code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-css
- concepts/qec/qudit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_triorthogonal
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_triorthogonal
---

# Prime-qudit triorthogonal code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_triorthogonal) (`code_id: qudit_triorthogonal`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $m \times n$ matrix over $\mathbb{F}_p=\mathbb{Z}_p$ is triorthogonal if its rows $r_1, \ldots, r_m$ satisfy $|r_i \cdot r_j| = 0$ and $|r_i \cdot r_j \cdot r_k| = 0$ modulo $p$, where addition and multiplication are done on $\mathbb{F}_p$.
The triorthogonal prime-qudit CSS code associated with the matrix is constructed by mapping nonzero entries in self-orthogonal rows to $X$ operators, and $Z$ operators for each row in the orthogonal complement  ([arXiv:1811.08461](https://arxiv.org/abs/1811.08461), [arXiv:2403.06228](https://arxiv.org/abs/2403.06228)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- Admits a transversal gate from the third level of the qudit Clifford hierarchy  ([arXiv:1811.08461](https://arxiv.org/abs/1811.08461)).

## Relations

- _parent_: [[concepts/qec/qudit-css]]
- _parent_: [[concepts/qec/galois-css]]
