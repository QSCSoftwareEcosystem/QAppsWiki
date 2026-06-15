---
type: concept
name: $⟦6,4,2⟧$ error-detecting code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/4612-color
- concepts/qec/iceberg
- concepts/qec/qubit-concatenated
- concepts/qec/triangular-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_6_4_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_6_4_2
---

# $⟦6,4,2⟧$ error-detecting code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_6_4_2) (`code_id: stab_6_4_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Self-complementary six-qubit code with rate $2/3$ that is unique for its parameters, up to equivalence  ([arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)).
Concatenations of this code with itself yield the $⟦6^r,4^r,2^r⟧$ level-$r$ *many-hypercube* code  ([arXiv:2403.16054](https://arxiv.org/abs/2403.16054)).

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{cccccc}
  Z & Z & Z & Z & Z & Z \\
  X & X & X & X & X & X
\end{array}~.
\end{align}
Stabilizer generators are shown in \ref{figure:stab_6_4_2_ops}.
See  ([arXiv:2403.16054](https://arxiv.org/abs/2403.16054)) for a set of logical Paulis.

(source: raw/error-correction-zoo.md)

## Encoders

- See  ([arXiv:2403.16054](https://arxiv.org/abs/2403.16054)).

## Transversal gates

- CNOT and Hadamard gates  ([arXiv:2403.16054](https://arxiv.org/abs/2403.16054)).
- A $CZ$ gate implemented by transversal $S$ and $S^{\dagger}$  ([arXiv:1912.10063](https://arxiv.org/abs/1912.10063)); see also  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).

## General gates

- Universal Clifford gates via the logical Clifford synthesis (LCS) algorithm  ([arXiv:1907.00310](https://arxiv.org/abs/1907.00310)) ([arXiv:1803.06987](https://arxiv.org/abs/1803.06987)).

## Decoders

- Efficient decoder for the many-hypercube code  ([arXiv:2403.16054](https://arxiv.org/abs/2403.16054)).

## Realizations

- Trapped-ion devices: Bayesian quantum phase estimation on a device by Quantinuum  ([arXiv:2306.16608](https://arxiv.org/abs/2306.16608)).
- Neutral atom arrays: state initialization of the $⟦16,4,4⟧$ doubly concatenated code (a.k.a., the level-two many-hypercube code) on a device by Infleqtion  ([arXiv:2509.13247](https://arxiv.org/abs/2509.13247)).

## Relations

- _parent_: [[concepts/qec/iceberg]] — The $⟦2m,2m-2,2⟧$ error-detecting code for $m=3$ reduces to the $⟦6,4,2⟧$ error-detecting code.
- _parent_: [[concepts/qec/triangular-color]] — The $⟦6,4,2⟧$ error-detecting code is a color code defined on a single hexagon of the 6.6.6 or 4.6.12 tilings. The $⟦6,4,2⟧$ code can be concatenated with the surface code to yield the 6.6.6 color code  ([arXiv:1604.04062](https://arxiv.org/abs/1604.04062)).
- _parent_: [[concepts/qec/4612-color]] — The $⟦6,4,2⟧$ error-detecting code is a color code defined on a single hexagon of the 6.6.6 or 4.6.12 tilings.
- _cousin_: [[concepts/qec/qubit-concatenated]] — Concatenations of this code with itself yield the level-$r$ $⟦6^r,4^r,2^r⟧$ many-hypercube code  ([arXiv:2403.16054](https://arxiv.org/abs/2403.16054)). The $⟦6,4,2⟧$ code can be concatenated with the surface code to yield the 6.6.6 color code  ([arXiv:1604.04062](https://arxiv.org/abs/1604.04062)).
