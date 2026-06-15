---
type: concept
name: Layer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fracton
- concepts/qec/good-qldpc
- concepts/qec/qldpc
- concepts/qec/qubit-concatenated
- concepts/qec/qubit-css
- concepts/qec/self-correct
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/layer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: layer
---

# Layer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/layer) (`code_id: layer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of qubit QLDPC CSS codes with stabilizer generator weights $\leq 6$ that are obtained by coupling layers of 2D surface codes according to the Tanner graph of a QLDPC code (or a more general qubit stabilizer code).
Geometric locality is maintained because, instead of being concatenated, each pair of parallel surface-code squares is fused (or quasi-concatenated) with perpendicular surface-code squares via lattice surgery.

(source: raw/error-correction-zoo.md)

## Rate

Layer codes achieve the 3D BPT bound, with parameters  $⟦n,\Theta(n^{1/3}),\Theta(n^{1/3})⟧$, when asymptotically good QLDPC codes are used in the construction.

## Decoders

- Decoders against stochastic and adversarial noise  ([arXiv:2510.06659](https://arxiv.org/abs/2510.06659)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qldpc]] — Layer codes are constructed by coupling layers of 2D surface codes according to the Tanner graph of a QLDPC code.
- _cousin_: [[concepts/qec/topological-abelian]] — The Layer code realizes 2D layers of $\mathbb{Z}_2$ gauge theory coupled along defects.
- _cousin_: [[concepts/qec/fracton]] — Layer codes are non-translation invariant 3D lattice stabilizer codes that can be viewed as fracton topological defect networks  ([arXiv:2309.16503](https://arxiv.org/abs/2309.16503)).
- _cousin_: [[concepts/qec/good-qldpc]] — Layer codes achieve the 3D BPT bound, with parameters  $⟦n,\Theta(n^{1/3}),\Theta(n^{1/3})⟧$, when asymptotically good QLDPC codes are used in the construction.
- _cousin_: [[concepts/qec/qubit-concatenated]] — Each pair of surface-code squares in a layer code is fused (or quasi-concatenated) with perpendicular surface-code squares via lattice surgery.
- _cousin_: [[concepts/qec/self-correct]] — The energy barrier of excitations for layer codes constructed using asymptotically good QLDPC codes scales as order $\Theta(n^{1/3})$  ([arXiv:2309.16503](https://arxiv.org/abs/2309.16503)). Layer codes are partially self-correcting quantum memories  ([arXiv:2510.06659](https://arxiv.org/abs/2510.06659), [arXiv:2510.09218](https://arxiv.org/abs/2510.09218)). Layer codes constructed from random CSS codes have near-optimal scaling of code parameters and a polynomial energy barrier, exhibiting behavior consistent with partial self-correction  ([arXiv:2510.06659](https://arxiv.org/abs/2510.06659)).
