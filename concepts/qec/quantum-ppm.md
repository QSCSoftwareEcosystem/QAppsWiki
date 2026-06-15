---
type: concept
name: Pulse-position (PPM) c-q modulation format
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Pulse-position (PPM) c-q modulation code
- Pulse-position (PPM) c-q modulation scheme
- Pulse-position (PPM) c-q signaling format
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/coherent-state-c-q
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_ppm
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_ppm
---

# Pulse-position (PPM) c-q modulation format

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_ppm) (`code_id: quantum_ppm`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $q$-PPM c-q code is a coherent-state c-q code whose $j$th codeword corresponds to a tensor-product state of zero-amplitude coherent states at all modes except mode $j$.
For example, a 3-PPM encoding corresponds to the three-mode states $|\alpha\rangle|0\rangle|0\rangle$, $|0\rangle|\alpha\rangle|0\rangle$, and $|0\rangle|0\rangle|\alpha\rangle$ for some complex $\alpha$.
The dual of a PPM code is obtained by the exchange $0\leftrightarrow\alpha$.

(source: raw/error-correction-zoo.md)

## Protection

The error probability under an optimal quantum detector is worked out in .

## Decoders

- Conditional pulse nulling (CPN) receiver .

## Realizations

- Conditional pulse nulling (CPN) receiver  ([arXiv:1111.4017](https://arxiv.org/abs/1111.4017)).

## Relations

- _parent_: [[concepts/qec/coherent-state-c-q]]
- _cousin_: [`ppm`](https://errorcorrectionzoo.org/c/ppm) — PPM c-q codes are quantum analogues of PPM codes.
- _cousin_: [`biorthogonal_spherical`](https://errorcorrectionzoo.org/c/biorthogonal_spherical) — PPM c-q codewords are c-q spherical codes whose constellation consists of the standard basis vectors. Adjoining negatives yields the corresponding biorthogonal c-q spherical code.
