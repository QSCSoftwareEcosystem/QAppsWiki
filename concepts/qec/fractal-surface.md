---
type: concept
name: Fractal surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-surface
- concepts/qec/higher-dimensional-surface
- concepts/qec/hypergraph-product
- concepts/qec/self-correct
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fractal_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fractal_surface
---

# Fractal surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fractal_surface) (`code_id: fractal_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Kitaev surface code on a fractal geometry, which is obtained by removing qubits from the surface code on a cubic lattice.
A related construction, the *fractal product code*, is a hypergraph product of two classical codes defined on a Sierpinski carpet graph  ([arXiv:1411.7046](https://arxiv.org/abs/1411.7046)). 
The underlying classical codes form classical self-correcting memories  ([arXiv:cond-mat/0212497](https://arxiv.org/abs/cond-mat/0212497), [arXiv:1002.1227](https://arxiv.org/abs/1002.1227), [doi:10.1239/jap/1019737983](https://doi.org/10.1239/jap/1019737983)).

(source: raw/error-correction-zoo.md)

## Decoders

- Sweep local automaton decoder  ([arXiv:2201.03568](https://arxiv.org/abs/2201.03568)).

## Relations

- _parent_: [[concepts/qec/higher-dimensional-surface]] — Fractal surface codes are obtained by removing qubits from the 3D surface code on a cubic lattice.
- _cousin_: [[concepts/qec/3d-surface]] — Fractal surface codes are obtained by removing qubits from the 3D surface code on a cubic lattice.
- _cousin_: [[concepts/qec/hypergraph-product]] — The related fractal product code is a hypergraph product of two classical codes defined on a Sierpinski carpet graph  ([arXiv:1411.7046](https://arxiv.org/abs/1411.7046)).
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — The fractal product code is a hypergraph product of two classical codes defined on a Sierpinski carpet graph  ([arXiv:1411.7046](https://arxiv.org/abs/1411.7046)).
- _cousin_: [[concepts/qec/self-correct]] — The classical codes underlying the fractal product code form classical self-correcting memories  ([arXiv:cond-mat/0212497](https://arxiv.org/abs/cond-mat/0212497), [arXiv:1002.1227](https://arxiv.org/abs/1002.1227), [doi:10.1239/jap/1019737983](https://doi.org/10.1239/jap/1019737983)).
