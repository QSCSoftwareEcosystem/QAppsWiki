---
type: concept
name: Quantum low-weight check (QLWC) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qlwc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qlwc
---

# Quantum low-weight check (QLWC) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qlwc) (`code_id: qlwc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of $⟦n,k,d⟧$ stabilizer codes for which the number of sites participating in each stabilizer generator is bounded by a constant as $n\to\infty$.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/stabilizer]]
- _cousin_: [`unary`](https://errorcorrectionzoo.org/c/unary) — A family of approximate non-stabilizer qubit QLWC codes with linear distance and rate has been constructed  ([arXiv:1802.07419](https://arxiv.org/abs/1802.07419)) using unary codes that arise from the Feynman-Kitaev clock construction  ([doi:10.1090/gsm/047](https://doi.org/10.1090/gsm/047)).
- _cousin_: [[concepts/qec/approximate-qecc]] — A family of approximate non-stabilizer qubit QLWC codes with linear distance and rate has been constructed  ([arXiv:1802.07419](https://arxiv.org/abs/1802.07419)) using unary codes that arise from the Feynman-Kitaev clock construction  ([doi:10.1090/gsm/047](https://doi.org/10.1090/gsm/047)).
