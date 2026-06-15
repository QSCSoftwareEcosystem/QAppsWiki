---
type: concept
name: Fracton stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-stabilizer
- concepts/qec/qudit-stabilizer
- concepts/qec/spt
- concepts/qec/surface
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fracton
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fracton
---

# Fracton stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fracton) (`code_id: fracton`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 3D modular-qudit stabilizer code whose codewords make up the ground-state space of a Hamiltonian in a fracton phase.
Unlike topological phases, whose excitations can move in any direction, fracton phases are characterized by excitations whose movement is restricted.

Qubit fracton stabilizer codes are commonly grouped into the following three sub-types  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)):
\begin{enumerate}[(1)]
\item *Foliated type-I fracton phase*: Excitations are mobile in less than 3 dimensions, but codes can be grown by *foliation*, i.e., stacking copies of the 2D surface code and applying a constant-depth circuit  ([arXiv:1712.05892](https://arxiv.org/abs/1712.05892)).
\item *Fractal type-I fracton phase*: Excitations are mobile in less than 3 dimensions, and codes are not foliated.
\item *Type-II fracton phase*: Excitations are not mobile in any dimension and there are no string operators.
\end{enumerate}

Fracton phases can be understood as topological defect networks, meaning that they can be described in the language of topological quantum field theory with defects  ([arXiv:2002.05166](https://arxiv.org/abs/2002.05166), [arXiv:2112.14717](https://arxiv.org/abs/2112.14717)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qudit-stabilizer]]
- _parent_: [[concepts/qec/3d-stabilizer]]
- _cousin_: [[concepts/qec/topological]] — Unlike topological phases, whose excitations can move in any direction, fracton phases are characterized by excitations whose movement is restricted. Fracton phases can be understood as topological defect networks, meaning that they can be described in the language of topological quantum field theory with defects  ([arXiv:2002.05166](https://arxiv.org/abs/2002.05166), [arXiv:2112.14717](https://arxiv.org/abs/2112.14717)).
- _cousin_: [[concepts/qec/surface]] — Foliated type-I fracton phase codes can be grown by *foliation*, i.e., stacking copies of the 2D surface code; see  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).
- _cousin_: [[concepts/qec/spt]] — Certain 3D CSS fracton codes can be ungauged  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) into 2D fractal-like SPT Hamiltonians; the paper gives an explicit construction from the 3D fractal code  ([arXiv:1805.01836](https://arxiv.org/abs/1805.01836)). In subsystem-symmetry gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) constructions, symmetry charges transforming under planar symmetries in one, two, or three directions become planon, lineon, or fracton excitations, respectively  ([arXiv:1806.08679](https://arxiv.org/abs/1806.08679)).
