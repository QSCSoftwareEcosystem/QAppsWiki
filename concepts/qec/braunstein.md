---
type: concept
name: $⟦5,1,3⟧_{\mathbb{R}}$ Braunstein five-mode code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Five-wavepacket code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/analog-stabilizer
- concepts/qec/quantum-cyclic
- concepts/qec/qudit-5-1-3
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/braunstein
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: braunstein
---

# $⟦5,1,3⟧_{\mathbb{R}}$ Braunstein five-mode code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/braunstein) (`code_id: braunstein`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An analog stabilizer version of the five-qubit perfect code, encoding one mode into five and correcting arbitrary errors on any one mode.

(source: raw/error-correction-zoo.md)

## Encoders

- Seven beam splitters  ([doi:10.1103/PhysRevA.81.062305](https://doi.org/10.1103/PhysRevA.81.062305)).

## Decoders

- Error correction can be done using linear-optical elements and feedback  ([doi:10.1038/27850](https://doi.org/10.1038/27850)).

## Relations

- _parent_: [[concepts/qec/analog-stabilizer]]
- _parent_: [[concepts/qec/quantum-cyclic]]
- _parent_: [[concepts/qec/ame]] — Braunstein five-mode codewords are CV AME  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/qudit-5-1-3]] — The Braunstein five-mode code is a bosonic analogue of the five-qudit code.
