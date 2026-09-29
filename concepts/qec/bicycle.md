---
type: concept
name: Bicycle code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-bicycle
- concepts/qec/mirror
- concepts/qec/self-dual-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bicycle
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bicycle
---

# Bicycle code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bicycle) (`code_id: bicycle`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An even-length CSS code whose stabilizer generator matrix blocks are $H_{X}=H_{Z}=(A|A^T)$, where $A$ is a sparse circulant matrix.
The fact that $A$ commutes with its transpose ensures that the CSS condition is satisfied.
Bicycle codes are the first QLDPC codes.

A notable example is an $⟦2^n,2^{(n+1)/2},2^{(n-1)/2}⟧$ code constructed from the repetition code and the Cayley graph of $\mathbb{Z}_2^n$  ([arXiv:1206.2656](https://arxiv.org/abs/1206.2656)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/self-dual-css]] — Bicycle codes use the same check matrix $H_X=H_Z=(A|A^T)$ for both check types  ([arXiv:quant-ph/0304161](https://arxiv.org/abs/quant-ph/0304161)). Their $X$- and $Z$-type stabilizer spaces therefore coincide.
- _parent_: [[concepts/qec/generalized-bicycle]] — A GB code whose circulants satisfy $B = A^T$ reduces to a bicycle code.
- _parent_: [[concepts/qec/mirror]] — Bicycle codes are mirror codes up to qubit permutations and Hadamard gates  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
