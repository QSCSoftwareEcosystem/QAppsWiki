---
type: concept
name: Abelian two-block group-algebra code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Multivariate bicycle (MB) code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2bga
- concepts/qec/abelian-lifted-product
- concepts/qec/galois-hypergraph-product
- concepts/qec/multivariate-multicycle
- concepts/qec/perm-self-dual-css
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/abelian_2bga
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: abelian_2bga
---

# Abelian two-block group-algebra code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/abelian_2bga) (`code_id: abelian_2bga`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 2BGA code LP$(a,b)$ whose group $G$ is Abelian, equivalently a multi-dimensional index-two quasi-cyclic code.
Since any finite Abelian group is a direct product of cyclic groups, the group algebra elements $a$ and $b$ can be treated as multivariate polynomials.
The family includes GB (one variable), bivariate bicycle (two variables), and higher-variable codes, providing some of the best known short codes with small stabilizer weights.

Writing $G=\mathbb{Z}_{\ell_1}\times \mathbb{Z}_{\ell_2}\times \cdots \times \mathbb{Z}_{\ell_D}$, the elements $a$ and $b$ become $D$-variate polynomials in $\mathbb{F}_q[x_1,\ldots,x_D]/\langle x_1^{\ell_1}-1,\ldots,x_D^{\ell_D}-1 \rangle$, yielding stabilizer generator matrices
\begin{align}
  H_X=(A|B)~,\quad H_Z=(B^T|-A^T)~,
\end{align}
where $A$ and $B$ are sums of Kronecker products of circulant matrices representing $a$ and $b$.
An equivalent construction in terms of Kronecker products of circulant matrices was introduced in Ref.  ([arXiv:1212.6703](https://arxiv.org/abs/1212.6703)).
Related higher-dimensional quasi-cyclic and convolutional quantum codes are constructed in Ref.  ([arXiv:2305.00137](https://arxiv.org/abs/2305.00137)).

The decomposition of $G$ into cyclic factors, and hence the number of variables $D$, is not unique (see the MM code entry).
For example, $\mathbb{Z}_{15}$ yields a GB code in one variable, whereas the isomorphic $\mathbb{Z}_{5}\times\mathbb{Z}_{3}$ yields a bivariate bicycle code in two variables.

Qubit Abelian 2BGA codes in $r$ variables have been studied in the trivariate ($r=3$) case, in which a third, dependent variable $z=xy$ supplements the two variables of a bivariate bicycle code  ([arXiv:2406.19151](https://arxiv.org/abs/2406.19151)).
Such codes with check weight at most six admit bi-planar (thickness-two) Tanner graphs, and there is a criterion for determining whether a code admits a toric layout  ([arXiv:2406.19151](https://arxiv.org/abs/2406.19151)).
Weight-five examples, such as a $⟦30,4,5⟧$ code, admit bi-planar toric layouts with a single long-range connection per check and depth-seven syndrome-extraction circuits, whereas weight-four codes can instead admit tangled toric layouts  ([arXiv:2406.19151](https://arxiv.org/abs/2406.19151)).

(source: raw/error-correction-zoo.md)

## Protection

The code dimension $k$ of an Abelian 2BGA code is always even .
Bounds on code parameters and an enumeration of codes with small row weights, including codes with $kd \geq n$, are given in Ref.  ([arXiv:2306.16400](https://arxiv.org/abs/2306.16400)).

## General gates

- Several qubit Abelian 2BGA codes admit fault-tolerant logical circuits implemented via transversal operations combined with qubit permutations, obtained from code automorphism groups  ([arXiv:2406.19151](https://arxiv.org/abs/2406.19151)).
- Certain qubit Abelian 2BGA codes admit a constant-depth inter-code logical $CZ$ gate between two copies of the code via the 2-copy-cup gate  ([arXiv:2602.23307](https://arxiv.org/abs/2602.23307)).
The gate exists when the check polynomials satisfy a pre-orientation condition equivalent to a graph perfect-matching problem  ([arXiv:2602.23307](https://arxiv.org/abs/2602.23307)).
Examples include the $⟦16,6,4⟧$ copy-cup code and check-weight-six codes such as $⟦72,8,6⟧$, $⟦108,12,6⟧$, and $⟦144,16,6⟧$  ([arXiv:2602.23307](https://arxiv.org/abs/2602.23307)).

## Code capacity threshold

- Qubit Abelian 2BGA families with fixed check weight and polynomially growing distance have vanishing rate  ([arXiv:2607.21160](https://arxiv.org/abs/2607.21160)). When such a family has a unique threshold, its optimal code capacity threshold under bit-flip noise is constrained by the Kramers-Wannier self-duality of zero-rate PSD codes  ([arXiv:2607.21160](https://arxiv.org/abs/2607.21160)).

## Relations

- _parent_: [[concepts/qec/2bga]] — Abelian 2BGA codes are 2BGA codes whose group is Abelian.
- _parent_: [[concepts/qec/abelian-lifted-product]] — Abelian 2BGA codes are the one-by-one (scalar) Abelian LP codes.
- _parent_: [[concepts/qec/multivariate-multicycle]] — Abelian 2BGA codes are MM codes with $t=2$.
- _cousin_: [[concepts/qec/galois-hypergraph-product]] — An Abelian 2BGA code whose elements $a$ and $b$ are supported on subgroups intersecting trivially is a square-matrix hypergraph-product code constructed from a pair of classical group-algebra codes  ([arXiv:2306.16400](https://arxiv.org/abs/2306.16400)).
Elements given by polynomials in disjoint sets of variables satisfy this condition.
See the cyclic HGP code entry for the case of two cyclic codes.
- _cousin_: [[concepts/qec/translationally-invariant-stabilizer]] — Qubit Abelian 2BGA codes admitting a toric layout have translationally invariant checks on an $r$-dimensional torus  ([arXiv:2406.19151](https://arxiv.org/abs/2406.19151)).
- _cousin_: [[concepts/qec/perm-self-dual-css]] — Qubit Abelian 2BGA codes are permutationally self-dual  ([arXiv:2306.16400](https://arxiv.org/abs/2306.16400)). Exchanging the two blocks of qubits while inverting each group element is an involutive $XZ$-duality  ([arXiv:2407.03973](https://arxiv.org/abs/2407.03973)).
