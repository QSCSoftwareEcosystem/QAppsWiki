---
type: concept
name: Galois-qudit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-cws
- concepts/qec/galois-non-stabilizer
- concepts/qec/qudit-stabilizer
- concepts/qec/stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_stabilizer
---

# Galois-qudit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_stabilizer) (`code_id: galois_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $((n,K,d))_q$ Galois-qudit code whose logical subspace is the joint eigenspace of commuting Galois-qudit Pauli operators forming the code's stabilizer group $\mathsf{S}$. Traditionally, the logical subspace is the joint $+1$ eigenspace, and the stabilizer group does not contain $e^{i \phi} I$ for any $\phi \neq 0$. The distance $d$ is the minimum weight of a Galois-qudit Pauli string that implements a nontrivial logical operation in the code.

A Galois-qudit stabilizer code encoding an integer number of qudits ($K=q^k$) is denoted as $⟦n,k⟧_q$ or $⟦n,k,d⟧_q$.
This notation differentiates between Galois-qudit and modular-qudit $⟦n,k,d⟧_{\mathbb{Z}_q}$ stabilizer codes, although the same notation is usually used for both.
Galois-qudit stabilizer codes need not encode an integer number of qudits, with $K=q^{n-\frac{r}{m}}$, where $r$ is the number of generators of the stabilizer group, and $q=p^m$ given prime $p$ for all Galois qudits.
As a result, $⟦n,k,d⟧$ notation is often used with non-integer $k=\log_q K$.

\begin{defterm}{Galois symplectic representation}
\label{topic:galois-symplectic-representation}
The single Galois-qudit Pauli string $X_{a} Z_{b}$ for $a,b\in \mathbb{F}_q$ is converted to the vector $(a|b)\in \mathbb{F}_q^2$.
The multi Galois-qudit version follows naturally.
\end{defterm}

A pair of Galois-qudit stabilizers on $n$ Galois qudits with Galois symplectic representation vectors $(a|b)$ and $(a^{\prime}|b^{\prime})$ commute iff their *trace symplectic inner product* is zero,
\begin{align}
\text{tr}(a \cdot b^{\prime} - a^{\prime}\cdot b) = \sum_{j=1}^{n} \text{tr}(a_j b^{\prime}_j - a^{\prime}_j b_j) = 0~.
\end{align}
Galois symplectic representations of stabilizer group elements form a trace-symplectic self-orthogonal linear code over $\mathbb{F}_q^{2n}$.
The trace-symplectic inner product reduces to the *symplectic inner product* when the field trace is removed, and a symplectic self-orthogonal set of vectors is automatically trace-symplectic self-orthogonal.

Another correspondence between Galois-qudit Pauli matrices and elements of the Galois field $\mathbb{F}_{q^2}$ yields the one-to-one correspondence between Galois-qudit stabilizer codes and trace-alternating self-orthogonal additive codes over $\mathbb{F}_{q^2}$  ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)).

\begin{defterm}{$\mathbb{F}_{q^2}$ representation}
\label{topic:gfqsq-representation}
An $n$-qudit Galois-qudit Pauli stabilizer can be represented as a length-$n$ vector over $\mathbb{F}_{q^2}$ using the one-to-one correspondence between the $q^2$ Galois-qudit Pauli matrices and elements of $\mathbb{F}_{q^2}$.
Given a basis $(\beta,\beta^q)$ for $\mathbb{F}_{q^2}$ over $\mathbb{F}_q$, the vector $(a|b)\in \mathbb{F}_q^2$ (representing a Galois-qudit Pauli string in the Galois symplectic representation) is in one-to-one correspondence with element $a \beta + b \beta^q \in \mathbb{F}_{q^2}$  ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)).
\end{defterm}

The sets of $\mathbb{F}_{q^2}$-represented vectors for all generators yield a trace-alternating self-orthogonal additive code over $\mathbb{F}_{q^2}$.

Recalling that $q=p^m$, Galois-qudit stabilizer codes can also be treated as prime-qudit stabilizer codes on $mn$ qudits, giving $k=nm-r$  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)).
In principle, Galois-qudit stabilizer states can be expressed in terms of linear and quadratic functions over $\mathbb{Z}_p^{mn}$  ([arXiv:quant-ph/0408190](https://arxiv.org/abs/quant-ph/0408190)).
Such states correspond to the set of states with positive Wigner functions  ([arXiv:quant-ph/0602001](https://arxiv.org/abs/quant-ph/0602001), [arXiv:quant-ph/0702004](https://arxiv.org/abs/quant-ph/0702004)).

Galois-qudit stabilizer codes can equivalently  ([arXiv:quant-ph/0111080](https://arxiv.org/abs/quant-ph/0111080)) (see also  ([arXiv:quant-ph/0703112](https://arxiv.org/abs/quant-ph/0703112))) be defined using graphs, yielding an analytical form for the codewords  ([arXiv:quant-ph/0012111](https://arxiv.org/abs/quant-ph/0012111)).

(source: raw/error-correction-zoo.md)

## Protection

Detects errors on up to $d-1$ qudits, and corrects erasure errors on up to $d-1$ qudits. Corrects errors on $\left\lfloor (d-1)/2 \right\rfloor$ qudits.
There are algorithms to calculate the minimum distance  ([arXiv:2308.15140](https://arxiv.org/abs/2308.15140)).
There are established shortening/lengthening procedures for pure Galois-qudit stabilizer codes  ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)) ([arXiv:1502.05267](https://arxiv.org/abs/1502.05267)).

## Encoders

- Encoder with $O(n^2)$ gates can be determined in classical runtime of order $O(n^3)$  ([arXiv:quant-ph/0211014](https://arxiv.org/abs/quant-ph/0211014)).

## General gates

- As opposed to modular qudits for composite $q$, Galois qudits inherit most of the properties of the prime-qudit Clifford group due to the correspondence between a $q=p^m$ Galois qudit and $m$ prime qudits of dimension $p$  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)).

## Decoders

- Syndrome extraction and computation based on classical additive codes  ([doi:10.1103/PhysRevA.103.042420](https://doi.org/10.1103/PhysRevA.103.042420)).

## Relations

- _parent_: [[concepts/qec/galois-non-stabilizer]] — A Galois-qudit stabilizer code with stabilizer group $\mathsf{S}$ can be thought of as a Galois-qudit USt with only the identity coset representative. Conversely, if $K = q^k$, and if the set of coset representatives of a Galois-qudit USt form a $q$-ary linear code, then they can be absorbed into a Galois-qudit stabilizer group that defines the USt.
- _parent_: [[concepts/qec/stabilizer]]
- _cousin_: [[concepts/qec/galois-cws]] — Galois-qudit CWS codes whose underlying classical code is a linear $q$-ary code are Galois-qudit stabilizer codes containing a cluster-state codeword.
- _cousin_: [[concepts/qec/qudit-stabilizer]] — Recalling that $q=p^m$, Galois-qudit stabilizer codes can also be treated as prime-qudit stabilizer codes on $mn$ qudits, giving $k=nm-r$  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)). The case $m=1$ reduces to conventional prime-qudit stabilizer codes on $n$ qudits. A modular-qudit stabilizer code with composite dimension $q$ contains a subcode that is isomorphic to a $p$-dimensional prime-qudit stabilizer code for every prime factor $p$ of $q$, and the distance of the full stabilizer code is bounded by the distance of this subcode .
- _cousin_: [`q-ary_additive`](https://errorcorrectionzoo.org/c/q-ary_additive) — Galois-qudit stabilizer codes are the closest quantum analogues of additive codes over $\mathbb{F}_q$ because addition in the field corresponds to multiplication of stabilizers in the quantum case.
- _cousin_: [`dual_additive`](https://errorcorrectionzoo.org/c/dual_additive) — Galois-qudit stabilizer codes are in one-to-one correspondence with trace-symplectic self-orthogonal additive codes of length $2n$ over $\mathbb{F}_q$ via the Galois symplectic representation  ([doi:10.1109/18.959288](https://doi.org/10.1109/18.959288)). They are also in one-to-one correspondence with trace-alternating self-orthogonal additive codes of length $n$ over $\mathbb{F}_{q^2}$ via the $\mathbb{F_{q^2}$ representation}.
- _cousin_: [`t-designs`](https://errorcorrectionzoo.org/c/t-designs) — Stabilizer states on $n$ Galois qubits form 2-designs on complex projective spaces $\mathbb{C}P^{p^{mn}}$  ([arXiv:quant-ph/0405016](https://arxiv.org/abs/quant-ph/0405016)).
- _cousin_: [`complex_projective`](https://errorcorrectionzoo.org/c/complex_projective) — Stabilizer states on $n$ Galois qubits form 2-designs on complex projective spaces $\mathbb{C}P^{p^{mn}}$  ([arXiv:quant-ph/0405016](https://arxiv.org/abs/quant-ph/0405016)).

## Notes

- Tables of bounds and examples of Galois-qudit stabilizer codes for various $n$ and $k$, based on algorithms developed in Refs.  ([doi:10.1007/978-3-540-37634-7_13](https://doi.org/10.1007/978-3-540-37634-7_13), [arXiv:2405.15057](https://arxiv.org/abs/2405.15057)), are maintained by M. Grassl at this [website](https://www.codetables.de/). A Magma implementation exists at this [website](https://magma.maths.usyd.edu.au/magma/handbook/text/1976). A modular-qudit stabilizer code with composite dimension $q$ contains a subcode that is isomorphic to a $p$-dimensional prime-qudit stabilizer code for every prime factor $p$ of $q$, and the distance of the full stabilizer code is upper bound by the distance of this subcode .
- The number of Galois-qudit stabilizer codes was determined in Ref.  ([arXiv:quant-ph/0602001](https://arxiv.org/abs/quant-ph/0602001)).
- See Quantum Codes qudit stabilizer database, maintained by N. Aydin, P. Liu, and B. Yoshino  ([arXiv:2106.12065](https://arxiv.org/abs/2106.12065), [arXiv:2108.03567](https://arxiv.org/abs/2108.03567)), at this [website](http://quantumcodes.info/).
- Review of nonbinary stabilizer codes  ([doi:10.1201/9781584889007-18](https://doi.org/10.1201/9781584889007-18)).
