---
type: concept
name: 2D subsystem color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- 2D gauge color code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/subsystem-color
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/2d_subsystem_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 2d_subsystem_color
---

# 2D subsystem color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/2d_subsystem_color) (`code_id: 2d_subsystem_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A subsystem version of the 2D color code.
The original topological subsystem-code example is defined on the Union Jack lattice  ([arXiv:0908.4246](https://arxiv.org/abs/0908.4246)); the square-octagon-lattice hypergraph construction of  ([arXiv:1012.0425](https://arxiv.org/abs/1012.0425)) reproduces the same code from a complementary viewpoint.

(source: raw/error-correction-zoo.md)

## Protection

One family of subsystem codes has parameters $⟦3m,2g,2m+2g-2,d⟧$, where $m$ is the number of vertices of the original embedded two-colex, $g$ is the genus of the surface embedding the two-colex, and the distance is bounded from below by the length of the smallest nontrivial homological cycle of the two-colex $\Gamma$  ([arXiv:1207.0479](https://arxiv.org/abs/1207.0479)) ([arXiv:1805.12542](https://arxiv.org/abs/1805.12542)).

## Decoders

- For the Union-Jack/square-octagon member, decoding can be reduced to correcting $Z$ errors using stabilizers of the topological color code  ([arXiv:1012.0425](https://arxiv.org/abs/1012.0425)).

## General gates

- Braiding twist defects  ([arXiv:1006.5260](https://arxiv.org/abs/1006.5260)).

## Code capacity threshold

- The threshold under ML decoding for depolarizing noise corresponds to the value of a critical point of a disordered spin model, calculated to be $5.5(2)\%$ in Ref.  ([arXiv:1204.1838](https://arxiv.org/abs/1204.1838)).
- Erasure noise: $50\%$ threshold error rate using the optimal erasure decoder  ([doi:10.1109/TCOMM.2023.3277534](https://doi.org/10.1109/TCOMM.2023.3277534)), and $9.7\%$ and $44\%$ using gauge-fixing decoders  ([arXiv:2111.14594](https://arxiv.org/abs/2111.14594), [doi:10.1109/ITW46852.2021.9457583](https://doi.org/10.1109/ITW46852.2021.9457583)).

## Relations

- _parent_: [[concepts/qec/subsystem-color]]
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _cousin_: [[concepts/qec/2d-color]] — Gauge fixing relates 2D subsystem color codes to 2D color codes on the same lattice  ([arXiv:0908.4246](https://arxiv.org/abs/0908.4246), [arXiv:1311.0879](https://arxiv.org/abs/1311.0879)); the original Union-Jack member is reproduced by the square-octagon-lattice construction of  ([arXiv:1012.0425](https://arxiv.org/abs/1012.0425)).
