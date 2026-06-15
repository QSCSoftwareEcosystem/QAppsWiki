---
type: concept
name: Hopf-algebra quantum-double code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/enriched-string-net
- concepts/qec/qudit-surface
- concepts/qec/string-net
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hopf_quantum_double
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hopf_quantum_double
---

# Hopf-algebra quantum-double code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hopf_quantum_double) (`code_id: hopf_quantum_double`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose codewords realize 2D gapped topological order defined on qudits valued in a Hopf algebra $H$.
The code Hamiltonian is a generalization  ([arXiv:1007.5283](https://arxiv.org/abs/1007.5283), [arXiv:1206.2308](https://arxiv.org/abs/1206.2308)) of the quantum double model from group algebras to Hopf algebras, as anticipated by Kitaev  ([arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021)).
Boundaries of these models have been examined  ([arXiv:2207.03970](https://arxiv.org/abs/2207.03970), [arXiv:2208.06317](https://arxiv.org/abs/2208.06317)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/string-net]] — String-net model ground states reduce to Hopf-algebra quantum-double ground states for categories $\text{Rep}(H)$, where $H$ is a Hopf algebra  ([arXiv:1206.2308](https://arxiv.org/abs/1206.2308)).
- _cousin_: [[concepts/qec/enriched-string-net]] — Extending the Hopf algebra quantum-double construction to a weak Hopf algebra construction yields an alternative formulation  ([arXiv:1006.5823](https://arxiv.org/abs/1006.5823)) ([arXiv:1309.4181](https://arxiv.org/abs/1309.4181)) for realizing multi-fusion string-net topological orders because of the relationship between representations of weak Hopf algebras and multi-fusion categories  ([arXiv:math/0203060](https://arxiv.org/abs/math/0203060)). Tensor network constructions can be done for either formulation  ([arXiv:2204.05940](https://arxiv.org/abs/2204.05940), [arXiv:2302.08131](https://arxiv.org/abs/2302.08131)).
- _cousin_: [[concepts/qec/qudit-surface]] — The modular-qudit surface code can be generalized to a Hopf-algebra quantum-double code whose ground states remain the same but whose excitations are based on quasitriangular semisimple Hopf algebras of $\mathbb{Z}_q$  ([arXiv:2210.07909](https://arxiv.org/abs/2210.07909)).
