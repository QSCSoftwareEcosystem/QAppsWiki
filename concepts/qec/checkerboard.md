---
type: concept
name: Checkerboard model code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fracton
- concepts/qec/lifted-product
- concepts/qec/qldpc
- concepts/qec/qubit-css
- concepts/qec/xcube
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/checkerboard
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: checkerboard
---

# Checkerboard model code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/checkerboard) (`code_id: checkerboard`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A foliated type-I fracton code defined on a cubic lattice that admits weight-eight  $X$- and $Z$-type stabilizer generators on the eight vertices of each cube in the lattice.
A tetrahedral Ising model can be used to obtain the checkerboard model by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) its subsystem symmetry  ([arXiv:1603.04442](https://arxiv.org/abs/1603.04442)).
In that construction, the checkerboard model is self-dual under exchange of $X$- and $Z$-type stabilizers, and its composites include dimension-1 and dimension-2 excitations, i.e., lineons and planons in later terminology, with anyonic mutual and self-statistics  ([arXiv:1603.04442](https://arxiv.org/abs/1603.04442)).

Variants include the twisted checkerboard model  ([arXiv:1805.06899](https://arxiv.org/abs/1805.06899)).

(source: raw/error-correction-zoo.md)

## Decoders

- Parallelized matching decoder  ([arXiv:1901.08061](https://arxiv.org/abs/1901.08061)).

## Code capacity threshold

- Independent $X,Z$ noise: $\approx 10.7\%$, higher than 3D surface code and color code  ([arXiv:2112.05122](https://arxiv.org/abs/2112.05122), [arXiv:2512.22888](https://arxiv.org/abs/2512.22888)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/fracton]] — The checkerboard model is equivalent to two copies of the X-cube model via a local constant-depth unitary  ([arXiv:1806.08633](https://arxiv.org/abs/1806.08633)). Hence, it is a foliated type-I fracton code.
- _parent_: [[concepts/qec/lifted-product]] — The checkerboard model code can be formulated directly as an LP code  ([arXiv:2312.08462](https://arxiv.org/abs/2312.08462)).
- _cousin_: [[concepts/qec/xcube]] — The checkerboard model is equivalent to two copies of the X-cube model via a local constant-depth unitary  ([arXiv:1806.08633](https://arxiv.org/abs/1806.08633)).
