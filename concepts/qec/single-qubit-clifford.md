---
type: concept
name: $⟦2^{2r-1}-1,1,2^r-1⟧$ quantum punctured RM code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-reed-muller
- concepts/qec/self-dual-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/single_qubit_clifford
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: single_qubit_clifford
---

# $⟦2^{2r-1}-1,1,2^r-1⟧$ quantum punctured RM code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/single_qubit_clifford) (`code_id: single_qubit_clifford`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A quantum Reed-Muller code constructed from a punctured self-dual RM code and its even subcode for $r \geq 2$.

(source: raw/error-correction-zoo.md)

## Transversal gates

- All single-qubit gates in the Clifford group.

## Relations

- _parent_: [[concepts/qec/quantum-reed-muller]] — The $⟦2^{2r-1}-1,1,2^r-1⟧$ quantum punctured RM codes are special cases of the $⟦\sum_{i=w+1}^m \binom{m}{i}, \sum_{i=0}^{w} \binom{m}{i}, \sum_{i=w+1}^{r+1} \binom{r+1}{i}⟧$ family for $m \to 2r-1$, $w \to 0$, and $r \to r-1$.
- _parent_: [[concepts/qec/self-dual-css]] — Puncturing a self-dual RM code yields a classical punctured RM code whose dual is its even subcode; applying the CSS construction to the even subcode yields this self-dual CSS family .
