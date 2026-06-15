---
type: concept
name: Generalized homological-product qubit CSS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-homological-product-css
- concepts/qec/qldpc
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_generalized_homological_product_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_generalized_homological_product_css
---

# Generalized homological-product qubit CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_generalized_homological_product_css) (`code_id: qubit_generalized_homological_product_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit CSS code whose properties are determined from an underlying chain complex via the qubit CSS-to-homology correspondence. This complex often consists of some type of product of other chain complexes.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _parent_: [[concepts/qec/qldpc]] — Homological products are a primary tool for generating qubit QLDPC codes with favorable parameters. Typically, whenever the input codes are binary LDPC or qubit QLDPC, the resulting code will be qubit QLDPC with non geometrically local stabilizer generators.
- _parent_: [[concepts/qec/generalized-homological-product-css]]
