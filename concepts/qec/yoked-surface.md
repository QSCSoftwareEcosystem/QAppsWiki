---
type: concept
name: Yoked surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-concatenated
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/yoked_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: yoked_surface
---

# Yoked surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/yoked_surface) (`code_id: yoked_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of $⟦n,k,d⟧$ qubit CSS codes resulting from a concatenation of a QMDPC code with a rotated surface code.
Concatenation does not impose additional connectivity constraints and can triple the number of logical qubits per physical qubit when compared to the original surface code.
Concatenation with 1D (2D) QMDPC yields codes with twice (four times) the distance.
Using the concatenation convention of the Zoo, the stabilizer generators of the inner QMDPC code are referred to as *yokes* in this context; the cited paper  ([arXiv:2312.04522](https://arxiv.org/abs/2312.04522)) uses the opposite inner/outer terminology.

(source: raw/error-correction-zoo.md)

## Decoders

- Soft information from the outer surface codes can be utilized via a message passing algorithm  ([arXiv:quant-ph/0606126](https://arxiv.org/abs/quant-ph/0606126)).
- Yokes can be measured using lattice surgery  ([arXiv:2312.04522](https://arxiv.org/abs/2312.04522)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qubit-concatenated]] — Using the concatenation convention of the Zoo, a yoked surface code is a concatenation of a QMDPC code (inner code) with a rotated surface code (outer code). The cited paper  ([arXiv:2312.04522](https://arxiv.org/abs/2312.04522)) uses the opposite inner/outer terminology.
