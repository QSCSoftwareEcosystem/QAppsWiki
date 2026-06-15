---
type: concept
name: Clifford subgroup-orbit QSC
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Sidelnikov QSC
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qsc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_sidelnikov
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_sidelnikov
---

# Clifford subgroup-orbit QSC

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_sidelnikov) (`code_id: quantum_sidelnikov`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $((2^r,2,2-\sqrt{2},8))$ QSC for $r \geq 1$ constructed using the real Clifford subgroup-orbit code.
Logical constellations are constructed by applying elements of an index-two subgroup of the real Clifford group, when taken as a subgroup of the orthogonal group  ([arXiv:math/0001038](https://arxiv.org/abs/math/0001038)) to $2$ different vectors on the complex sphere.
The code is known as the *Witting code* for $r=2$ because its two logical constellations form vertices of Witting polytopes.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qsc]]
- _cousin_: [`sidelnikov`](https://errorcorrectionzoo.org/c/sidelnikov) — Clifford group-orbit QSCs are quantum counterparts of real Clifford subgroup-orbit codes.
- _cousin_: [`witting_polytope`](https://errorcorrectionzoo.org/c/witting_polytope) — Logical constellations of the Clifford subgroup-orbit code for $r=2$ form vertices of Witting polytopes.
- _cousin_: [`24cell`](https://errorcorrectionzoo.org/c/24cell) — Logical constellations of the Clifford subgroup-orbit code for $r=1$ form vertices of 24-cells when mapped into the real sphere, while code constellations form vertices of a disphenoidal 288-cell.
- _cousin_: [`disphenoidal288cell`](https://errorcorrectionzoo.org/c/disphenoidal288cell) — Logical constellations of the Clifford subgroup-orbit code for $r=1$ form vertices of 24-cells when mapped into the real sphere, while code constellations form vertices of a disphenoidal 288-cell.
