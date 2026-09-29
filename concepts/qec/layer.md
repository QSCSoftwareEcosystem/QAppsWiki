---
type: concept
name: Layer code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fracton
- concepts/qec/good-qldpc
- concepts/qec/mapping-cone
- concepts/qec/qldpc
- concepts/qec/qubit-concatenated
- concepts/qec/self-correct
- concepts/qec/symplectic-cone
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

Member of a family of geometrically local 3D qubit QLDPC codes obtained by coupling layers of 2D surface codes according to the check-qubit incidence structure of an input QLDPC code.
Geometric locality is maintained because, instead of being concatenated, each pair of parallel surface-code squares is fused (or quasi-concatenated) with perpendicular surface-code squares via lattice surgery.

The original CSS construction has stabilizer-generator weight at most six  ([arXiv:2309.16503](https://arxiv.org/abs/2309.16503)).
The symplectic cone framework extends the construction to non-CSS QLDPC inputs.
For an input code of $n$ qubits and $n_S$ checks, the output lies in a 3D grid $[n_S]\times[O(wq)n]\times[n_S]$ with at most three qubits per edge.
Its maximum stabilizer-generator weight is nine, its total qubit degree is at most eight, and its distance is order $\Omega(n_S/(wq))$ times the input distance, where $w$ and $q$ are the input check weight and total qubit degree  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
The generalization also applies to the 4D and 5D layer codes  ([arXiv:2605.18961](https://arxiv.org/abs/2605.18961), [arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).

(source: raw/error-correction-zoo.md)

## Rate

Layer codes achieve the 3D BPT bound, with parameters $⟦n,\Theta(n^{1/3}),\Theta(n^{2/3})⟧$, when asymptotically good QLDPC codes are used in the construction.

## Decoders

- Decoders against stochastic and adversarial noise  ([arXiv:2510.06659](https://arxiv.org/abs/2510.06659)).

## Relations

- _parent_: [[concepts/qec/symplectic-cone]] — Layer codes are height-2 symplectic cones whose embedded column complex is the input QLDPC code; CSS Layer codes reduce to ordinary mapping cones, while the non-CSS construction uses a defect map to preserve symplectic commutation  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361), [arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
- _parent_: [[concepts/qec/qldpc]] — Layer codes are QLDPC codes constructed by coupling layers of 2D surface codes according to the check-qubit incidence structure of a QLDPC input code  ([arXiv:2309.16503](https://arxiv.org/abs/2309.16503), [arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
- _cousin_: [[concepts/qec/mapping-cone]] — CSS Layer codes are height-2 mapping cones whose levels are stacks of 2D surface codes and whose string defects implement the chain homotopy; non-CSS Layer codes require the symplectic cone generalization  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361), [arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
- _cousin_: [[concepts/qec/topological-abelian]] — The Layer code realizes 2D layers of $\mathbb{Z}_2$ gauge theory coupled along defects.
- _cousin_: [[concepts/qec/fracton]] — Layer codes are non-translation invariant 3D lattice stabilizer codes that can be viewed as fracton topological defect networks  ([arXiv:2309.16503](https://arxiv.org/abs/2309.16503)).
- _cousin_: [[concepts/qec/good-qldpc]] — Layer codes achieve the 3D BPT bound, with parameters $⟦n,\Theta(n^{1/3}),\Theta(n^{2/3})⟧$, when asymptotically good QLDPC codes are used in the construction.
- _cousin_: [[concepts/qec/qubit-concatenated]] — Each pair of surface-code squares in a layer code is fused (or quasi-concatenated) with perpendicular surface-code squares via lattice surgery.
- _cousin_: [[concepts/qec/self-correct]] — The energy barrier of excitations for layer codes constructed using asymptotically good QLDPC codes scales as order $\Theta(n^{1/3})$  ([arXiv:2309.16503](https://arxiv.org/abs/2309.16503)). Layer codes are partially self-correcting quantum memories  ([arXiv:2510.06659](https://arxiv.org/abs/2510.06659), [arXiv:2510.09218](https://arxiv.org/abs/2510.09218)). Layer codes constructed from random CSS codes have near-optimal scaling of code parameters and a polynomial energy barrier, exhibiting behavior consistent with partial self-correction  ([arXiv:2510.06659](https://arxiv.org/abs/2510.06659)).
