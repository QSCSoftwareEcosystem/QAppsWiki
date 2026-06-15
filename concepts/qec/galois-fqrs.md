---
type: concept
name: Folded quantum RS (FQRS) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_fqrs
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_fqrs
---

# Folded quantum RS (FQRS) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_fqrs) (`code_id: galois_fqrs`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

CSS code on $q^m$-dimensional Galois-qudits that is constructed from folded RS (FRS) codes (i.e., an RS code whose coordinates have been grouped together) via the Galois-qudit CSS construction.
This code is used to construct Singleton-bound approaching approximate quantum codes.

More technically, an $m$-folded quantum RS code is a member of the $⟦n/m, R \cdot n/m, d/m⟧_{q^m}$ CSS code family for any $0<R<1$.
See  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)) for an expression of the codewords.
A folded quantum generalized RS (GRS) code can be defined in similar fashion from GRS codes  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).

(source: raw/error-correction-zoo.md)

## Protection

For every $\gamma>0$ and $0<R<1$, there are folded quantum RS code families of rate $R$ with local dimension $q=n^{O(1/\gamma^2)}$ that are $((1-R-\gamma)/2,n^{O(1/\gamma)})$-quantum list-decodable  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).

## Decoders

- Efficiently $((1-R-\gamma)/2,n^{O(1/\gamma)})$-quantum list-decodable codes exist for every fixed $\gamma>0$ and rate $0<R<1$  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).

## Relations

- _parent_: [[concepts/qec/galois-css]] — Folding a quantum polynomial code on $q$-dimensional Galois qudits yields an FQRS code on $q^m$-dimensional Galois qudits.
- _cousin_: [`folded_reed_solomon`](https://errorcorrectionzoo.org/c/folded_reed_solomon) — Folded quantum RS codes are quantum analogues of folded RS codes.
- _cousin_: [`generalized_reed_solomon`](https://errorcorrectionzoo.org/c/generalized_reed_solomon) — A folded quantum generalized RS (GRS) code can be constructed in similar fashion from GRS codes as FQRS codes are constructed from FRS codes  ([arXiv:2212.09935](https://arxiv.org/abs/2212.09935)).
