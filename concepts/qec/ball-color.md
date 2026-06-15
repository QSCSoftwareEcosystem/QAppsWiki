---
type: concept
name: Ball code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/color
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ball_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ball_color
---

# Ball code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ball_color) (`code_id: ball_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A distance-two color code defined on a colorable $D$-ball, equivalently on a $D$-colex with boundary  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
In the morphing construction of Ref.  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)), ball codes arise as the child codes associated with the morphed ball-like regions.
This family includes hypercube codes (defined on balls constructed from hyperoctahedra) and 3D ball codes (defined on duals of certain Archimedean solids).

(source: raw/error-correction-zoo.md)

## Protection

A $D$-dimensional ball code defined on a ball-like region $B_v$ has parameters $⟦|B_v^D|,|B_v^1|-D,2⟧$  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
The hypercube code family has parameters $⟦2^D,D,2⟧$  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
3D ball codes on duals of the truncated octahedron, truncated cuboctahedron, and truncated icosidodecahedron have parameters $⟦24,11,2⟧$, $⟦48,23,2⟧$, and $⟦120,59,2⟧$, respectively  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).

## Transversal gates

- The 3D ball codes on duals of the truncated octahedron, truncated cuboctahedron, and truncated icosidodecahedron admit logical $CCZ$-type gates implemented by physical $T$ and $T^\dagger$ gates  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).

## Magic scaling exponent

The 3D ball codes on duals of the truncated octahedron, truncated cuboctahedron, and truncated icosidodecahedron have $\gamma$ close to one  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).

## Relations

- _parent_: [[concepts/qec/color]] — Ball codes are color codes defined on a $D$-dimensional colex  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [`polyhedron`](https://errorcorrectionzoo.org/c/polyhedron) — Polytopes dual to the hyperoctahedron, truncated octahedron, truncated cuboctahedron, and truncated icosidodecahedron are used to construct 3D ball codes.
