---
type: concept
name: Spin GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/gkp
- concepts/qec/single-spin
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/spin_gkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: spin_gkp
---

# Spin GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/spin_gkp) (`code_id: spin_gkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An analogue of the single-mode GKP code designed for atomic ensembles. It was designed using the Holstein-Primakoff mapping  ([doi:10.1103/PhysRev.58.1098](https://doi.org/10.1103/PhysRev.58.1098), [doi:10.2307/3212170](https://doi.org/10.2307/3212170), [doi:10.1103/RevModPhys.63.375](https://doi.org/10.1103/RevModPhys.63.375)) to pull back the phase-space structure of a bosonic system to the compact phase space of a quantum spin. A different construction emerges depending on which particular expression for GKP codewords is pulled back.

(source: raw/error-correction-zoo.md)

## Protection

Protects against errors native to spin systems like random rotations and stochastic relaxation.

## Encoders

- Linear combination of unitaries method  ([arXiv:1412.4687](https://arxiv.org/abs/1412.4687), [arXiv:1610.06546](https://arxiv.org/abs/1610.06546), [arXiv:2203.08882](https://arxiv.org/abs/2203.08882)), which may be applicable to more general codewords.

## General gates

- Approximate Clifford-group generators are composed of Hamiltonians at most quadratic in angular momentum operators of two spin systems. Assuming that these generators can be implemented with high fidelity, a magic state can be prepared from an atomic ensemble analog of the vacuum state.

## Relations

- _parent_: [[concepts/qec/single-spin]]
- _cousin_: [[concepts/qec/gkp]] — Spin-GKP code constructions utilize the Holstein-Primakoff mapping  ([doi:10.1103/PhysRev.58.1098](https://doi.org/10.1103/PhysRev.58.1098), [doi:10.2307/3212170](https://doi.org/10.2307/3212170), [doi:10.1103/RevModPhys.63.375](https://doi.org/10.1103/RevModPhys.63.375)) to convert various expressions for square-lattice GKP states into codes for spin systems.
