---
type: concept
name: Penrose tiling code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/oscillators
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/penrose
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: penrose
---

# Penrose tiling code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/penrose) (`code_id: penrose`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes quantum information into superpositions of rotated and translated versions of different Penrose tilings of $\mathbb{R}^n$.

Letting $|T\rangle$ be a Penrose tiling, the codeword corresponding to this tiling is a superposition of all tilings in the tiling's orbit under Euclidean transformations,
\begin{align}
  |\overline{T}\rangle=\int \textnormal{d}g|gT\rangle~,
\end{align}
where $g$ is a Euclidean transformation.

(source: raw/error-correction-zoo.md)

## Protection

Properties of Penrose tilings such as local indistinguishability and local recoverability ensure that Penrose tiling codes can correct erasures of any finite region of space.

## Relations

- _parent_: [[concepts/qec/oscillators]] — Penrose tiling codes encode information into Penrose tilings, which are non-periodic tilings of $\mathbb{R}^n$.

## Notes

- Popular summary of Penrose tiling codes in [Quanta Magazine](https://www.quantamagazine.org/never-repeating-tiles-can-safeguard-quantum-information-20240223).
