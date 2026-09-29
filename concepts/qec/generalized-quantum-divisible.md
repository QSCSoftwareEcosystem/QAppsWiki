---
type: concept
name: Generalized quantum divisible code
status: provisional
updated: '2026-09-29'
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

A level-$\nu$ generalized quantum divisible code is a CSS code specified by an $X$-type stabilizer generator matrix $S$, a logical generator matrix $L$, and an odd-integer vector $t$  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
The matrix $S$ is $(\nu,t)$-null, while $L$ is $(\nu,t)$-orthonormal.
The vertically stacked matrix $G=[L;S]$ is $(\nu,t)$-orthogonal.
Such codes admit gates at the $\nu$th level of the \term{Clifford hierarchy}.

The $(\nu,t)$-norm of a binary vector $v$ is
\begin{align}
  \lVert v\rVert_{\nu,t}=\sum_i v_i t_i \pmod {2^\nu}.
\end{align}
Two vectors $v,w$ are $(\nu,t)$-orthogonal if
\begin{align}
  \sum_i v_i t_i w_i \equiv 0 \pmod {2^{\nu-1}}.
\end{align}
A set of vectors is $(\nu,t)$-orthogonal if the spans of every two disjoint subsets are $(\nu,t)$-orthogonal.
An orthogonal set is null if every vector in its span has zero norm.
It is orthonormal if each row has norm one.

Equivalently, $(\nu,t)$-orthogonality of $G$ requires
\begin{align}
  2^{|A|-1}\sum_i t_i\prod_{a\in A}G_{a i}\equiv 0\pmod {2^\nu}
\end{align}
for every set $A$ of at least two and at most $\nu$ distinct rows  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
The conditions range over the rows of the full matrix $G$, so they constrain logical $X$ representatives as well as $X$-type stabilizers.
At level three, all weighted pair products therefore vanish modulo four and all weighted triple products vanish modulo two.

For positive stabilizer signs and $t=(1,\ldots,1)$, preservation of the code space by the transversal $Z$-rotation by $\pi/2^{\nu-1}$ requires
\begin{align}
  2^\nu&\mid \mathrm{wt}(w) &&\text{for all }w\in\operatorname{span}(S),\\
  2^{\nu-1}&\mid \mathrm{wt}(w*z) &&\text{for all }w\in\operatorname{span}(S),\ z\in\operatorname{span}(G),
\end{align}
where $\mathrm{wt}$ is the Hamming weight and $*$ is the entrywise product  ([arXiv:2109.13481](https://arxiv.org/abs/2109.13481)).

Generalized quantum divisible codes can be level-lifted from $\nu$ to $\nu+1$  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
This procedure recursively yields towers from a ground code  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- A level-$\nu$ generalized quantum divisible code admits a diagonal transversal gate at the $\nu$th level of the \term{Clifford hierarchy}  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).

## Relations

- _parent_: [[concepts/qec/qubit-css]] — Generalized quantum divisible codes are CSS codes. Any self-dual CSS code yields a level-three generalized quantum divisible code when level-lifted  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — Both generalized quantum divisible codes and triorthogonal codes are CSS codes. Every level-three generalized quantum divisible code is a triorthogonal code, while the converse was left open in Ref.  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
- _cousin_: [[concepts/qec/random-stabilizer]] — Random CSS codes  ([arXiv:quant-ph/9512032](https://arxiv.org/abs/quant-ph/9512032)) can be used to construct families of $⟦O(d^{\nu−1}), \Omega(d), d⟧$ level-$\nu$ generalized quantum divisible codes  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
