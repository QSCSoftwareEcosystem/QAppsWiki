---
type: concept
name: $((8,16,2))$ $PG(3,2)$ code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/phantom
- concepts/qec/qubits-into-qubits
- concepts/qec/self-complementary
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_8_4_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_8_4_2
---

# $((8,16,2))$ $PG(3,2)$ code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_8_4_2) (`code_id: qubit_8_4_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Eight-qubit code encoding four logical qubits whose logical basis consists of a GHZ state together with fifteen states built from the incidence geometry of the projective space $PG(3,2)$.

(source: raw/error-correction-zoo.md)

## Protection

Distance two, and this is optimal because no $((8,16,3))$ code exists  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).
No Pauli stabilizer subsystem phantom code of type $⟦8,4,r,d\geq2⟧$ exists, so this exceptional $k=4$ phantom code is necessarily nonstabilizer  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).

## Transversal gates

- Even physical-qubit permutations act as $GL(4,\mathbb{F}_2)$ on the logical basis, and odd permutations extend the permutation automorphism group to the full symmetric group $S_8$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).
- $T^{\otimes 8}$ is a transversal non-Clifford gate implementing $2\ket{\overline{0}}\bra{\overline{0}}-I$ on the logical subspace  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).
- A specific odd permutation implements a non-Clifford logical involution, and the full permutation automorphism group is $S_8$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/phantom]] — This is the exceptional nonstabilizer $k=4$ qubit phantom code of minimal length eight that violates the generic bound $n\geq 2^k-1$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).
- _cousin_: [[concepts/qec/self-complementary]] — The logical basis of the $((8,16,2))$ $PG(3,2)$ code contains a GHZ state and linear combinations of self-complementary states  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).
