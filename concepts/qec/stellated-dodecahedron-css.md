---
type: concept
name: $⟦30,8,3⟧$ Bring code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Small stellated dodecahedron code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/two-dimensional-hyperbolic-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stellated_dodecahedron_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stellated_dodecahedron_css
---

# $⟦30,8,3⟧$ Bring code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stellated_dodecahedron_css) (`code_id: stellated_dodecahedron_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦30,8,3⟧$ hyperbolic surface code on a quotient of the $\{5,5\}$ hyperbolic tiling called Bring's curve.
Its qubits and stabilizer generators lie on the vertices of the small stellated dodecahedron. It admits a set of weight-five stabilizer generators.

(source: raw/error-correction-zoo.md)

## Transversal gates

- Clifford group of four of the eight logical qubits can be implemented by transversal gates combined with qubit permutations  ([arXiv:2202.06647](https://arxiv.org/abs/2202.06647)).

## Decoders

- Fault-tolerant parity-check schedules whose performance is similar to those of the surface-17 code, but with qubit overhead reduced by a factor of 2.6 }.

## Relations

- _parent_: [[concepts/qec/two-dimensional-hyperbolic-surface]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [`polyhedron`](https://errorcorrectionzoo.org/c/polyhedron) — Bring code and related codes listed in  ([arXiv:1712.07666](https://arxiv.org/abs/1712.07666)) arrange qubits and stabilizer generators on star polyhedra.
- _cousin_: [`golay`](https://errorcorrectionzoo.org/c/golay) — The automorphism group of the parity-check matrix of the Golay code is the same as a certain automorphism group of the Bring code  ([arXiv:2202.06647](https://arxiv.org/abs/2202.06647)).
- _cousin_: [`dodecahedron`](https://errorcorrectionzoo.org/c/dodecahedron) — The qubits and stabilizer generators of the $⟦30,8,3⟧$ Bring code lie on the vertices of the small stellated dodecahedron.
