---
type: concept
name: Quantum divisible code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-quantum-divisible
- concepts/qec/quantum-triorthogonal
- concepts/qec/qubit-concatenated
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_divisible
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_divisible
---

# Quantum divisible code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_divisible) (`code_id: quantum_divisible`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A level-$\nu$ quantum divisible code is a CSS code whose $X$-type stabilizers form a $\nu$-even linear binary code in the symplectic representation and which admits a transversal gate at the $\nu$th level of the \term{Clifford hierarchy}.
A CSS code is *doubly even* (*triply even*) if all $X$-type stabilizers have weight divisible by four (eight), i.e., if they form a doubly even (triply even) linear binary code.

The definition can be generalized to *weakly* $\nu$-*divisible* (see, e.g., Ref.  ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752))), which means that there exist some disjoint qubit subsets $M^{\pm}$ such that 
\begin{align}
  | x \cap M^{+} | - | x \cap M^{-} | \equiv 0 \mod \nu
\end{align}
for all rows $x$ of the code's $X$-type stabilizer generator matrix.
CSS codes satisfying the above with $\nu = 2$ ($\nu = 4$, $\nu = 8$) are called *weak even* (*weak doubly even*, *weak triply even*).
This generalization reduces to the original definition when $M^{+}$ is the full set of qubits, and $M^{-}$ the empty set.

An alternative definition  ([arXiv:2109.13481](https://arxiv.org/abs/2109.13481), [arXiv:2204.13176](https://arxiv.org/abs/2204.13176)), not used here, is a CSS code defined from two linear binary codes $C_{1,2}$ such that it is quantum divisible with $\nu > 1$, and all weights in each coset of $C_2$ in $C_1$ are congruent to $\nu$.
For example  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)), if $C_2$ is the first-order RM$(1,m)$ code, and $C_1/ C_2$ consists of quadratic forms with a bounded rank, then $⟦n = 2^m − 1, 1 \leq k \leq 1 + \sum_{i=1}^{m-4}(m − i), d = 3⟧$ is a family of such codes.

(source: raw/error-correction-zoo.md)

## Transversal gates

- A self-dual weakly doubly even $⟦n,1,d⟧$ CSS code admits a partitioned transversal physical $S$ gate that realizes $\overline{S}^m$, where $m=|M^+|-|M^-| \pmod 4$; for odd $m$, together with transversal Hadamard and CNOT, this yields the full logical Clifford group transversally  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)) ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).
- A weakly triply even $⟦n,1,d⟧$ CSS code with a strongly transversal logical $X$ gate admits a partitioned transversal physical $T$ gate that realizes $\overline{T}^m$, where $m=|M^+|-|M^-| \pmod 8$  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239)) ([arXiv:2408.12752](https://arxiv.org/abs/2408.12752)).
- If the $X$-type stabilizers of a CSS code form an $\nu$-even classical code, and if all $X$-type logicals are $(\nu-1)$-even, then the code admits a diagonal transversal gate in the $\nu$th level of the \term{Clifford hierarchy}  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).

## General gates

- The $⟦2^m − 1, 1 \leq k \leq 1 + \sum_{i=1}^{m-4}(m − i), 3⟧$ quantum divisible code family can serve as outer codes of either the five-qubit $⟦5,1,3⟧$ or Steane $⟦7,1,3⟧$ code to realize a $T$ gate on the inner code  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
For example, when $m=5$ ($m=6$), the resulting $⟦31,5,3⟧$ ($⟦63,7,3⟧$) code yields the $T$ gate on the inner five-qubit (Steane) code.
The induced logical gate on the $k$ logical qubits is, up to global phase, $\exp{(\frac{i \pi}{8} Z^{\otimes k})}$, which decomposes into a $T$ gate on every logical qubit, controlled-Phase$^\dagger$ on every pair, and $CCZ$ on every triple  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).

## Fault tolerance

- The $T$ gate realized by concatenating members of the $⟦2^m − 1, 1 \leq k \leq 1 + \sum_{i=1}^{m-4}(m − i), 3⟧$ quantum divisible code family with either the five-qubit $⟦5,1,3⟧$ or Steane $⟦7,1,3⟧$ code is fault-tolerant and does not require magic-state distillation  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
The gate is performed on the inner five-qubit/Steane code and does require encoding and decoding algorithms to pass between the inner and outer codes.

## Realizations

- Triply even codes can yield secure multi-party quantum computation  ([arXiv:2206.04871](https://arxiv.org/abs/2206.04871)).

## Relations

- _parent_: [[concepts/qec/generalized-quantum-divisible]] — Generalized level-$\nu$ quantum divisible codes reduce to quantum level-$\nu$ divisible codes when $t$ is a vector with $\pm 1$ entries.
The classical code formed by their $X$-type stabilizer generator matrix is $\nu$-even  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
Both types of codes realize transversal gates outside of the Clifford group.
- _cousin_: [`divisible`](https://errorcorrectionzoo.org/c/divisible) — The $X$-type stabilizers of a level-$\nu$ quantum divisible code form a $\nu$-even linear binary code.
- _cousin_: [`biorthogonal`](https://errorcorrectionzoo.org/c/biorthogonal) — Quantum divisible codes can be constructed out of first-order RM$(1,m)$ codes  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — The $⟦31,5,3⟧$ member together with the five-qubit code can be viewed as a factorization of a $⟦31,1,3⟧$ triorthogonal code  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — A fault-tolerant $T$ gate on the five-qubit or Steane code can be obtained by concatenating with particular quantum divisible codes  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
