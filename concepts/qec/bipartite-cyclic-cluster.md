---
type: concept
name: Bipartite cyclic cluster (BCC) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cluster-state
- concepts/qec/generalized-bicycle
- concepts/qec/quantum-cyclic
- concepts/qec/qubit-css
- concepts/qec/twisted-xzzx
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bipartite_cyclic_cluster
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bipartite_cyclic_cluster
---

# Bipartite cyclic cluster (BCC) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bipartite_cyclic_cluster) (`code_id: bipartite_cyclic_cluster`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Cyclic CSS code constructed from a bipartite cluster state with cyclic invariance,
emphasizing simplicity of state preparation over simplicity of stabilizers.

A BCC code encodes $k$ logical qubits into $n = k n_0$ physical qubits.
Qubits are labeled by pairs $(m,j)$ with $m$ defined modulo $n_0$ and $1 \leq j \leq k$,
partitioned into sets $A$ (indices $j \in \mathcal{A}$) and $B$ (indices $j \notin \mathcal{A}$).
The code is defined by a bipartite graph $G$ on the qubits, with edges only between $A$ and $B$,
that is invariant under cyclic shifts $(m,j) \to (m+1,j)$.
Code states are prepared by initializing $A$-qubits in $|\pm\rangle$ and $B$-qubits in $|0/1\rangle$,
then applying CNOT gates (source in $A$, target in $B$) along the edges of $G$.
The $2^k$ resulting basis states confirm that $k$ logical qubits are encoded.
After a Hadamard on each $B$-qubit, this gives a CSS code.

The $X$-type stabilizers arise from conjugating $X_{m,j} X_{m+1,j}$ (for $j \in \mathcal{A}$) by the CNOT circuit,
and the $Z$-type stabilizers from $Z_{m,j} Z_{m+1,j}$ (for $j \in \mathcal{B}$).

For $k=2$, the graph $G$ is parameterized by a set $\mathcal{S}$ of odd integers modulo $n = 2n_0$:
even qubit $m$ connects to odd qubit $m'$ iff $(m'-m) \bmod n \in \mathcal{S}$.

A related non-CSS construction, the *cyclic cluster code*, drops the bipartiteness requirement on $G$.
For $d=3$, this construction applied to the $⟦10,2,3⟧$ BCC code yields the $⟦5,1,3⟧$ five-qubit perfect code  ([arXiv:2509.06865](https://arxiv.org/abs/2509.06865)).

(source: raw/error-correction-zoo.md)

## Protection

The distance satisfies $d \leq |\mathcal{S}| + 1$,
since $U^\dagger X_{m,j} U$ for $j \in \mathcal{A}$ gives a logical operator of weight $|\mathcal{S}|+1$  ([arXiv:2509.06865](https://arxiv.org/abs/2509.06865)).
A weight-four GB code of odd distance $d$ satisfies $n \geq 1 + d^2$  ([arXiv:2203.17216](https://arxiv.org/abs/2203.17216)),
so the $⟦d^2+1,2,d⟧$ BCC codes are optimal among weight-four BCC codes.

## Encoders

- Initialize $A$-qubits in $|+\rangle$ and $B$-qubits in $|0\rangle$, then apply CNOT gates along edges of $G$, followed by Hadamard on each $B$-qubit.

## Transversal gates

- For $k=2$, all BCC codes admit a transversal Hadamard-SWAP logical gate via qubit permutation $(m,1) \mapsto (-m,2)$ followed by Hadamard on all qubits  ([arXiv:2509.06865](https://arxiv.org/abs/2509.06865)).
- The $⟦d^2+1,2,d⟧$ BCC codes also admit a logical Hadamard without SWAP via $m \mapsto md \pmod{n}$ followed by Hadamard  ([arXiv:2509.06865](https://arxiv.org/abs/2509.06865)).

## Fault tolerance

- For distance-3 BCC codes ($|\mathcal{S}|=2$), a single error produces at most weight-1 logical error, so fault tolerance is preserved  ([arXiv:2509.06865](https://arxiv.org/abs/2509.06865)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/generalized-bicycle]] — BCC codes are GB codes with weight-two circulant $A$ (polynomial $a(x)=1+x$)  ([arXiv:2509.06865](https://arxiv.org/abs/2509.06865)).
- _parent_: [[concepts/qec/quantum-cyclic]] — BCC codes are invariant under cyclic shifts by construction  ([arXiv:2509.06865](https://arxiv.org/abs/2509.06865)).
- _cousin_: [[concepts/qec/cluster-state]] — BCC codes are obtained by applying Hadamard on the $B$-sublattice of a bipartite cluster state, converting CZ-gate preparation into CNOT-gate preparation  ([arXiv:2509.06865](https://arxiv.org/abs/2509.06865)).
- _cousin_: [[concepts/qec/twisted-xzzx]] — The $⟦d^2+1,2,d⟧$ twisted XZZX toric codes (parameters $a=1,b=d$) are Clifford-equivalent to BCC codes for odd $d$  ([arXiv:2509.06865](https://arxiv.org/abs/2509.06865)).
