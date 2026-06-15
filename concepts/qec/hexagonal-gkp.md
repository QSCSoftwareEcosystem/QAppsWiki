---
type: concept
name: Hexagonal GKP code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/multimodegkp
- concepts/qec/single-mode
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hexagonal_gkp
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hexagonal_gkp
---

# Hexagonal GKP code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hexagonal_gkp) (`code_id: hexagonal_gkp`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Single-mode GKP qudit-into-oscillator code based on the triangular lattice. Offers the best error correction against displacement noise in a single mode due to the optimal packing of the underlying lattice  ([arXiv:quant-ph/0008040](https://arxiv.org/abs/quant-ph/0008040)).

(source: raw/error-correction-zoo.md)

## Realizations

- Microwave cavity coupled to superconducting circuits: reduced form of GKP error correction, where displacement error syndromes are measured to one bit of precision using an ancillary transmon  ([arXiv:1907.12487](https://arxiv.org/abs/1907.12487)).

## Relations

- _parent_: [[concepts/qec/multimodegkp]]
- _parent_: [[concepts/qec/single-mode]]
- _cousin_: [`hexagonal`](https://errorcorrectionzoo.org/c/hexagonal) — The hexagonal GKP code is based on the triangular lattice.

## Notes

- Hexagonal GKP codes were obtained after iterative numerical optimization of encoding and recovery against photon loss, starting with Haar-random states  ([arXiv:1801.07271](https://arxiv.org/abs/1801.07271)).
