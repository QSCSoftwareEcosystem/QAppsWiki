---
type: concept
name: Subsystem Hypergraph Product Simplex (SHYPS) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/single-shot
- concepts/qec/subsystem-quantum-parity
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/shyps
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: shyps
---

# Subsystem Hypergraph Product Simplex (SHYPS) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/shyps) (`code_id: shyps`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Family of quantum LDPC codes obtained by combining the subsystem hypergraph product code construction with classical simplex codes. 
The results are CSS subsystem codes with weight-three gauge generators and code parameters $⟦n=(2^r − 1)^2, k=r^2, d=2^{r-1}⟧$ for $r \geq 3$.

Due to their symmetric structure, SHYPS codes inherit the large automorphism group of the underlying classical simplex codes. 
More precisely, $| Aut( SHYPS(r) ) | \geq |GL(r,\mathbb{F}_2)|^2$, which is exponential in the number of logical qubits. 
This large automorphism group can be leveraged to obtain a depth-one fault-tolerant implementation for a large set of logical Clifford operators. 
This set of depth-one Clifford generators is sufficiently large to allow for efficient compilation, i.e., any $m$-qubit Clifford operator can be executed in depth of order $O(m)$. 
SHYPS codes exhibit practical single-shot features, so only order $O(m)$ rounds of syndrome extraction are required to fault-tolerantly execute any logical $m$-qubit Clifford circuit.

(source: raw/error-correction-zoo.md)

## Protection

Memory simulations of the $⟦49, 9, 4⟧$ and $⟦225, 16, 8⟧$ SHYPS codes under circuit-level noise, using a sliding-window BPLSD decoder, yield pseudo-thresholds of approximately $0.32\%$ and $0.35\%$, respectively  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).
Depth-126 logical Clifford-circuit simulations on two blocks of the $⟦49, 9, 4⟧$ SHYPS code were also performed in  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).

## Rate

The exact encoding rate is $k/n = r^2/(2^r-1)^2$, i.e., asymptotically as $\Theta( (\log n)^2/n )$  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).

## Transversal gates

- Cross-block transversal CNOT gates $\prod_{i=1}^n CNOT_{i, n+(\sigma_1\otimes\sigma_2)(i)}$ for $\sigma_1, \sigma_2$ automorphisms of the classical simplex code. These operators implement a generating set of cross-block logical CNOT gates.
- In-block phase-type fold-transversal gates with $Sp(2k,\mathbb{F}_2)$ representation $\begin{pmatrix} I & (\sigma \otimes \sigma^T)\tau \\ 0 & 1\end{pmatrix}$ for $\sigma$ an automorphism of the classical simplex code, and $\tau$ a self-inverse permutation which acts like $\tau (e_i \otimes e_j) = e_j \otimes e_i$ for the canonical basis $\{e_i\}$ of $\mathbb{F}_2^{\sqrt{n}}$. These operators implement a generating set of logical in-block diagonal gates  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).
- Cross-block phase-type fold-transversal gates $\prod_{i=1}^n CZ_{i, n+(\sigma_1\otimes\sigma_2)\tau(i)}$ for $\sigma_1, \sigma_2$ automorphisms of the classical simplex code and $\tau$ as above. These operators implement a generating set of logical cross-block diagonal gates  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).
- Fold-transversal Hadamard gate $H^{\otimes n} \tau $, with $\tau$ as above. Implements logical Hadamard-SWAP operator $H^{\otimes k} \tau_k $, with $\tau_k$ defined analogously to $\tau$  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).

## Decoders

- BPLSD decoder  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).

## General gates

- Arbitrary $m$-qubit logical Clifford gates can be implemented in $4m( 1+o(1) )$ logical cycles, each consisting of a depth-one physical Clifford layer followed by a depth-six syndrome-extraction round  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).
- Worst-case logical Clifford operation on $b$ blocks can be implemented fault-tolerantly in depth roughly $4bk$ using at most $b$ auxiliary code blocks  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).

## Fault tolerance

- Logical Clifford operation on $b$ blocks can be implemented fault-tolerantly in depth $4br^2( 1+o(1) )$ while remaining compatible with one syndrome-extraction round between logical generators  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).

## Relations

- _parent_: [[concepts/qec/subsystem-quantum-parity]]
- _cousin_: [`simplex`](https://errorcorrectionzoo.org/c/simplex) — SHYPS code gauge generator matrices are constructed from hypergraph products of simplex codes  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).
- _cousin_: [[concepts/qec/single-shot]] — SHYPS codes exhibit practical single-shot signatures, including logical error-rate stability under small-window sliding-window decoding and constant single-shot distance $d_{\mathrm{ss}}=3$, which supports using one syndrome-extraction round between logical generators  ([arXiv:2502.07150](https://arxiv.org/abs/2502.07150)).
