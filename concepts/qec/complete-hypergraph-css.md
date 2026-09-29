---
type: concept
name: Complete-hypergraph CSS code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hypercube-quantum
- concepts/qec/phantom
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/complete_hypergraph_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: complete_hypergraph_css
---

# Complete-hypergraph CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/complete_hypergraph_css) (`code_id: complete_hypergraph_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Family of qubit CSS codes, one for each rank $t\geq2$ and each number $k\geq t$ of logical qubits, whose physical qubits store the parities of all subsets of at most $t$ logical qubits.
A layer of physical single-qubit diagonal gates at level $t$ of the \term{Clifford hierarchy} realizes every addressable diagonal logical gate at that level, at the smallest block length for which this is possible  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)).

One physical qubit is placed on each nonempty subset $A\subseteq\{1,\dots,k\}$ of size at most $t$, so that $n=\sum_{s=1}^{t}\binom{k}{s}$.
For fixed $t$, this is of order $\Theta(k^t)$  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)).
There are no $X$-type stabilizer generators.
The $Z$-type generators are the weight-three checks $Z_A Z_{A\setminus\{i\}} Z_{\{i\}}$ for $|A|\geq2$ and a chosen $i\in A$, which together enforce $z_A=\bigoplus_{i\in A}z_{\{i\}}$  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)).
Logical operators are $\overline{Z}_i=Z_{\{i\}}$ on a singleton qubit and $\overline{X}_i=\prod_{A\ni i}X_A$.
The $X$-logical subspace is the classical simplex code punctured to the coordinates labelled by subsets of size at most $t$.
Physical qubits carrying the parity of more than two logical qubits were introduced as the higher-order parity encoding  ([arXiv:2205.09517](https://arxiv.org/abs/2205.09517)).
The rank-$t$ family is that encoding with a completely symmetric choice of codespace, taking every subset of size at most $t$.

At rank $t=k$ the puncturing is trivial.
There are $n=2^k-1$ physical qubits, one per nonzero vector of $\mathbb{F}_2^k$, the $Z$-type stabilizer space is the classical Hamming code, and the $X$-logical subspace is the full simplex code.
This member is the *simplex phantom code*  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)) which attains the phantom-code bound $n\geq2^k-1$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).

(source: raw/error-correction-zoo.md)

## Protection

The $X$-distance is $d_x=\sum_{s=0}^{t-1}\binom{k-1}{s}$, attained by the logical operators $\overline{X}_i$  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)).
For fixed $t$, this is of order $\Theta(k^{t-1})$.
Every logical $Z$ operator has a weight-one representative on a singleton qubit, so phase errors are not protected  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)).

## Transversal gates

- A tensor product of physical $Z^{(t)}=Z^{1/2^{t-1}}$ rotations and their powers realizes every element of the addressable diagonal logical group at level $t$ of the \term{Clifford hierarchy}  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)). The block length $n=\sum_{s=1}^{t}\binom{k}{s}$ is exactly the minimum at which that logical group can be realized by transversal single-qubit diagonal gates  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)).
- A parity qubit carrying the parity of $t$ logical qubits turns the diagonal logical rotation $\exp(i\phi\overline{Z}_{q_1}\cdots\overline{Z}_{q_t})$ into a physical single-qubit rotation, at arbitrary angle  ([arXiv:2205.09517](https://arxiv.org/abs/2205.09517)).
- At rank two, physical $S$ gates and their powers give every addressable logical $S$ and CZ gate. At rank three, physical $T$ gates give every addressable logical $T$, CS, and CCZ gate  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _cousin_: [[concepts/qec/phantom]] — The simplex phantom code is a member of this family  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)). It attains the phantom-code bound $n\geq2^k-1$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).
- _cousin_: [`simplex`](https://errorcorrectionzoo.org/c/simplex) — The $X$-logical subspace of a rank-$t$ complete-hypergraph CSS code is the simplex code punctured to the coordinates labelled by subsets of size at most $t$, and is the full simplex code for the simplex phantom code.
- _cousin_: [`hamming`](https://errorcorrectionzoo.org/c/hamming) — The $Z$-type stabilizer space of the simplex phantom code is the Hamming code.
- _cousin_: [[concepts/qec/hypercube-quantum]] — The simplex phantom code is obtained from the $⟦2^k,k,2⟧$ hypercube quantum code by deleting one qubit and discarding the $X$-type stabilizer generator  ([arXiv:2609.19250](https://arxiv.org/abs/2609.19250)).
