---
type: concept
name: $SU(3)$ Tverberg spin code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/single-spin
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/su3_tverberg_spin
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: su3_tverberg_spin
---

# $SU(3)$ Tverberg spin code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/su3_tverberg_spin) (`code_id: su3_tverberg_spin`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

$SU(3)$ single-spin code family obtained from the two-step Tverberg construction  ([arXiv:quant-ph/9908066](https://arxiv.org/abs/quant-ph/9908066)) in the totally symmetric $N$-particle irrep $\mathcal{H}=\mathrm{Sym}^N(\mathbb{C}^3)$ of $\mathfrak{su}(3)$, which has dimension $\binom{N+2}{2}$.
Its weight basis is indexed by the discrete simplex $\Delta_{3,N}$, whose centered form is the triangular $A_2$ lattice.

A distance-two intermediate subspace can be chosen as
\begin{align}
  \mathcal{B}=\mathrm{span}\{|a_1a_2a_3\rangle: a_1-a_2\equiv0\pmod 3\}~,
\end{align}
giving $\dim\mathcal{B}\approx\binom{N+2}{2}/3$  ([arXiv:1205.4517](https://arxiv.org/abs/1205.4517))}.
A symmetric partition of this sublattice into pairs in the central hexagon and triples near the corners yields an error-detecting code for single Lie-algebra errors of dimension $\frac{4}{27}\binom{N+2}{2}+O(N)$ .

(source: raw/error-correction-zoo.md)

## Protection

Detects errors in the $\mathfrak{su}(3)$ Lie-algebra error set.
More generally, for the Lie-type graph metric $V_t=\mathrm{span}(\mathfrak{su}(3)\oplus \mathbb{C}I)^t$, a distance-$d$ construction can be obtained by first choosing a graph-distance-$d$ subset of the discrete simplex $\Delta_{3,N}$ .

## Rate

For general distance $d$, the two-step construction uses an asymptotically optimal distance-$d$ sublattice of the centered $\Delta_{3,N}$ discrete simplex for the intermediate space.
If $d=2t$, then $\dim\mathcal{B}=\dim\mathcal{H}/(3t^2)+O(N)$; if $d=2t+1$, then $\dim\mathcal{B}=\dim\mathcal{H}/(3t^2+3t+1)+O(N)$ .

## Relations

- _parent_: [[concepts/qec/single-spin]]
