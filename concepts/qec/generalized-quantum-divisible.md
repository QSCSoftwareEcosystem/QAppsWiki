---
type: concept
name: Generalized quantum divisible code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-triorthogonal
- concepts/qec/qubit-css
- concepts/qec/random-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/generalized_quantum_divisible
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: generalized_quantum_divisible
---

# Generalized quantum divisible code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/generalized_quantum_divisible) (`code_id: generalized_quantum_divisible`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A level-$\nu$ generalized quantum divisible code is a CSS code whose $X$-type stabilizers, in the symplectic representation, have zero norm and form a $(\nu,t)$-null matrix (defined below) with respect to some odd-integer vector $t$  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
Such codes admit gates at the $\nu$th level of the \term{Clifford hierarchy}.
Such codes can also be level-lifted  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)), $\nu\to\nu+1$, which recursively yields towers of generalized divisible codes from a particular ground code.

Given an odd-integer coefficient length-$n$ vector $t$, two vectors $v,w$ are $(\nu,t)$*-orthogonal* if
\begin{align}
	\sum_i v_i t_i w_i \equiv 0 \mod 2^{\nu-1}~.
\end{align}
A matrix whose rows make up such vectors is called $(\nu,t)$-orthogonal.

(source: raw/error-correction-zoo.md)

## Transversal gates

- A level-$\nu$ generalized quantum divisible code admits a diagonal transversal gate at the $\nu$th level of the \term{Clifford hierarchy}  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).

## Relations

- _parent_: [[concepts/qec/qubit-css]] — Generalized quantum divisible codes are CSS codes. Any self-dual CSS code yields a level-three generalized quantum divisible code when level-lifted  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — Triorthogonal codes are stabilizer codes, while generalized quantum divisible codes are CSS codes. Every level-three generalized divisible code is a triorthogonal code, but whether the converse is true or false is not known  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
- _cousin_: [[concepts/qec/random-stabilizer]] — Random CSS codes  ([arXiv:quant-ph/9512032](https://arxiv.org/abs/quant-ph/9512032)) can be used to construct families of $⟦O(d^{\nu−1}), \Omega(d), d⟧$ level-$\nu$ generalized quantum divisible codes  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
