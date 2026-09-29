---
type: concept
name: Two-branch coset CSS code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qldpc
- concepts/qec/quasi-cyclic-qldpc
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/two_branch_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: two_branch_css
---

# Two-branch coset CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/two_branch_css) (`code_id: two_branch_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit CSS code whose base stabilizer generator matrices place the support of each check on translated cosets of a multiplicative subgroup $M$ of a finite field, once in each of two copies of the qubit set called *branches*  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
The branch coefficients are chosen so that any overlap between an $X$-type and a $Z$-type check occurs once in each branch and is therefore even.
Any overlap between two checks of the same type occurs in at most one branch, which excludes four-cycles.
A cyclic lift of the base pair by circulant permutation matrices can then randomize the edge connections while preserving these constraints  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).

Fix a column weight $J$, a finite field $\mathbb{F}$, and a subgroup $M$ of $\mathbb{F}^{\times}$ of order $L/2$.
Qubits are indexed by triples $(\lambda,t,h)$ with branch $\lambda\in\{0,1\}$, translation $t\in\mathbb{F}$, and $h\in M$, and checks of each type by pairs $(i,r)$ with $i<J$ and $r\in\mathbb{F}$.
Each branch carries coefficient vectors $a^{(\lambda)},b^{(\lambda)}\in\mathbb{F}^J$, and qubit $(\lambda,t,h)$ lies in the $X$-type checks $(i,t+a^{(\lambda)}_i h)$ and the $Z$-type checks $(j,t+b^{(\lambda)}_j h)$ for all $i,j<J$.
Every check then has weight $L=2|M|$, every qubit has degree $J$ in each matrix, and the base length is $2|\mathbb{F}||M|$.
Under the nonzero-difference conditions of Ref.  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)), an $X$-type check $(i,r)$ and a $Z$-type check $(j,s)$ share a qubit in branch $\lambda$ exactly when $s-r\in(b^{(\lambda)}_j-a^{(\lambda)}_i)M$, and then exactly one.
The coset equalities $(b^{(0)}_j-a^{(0)}_i)M=(b^{(1)}_j-a^{(1)}_i)M$ for all $i,j$ therefore make the two matrices orthogonal  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
Disjointness of the same-type difference cosets $(a^{(0)}_{i'}-a^{(0)}_i)M$ and $(a^{(1)}_{i'}-a^{(1)}_i)M$, and likewise for $b$, excludes same-type four-cycles  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
These coset conditions turn the search for a regular base pair into a finite check on field coefficients.
When every $X$-type and $Z$-type check share zero or two base qubits, the base pair can be given a $G$-lift over a cyclic group by circulant permutation matrices.
The shifts on each shared pair are constrained so that the two lifted blocks cancel, which preserves orthogonality  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
The remaining circulant shifts are chosen to raise the girth and to remove targeted low-weight logical operators  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).

A $64$-fold lift of the $(3,10)$-regular $⟦160,76,4⟧$ base over $\mathbb{F}_{16}$ yields a $⟦10240,4108,18 \leq d \leq 32⟧$ code of rate $0.401$ whose same-type Tanner graphs have girth at least eight  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
See Ref.  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)) for base codes at other column and row weights.

(source: raw/error-correction-zoo.md)

## Protection

Base codes are listed for column weights three, four, and five, with exact distances up to $12$  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
A $(3,30)$-regular base over $\mathbb{F}_{31}$ yields a $⟦930,748,6⟧$ code attaining the design rate $1-2J/L=0.8$  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
This field size and base length are the smallest possible at that design rate under the two-branch coset conditions  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).

## Decoders

- Joint belief propagation with low-complexity deterministic post-processing  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)). For the $⟦10240,4108,18 \leq d \leq 32⟧$ code, this decoder reaches a frame error rate of $10^{-7}$ at depolarizing probability $p=0.058$  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).

## Relations

- _parent_: [[concepts/qec/qubit-css]] — Multiplicative-coset conditions make the two binary stabilizer generator matrices orthogonal, so they define a qubit CSS code  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
- _parent_: [[concepts/qec/qldpc]] — The check weight $L=2|M|$ and qubit degree $J$ of a two-branch coset CSS code are independent of the field size and of the lift  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
- _cousin_: [[concepts/qec/quasi-cyclic-qldpc]] — The optional cyclic lift produces QC-QLDPC codes whose stabilizer generator matrices are arrays of circulant permutation blocks and are invariant under a simultaneous shift of the lift coordinates  ([arXiv:2605.23894](https://arxiv.org/abs/2605.23894)).
