---
type: concept
name: Combinatorial PI code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- AAB code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-permutation-invariant
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/combinatorial_permutation_invariant
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: combinatorial_permutation_invariant
---

# Combinatorial PI code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/combinatorial_permutation_invariant) (`code_id: combinatorial_permutation_invariant`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of a family of PI quantum codes whose correction properties are derived from solving a family of combinatorial identities.
The code encodes one logical qubit in superpositions of Dicke states whose coefficients are square roots of ratios of binomial coefficients.

(source: raw/error-correction-zoo.md)

## Protection

A code $Q_{g,m,\delta,\epsilon}$ is defined for nonnegative integers $g$, $m$, and $\delta$ as well as a sign $\epsilon$  ([arXiv:2310.05358](https://arxiv.org/abs/2310.05358)).
The number of qubits is $n = 2g+m+\delta+1$.
The code corrects errors on up to $t$ qubits for $m\geq t$, $\delta\geq 2t$, and either $(g\geq 2t,\epsilon=-)$ or $(g\geq 2t+1,\epsilon=+)$.
Under the same conditions, the code also corrects all patterns of $2t$ deletions  ([arXiv:2310.05358](https://arxiv.org/abs/2310.05358)).

## Transversal gates

- A class of combinatorial PI codes called $(b,g,1)$-codes has been identified that admits logical gates in the diagonal \term{Clifford hierarchy} from transversal $Z$-axis rotations  ([arXiv:2411.13142](https://arxiv.org/abs/2411.13142)).

## Relations

- _parent_: [[concepts/qec/qubit-permutation-invariant]]

## Notes

- See Quantum News and Views article  ([doi:10.22331/qv-2024-05-13-80](https://doi.org/10.22331/qv-2024-05-13-80)).
