---
type: concept
name: Rotor GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/css
- concepts/qec/gkp
- concepts/qec/quantum-concatenated
- concepts/qec/rotor-stabilizer
- concepts/qec/single-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rotor_gkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rotor_gkp
---

# Rotor GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rotor_gkp) (`code_id: rotor_gkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

GKP code protecting against small angular position and momentum shifts of a planar rotor.

(source: raw/error-correction-zoo.md)

## Protection

In the standard $Z_N\subset Z_{dN}$ construction, the $d$-dimensional codespace corrects angular shifts $|\delta\phi|<\pi/(dN)$ and angular-momentum shifts $|\delta\ell|<N/2$.

## Relations

- _parent_: [[concepts/qec/rotor-stabilizer]]
- _parent_: [[concepts/qec/css]] — Rotor GKP code stabilizers are purely position and purely momentum rotor Pauli-type operators, making these codes CSS.
- _parent_: [[concepts/qec/single-subsystem]]
- _cousin_: [[concepts/qec/gkp]] — GKP (rotor GKP) codes protect against shifts in linear (angular) degrees of freedom.
- _cousin_: [[concepts/qec/quantum-concatenated]] — The rotor GKP code can be thought of as a concatenation of a homological rotor code and a modular-qudit GKP code  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).
