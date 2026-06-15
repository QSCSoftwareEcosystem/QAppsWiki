---
type: concept
name: Homological number-phase code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-homological-product-css
- concepts/qec/gkp-stabilizer
- concepts/qec/homological-rotor
- concepts/qec/number-phase
- concepts/qec/oscillator-stabilizer
- concepts/qec/oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/homological_number-phase
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: homological_number-phase
---

# Homological number-phase code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/homological_number-phase) (`code_id: homological_number-phase`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A homological $n$-rotor code mapped into the Fock-state space of $n$ oscillators by identifying non-negative rotor angular-momentum states with oscillator Fock states.
The resulting oscillator code can encode logical rotors or qudits due to the presence of torsion in the chain complex defining the original rotor code.
These codes are tailored to settings in which photon loss is present but random rotations, i.e., dephasing, are the dominant noise mechanism  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).

Due to the absence of negative Fock states, a given homological rotor code first has to be rotated such that it has non-trivial support in the all-positive momentum orthant.
This can be done by flipping the signs of the angular momenta of some of the rotors  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).
Ideal codewords are not normalizable, and approximate versions have to be constructed.

Since homological rotor codes use an extension of the qubit CSS-to-homology correspondence to rotors, the mapping into oscillators makes such homological encodings possible for oscillators.

(source: raw/error-correction-zoo.md)

## Protection

The homology group of the logical operators has a torsion component because the chain complexes are defined over the ring of integers, which yields codes with finite logical dimension.
Products of chain complexes can also yield rotor codes.

The distances of the original homological rotor code are preserved, although the resulting number-phase code is approximately error-correcting due to the non-orthogonality of Pegg-Barnett phase states  ([doi:10.1088/0305-4470/19/18/030](https://doi.org/10.1088/0305-4470/19/18/030)), which act as the angular position states in the number-phase interpretation of the oscillator.

## Relations

- _parent_: [[concepts/qec/oscillators]] — Homological number-phase codes are bosonic codes encoding logical qudits and/or logical rotors.
- _cousin_: [[concepts/qec/homological-rotor]] — Homological number-phase codes can be thought of as homological rotor codes but whose underlying rotors consist of the number and phase degrees of freedom of physical modes.
- _cousin_: [[concepts/qec/oscillator-stabilizer]] — Homological number-phase codewords span the joint right eigenspace of powers of the non-unitary Susskind–Glogower phase operators and unitary bosonic rotation operators.
- _cousin_: [[concepts/qec/gkp-stabilizer]] — Homological number-phase codes are finite-dimensional cousins of number-phase-rotor GKP-stabilizer codes: both use number-phase resource states and Clifford-semigroup encoders to protect oscillator information against photon loss and dephasing  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).
- _cousin_: [[concepts/qec/number-phase]] — Homological number-phase codes are multi-mode generalizations of number-phase codes, obtained by projecting suitably parity-flipped homological rotor codes onto the non-negative angular-momentum orthant  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).
- _cousin_: [[concepts/qec/generalized-homological-product-css]] — Homological number-phase codes are non-stabilizer codes constructed from chain complexes over the integers. The homology group of the logical operators has a torsion component because the chain complexes are defined over the ring of integers, which yields codes with finite logical dimension.
