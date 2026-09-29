---
type: concept
name: Perturbed bivariate bicycle (PBB) code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/gross
- concepts/qec/qldpc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/perturbed_bb
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: perturbed_bb
---

# Perturbed bivariate bicycle (PBB) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/perturbed_bb) (`code_id: perturbed_bb`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit stabilizer code defined over the ring $R=\mathbb{F}_2[x,y]/(x^{\ell}-1,y^{m}-1)$ by four polynomials $A,B,C,D\in R$  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).
The polynomials $C$ and $D$ add $Z$-type support to the $X$-type checks of the BB code defined by $A$ and $B$.
Such codes are not CSS in general.

With each polynomial represented by an $\ell m\times\ell m$ circulant matrix, the stabilizer matrix in symplectic $(X|Z)$ form is
\begin{align}
  H=\begin{pmatrix} A & B & C & D \\ 0 & 0 & B^{\top} & A^{\top} \end{pmatrix}~,
\end{align}
where $A^{\top}$ is the image of $A$ under $x\mapsto x^{-1}$ and $y\mapsto y^{-1}$.
All generators commute iff $AC^{\top}+BD^{\top}$ is symmetric over $\mathbb{F}_2$  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).
Some PBB codes are equivalent to CSS codes under single-qubit Hadamard or $S$ gates  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).

(source: raw/error-correction-zoo.md)

## Decoders

- BP-OSD decoder applied to the full symplectic check matrix  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).

## Relations

- _parent_: [[concepts/qec/qldpc]] — PBB codes have stabilizer generators of weight at most the total number of terms of $A$, $B$, $C$, and $D$  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).
- _cousin_: [[concepts/qec/gross]] — The $⟦144,12,12⟧$ PBB code perturbs the gross-code polynomials $A=x^3+y+y^2$ and $B=y^3+x+x^2$ by $C=y+x^3y$ and $D=y^3+x^3y^3$, with mixed stabilizer generators of weight eight  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).

## Notes

- A catalogue of PBB codes found by LLM-guided search is available at [qcode-discovery](https://github.com/qiskit-community/qcode-discovery)  ([arXiv:2606.02418](https://arxiv.org/abs/2606.02418)).
