---
type: concept
name: Abelian TQD code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/commuting-projector
- concepts/qec/topological-abelian
- concepts/qec/tqd
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tqd_abelian
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tqd_abelian
---

# Abelian TQD code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tqd_abelian) (`code_id: tqd_abelian`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

TQD code whose codewords realize a 2D Abelian twisted-quantum-double topological order.
For Abelian TQDs, the corresponding anyon theory is defined by an Abelian group and a group cocycle built from Type-I, Type-II, or Type-III 3-cocycles  ([arXiv:1211.3695](https://arxiv.org/abs/1211.3695), [arXiv:2112.11394](https://arxiv.org/abs/2112.11394), [arXiv:2403.12119](https://arxiv.org/abs/2403.12119)).
Abelian TQDs with Type-I and -II cocycles account for all 2D Abelian topological orders that admit gapped boundaries  ([arXiv:1008.0654](https://arxiv.org/abs/1008.0654)).
Abelian TQDs with Type-III cocycles may admit non-Abelian topological orders. 

Type-I and -II Abelian TQD codes can be realized as modular-qudit lattice stabilizer codes on composite-dimensional qudits by starting from a stack of Abelian quantum double models (it suffices to take $\prod_i \mathbb{Z}_{N_i^2}$ toric codes for $G=\prod_i \mathbb{Z}_{N_i}$) and condensing certain bosonic anyons  ([arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).
Many Abelian TQD code Hamiltonians were originally formulated as commuting-projector models  ([arXiv:1810.08204](https://arxiv.org/abs/1810.08204), [arXiv:2001.11516](https://arxiv.org/abs/2001.11516)).

(source: raw/error-correction-zoo.md)

## Encoders

- Fault-tolerant state-preparation circuits for all non-chiral abelian topological phases  ([arXiv:2403.12119](https://arxiv.org/abs/2403.12119)).

## Fault tolerance

- Fault-tolerant state-preparation circuits for all non-chiral abelian topological phases  ([arXiv:2403.12119](https://arxiv.org/abs/2403.12119)).

## Relations

- _parent_: [[concepts/qec/tqd]] — The anyon theory corresponding to Abelian TQD codes is defined by an Abelian group and a Type-I, Type-II, or Type-III 3-cocycle.
Abelian TQDs with Type-I and -II cocycles account for all 2D Abelian topological orders that admit gapped boundaries  ([arXiv:1008.0654](https://arxiv.org/abs/1008.0654)).
- _cousin_: [[concepts/qec/commuting-projector]] — Many Abelian TQD code Hamiltonians were originally formulated as commuting-projector models  ([arXiv:2001.11516](https://arxiv.org/abs/2001.11516)).
- _cousin_: [[concepts/qec/topological-abelian]] — Abelian TQDs with Type-I and -II cocycles account for all 2D Abelian topological orders that admit gapped boundaries  ([arXiv:1008.0654](https://arxiv.org/abs/1008.0654)).
Conversely, every Abelian anyon theory is a subtheory of some TQD  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)). 
Any Abelian anyon theory $A$ can be realized at one of the surfaces of a 3D Walker-Wang model whose underlying theory is an Abelian TQD containing $A$ as a subtheory  ([arXiv:1907.02075](https://arxiv.org/abs/1907.02075), [arXiv:2202.05442](https://arxiv.org/abs/2202.05442)) ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
