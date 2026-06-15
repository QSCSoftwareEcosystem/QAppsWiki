---
type: concept
name: Two-foliated fracton code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Anisotropic lineon code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fracton
- concepts/qec/hypergraph-product
- concepts/qec/spt
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/two_foliated
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: two_foliated
---

# Two-foliated fracton code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/two_foliated) (`code_id: two_foliated`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A type-I fracton code obtained by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) a 3D paramagnet with planar subsystem symmetries in two directions.
In that construction, the gauge charges are lineons and the flux excitations are also lineons moving in the same direction, yielding the anisotropic lineon model  ([arXiv:1806.08679](https://arxiv.org/abs/1806.08679)).

(source: raw/error-correction-zoo.md)

## General gates

- The code admits a cup product structure and a logical CZ gate from physical CZ gates  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).

## Relations

- _parent_: [[concepts/qec/hypergraph-product]] — The two-foliated fracton code is a hypergraph product of the repetition code and the plaquette Ising code on a square lattice with periodic boundary conditions  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).
- _parent_: [[concepts/qec/fracton]] — The two-foliated fracton code is a foliated type-I fracton code.
- _cousin_: [`plaquette_ising`](https://errorcorrectionzoo.org/c/plaquette_ising) — The two-foliated fracton code is a hypergraph product of the repetition code and the plaquette Ising code on a square lattice with periodic boundary conditions  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The two-foliated fracton code is a hypergraph product of the repetition code and the plaquette Ising code on a square lattice with periodic boundary conditions  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).
- _cousin_: [[concepts/qec/spt]] — Gauging a 3D paramagnet with planar subsystem symmetries in two directions yields the anisotropic lineon model; each symmetry charge becomes a lineon gauge charge, while certain pairs become planons  ([arXiv:1806.08679](https://arxiv.org/abs/1806.08679)).
