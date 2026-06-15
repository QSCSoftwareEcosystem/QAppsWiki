---
type: concept
name: Rotor stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/css
- concepts/qec/galois-stabilizer
- concepts/qec/qudit-stabilizer
- concepts/qec/rotor
- concepts/qec/stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rotor_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rotor_stabilizer
---

# Rotor stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rotor_stabilizer) (`code_id: rotor_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Rotor code whose codespace is defined as the common $+1$ eigenspace of a group of mutually commuting rotor generalized Pauli operators.
The stabilizer group can be either discrete or continuous, corresponding to modular or linear constraints on angular positions and momenta.
Both cases can yield finite or infinite logical dimension.
Exact codewords are non-normalizable, so approximate constructions have to be considered.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/rotor]]
- _parent_: [[concepts/qec/stabilizer]]
- _cousin_: [[concepts/qec/css]] — A rotor stabilizer code admitting a set of generators such that each generator consists of either angular position or angular momentum operators is a CSS code.
- _cousin_: [[concepts/qec/qudit-stabilizer]] — By combining the paper's bounded-phase-space and integer-local-dimension constructions, prime-qudit stabilizer codes can be algebraically imported into rotor-code settings  ([arXiv:2303.17000](https://arxiv.org/abs/2303.17000)).
- _cousin_: [[concepts/qec/galois-stabilizer]] — Galois-qudit stabilizer codes can be imported into integral-domain settings, and rotor codes and their parameters can be obtained through a synthesis of these cases  ([arXiv:2303.17000](https://arxiv.org/abs/2303.17000)).
