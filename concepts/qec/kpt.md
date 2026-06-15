---
type: concept
name: Kim-Preskill-Tang (KPT) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/holographic
- concepts/qec/qubits-into-qubits
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/kpt
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: kpt
---

# Kim-Preskill-Tang (KPT) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/kpt) (`code_id: kpt`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An approximate quantum error-correcting code that protects the encoded interior of a black hole from computationally bounded exterior observers.
Under the assumption that the Hawking radiation emitted by an old black hole is pseudorandom, there exists a subspace of the radiation system that encodes the black hole interior, entangled with the late outgoing Hawking quanta.
The logical operators of this code, called ghost operators in  ([arXiv:2003.05451](https://arxiv.org/abs/2003.05451)), commute with efficient operations acting on the radiation, protecting the interior up to corrections exponentially small in the black hole's entropy.
The construction is state dependent: the encoding depends on the state that collapsed to form the black hole  ([arXiv:2003.05451](https://arxiv.org/abs/2003.05451)).

This code has been tested in various models of gravity  ([arXiv:2003.05451](https://arxiv.org/abs/2003.05451), [arXiv:2203.01961](https://arxiv.org/abs/2203.01961)).

(source: raw/error-correction-zoo.md)

## Protection

Protection relies on the pseudorandomness of the radiation and on restricting noise to efficient quantum computations acting on the radiation alone.
Such operations commute with the interior logical algebra up to errors exponentially small in the remaining black-hole entropy  ([arXiv:2003.05451](https://arxiv.org/abs/2003.05451)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/holographic]] — The robustness of KPT codes does not rely on arguments from holographic duality, but such codes do aim to describe interiors of black holes.
