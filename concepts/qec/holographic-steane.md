---
type: concept
name: Heptagon holographic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Holographic Steane code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/block-perfect
- concepts/qec/holographic-tensor
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/holographic_steane
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: holographic_steane
---

# Heptagon holographic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/holographic_steane) (`code_id: holographic_steane`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Holographic tensor-network code constructed out of a network of encoding isometries of the Steane code.
Depending on how the isometry tensors are contracted, there is a zero-rate and a finite-rate code family.

(source: raw/error-correction-zoo.md)

## Decoders

- Optimal erasure decoder  ([arXiv:1806.06472](https://arxiv.org/abs/1806.06472)).

## Code capacity threshold

- $~33\%$ under erasures using optimal erasure decoder for the finite-rate family, and $50\%$ for the zero-rate family  ([arXiv:1806.06472](https://arxiv.org/abs/1806.06472)).
- Depolarizing noise: $9.4\%$ using tensor-network decoder, and $\approx 7\%$ using integer optimization decoder  ([arXiv:2012.07317](https://arxiv.org/abs/2012.07317)).
- $18.985\%$ against depolarizing noise for zero-rate code under tensor-network decoder  ([arXiv:2408.06232](https://arxiv.org/abs/2408.06232)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/holographic-tensor]] — The encoding of the heptagon holographic code is a holographic tensor network consisting of the encoding isometry for the Steane code, which is a planar-perfect tensor.
- _cousin_: [[concepts/qec/block-perfect]] — The encoding of the heptagon holographic code is a holographic tensor network consisting of the encoding isometry for the Steane code, which is a planar-perfect tensor.
