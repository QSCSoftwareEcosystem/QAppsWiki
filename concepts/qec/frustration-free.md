---
type: concept
name: Frustration-free Hamiltonian code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/commuting-projector
- concepts/qec/hamiltonian
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/frustration_free
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: frustration_free
---

# Frustration-free Hamiltonian code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/frustration_free) (`code_id: frustration_free`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Hamiltonian-based code whose Hamiltonian is frustration free, i.e., whose ground states minimize the energy of each term.

(source: raw/error-correction-zoo.md)

## Protection

Geometrically local frustration-free code Hamiltonians on Euclidean manifolds are stable with respect to sufficiently weak quasi-local perturbations when they satisfy *local topological quantum order* (LTQO) together with the *Local-Gap* condition; LTQO also implies an area law for the entanglement entropy of the ground-state subspace  ([arXiv:1109.1588](https://arxiv.org/abs/1109.1588)).
See also  ([arXiv:2110.11194](https://arxiv.org/abs/2110.11194)).

## Encoders

- Lindbladian-based dissipative encoding can be constructed for a codespace that is the ground-state subspace of a frustration-free Hamiltonian  ([arXiv:0809.0613](https://arxiv.org/abs/0809.0613), [arXiv:1112.4860](https://arxiv.org/abs/1112.4860), [arXiv:0803.1447](https://arxiv.org/abs/0803.1447), [arXiv:1802.00010](https://arxiv.org/abs/1802.00010)).

## Relations

- _parent_: [[concepts/qec/hamiltonian]]
- _cousin_: [[concepts/qec/commuting-projector]] — Frustration-free Hamiltonians can contain non-commuting projectors; an example is the AKLT model  ([doi:10.1007/978-3-662-06390-3_18](https://doi.org/10.1007/978-3-662-06390-3_18)). On the other hand, commuting-projector Hamiltonians can be frustrated; an example is the 1D classical Ising model on a circle for odd $n$ with one two-body interaction having the opposite sign.
- _cousin_: [[concepts/qec/topological]] — Geometrically local frustration-free code Hamiltonians on Euclidean manifolds are stable with respect to sufficiently weak quasi-local perturbations when they satisfy local topological quantum order together with the Local-Gap condition; LTQO also implies an area law for the entanglement entropy of the ground-state subspace  ([arXiv:1109.1588](https://arxiv.org/abs/1109.1588)). See also  ([arXiv:2110.11194](https://arxiv.org/abs/2110.11194)).
