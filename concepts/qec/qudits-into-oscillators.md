---
type: concept
name: Qudit-into-oscillator code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudits_into_oscillators
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudits_into_oscillators
---

# Qudit-into-oscillator code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudits_into_oscillators) (`code_id: qudits_into_oscillators`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes $K$-dimensional Hilbert space into $n$ bosonic modes.

(source: raw/error-correction-zoo.md)

## Decoders

- Given an encoding of a finite-dimensional code, a decoder that yields the optimal entanglement fidelity can be obtained by solving a semi-definite program  ([arXiv:quant-ph/0109155](https://arxiv.org/abs/quant-ph/0109155), [arXiv:quant-ph/0307138](https://arxiv.org/abs/quant-ph/0307138)) (see also Ref.  ([arXiv:0706.3400](https://arxiv.org/abs/0706.3400))). This approximate QEC technique can be adapted to bosonic codes as long as they are restricted to a finite-dimensional subspace of the oscillator Hilbert space  ([arXiv:1708.05010](https://arxiv.org/abs/1708.05010)).

## Relations

- _parent_: [[concepts/qec/oscillators]] — Qudit-into-oscillator codes are bosonic codes with a finite-dimensional logical subspace.
- _cousin_: [[concepts/qec/approximate-qecc]] — Approximate QEC techniques of finding the entanglement fidelity can be adapted to bosonic codes with a finite-dimensional codespace  ([arXiv:1708.05010](https://arxiv.org/abs/1708.05010)).
