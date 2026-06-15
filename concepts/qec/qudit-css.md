---
type: concept
name: Modular-qudit CSS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/css
- concepts/qec/qudit-stabilizer
- concepts/qec/two-block-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_css
---

# Modular-qudit CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_css) (`code_id: qudit_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $((n,K,d))_q$ modular-qudit stabilizer code admitting a set of stabilizer generators that
are either $Z$-type or $X$-type Pauli strings.
Codes can be defined from two classical codes and/or chain complexes over the ring $\mathbb{Z}_q$ via an extension of qubit CSS-to-homology correspondence to modular qudits  ([arXiv:quant-ph/0605094](https://arxiv.org/abs/quant-ph/0605094)).
The homology group of the logical operators has a torsion component because the chain complexes are defined over a ring, which yields codes whose logical dimension is not a power of $q$.

The stabilizer generator matrix, taking values from $\mathbb{Z}_q$, is of the form
\begin{align}
H=\begin{pmatrix}0 & H_{Z}\\
H_{X} & 0
\end{pmatrix}
\label{eq:parityq}
\end{align}
such that the rows of the two blocks must be orthogonal
\begin{align}
H_X H_Z^T=0~.
\label{eq:commQ}
\end{align}
The above condition guarantees that the $X$-stabilizer generators, defined in the modular symplectic representation as rows of $H_X$, commute with the $Z$-stabilizer generators associated with $H_Z$.

For composite $q$, such codes need not encode an integer number of qudits, but there are general structure theorems  ([doi:10.1142/S0219749914500208](https://doi.org/10.1142/S0219749914500208)) ([arXiv:2405.03559](https://arxiv.org/abs/2405.03559)), with the latter relating to homology.
An $(n,K_X,d_X)_{\mathbb{Z}_q}$ linear code $C_X$ and an $(n,K_Z,d_Z)_{\mathbb{Z}_q}$ linear code $C_Z$, satisfying $C_X^\perp \subseteq C_Z$, yield an $((n,K_X K_Z / q^n))_{\mathbb{Z}_q}$ modular-qudit CSS code with distance $d\geq\min\{d_X,d_Z\}$.
Specializing to the case when $C_Z=(n,K,d)_{\mathbb{Z}_q}$ is dual-containing yields an $((n,K^2 / q^n))_{\mathbb{Z}_q}$ *self-dual modular-qudit CSS code* with $C_X = C_Z$  ([doi:10.1142/S0219749914500208](https://doi.org/10.1142/S0219749914500208)).

For prime $q=p$, the logical dimension returns to being a power of $q$: encoding is based on two related $p$-ary linear codes, an $[n,k_X,d_X]_p $ code $C_X$ and $[n,k_Z,d_Z]_p $ code $C_Z$,
satisfying $C_X^\perp \subseteq C_Z$. The resulting CSS code has $k=k_X+k_Z-n$ logical qubits and distance $d\geq\min\{d_X,d_Z\}$.
Specializing to the case when $C_Z=[n,k,d]_p$ is dual-containing yields an $⟦n,2k-n,\geq d_Z⟧_p$ *self-dual prime-qudit CSS code* with $C_X = C_Z$.
The $H_X$ ($H_Z$) block of $H$ \eqref{eq:parityq} is the parity-check matrix of the code $C_X$ ($C_Z$). 
The requirement $C_X^\perp \subseteq C_Z$ guarantees \eqref{eq:commQ}.
Basis states for the code are, for coset representatives $\gamma \in C_X/C_Z^\perp$,
\begin{align}
|\gamma + C_Z^\perp \rangle = \frac{1}{\sqrt{|C_Z^\perp|}} \sum_{\eta \in C_Z^\perp} |\gamma + \eta\rangle.
\end{align}

(source: raw/error-correction-zoo.md)

## Transversal gates

- Modular-qudit generalizations of CNOT gates are transversal interblock gates for all modular-qudit CSS codes.
- Scalar multiplication physical gates, which map $|x\rangle \mapsto |ax\rangle$ for $a \in \mathbb{Z}_q^\times$, the mutiplicative group modulo $q$.

## Relations

- _parent_: [[concepts/qec/qudit-stabilizer]] — Modular-qudit CSS codes are modular-qudit stabilizer codes whose stabilizer groups admit a generating set of pure-$X$ and pure-$Z$ Pauli strings. 
Any $⟦n,k,d⟧_{\mathbb{Z}_q}$ stabilizer code can be mapped onto a $⟦2n,2k,\geq d⟧_{\mathbb{Z}_q}$ two-block CSS code code via symplectic doubling, which preserves geometric locality of a code up to a constant factor.
- _parent_: [[concepts/qec/css]]
- _cousin_: [[concepts/qec/two-block-quantum]] — Any $⟦n,k,d⟧_{\mathbb{Z}_q}$ stabilizer code can be mapped onto a $⟦2n,2k,\geq d⟧_{\mathbb{Z}_q}$ two-block CSS code code via symplectic doubling, which preserves geometric locality of a code up to a constant factor.
- _cousin_: [`q-ary_linear_over_zq`](https://errorcorrectionzoo.org/c/q-ary_linear_over_zq) — The modular-qudit CSS construction uses two related $q$-ary linear codes over $\mathbb{Z}_q$, $C_X$ and $C_Z$.
