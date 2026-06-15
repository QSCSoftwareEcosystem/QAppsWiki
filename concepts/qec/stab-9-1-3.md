---
type: concept
name: $⟦9,1,3⟧_{\mathbb{Z}_q}$ modular-qudit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-quantum-parity
- concepts/qec/group-quantum-repetition
- concepts/qec/quantum-concatenated
- concepts/qec/qudit-css
- concepts/qec/real-projective-plane
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_9_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_9_1_3
---

# $⟦9,1,3⟧_{\mathbb{Z}_q}$ modular-qudit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_9_1_3) (`code_id: stab_9_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Modular-qudit CSS code that generalizes the $⟦9,1,3⟧$ Shor code to $q$-level systems.

(source: raw/error-correction-zoo.md)

## Protection

Protects against any quantum error arising from any one of the nine quantum registers.

## Encoders

- Generalized CNOT, Toffoli, and quantum Fourier transform gates.

## Relations

- _parent_: [[concepts/qec/qudit-css]]
- _parent_: [[concepts/qec/group-quantum-parity]] — The $⟦9,1,3⟧_{G}$ group-based QPC reduces to the $⟦9,1,3⟧_{\mathbb{Z}_q}$ modular-qudit code for $G=\mathbb{Z}_q$.
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/real-projective-plane]] — The qudit Shor code is a small qudit surface code on a Möbius strip with smooth boundary, which is obtained from removing a face of the tessellation of the projective plane $\mathbb{R}P^2$  ([arXiv:quant-ph/9810055](https://arxiv.org/abs/quant-ph/9810055)).
- _cousin_: [[concepts/qec/group-quantum-repetition]] — The $⟦9,1,3⟧_{\mathbb{Z}_q}$ modular-qudit code is a concatenation of a bit-flip with a phase-flip group repetition code for $G=\mathbb{Z}_q$.
- _cousin_: [[concepts/qec/quantum-concatenated]] — The $⟦9,1,3⟧_{\mathbb{Z}_q}$ modular-qudit code is a concatenation of a bit-flip with a phase-flip group repetition code for $G=\mathbb{Z}_q$.
