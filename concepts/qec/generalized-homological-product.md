---
type: concept
name: Generalized homological-product code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/general-qldpc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/generalized_homological_product
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: generalized_homological_product
---

# Generalized homological-product code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/generalized_homological_product) (`code_id: generalized_homological_product`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Stabilizer code whose properties are determined from an underlying chain complex, which often consists of some type of product of other chain complexes.
The \ref{topic:CSS-to-homology-correspondence} yields an interpretation of codes in terms of chain complexes, thus allowing for the use of various products from homology in constructing codes.

The codes participating in the product can be quantum, classical, or mixed.
Homology can be used to design codes for qubits, modular qudits, Galois qudits, as well as rotors; most codes are CSS codes.
However, products can be of more than two underlying codes, in which case the output code need not be CSS (e.g., for XYZ product codes).

The simplest product is a tensor product, with more general products imposing equivalence or symmetry relations on the outputs of the tensor product.
A product of two codes can be interpreted as a fiber bundle, with one element of the product being the base and the other being the fiber.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/general-qldpc]] — Homological products are a primary tool for generating QLDPC codes with favorable parameters. Typically, whenever the input codes are LDPC or QLDPC, the resulting code will be QLDPC with non geometrically local stabilizer generators.
