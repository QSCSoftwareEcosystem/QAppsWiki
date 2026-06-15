---
type: concept
name: EA analog stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/analog-stabilizer
- concepts/qec/ea-oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_analog_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_analog_stabilizer
---

# EA analog stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_analog_stabilizer) (`code_id: ea_analog_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Constructed using a variation of the analog stabilizer formalism designed to utilize pre-shared entanglement between sender and receiver.

(source: raw/error-correction-zoo.md)

## Protection

Optimal code parameters have been determined  ([arXiv:0804.1404](https://arxiv.org/abs/0804.1404)).

## Relations

- _parent_: [[concepts/qec/ea-oscillators]]
- _cousin_: [[concepts/qec/analog-stabilizer]] — EA analog stabilizer codes utilize additional ancillary modes in a pre-shared entangled state, but reduce to ordinary analog stabilizer codes when said modes are interpreted as noiseless physical modes.
