---
type: concept
name: Mitten code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/lifted-product
- concepts/qec/qubit-generalized-homological-product-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/mitten
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: mitten
---

# Mitten code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/mitten) (`code_id: mitten`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of LP codes $\mathrm{LP}(A,B)$ with one-by-two base matrices $A=[a_0~a_1]$ and $B=[b_0~b_1]$ whose entries are weight-three elements of the group algebra $\mathbb{F}_2[G]$ of a non-Abelian group $G$  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
The $G$-lift of this shape yields five blocks of $|G|$ data qubits and two blocks each of $X$- and $Z$-type checks, hence check weight nine and encoding rate at least $20\%$.
A non-Abelian $G$ evades the distance ceiling of Abelian lifts of the same shape, allowing distances of about $20$ with a few hundred data qubits.

In the canonical form of the base matrices,
\begin{align}
  A = [\,g_1+g_2+g_3~~e+g_4+g_5\,]~,\qquad B = [\,h_1+h_2+h_3~~e+h_4+h_5\,]~,
\end{align}
$e$ is the identity and $g_i,h_i$ are group elements, and the left regular representation of $a_1$ and the right regular representation of $b_1$ are required to be full rank  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
Each row of the block check matrices spans five column blocks, four similar ones (the *fingers*) carrying one regular action of $G$ and a distinguished one (the *thumb*) carrying the other, whence the name.
The full-rank condition guarantees a canonical logical basis related by the group action, which underlies the modular surgery toolkit  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).

Instances include a $⟦540,108,18⟧$ code over $C_9 \rtimes C_{12}$  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
See Ref.  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)) for eight instances from $⟦150,30,10⟧$ to $⟦975,195,\leq 24⟧$ and their lift groups.

(source: raw/error-correction-zoo.md)

## Protection

For an Abelian lift group, the minimum-weight codeword of the first base matrix produces a logical operator of that weight  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
This caps the distance at the weight of the base matrices, hence at six for this shape.

## Rate

Every reported instance realizes an encoding rate of exactly $20\%$  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).

## General gates

- Mitten codes admit a canonical logical basis  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
Its $X$-type and $Z$-type logical operators each form a single orbit of the group action on the operator labeled by the identity element.
Each logical operator is supported on only two of the five data blocks, and the supports of a conjugate pair intersect in exactly one data qubit.
This structure yields a modular logical toolkit based on graph surgery  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
All Clifford operations follow either from bridging two reusable seed surgery gadgets of tens of qubits each, or from a single fixed extractor  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
The extractor can measure any logical Pauli product.
- Many logical measurements can be executed in parallel by parallel surgery  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
Magic states can be injected into all logical qubits at once, supplying the non-Clifford resource for universal computation  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).

## Decoders

- Telescoping decoder, which sends progressively harder shots through successive BP, Relay-BP, and integer-programming stages  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).

## Fault tolerance

- Syndrome-extraction schedules found with sQetch are estimated to preserve circuit-level distance for the reported instances other than the $⟦150,30,10⟧$ code  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
The best schedule for the $⟦150,30,10⟧$ code has estimated circuit-level distance eight  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
Surgery schedules are likewise estimated to preserve distance  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).

## Threshold

- Circuit-level depolarizing noise with no idling noise: effective finite-size threshold of about $0.7\%$ for the family as a memory  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
- Under the same noise model and without extrapolation, the $⟦300,60,14⟧$ code attains a block logical error rate of about $10^{-11}$ per round at $0.1\%$ physical error rate  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
At $0.4\%$, the $⟦975,195,\leq 24⟧$ code reaches about $4\times 10^{-8}$, nearly two orders of magnitude below a $⟦112320,195,24⟧$ stack of rotated surface codes decoded by MWPM  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
The mitten code uses two orders of magnitude fewer physical qubits than the stack.
Decoding $15$ billion logical surgery operations on the $⟦540,108,18⟧$ code at $0.1\%$ yielded two logical failures  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]] — Mitten codes are qubit CSS codes obtained from a product of chain complexes over a group algebra  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
- _parent_: [[concepts/qec/lifted-product]] — Mitten codes are LP codes of one-by-two base matrices over a non-Abelian group algebra  ([arXiv:2607.28795](https://arxiv.org/abs/2607.28795)).
The base matrices are taken in a canonical form in which the left regular representation of $a_1$ and the right regular representation of $b_1$ are full rank.
