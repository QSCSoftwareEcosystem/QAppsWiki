---
type: concept
name: $⟦3,1,2⟧_3$ Three-qutrit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/holographic-tensor
- concepts/qec/polynomial
- concepts/qec/quantum-mds
- concepts/qec/quantum-secret-sharing
- concepts/qec/small-distance-quantum
- concepts/qec/three-qutrit-permutation-invariant
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_3_1_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_3_1_2
---

# $⟦3,1,2⟧_3$ Three-qutrit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_3_1_2) (`code_id: stab_3_1_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦3,1,2⟧_3$ prime-qudit CSS code that is the smallest qutrit stabilizer code to detect a single-qutrit error.
It has stabilizer generators $ZZZ$ and $XXX$. The code defines a quantum secret-sharing scheme and serves as a minimal model for the AdS/CFT holographic duality. It is also the smallest non-trivial instance of a quantum maximum distance separable code (QMDS), saturating the quantum Singleton bound.

The codewords are
\begin{align}
  \begin{split}
    | \overline{0} \rangle &= \frac{1}{\sqrt{3}} (| 000 \rangle + | 111 \rangle + | 222 \rangle) \\
    | \overline{1} \rangle &= \frac{1}{\sqrt{3}} (| 012 \rangle + | 120 \rangle + | 201 \rangle) \\
    | \overline{2} \rangle &= \frac{1}{\sqrt{3}} (| 021 \rangle + | 102 \rangle + | 210 \rangle)~.
  \end{split}
\end{align}
The elements in the superposition of each logical codeword are related to each other via cyclic permutations.

(source: raw/error-correction-zoo.md)

## Protection

Detects single qutrit errors and protects against a single-qutrit erasure. It is the smallest single-erasure correcting qudit code for $q>2$, and there does not exist a three-qubit code with analogous properties.

The code is an example of a $((2,3))$ threshold scheme where a secret (the quantum information) is split into $n=3$ shares and can be reconstructed from any $k=2$ of them.

The key property of this code is that the reduced density matrix of any single qutrit is maximally mixed, meaning no information can be extracted from that qutrit. Therefore, a single qutrit tells you nothing about the encoded message, but access to any pair of qutrits reveals the secret.

## Encoders

- In addition to thinking about the encoding of states, it is also interesting to look at the transformation of operators from the physical space into the logical space. Due to the unique structure and recovery protocol of the three-qutrit code, the representation of a logical operator $ \overline{O} $ is not unique. Instead, $ \overline{O} $ can be constructed from unitary matrices with support on only two out of the three qutrits. Therefore, the logical operator has valid representations supported on different pairs of qutrits. This operator construction is directly analogous to the construction of operators in the bulk (at the center) of the AdS$_3$-Rindler reconstruction. The three-qutrit code can then be used to describe how these local bulk operators are protected against localized boundary errors  ([arXiv:1411.7041](https://arxiv.org/abs/1411.7041)).

## Decoders

- The quantum information (the secret) can be recovered from a unitary transformation acting on only two qutrits, $ U_{ij} \otimes I $, where $U_{ij}$ acts on qutrits $i,j$ and $I$ is the identity on the remaining qutrit. By the cyclic structure of the codewords, this unitary transformation performs a permutation that recovers the information and stores it in one of the two qutrits involved in recovery.

## Relations

- _parent_: [[concepts/qec/polynomial]] — The three-qutrit code is the smallest member of a family of $⟦2m-1,1,m⟧_{p}$ prime-qudit quantum RS codes for $p=3$ and $m=2$  ([arXiv:quant-ph/9901025](https://arxiv.org/abs/quant-ph/9901025)).
- _parent_: [[concepts/qec/holographic-tensor]] — The three-qutrit code is a radius-one holographic tensor-network code and serves as a minimal model for holography  ([arXiv:1411.7041](https://arxiv.org/abs/1411.7041), [arXiv:1607.03901](https://arxiv.org/abs/1607.03901)).
- _parent_: [[concepts/qec/ame]] — Three-qutrit codewords are AME, and the three-qutrit code stems from the $⟦4,0,3⟧_3$ AME state  ([arXiv:1306.2879](https://arxiv.org/abs/1306.2879), [arXiv:1506.08857](https://arxiv.org/abs/1506.08857), [arXiv:2005.01426](https://arxiv.org/abs/2005.01426)).
- _parent_: [[concepts/qec/quantum-mds]] — The three-qutrit code is the smallest nontrivial quantum MDS code.
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/quantum-secret-sharing]] — The three-qutrit code defines a minimal secret-sharing scheme  ([arXiv:quant-ph/9901025](https://arxiv.org/abs/quant-ph/9901025)) that is substantially generalized by approximate secret-sharing codes.
- _cousin_: [[concepts/qec/three-qutrit-permutation-invariant]] — Projecting the three-qutrit code into the PI qutrit subspace yields the three-qutrit single-deletion code  ([arXiv:2509.20545](https://arxiv.org/abs/2509.20545)).

## Notes

- Connections to AdS/CFT from the perspective of how arbitrary operators are encoded into the logical space. This encoding is analogous and helps explain why operators acting on the bulk are protected against localized boundary errors  ([arXiv:1411.7041](https://arxiv.org/abs/1411.7041)).
