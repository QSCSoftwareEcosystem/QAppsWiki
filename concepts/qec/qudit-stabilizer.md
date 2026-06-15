---
type: concept
name: Modular-qudit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-lego
- concepts/qec/qudit-cws
- concepts/qec/qudit-non-stabilizer
- concepts/qec/stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_stabilizer
---

# Modular-qudit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_stabilizer) (`code_id: qudit_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $((n,K,d))_q$ modular-qudit code whose logical subspace is the joint eigenspace of commuting qudit Pauli operators forming the code's stabilizer group $\mathsf{S}$  ([arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)).
Traditionally, the logical subspace is the joint $+1$ eigenspace, and the stabilizer group does not contain $e^{i \phi} I$ for any $\phi \neq 0$.
The distance $d$ is the minimum weight of a qudit Pauli string that implements a nontrivial logical operation in the code.

A modular-qudit stabilizer code encoding an integer number of qudits ($K=q^k$) is denoted as $⟦n,k⟧_{\mathbb{Z}_q}$ or $⟦n,k,d⟧_{\mathbb{Z}_q}$.
For composite $q$, such codes need not encode an integer number of qudits, with $K=q^n/|\mathsf{S}|$  ([arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)) ([arXiv:1101.1519](https://arxiv.org/abs/1101.1519)).
This is because $|{\mathsf{S}}|$ need not be a power of $q$, as group generators may have different orders. 
As a result, $⟦n,k,d⟧$ notation is often used with non-integer $k=\log_q K$, and the code dimension can be inferred from the prime decomposition of $q$  ([arXiv:2501.04888](https://arxiv.org/abs/2501.04888)).
*Prime-qudit* stabilizer codes, where $q=p$ for some prime $p$, do not suffer from this issue and encode $k$ logical qudits, with $K=p^k$.

\begin{defterm}{Modular symplectic representation}
\label{topic:modular-symplectic-representation}
The single modular-qudit Pauli string $X_{a} Z_{b}$ for $a,b\in \mathbb{Z}_q$ is converted to the vector $(a|b)\in \mathbb{Z}_q^2$.
The multi modular-qudit version follows naturally.
\end{defterm}

Each code can be represented by a *check matrix* (a.k.a. *stabilizer generator matrix*) $H=(A|B)$, where each row $(a|b)$ is the modular symplectic representation of a stabilizer generator. The check matrix can be brought into standard form via Gaussian elimination  ([arXiv:1101.1519](https://arxiv.org/abs/1101.1519)).

Modular-qudit stabilizer states can be expressed in terms of linear and quadratic functions over $\mathbb{Z}_q^n$  ([arXiv:quant-ph/0408190](https://arxiv.org/abs/quant-ph/0408190)).
They correspond to the set of states with positive Wigner functions  ([arXiv:quant-ph/0602001](https://arxiv.org/abs/quant-ph/0602001), [arXiv:quant-ph/0702004](https://arxiv.org/abs/quant-ph/0702004)) (see  ([arXiv:1712.08628](https://arxiv.org/abs/1712.08628)) for a robust version of Hudson's theorem for odd prime-dimensional qudits).
Stabilizer states saturate various uncertainty relations  ([arXiv:2403.13632](https://arxiv.org/abs/2403.13632)).
General modular-qudit stabilizer codes can equivalently  ([arXiv:quant-ph/0111080](https://arxiv.org/abs/quant-ph/0111080)) be defined using graphs, yielding an analytical form for the codewords  ([arXiv:quant-ph/0012111](https://arxiv.org/abs/quant-ph/0012111)).

There is a quantum GV bound for modular-qudit stabilizer codes  ([doi:10.1109/ACCESS.2018.2865918](https://doi.org/10.1109/ACCESS.2018.2865918)).

(source: raw/error-correction-zoo.md)

## Protection

Detects errors on up to $d-1$ qudits, and corrects erasure errors on up to $d-1$ qudits. More generally, define the normalizer $\mathsf{N(S)}$ of $\mathsf{S}$ to be the set of all Pauli operators that commute with all $S\in\mathsf{S}$. A stabilizer code can correct a Pauli error set ${\mathcal{E}}$ if and only if $E^\dagger F \notin \mathsf{N(S)}\setminus \mathsf{S}$ for all $E,F \in {\mathcal{E}}$.

## Encoders

- Encoder circuits for prime-qudit stabilizer codes  ([arXiv:2509.25587](https://arxiv.org/abs/2509.25587)).

## Magic scaling exponent

The *magic-state yield parameter* $\gamma = \log_d(n/k)$ quantifies the overhead cost of magic-state distillation per the original protocol  ([arXiv:quant-ph/0403025](https://arxiv.org/abs/quant-ph/0403025), [arXiv:1209.2426](https://arxiv.org/abs/1209.2426)).

## Transversal gates

- All qudit stabilizer codes realize modular qudit Pauli transformations transversally.

## General gates

- Gates in the qudit Clifford hierarchy can be done using *qudit gate teleportation*, in which a gate can be obtained from a particular *qudit magic state*. Magic states that are eigenstates of qudit Clifford operators have been classified for prime qudit dimensions 3 and 5  ([arXiv:2003.07164](https://arxiv.org/abs/2003.07164)).

## Decoders

- Trellis decoder for prime-dimensional qudits, which builds a compact representation of the algebraic structure of the normalizer $\mathsf{N(S)}$  ([arXiv:2106.08251](https://arxiv.org/abs/2106.08251)).

## Relations

- _parent_: [[concepts/qec/qudit-non-stabilizer]] — A modular-qudit stabilizer code with stabilizer group $\mathsf{S}$ can be thought of as a modular-qudit USt with only the identity coset representative. Conversely, if $K = q^k$, and if the set of coset representatives of a modular-qudit USt form a $q$-ary linear code over $\mathbb{Z}_q$, then they can be absorbed into a modular-qudit stabilizer group that defines the USt.
- _parent_: [[concepts/qec/stabilizer]]
- _parent_: [[concepts/qec/quantum-lego]] — Modular-qudit stabilizer codes are quantum Lego codes built out of atomic blocks such as the 2-qudit repetition code, single-qudit trivial stabilizer codes, and tensor-products of the $|0\rangle$ state  ([arXiv:2109.11996](https://arxiv.org/abs/2109.11996)).
- _cousin_: [[concepts/qec/qudit-cws]] — Modular-qudit CWS codes whose underlying classical code is a linear $q$-ary code over $\mathbb{Z}_q$ are modular-qudit stabilizer codes containing a cluster-state codeword; see  ([arXiv:1505.00283](https://arxiv.org/abs/1505.00283)), which defines CWS codes as admitting an underlying stabilizer state that is not necessarily a cluster state.
- _cousin_: [`q-ary_linear_over_zq`](https://errorcorrectionzoo.org/c/q-ary_linear_over_zq) — Modular-qudit stabilizer codes are the closest quantum analogues of additive codes over $\mathbb{Z}_q$ because addition in the ring corresponds to multiplication of stabilizers in the quantum case.
- _cousin_: [`t-designs`](https://errorcorrectionzoo.org/c/t-designs) — Stabilizer states on $n$ prime-dimensional qudits form complex projective 2-designs on $\mathbb{C}P^{p^n-1}$, and they form 3-designs if and only if $p=2$  ([arXiv:1510.02767](https://arxiv.org/abs/1510.02767)). The prime-qudit Clifford group is a unitary 2-design on $U(p^n)$  ([arXiv:2108.04200](https://arxiv.org/abs/2108.04200)).
- _cousin_: [`unitary_design`](https://errorcorrectionzoo.org/c/unitary_design) — The prime-qudit Clifford group is a unitary 2-design on $U(p^n)$  ([arXiv:2108.04200](https://arxiv.org/abs/2108.04200)).
- _cousin_: [`complex_projective`](https://errorcorrectionzoo.org/c/complex_projective) — Stabilizer states on $n$ prime-dimensional qudits form complex projective 2-designs on $\mathbb{C}P^{p^n-1}$  ([arXiv:1510.02767](https://arxiv.org/abs/1510.02767)).

## Notes

- Distance upper bounds for Galois-qudit stabilizer codes for various $n$ and $k$, based on algorithms developed in Refs.  ([doi:10.1007/978-3-540-37634-7_13](https://doi.org/10.1007/978-3-540-37634-7_13), [arXiv:2405.15057](https://arxiv.org/abs/2405.15057)) and maintained by M. Grassl at this [website](https://www.codetables.de/), hold for general modular-qudit codes because they are based on linear programming.
- A standardized definition of the qudit stabilizer group is developed in  ([arXiv:1101.1519](https://arxiv.org/abs/1101.1519)).
- The number of modular-qudit stabilizer codes was determined in Refs.  ([arXiv:quant-ph/0602001](https://arxiv.org/abs/quant-ph/0602001), [arXiv:2209.01449](https://arxiv.org/abs/2209.01449)).
