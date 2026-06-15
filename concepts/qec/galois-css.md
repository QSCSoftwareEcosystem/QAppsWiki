---
type: concept
name: Galois-qudit CSS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Euclidean code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/css
- concepts/qec/galois-true-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_css
---

# Galois-qudit CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_css) (`code_id: galois_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦n,k,d⟧_q $ Galois-qudit true stabilizer code admitting a set of stabilizer generators that
are either $Z$-type or $X$-type Galois-qudit Pauli strings.
Codes can be defined from chain complexes over $\mathbb{F}_q$ via an extension of qubit CSS-to-homology correspondence to Galois qudits.

The stabilizer generator matrix  ([arXiv:quant-ph/0211014](https://arxiv.org/abs/quant-ph/0211014)), taking values from $\mathbb{F}_q$, is of the form
\begin{align}
H=\begin{pmatrix}0 & H_{Z}\\
H_{X} & 0
\end{pmatrix}
\label{eq:parityg}
\end{align}
such that the rows of the two blocks must be orthogonal
\begin{align}
H_X H_Z^T=0~.
\label{eq:commG}
\end{align}
The above condition guarantees that the $X$-stabilizer generators, defined in the Galois symplectic representation as rows of $H_X$, commute with the $Z$-stabilizer generators associated with $H_Z$.

Encoding is based on two related $q$-ary linear codes,
an $[n,k_X,d_X]_q $ code $C_X$ and $[n,k_Z,d_Z]_q $ code $C_Z$,
satisfying $C_X^\perp \subseteq C_Z$ .
The resulting CSS code has $k=k_X+k_Z-n$ logical Galois qudits and distance $d\geq\min\{d_X,d_Z\}$.
The $H_X$ ($H_Z$) block of $H$ \eqref{eq:parityg} is the parity-check matrix of the code $C_X$ ($C_Z$). The requirement $C_X^\perp \subseteq C_Z$ guarantees \eqref{eq:commG}.
Specializing to the case when $C_Z=[n,k,d]_q$ is dual-containing yields a $⟦n,2k-n,\geq d_Z⟧_q$ *self-dual Galois-qudit CSS code* with $C_X = C_Z$.
When the field is a quadratic extension, such as $\mathbb{F}_4/\mathbb{F}_2$, a Galois-qudit CSS code is *Hermitian self-dual* when its $Z$-type check code is the Frobenius conjugate of its $X$-type check code, $C_Z=\overline{C_X}$.
Basis states for the code are, for coset representatives $\gamma \in C_X/C_Z^\perp$,
\begin{align}
|\gamma + C_Z^\perp \rangle = \frac{1}{\sqrt{|C_Z^\perp|}} \sum_{\eta \in C_Z^\perp} |\gamma + \eta\rangle.
\end{align}

Galois-qudit CSS codes can also be understood in terms of graphs via the *reflexive stabilizer* framework, which also allows one to define a code for a given set of Pauli errors  ([arXiv:2110.08414](https://arxiv.org/abs/2110.08414)).

(source: raw/error-correction-zoo.md)

## Protection

Detects errors on $d-1$ qudits, corrects errors on $\left\lfloor (d-1)/2 \right\rfloor$ qudits.
A quantum version of the Griesmer bound has been derived for Galois-qudit CSS codes  ([arXiv:0812.2674](https://arxiv.org/abs/0812.2674)).

An $⟦n,k,d⟧_q$ CSS code can be propagated to an $⟦n-2,k,d-1⟧_q$ code  ([arXiv:2208.05353](https://arxiv.org/abs/2208.05353)).

## Encoders

- Fault-tolerant encoding  ([arXiv:0712.3223](https://arxiv.org/abs/0712.3223)).

## Relations

- _parent_: [[concepts/qec/galois-true-stabilizer]] — The Galois-qudit CSS construction yields a true stabilizer code .
- _parent_: [[concepts/qec/css]]
- _cousin_: [`q-ary_linear`](https://errorcorrectionzoo.org/c/q-ary_linear) — The Galois-qudit CSS construction uses two related $q$-ary linear codes, $C_X$ and $C_Z$.
- _cousin_: [`q-ary_cyclic`](https://errorcorrectionzoo.org/c/q-ary_cyclic) — Galois CSS codes can be constructed using self-orthogonal $q$-ary cyclic codes  ([arXiv:1608.06674](https://arxiv.org/abs/1608.06674)).
- _cousin_: [`griesmer`](https://errorcorrectionzoo.org/c/griesmer) — A quantum version of the Griesmer bound has been derived for Galois-qudit CSS codes  ([arXiv:0812.2674](https://arxiv.org/abs/0812.2674)) and Galois-qudit stabilizer codes  ([doi:10.1109/JSAIT.2025.3562287](https://doi.org/10.1109/JSAIT.2025.3562287)).
