---
type: concept
name: Dense twist-defect surface code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Denser planar surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/iceberg
- concepts/qec/qubit-concatenated
- concepts/qec/twist-defect-surface
- concepts/qec/yoked-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/dense_twist_defect
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: dense_twist_defect
---

# Dense twist-defect surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/dense_twist_defect) (`code_id: dense_twist_defect`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of twist-defect surface codes whose twist defects are packed as densely as circuit-level error mechanisms allow, so that a rectangular patch of height $d$ and width $2d$ holding one domain wall encodes three logical qubits  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)).
Each twist defect at an end of the domain wall is a new endpoint for logical operators, which flip between $X$ and $Z$ type across the wall, so that loops and mixed Pauli strings become additional independent logical operators.
Merging the boundaries of an $n_{\text{row}}\times m_{\text{col}}$ grid of such rectangles gives one patch encoding $3 n_{\text{row}} m_{\text{col}}$ logical qubits, approaching one logical qubit per $d(d-1)$ physical qubits, roughly twice the rate of rotated surface-code patches  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)).

Twist defects carry non-CSS weight-five stabilizer generators containing a $Y$ Pauli operator, and the packing is made practical by a syndrome-extraction cycle for them that keeps the code decodable by minimum-weight perfect matching.
Rather than measuring such a generator directly, the cycle measures lower-weight gauge operators that commute with the stabilizer group but anticommute with each other.
Individual gauge outcomes are random, while the parity of two of them reconstructs the twist-defect stabilizer generator.
An additional weight-two domain wall removes matchable interior boundaries.
The resulting cycle uses one reset layer, four layers of two-qubit gates, and one measurement layer, on a degree-three connectivity graph.
It loses no distance parallel to the domain wall and one unit perpendicular to it, or no distance at all in an eight-layer variant.
Earlier twist-defect circuits needed at least seven layers and degree-six connectivity  ([arXiv:1709.02318](https://arxiv.org/abs/1709.02318), [arXiv:2201.05678](https://arxiv.org/abs/2201.05678)), or halved the distance along the domain wall and gave up matching-based decoding  ([arXiv:2307.10147](https://arxiv.org/abs/2307.10147)).

One rectangular patch with two twist defects has an end-cycle stabilizer group forming a $⟦49,3,5⟧$ code  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)).
Concatenating each column of the dense packing with an $⟦n,n-2,2⟧$ error-detecting code roughly doubles the distance  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)).

(source: raw/error-correction-zoo.md)

## Protection

Placement of the twist defects is governed by two competing error mechanisms.
Logical $X$ and $Z$ errors propagate diagonally, with a distance set by the $L_\infty$ norm.
Logical $Y$ errors propagate horizontally or vertically, with a distance set by the $L_1$ norm.
Maintaining the distance therefore requires placing twist defects far enough from each other and from the boundaries of the patch  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)).

## Decoders

- Correlated minimum-weight perfect matching via sparse blossom  ([arXiv:2303.15933](https://arxiv.org/abs/2303.15933)), applied to detector error models constructed with Stim  ([arXiv:2103.02202](https://arxiv.org/abs/2103.02202)). The gauge-operator measurement scheme is designed to keep the code matchable, unlike lower-depth twist implementations that forfeit polynomial-time decoding  ([arXiv:2307.10147](https://arxiv.org/abs/2307.10147)).

## Fault tolerance

- Diagonally propagating $YY$ hook errors would halve the circuit-level distance. Their probability is suppressed because they require one specific low-entropy configuration of two-qubit depolarizing faults, each of small probability  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)). Twist defects are therefore placed according to the larger effective distance observed under circuit-level noise rather than the graphlike distance. Neither the code-level nor the circuit-level distance is an upper or a lower bound on the performance of these codes.
- Under uniform depolarizing circuit-level noise at physical error rate $10^{-3}$, the per-logical per-round logical error rate is $3.5^{-d}/10$ for both the three-qubit rectangular patch and the dense packing  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)). The corresponding rate for an idling rotated surface-code patch is $4^{-d}/10$  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)).
- Twist defects can be walked one lattice spacing every two rounds. The walk reverses the controls and targets of the two-qubit gates and alternates with a reflection, extending the walking technique for surface-code patches  ([arXiv:2302.02192](https://arxiv.org/abs/2302.02192)).

## Relations

- _parent_: [[concepts/qec/twist-defect-surface]]
- _cousin_: [[concepts/qec/yoked-surface]] — Each column of the twist-defect dense packing is concatenated with an $⟦n,n-2,2⟧$ error-detecting code as the inner code, in the concatenation convention of the Zoo. This roughly doubles the distance  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)). The inner stabilizer generators are $X^{\otimes n}$ and $Z^{\otimes n}$. Two of the $n$ outer code blocks serve as yoke qubits, so that the $j$th encoded qubit can be given the logical basis $X_j X_{n-1}$ and $Z_j Z_{n-2}$. This is the twist-defect analogue of the yoked surface code, which uses a column of one-qubit rotated surface-code patches in place of the dense packing. Unlike in that case, the logical operators of the dense packing generally lie in the interior. They must be moved to a boundary by twist-defect lattice surgery before the parity checks can be measured.
- _cousin_: [[concepts/qec/qubit-concatenated]] — Each column of the twist-defect dense packing is concatenated with an $⟦n,n-2,2⟧$ error-detecting code as the inner code, in the concatenation convention of the Zoo. This roughly doubles the distance  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)). The inner stabilizer generators are $X^{\otimes n}$ and $Z^{\otimes n}$. Two of the $n$ outer code blocks serve as yoke qubits, so that the $j$th encoded qubit can be given the logical basis $X_j X_{n-1}$ and $Z_j Z_{n-2}$. This is the twist-defect analogue of the yoked surface code, which uses a column of one-qubit rotated surface-code patches in place of the dense packing. Unlike in that case, the logical operators of the dense packing generally lie in the interior. They must be moved to a boundary by twist-defect lattice surgery before the parity checks can be measured.
- _cousin_: [[concepts/qec/iceberg]] — Each column of the twist-defect dense packing is concatenated with an $⟦n,n-2,2⟧$ error-detecting code as the inner code, in the concatenation convention of the Zoo. This roughly doubles the distance  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)). The inner stabilizer generators are $X^{\otimes n}$ and $Z^{\otimes n}$. Two of the $n$ outer code blocks serve as yoke qubits, so that the $j$th encoded qubit can be given the logical basis $X_j X_{n-1}$ and $Z_j Z_{n-2}$. This is the twist-defect analogue of the yoked surface code, which uses a column of one-qubit rotated surface-code patches in place of the dense packing. Unlike in that case, the logical operators of the dense packing generally lie in the interior. They must be moved to a boundary by twist-defect lattice surgery before the parity checks can be measured.
