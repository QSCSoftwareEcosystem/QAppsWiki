---
type: concept
name: Binary dihedral PI code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/combinatorial-permutation-invariant
- concepts/qec/diagonal-clifford
- concepts/qec/j-gross
- concepts/qec/quantum-triorthogonal
- concepts/qec/qubit-permutation-invariant
- concepts/qec/small-distance-quantum
- concepts/qec/stab-49-1-5
- concepts/qec/xp-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/binary_dihedral_permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: binary_dihedral_permutation_invariant
---

# Binary dihedral PI code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/binary_dihedral_permutation_invariant) (`code_id: binary_dihedral_permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Multi-qubit PI code designed to realize gates from the binary dihedral group transversally.
Can also be interpreted as a single-spin code.
The codespace projection is a projection onto an irrep of the *binary dihedral group* $ \mathsf{BD}_{2N} = \langle\omega I, X, P\rangle $ of order $8N$, where $ \omega $ is a $ 2N $th root of unity, and $ P = \text{diag} ( 1, \omega^2) $.

The construction includes three families and a handful of particular codes.
The first family has parameters $((2m+3,2,3))$ for $m$ not a power of two, realizing binary dihedral transversal gates that are not possible to realize in any qubit stabilizer code  ([arXiv:2310.17652](https://arxiv.org/abs/2310.17652)).
The second family is the case of $m$ being a power of two, corresponding to $((2^{m-1}+3,2,3))$ codes, each realizing a member of the \term{Clifford hierarchy} transversally.
The third family consists of $((n,2,d))$ codes with $n = \frac{1}{4}(3d^2+6d-7+2(d\text{ mod }8) )$, realizing $S$ and $T$ gates transversally.
The handful of codes have distance 5 (7, 9, 11, 13) and encode in 27 (49, 73, 107, 147) qubits, all realizing transversal $T$ gates.

(source: raw/error-correction-zoo.md)

## Transversal gates

- Binary dihedral group gates can be realized transversally, which include subgroups of any level of the \term{Clifford hierarchy} and subgroups which cannot be realized by any qubit stabilizer code.

## Relations

- _parent_: [[concepts/qec/qubit-permutation-invariant]]
- _cousin_: [[concepts/qec/small-distance-quantum]] — The first and second families of binary dihedral PI codes have distance three, and the third family has the member $((27,2,5))$.
- _cousin_: [[concepts/qec/combinatorial-permutation-invariant]] — The $Q_{3,1,2m-4,+}$ and $Q_{3,1,2^m-4,+}$ combinatorial PI codes reduce to the $((2m+3,2,3))$ and $((2^{m-1}+3,2,3))$ binary dihedral PI codes, respectively  ([arXiv:2310.05358](https://arxiv.org/abs/2310.05358)) (see also  ([arXiv:2411.13142](https://arxiv.org/abs/2411.13142))).
- _cousin_: [[concepts/qec/xp-stabilizer]] — Binary dihedral permutation invariant codewords form error spaces of XP stabilizer codes.
- _cousin_: [[concepts/qec/diagonal-clifford]] — The $((2^{r-1}+3,2,3))$ family of binary dihedral PI codes realizes the same (strongly) transversal gates as the $⟦2^r-1,1,3⟧$ quantum RM codes, but require fewer qubits in almost all cases.
- _cousin_: [[concepts/qec/stab-49-1-5]] — The $((27,2,5))$ binary dihedral PI code realizes the $T$ gate (strongly) transversally, but requires fewer qubits than the $⟦49,1,5⟧$ triorthogonal code.
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — There exist binary dihedral PI codes that have distance 5 (7, 9, 11, 13) and encode in 27 (49, 73, 107, 147) qubits, all realizing transversal $T$ gates.
- _cousin_: [[concepts/qec/j-gross]] — Binary dihedral PI codes can be interpreted as Clifford single-spin codes via the Dicke-state mapping.
