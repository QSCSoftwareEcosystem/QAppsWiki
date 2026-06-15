---
type: concept
name: $((2^m,2^{2^m−5m+1},8))$ Goethals-Preparata code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/non-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_goethals_preparata
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_goethals_preparata
---

# $((2^m,2^{2^m−5m+1},8))$ Goethals-Preparata code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_goethals_preparata) (`code_id: quantum_goethals_preparata`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of nonadditive $((2^m,2^{2^m−5m+1},8))$ CSS-like union stabilizer codes constructed using the classical Goethals and Preparata codes.

They can be viewed as union stabilizer codes constructed from the codespace of a $⟦2^m,2^m-7m+3,8⟧$ code, itself obtained via \ref{topic:steane-enlargement}, together with the coset representatives used to obtain the Goethals and Preparata codes  ([doi:10.1017/CBO9781139034807.012](https://doi.org/10.1017/CBO9781139034807.012)).

The Goethals and Preparata codes can each be used to obtain families of union stabilizer codes with distance 8 and 6, respectively  ([arXiv:0801.2144](https://arxiv.org/abs/0801.2144)).
A construction using the $\mathbb{Z}_4$ versions of these codes and the \term{Gray map} yields qubit code families with similar parameters }.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/non-stabilizer]]
- _cousin_: [`goethals`](https://errorcorrectionzoo.org/c/goethals) — The $((2^m,2^{2^m−5m+1},8))$ Goethals-Preparata code is constructed using the classical Goethals and Preparata codes  ([arXiv:0801.2144](https://arxiv.org/abs/0801.2144), [arXiv:0801.2150](https://arxiv.org/abs/0801.2150)). A construction using the $\mathbb{Z}_4$ versions of the Goethals and Preparata codes and the \term{Gray map} yields qubit code families with similar parameters }.
- _cousin_: [`preparata`](https://errorcorrectionzoo.org/c/preparata) — The $((2^m,2^{2^m−5m+1},8))$ Goethals-Preparata code is constructed using the classical Goethals and Preparata codes  ([arXiv:0801.2144](https://arxiv.org/abs/0801.2144), [arXiv:0801.2150](https://arxiv.org/abs/0801.2150)). A construction using the $\mathbb{Z}_4$ versions of the Goethals and Preparata codes and the \term{Gray map} yields qubit code families with similar parameters }.
- _cousin_: [`gray`](https://errorcorrectionzoo.org/c/gray) — A construction using the $\mathbb{Z}_4$ versions of the Goethals and Preparata codes and the \term{Gray map} yields qubit code families with similar parameters as the $((2^m,2^{2^m−5m+1},8))$ Goethals-Preparata code }.
