---
type: concept
name: $⟦36,6,6⟧$ mirror code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bb72
- concepts/qec/mirror
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/mirror_36_6_6
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: mirror_36_6_6
---

# $⟦36,6,6⟧$ mirror code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/mirror_36_6_6) (`code_id: mirror_36_6_6`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Abelian mirror code on $G=\mathbb{Z}_6\times\mathbb{Z}_6$ with check weight six that is not equivalent to a CSS code via Hadamard gates  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
Its symplectic double is the half-gross code.

The subsets defining the code are $A=\{(1,2),(4,3),(4,4)\}$ and $B=\{(2,4),(3,1),(4,1)\}$  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)).
Qubits form a $6\times 6$ periodic square lattice, and each stabilizer generator acts as $Z$ on a translate of $A$ and as $X$ on the mirror-image translate of $B$.
Table 1 of Ref.  ([arXiv:2603.05496](https://arxiv.org/abs/2603.05496)) lists an equivalent presentation over $\mathbb{Z}_2\times\mathbb{Z}_2\times\mathbb{Z}_3\times\mathbb{Z}_3$.
The code is not equivalent to a CSS code under local Clifford gates and qubit permutations.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/mirror]]
- _cousin_: [[concepts/qec/bb72]] — The symplectic double of the $⟦36,6,6⟧$ mirror code is the half-gross code . The other symplectic halves of the half-gross code have parameters $⟦36,6,5⟧$ and $⟦36,6,3⟧$.
