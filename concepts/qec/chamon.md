---
type: concept
name: Chamon model code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Chamon-Bravyi-Leemhuis-Terhal (CBLT) code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fracton
- concepts/qec/xyz-product
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/chamon
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: chamon
---

# Chamon model code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/chamon) (`code_id: chamon`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A foliated type-I fracton non-CSS code defined on a cubic lattice using one weight-eight stabilizer generator acting on the eight vertices of each cube in the lattice  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).

In the realization as an XYZ product of three repetition codes  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)), qubits live on the vertices and faces of a cubic lattice, each stabilizer generator has weight six, and the natural logical operators are membrane-like rather than string-like  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).

Variants include a CSS model that is expected to have the same excitation structure  ([arXiv:1603.04442](https://arxiv.org/abs/1603.04442)) and a modified Chamon code based on the XYZ product code construction  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).

(source: raw/error-correction-zoo.md)

## Protection

Flexible string operators confined to planes orthogonal to $[1,1,1]^T$ imply $d = O(\sqrt{N})$ for the stabilizer version  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).

## Rate

For the stabilizer version on an $n_1 \times n_2 \times n_3$ lattice, the number of logical qubits is $k = 4 \gcd(n_1,n_2,n_3)$  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).

## Decoders

- Repetition-based decoder, based on the three underlying repetition codes and improved by pre-treatment with a probabilistic greedy local algorithm  ([arXiv:2303.05267](https://arxiv.org/abs/2303.05267)).

## Code capacity threshold

- Depolarizing noise: $4.92\%$ with repetition-based decoder  ([arXiv:2303.05267](https://arxiv.org/abs/2303.05267)).

## Relations

- _parent_: [[concepts/qec/xyz-product]] — The Chamon model code can be obtained from an XYZ product of three repetition codes , in a construction different from the 3D surface code; see  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).
- _parent_: [[concepts/qec/fracton]] — The Chamon model is a 4-foliated type-I fracton code  ([arXiv:2206.12791](https://arxiv.org/abs/2206.12791)) and is the first example of a fracton phase  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The Chamon model code can be obtained from an XYZ product of three repetition codes , in a construction different from the 3D surface code; see  ([arXiv:2011.09746](https://arxiv.org/abs/2011.09746)).
