---
type: concept
name: $D_4$ hyper-diamond GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/4d-stabilizer
- concepts/qec/gkp-concatenated
- concepts/qec/quantum-repetition
- concepts/qec/qudits-into-oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/dfour_gkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: dfour_gkp
---

# $D_4$ hyper-diamond GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/dfour_gkp) (`code_id: dfour_gkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Two-mode GKP qubit-into-oscillator code based on the $D_4$ hyper-diamond lattice  ([arXiv:2201.12337](https://arxiv.org/abs/2201.12337)).

(source: raw/error-correction-zoo.md)

## General gates

- Logical Clifford operations are given by passive Gaussian unitaries. Non-Clifford gates can be done through Kerr-type interactions.

## Relations

- _parent_: [[concepts/qec/gkp-concatenated]] — The $D_4$ hyper-diamond GKP code can be seen as a concatenation of a rotated square-lattice GKP code with a repetition code  ([arXiv:2201.12337](https://arxiv.org/abs/2201.12337)). This is related to the fact that the four-bit repetition code yields the $D_4$ hyper-diamond lattice via \term{Construction A}.
- _parent_: [[concepts/qec/4d-stabilizer]]
- _parent_: [[concepts/qec/qudits-into-oscillators]]
- _cousin_: [`dfour`](https://errorcorrectionzoo.org/c/dfour) — The $D_4$ GKP code is built from the $D_4$ lattice.
- _cousin_: [[concepts/qec/quantum-repetition]] — The $D_4$ hyper-diamond GKP code can be seen as a concatenation of a rotated square-lattice GKP code with a repetition code  ([arXiv:2201.12337](https://arxiv.org/abs/2201.12337)). This is related to the fact that the four-bit repetition code yields the $D_4$ hyper-diamond lattice via \term{Construction A}.
