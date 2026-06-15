---
type: concept
name: Abelian quantum-double stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-double
- concepts/qec/tqd-abelian-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_double_abelian
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_double_abelian
---

# Abelian quantum-double stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_double_abelian) (`code_id: quantum_double_abelian`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit stabilizer code whose codewords realize 2D modular gapped Abelian topological order with trivial cocycle.
The corresponding anyon theory is defined by an Abelian group.
The $G=\mathbb{Z}_2$ instance on a torus is the toric code, and cyclic-group instances reduce to modular-qudit surface codes.
All such codes can be realized by a stack of modular-qudit surface codes because all finite Abelian groups are direct products of cyclic groups.

There exists an invariant that can be computed to uniquely characterize the anyons of a state in an Abelian quantum-double topological phase  ([arXiv:1407.2926](https://arxiv.org/abs/1407.2926)).

(source: raw/error-correction-zoo.md)

## Protection

Error-correcting properties established in Ref.  ([arXiv:1804.03203](https://arxiv.org/abs/1804.03203)) using operator algebra theory.
Correcting the maximum number of correctable errors is $NP$-complete  ([arXiv:2404.08552](https://arxiv.org/abs/2404.08552)).

## Encoders

- Any geometrically local unitary circuit connecting two quantum double models whose groups are not isomorphic must have depth at least linear in $n$  ([arXiv:1407.2926](https://arxiv.org/abs/1407.2926)).

## Decoders

- Efficient decoder correcting below the code distance  ([arXiv:2404.08552](https://arxiv.org/abs/2404.08552)).

## Relations

- _parent_: [[concepts/qec/tqd-abelian-stabilizer]] — The anyon theory corresponding to Abelian quantum double codes is defined by an Abelian group and trivial cocycle. Stacks of Abelian quantum double models are the starting point for constructing all Abelian TQD stabilizer codes by condensing bosons; for $G=\prod_i \mathbb{Z}_{N_i}$, it suffices to use $\prod_i \mathbb{Z}_{N_i^2}$ quantum doubles  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)). Conversely, every Abelian anyon theory is a subtheory of some Abelian TQD  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)). Upon gauging some symmetries  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)), Type-I and II $\mathbb{Z}_2^3$ TQDs realize the same topological order as certain Abelian quantum double models  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195), [arXiv:1508.03468](https://arxiv.org/abs/1508.03468)).
- _parent_: [[concepts/qec/quantum-double]] — The anyon theory corresponding to (Abelian) quantum double codes is defined by an (Abelian) group.
