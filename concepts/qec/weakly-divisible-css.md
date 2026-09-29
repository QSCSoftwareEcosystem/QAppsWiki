---
type: concept
name: Weakly divisible CSS code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-quantum-divisible
- concepts/qec/quantum-triorthogonal
- concepts/qec/qubit-concatenated
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/weakly_divisible_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: weakly_divisible_css
---

# Weakly divisible CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/weakly_divisible_css) (`code_id: weakly_divisible_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A weakly $\Delta$-divisible CSS code for $\Delta>1$ is a CSS code whose $X$-type stabilizer space obeys a signed divisibility condition on two disjoint sets of qubits.
The condition allows coordinates outside those sets and does not constrain the logical $X$ representatives.
Weakly four-divisible and weakly eight-divisible CSS codes are also called $\mathrm{DE}^*$ and $\mathrm{TE}^*$ codes, respectively.

More explicitly, the binary space $C_2$ of $X$-type stabilizers is weakly $\Delta$-divisible if there are disjoint subsets $M^+,M^-\subseteq[n]$ such that
\begin{align}
  |u\cap M^+|-|u\cap M^-|\equiv0\pmod\Delta
\end{align}
for every $u\in C_2$  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).
At least one of $M^+$ and $M^-$ is required to be nonempty  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)).
Coordinates outside $M^+\cup M^-$ do not contribute to the congruence.
Ordinary $\Delta$-divisibility is recovered by taking $M^+=[n]$ and $M^-=\emptyset$.
Weak $\Delta$-divisibility implies weak $\Delta^{\prime}$-divisibility for every divisor $\Delta^{\prime}$ of $\Delta$.

\subsection{Coset divisibility}
A stronger condition applies to a CSS code defined by binary linear codes $C_2\subseteq C_1$ and a character vector $y$ fixing the signs of the $Z$-type stabilizers.
Coset divisibility requires the codeword weights to be constant modulo $\Delta$ within each coset of $C_2$ in $C_1+y$  ([arXiv:2109.13481](https://arxiv.org/abs/2109.13481)) ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).

More explicitly, coset divisibility requires
\begin{align}
  \operatorname{wt}(u+w)\equiv\operatorname{wt}(w)\pmod\Delta
\end{align}
for every $u\in C_2$ and $w\in C_1+y$.
Taking $w=y$ shows that every coset-divisible code is weakly divisible with $M^-=\operatorname{supp}(y)$ and $M^+=[n]\setminus M^-$.
The converse need not hold because weak divisibility tests only this one element of $C_1+y$, rather than every logical coset representative.
Positive signs correspond to $y=0$, in which case the trivial coset shows that $C_2$ is a $\Delta$-divisible classical code.
A $\Delta$-coset-divisible code is also $\Delta^{\prime}$-coset-divisible for every divisor $\Delta^{\prime}$ of $\Delta$.

For $\Delta=2^\nu$ and $y=0$, the above is equivalent to $2^\nu$ dividing $\operatorname{wt}(u)$ for every $u\in C_2$, together with $2^{\nu-1}$ dividing $\operatorname{wt}(u*w)$ for every $u\in C_2$ and $w\in C_1$  ([arXiv:2109.13481](https://arxiv.org/abs/2109.13481)).
Here $*$ denotes the entrywise product.

(source: raw/error-correction-zoo.md)

## Transversal gates

- A weakly triply even $⟦n,1,d⟧$ CSS code with a strongly transversal logical $X$ gate admits a partitioned transversal physical $T$ gate that realizes $\overline{T}^m$, where $m=|M^+|-|M^-| \pmod 8$  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)) ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).
The logical gate is non-Clifford when $m$ is odd.
- For the coset-divisible subclass, the uniform transversal gate $\operatorname{diag}(1,e^{2\pi i/\Delta})$ preserves the code space and induces a logical diagonal gate determined by the coset residues  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
For $\Delta=2^\nu$, this gate corresponds to the all-ones exponent vector in the group of diagonal transversal gates preserving the code  ([arXiv:2601.21514](https://arxiv.org/abs/2601.21514)).
Algorithms determine this group for a given CSS code  ([arXiv:2303.15615](https://arxiv.org/abs/2303.15615), [arXiv:2607.26477](https://arxiv.org/abs/2607.26477)).
- Consider a CSS code whose $X$-type stabilizers form a $\nu$-even space, and for which the entrywise product of every $X$-type logical operator and $X$-type stabilizer has weight divisible by $2^{\nu-1}$.
Such a code admits a diagonal transversal gate at the $\nu$th level of the \term{Clifford hierarchy}  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).
- Transversal $T^\dagger$ preserves the quadratic-form family and induces, up to global phase, $\exp(i\pi Z^{\otimes k}/8)$ on its $k$ logical qubits  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
This logical gate decomposes into $T$ on every logical qubit, controlled-Phase$^\dagger$ on every pair, and $CCZ$ on every triple.

## Fault tolerance

- The $⟦31,5,3⟧$ and $⟦63,7,3⟧$ members can serve as outer codes for the five-qubit and Steane codes, respectively.
The resulting layered constructions implement a fault-tolerant logical $T$ gate on the inner code without teleporting magic states  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
Encoding and decoding are required to pass between the inner and outer codes.

## Realizations

- Triply even codes can yield secure multi-party quantum computation  ([arXiv:2206.04871](https://arxiv.org/abs/2206.04871)).

## Relations

- _parent_: [[concepts/qec/qubit-css]] — Weakly divisible CSS codes are CSS codes whose $X$-type stabilizer spaces satisfy a signed divisibility condition  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).
- _cousin_: [[concepts/qec/generalized-quantum-divisible]] — Weak divisibility constrains signed weights in the $X$-type stabilizer space, while generalized quantum divisibility constrains the joint matrix of logical $X$ representatives and stabilizers using odd coefficients on every qubit.
- _cousin_: [`simplex`](https://errorcorrectionzoo.org/c/simplex) — One coset-divisible family takes $C_2$ to be the length-$2^m-1$ simplex code and obtains $C_1$ by adjoining evaluation vectors of bounded-rank quadratic forms  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
This yields $⟦2^m-1,k,3⟧$ codes for $m\geq4$ with $k=1+\sum_{i=1}^{m-4}(m-i)$  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
Deleting quadratic-form rows from the logical generator matrix gives the members with smaller $k$  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — The $⟦31,5,3⟧$ member together with the five-qubit code can be viewed as a factorization of a $⟦31,1,3⟧$ triorthogonal code  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — Particular coset-divisible codes can be used as outer codes in layered constructions that implement a fault-tolerant $T$ gate on the five-qubit or Steane code  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
