---
type: concept
name: Modular-qudit subsystem color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Modular-qudit gauge color code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qudit-color
- concepts/qec/qudit-subsystem-css
- concepts/qec/sparse-subsystem
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_subsystem_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_subsystem_color
---

# Modular-qudit subsystem color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_subsystem_color) (`code_id: qudit_subsystem_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An extension of subsystem color codes to modular qudits.
Codes are defined analogously to qubit subsystem color codes, but a directionality is required in order to make the modular-qudit stabilizers commute  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).

(source: raw/error-correction-zoo.md)

## General gates

- A logical Hadamard gate can be achieved by gauge fixing, which yields universal computation  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).

## Relations

- _parent_: [[concepts/qec/qudit-subsystem-css]]
- _parent_: [[concepts/qec/sparse-subsystem]]
- _cousin_: [[concepts/qec/qudit-color]] — Gauge fixing a modular-qudit subsystem color code yields a modular-qudit color code, allowing a logical Hadamard gate and universal computation  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).
- _cousin_: [[concepts/qec/translationally-invariant-subsystem]] — Modular-qudit subsystem lattice color codes are defined analogously to qubit subsystem lattice color codes on suitable lattices of any spatial dimension, but a directionality is required in order to make the modular-qudit stabilizers commute  ([arXiv:1503.08800](https://arxiv.org/abs/1503.08800)).
