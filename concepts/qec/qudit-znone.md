---
type: concept
name: $\mathbb{Z}_q^{(1)}$ subsystem code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/double-semion
- concepts/qec/qudit-subsystem-stabilizer
- concepts/qec/qudit-surface
- concepts/qec/topological-abelian
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_znone
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_znone
---

# $\mathbb{Z}_q^{(1)}$ subsystem code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_znone) (`code_id: qudit_znone`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit subsystem code, based on the Kitaev honeycomb model  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) and its generalization  ([arXiv:1405.1780](https://arxiv.org/abs/1405.1780)), that is characterized by the $\mathbb{Z}_q^{(1)}$ anyon theory  ([doi:10.7907/5NDZ-W890](https://doi.org/10.7907/5NDZ-W890)), which is modular for odd prime $q$ and non-modular otherwise. Encodes a single $q$-dimensional qudit when put on a torus for odd $q$, and a $q/2$-dimensional qudit for even $q$. This code can be constructed using geometrically local gauge generators, but does not admit geometrically local stabilizer generators. For $q=2$, the code reduces to the subsystem code underlying the Kitaev honeycomb model code as well as the honeycomb Floquet code.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qudit-subsystem-stabilizer]]
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _parent_: [[concepts/qec/topological-abelian]] — The $\mathbb{Z}_q^{(1)}$ subsystem code is characterized by the $\mathbb{Z}_q^{(1)}$ anyon theory  ([doi:10.7907/5NDZ-W890](https://doi.org/10.7907/5NDZ-W890)). The anyon theory has a single generator $a \in \mathbb Z_N$ with $\theta(a) =e^{\frac{2\pi i}{N}a^2}$. It is modular for odd prime $q$ and non-modular otherwise.
- _cousin_: [[concepts/qec/qudit-surface]] — The $\mathbb{Z}_q^{(1)}$ subsystem code can be obtained from the $\mathbb{Z}_q$ square-lattice surface code by gauging out the anyon $e^{-1} m$ and applying transversal Clifford gates  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)). During this process, the square lattice is effectively expanded to a honeycomb tiling  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
- _cousin_: [[concepts/qec/double-semion]] — The anyonic exchange statistics of $\mathbb{Z}_4^{(1)}$ subsystem code resemble those of the double semion code, but its fusion rules realize the $\mathbb{Z}_4$ group.
