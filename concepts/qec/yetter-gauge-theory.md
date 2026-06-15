---
type: concept
name: Two-gauge theory code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Higher gauge theory code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/category-quantum
- concepts/qec/commuting-projector
- concepts/qec/enriched-walker-wang
- concepts/qec/frustration-free
- concepts/qec/topological
- concepts/qec/walker-wang
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/yetter_gauge_theory
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: yetter_gauge_theory
---

# Two-gauge theory code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/yetter_gauge_theory) (`code_id: yetter_gauge_theory`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code whose codewords realize lattice two-gauge theory  ([arXiv:math/0307200](https://arxiv.org/abs/math/0307200), [arXiv:hep-th/0304074](https://arxiv.org/abs/hep-th/0304074), [arXiv:hep-th/0412325](https://arxiv.org/abs/hep-th/0412325), [arXiv:math/0511710](https://arxiv.org/abs/math/0511710), [arXiv:1002.4636](https://arxiv.org/abs/1002.4636), [arXiv:1003.4485](https://arxiv.org/abs/1003.4485), [arXiv:1307.4793](https://arxiv.org/abs/1307.4793), [arXiv:1404.2634](https://arxiv.org/abs/1404.2634), [arXiv:1308.2926](https://arxiv.org/abs/1308.2926)) for a finite *two-group* (a.k.a. a *crossed module*) in arbitrary spatial dimension.
There exist several lattice-model formulations in arbitrary spatial dimension  ([arXiv:1309.4721](https://arxiv.org/abs/1309.4721), [arXiv:1702.00868](https://arxiv.org/abs/1702.00868)) as well as explicitly in 3D  ([arXiv:1606.06639](https://arxiv.org/abs/1606.06639), [arXiv:1802.10104](https://arxiv.org/abs/1802.10104), [arXiv:1901.02249](https://arxiv.org/abs/1901.02249), [arXiv:1904.00994](https://arxiv.org/abs/1904.00994)) and 4D  ([arXiv:1904.00994](https://arxiv.org/abs/1904.00994)), with the 3D case realizing the Yetter model  ([doi:10.1142/S0218216593000076](https://doi.org/10.1142/S0218216593000076), [doi:10.1112/S0024610798006838](https://doi.org/10.1112/S0024610798006838), [doi:10.1142/S0218216596000400](https://doi.org/10.1142/S0218216596000400), [arXiv:math/9903003](https://arxiv.org/abs/math/9903003)).

A two-gauge theory generalizes ordinary gauge theory by replacing the gauge group with a two-group (a.k.a. finite crossed module).
Lattice formulations place gauge fields not only on edges of a lattice (as they do in ordinary gauge theory), but also on higher-dimensional structures such as faces.

Ground-state degeneracy is a topological invariant for 3D manifolds  ([arXiv:1702.00868](https://arxiv.org/abs/1702.00868)); more precisely, it equals the number of homotopy classes of maps from the spatial manifold to the classifying space of the underlying finite two-group.
Excitations of the 3D models are studied in Refs.  ([arXiv:1909.07937](https://arxiv.org/abs/1909.07937), [arXiv:2206.09941](https://arxiv.org/abs/2206.09941), [arXiv:2202.08294](https://arxiv.org/abs/2202.08294)).
Generalizations of Ocneanu's tube algebras  ([doi:10.2969/aspm/03110235](https://doi.org/10.2969/aspm/03110235)) can be used to characterize excitations  ([arXiv:1909.07937](https://arxiv.org/abs/1909.07937), [arXiv:2305.17165](https://arxiv.org/abs/2305.17165)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/category-quantum]]
- _parent_: [[concepts/qec/commuting-projector]] — Two-gauge theory codewords span ground-state subspaces of frustration-free commuting-projector Hamiltonians.
- _parent_: [[concepts/qec/frustration-free]] — Two-gauge theory codewords span ground-state subspaces of frustration-free commuting-projector Hamiltonians.
- _parent_: [[concepts/qec/topological]] — Two-gauge theory codes realize lattice two-gauge theory for a finite two-group.
- _cousin_: [[concepts/qec/enriched-walker-wang]] — $G$-enriched Walker-Wang models realize 3D two-gauge theories  ([arXiv:1606.07144](https://arxiv.org/abs/1606.07144)).
- _cousin_: [[concepts/qec/walker-wang]] — Two-gauge theory codes for particular two-groups are dual to certain Walker-Wang models based on Abelian groups  ([arXiv:1606.06639](https://arxiv.org/abs/1606.06639)) ([arXiv:1901.02249](https://arxiv.org/abs/1901.02249)).
