---
type: concept
name: Multivariate multicycle (MM) code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Abelian multi-cycle (AMC) code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/double-homological-product
- concepts/qec/lacross
- concepts/qec/multi-block-quantum
- concepts/qec/multisector-hypergraph
- concepts/qec/quantum-quasi-cyclic
- concepts/qec/quantum-tanner
- concepts/qec/single-shot
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/multivariate_multicycle
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: multivariate_multicycle
---

# Multivariate multicycle (MM) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/multivariate_multicycle) (`code_id: multivariate_multicycle`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Multi-block CSS code whose $t$ commuting matrices represent elements $F_1,\ldots,F_t$ of the group algebra of a finite Abelian group, written as polynomials in $D$ variables.
Each element defines a two-term complex $S\xrightarrow{F_i}S$ over the group algebra $S$, and the tensor product of the $t$ complexes is a Koszul complex with $t+1$ terms whose boundary maps are the check and metacheck matrices  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910), [arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
For $t \geq 4$, the code has metachecks in both bases and admits complete single-shot decoding, while $t=2$ and $t=3$ recover Abelian 2BGA and tricycle codes  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).

Writing $G \cong \mathbb{Z}_{\ell_1}\times\cdots\times\mathbb{Z}_{\ell_D}$, the group algebra is the quotient polynomial ring $S=\mathbb{F}_q[x_1,\ldots,x_D]/\langle x_1^{\ell_1}-1,\ldots,x_D^{\ell_D}-1\rangle$, so that a code is specified by $t$ polynomials $F_1,\ldots,F_t \in S$, each represented by a sum of Kronecker products of circulant matrices  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910), [arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
The number of polynomials $t$ (the number of ``cycles'') and the number of variables $D$ can be chosen independently.
The number of variables is a matter of presentation.
By the Chinese remainder theorem, coprime cyclic factors can be split or merged, so $\mathbb{Z}_{15}$ and $\mathbb{Z}_{5}\times\mathbb{Z}_{3}$ present the same code with $D=1$ and $D=2$, respectively.

The level-$q$ space of the Koszul complex $K_{\bullet}(F_1,\ldots,F_t;S)$ is $S^{\binom{t}{q}}$, and its boundary maps $\partial_q$ are available in closed form  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
In the Koszul-complex formulation  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)), qubits are placed at the middle level $q=\lfloor t/2\rfloor$, yielding $P_X=\partial_q^T$ and $P_Z=\partial_{q+1}$.
The $X$-type metacheck matrix is $M_X = \partial_{q-1}^T$ whenever $t\geq 4$, and the $Z$-type metacheck matrix is $M_Z=\partial_{q+2}$ whenever $t\geq 3$.
The multi-block-complex formulation  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)) allows qudits to be placed at any level $0<j<t$ of the same complex.
It also admits a general Abelian group presentation whose relators define a periodicity lattice on $\mathbb{Z}^D$, i.e., a torus  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).

A CSS code together with metacheck matrices $M_X$ and $M_Z$ satisfying $M_X P_X = 0$ and $M_Z P_Z = 0$ forms a five-term chain complex and is dubbed a *metacheck CSS (mCSS) code*  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
An mCSS code is *balanced* when its outermost pair and its next-to-outermost pair of spaces each have equal dimensions  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
Any five-term segment of a longer chain complex yields an mCSS code, and the middle five terms of the Koszul complex of an MM code with even $t$ yield a balanced one.

Fixing $t$ and $D$ recovers several known code families, each with explicit MM polynomials  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
Abelian 2BGA codes ($t=2$) include GB codes ($D=1$), bivariate bicycle codes ($D=2$), and higher-variable Abelian 2BGA codes.
They also include cyclic hypergraph-product codes ($D=2$ with polynomials in disjoint variables) and La-cross codes with periodic boundary conditions ($D=2$, with $G=\mathbb{Z}_n\times\mathbb{Z}_n$).
Haah cubic codes on a cubic lattice have $t=2$ and $D=3$.
Weight-two elements $a_i=1+x_i$ with $t=D$ yield $D$-dimensional toric codes on regular or twisted tori, with arbitrary twists realized via general group presentations  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).

A $⟦144,12,12⟧$ MM code has the same parameters as, but is distinct from, the gross code  ([arXiv:2308.07915](https://arxiv.org/abs/2308.07915), [arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
A family of MM codes locally equivalent to 4D toric codes, with weight-six stabilizer generators and $k=6$, is constructed in Ref.  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
Codes with $t=5$ through $t=9$ provide the first explicit instances of collapsed 5D through 9D higher-dimensional codes  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
See Ref.  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)) for tables of MM codes with $t \geq 4$, including a $⟦648,60,(9,9)⟧$ code whose check and metacheck matrices are written out explicitly.

(source: raw/error-correction-zoo.md)

## Protection

Analytic expressions for the code dimension in two general cases, as well as lower (existence) and upper bounds on the distance, are derived in Ref.  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).

## Decoders

- BP-OSD and Tesseract decoders  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
- Few-shot sliding-window decoding  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
- Single-shot decoding using metachecks for $t \geq 4$, with confinement profiles surpassing those of known single-shot-decodable CSS codes of practical block size  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).

## Threshold

- Circuit-level noise: pseudo-threshold close to $1.1\%$ for MM codes locally equivalent to 4D toric codes, better than for toric or surface codes under a similar noise model  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).

## Relations

- _parent_: [[concepts/qec/multi-block-quantum]] — MM codes are multi-block CSS codes whose commuting matrices represent Abelian group-algebra elements  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910), [arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
- _parent_: [[concepts/qec/quantum-quasi-cyclic]] — After ordering coordinates by translation orbits, translation by any cyclic factor of the Abelian group simultaneously shifts every group-algebra block, making every MM code quasi-cyclic  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910), [arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
- _cousin_: [[concepts/qec/lacross]] — La-cross codes with periodic boundary conditions are $t=2$ MM codes over $\mathbb{Z}_n\times\mathbb{Z}_n$  ([arXiv:2404.13010](https://arxiv.org/abs/2404.13010), [arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
Their open-boundary versions fall outside the periodic group-algebra construction  ([arXiv:2404.13010](https://arxiv.org/abs/2404.13010), [arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
- _cousin_: [[concepts/qec/multisector-hypergraph]] — MM codes are related to $D$-dimensional homological (hypergraph) product codes in the same way that two-block codes are related to hypergraph-product codes  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910), [arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
MM codes can be viewed as collapsed versions of $t$-fold products of two-term complexes  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910), [arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
- _cousin_: [[concepts/qec/double-homological-product]] — Both Campbell double homological product codes and MM codes with $t \geq 4$ admit metachecks in both bases  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
The MM construction yields shorter codes  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
- _cousin_: [[concepts/qec/single-shot]] — MM codes with $t \geq 4$ admit metachecks in both bases and demonstrate complete single-shot decoding with record confinement profiles  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
Single-shot properties of these codes are also studied in Ref.  ([arXiv:2506.16910](https://arxiv.org/abs/2506.16910)).
- _cousin_: [[concepts/qec/quantum-tanner]] — Collapsed 5D through 9D MM codes have lower check weights than small instances of quantum Tanner codes  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)) (cf.  ([arXiv:2508.05095](https://arxiv.org/abs/2508.05095), [arXiv:2512.20532](https://arxiv.org/abs/2512.20532))).

## Notes

- See QuantumClifford.jl Julia software library for MM code instances, stabilizer states, and Clifford circuits  ([arXiv:2601.18879](https://arxiv.org/abs/2601.18879)).
