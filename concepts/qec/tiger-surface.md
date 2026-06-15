---
type: concept
name: Tiger surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/compactified-r
- concepts/qec/hypergraph-product
- concepts/qec/qudit-surface
- concepts/qec/tiger
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tiger_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tiger_surface
---

# Tiger surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tiger_surface) (`code_id: tiger_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A tiger-code family constructed from a hypergraph product of two repetition codes over the integers, rather than from concatenating a cat code with a qubit surface code.
The code is conjectured to realize phases of $U(1)$ gauge theory. 

An $r \times (2m-1)$ lattice encodes a logical qubit into $2rm-r$ bosonic modes with $d_X=m$ and $d_Z \geq 4rm\sin^2\!\left(\frac{\pi}{2m}\right)$  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)).
The $m=2$ case is the liger (long-tiger) surface code, which has $d_X=2$ and $d_Z=4r$.

(source: raw/error-correction-zoo.md)

## Protection

The code corrects at least $\lfloor (m-1)/2 \rfloor$ losses on arbitrary modes, and it detects pure-loss error patterns of total weight up to $2m-2$  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)).
Its Euclidean distance obeys
\begin{align}
  4rm\sin^2\!\left(\frac{\pi}{2m}\right)\leq d_Z \leq 4rm\sin^2\!\left(\frac{\pi}{2m}\right)+4\sum_{j=1}^{m-1}\sin^2\!\left(\frac{(m-j)\pi}{m}\right)
\end{align}
so choosing $r=\Omega(m^2)$ makes both $d_X$ and $d_Z$ grow with system size. For suitable nonzero syndrome choices, the liger surface code has exact orthogonality in both logical $X$- and $Z$-bases at arbitrary energy  ([arXiv:2411.09668](https://arxiv.org/abs/2411.09668)).

## Relations

- _parent_: [[concepts/qec/tiger]] — The tiger surface code is constructed from a hypergraph product of two repetition codes over the integers.
- _cousin_: [[concepts/qec/compactified-r]] — Both the compactified $\mathbb{R}$ gauge theory and tiger surface code are constructed from a hypergraph product of two repetition codes over the integers.
- _cousin_: [[concepts/qec/topological-abelian]] — The tiger surface code is conjectured to realize phases of $U(1)$ gauge theory.
- _cousin_: [[concepts/qec/qudit-surface]] — The tiger surface code can be thought of as a realization of the $q\to\infty$ $U(1)$ rotor limit  ([arXiv:1709.04460](https://arxiv.org/abs/1709.04460)) of the qudit surface code as a tiger code.
- _cousin_: [[concepts/qec/hypergraph-product]] — The tiger surface code is constructed from a hypergraph product of two repetition codes over the integers.
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The tiger surface code is constructed from a hypergraph product of two repetition codes over the integers.
