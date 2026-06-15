---
type: concept
name: $(5,1,2)$-convolutional code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-convolutional
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_5_1_2_convolutional
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_5_1_2_convolutional
---

# $(5,1,2)$-convolutional code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_5_1_2_convolutional) (`code_id: stab_5_1_2_convolutional`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Family of quantum convolutional codes that are 1D lattice generalizations of the five-qubit perfect code, with the former's lattice-translation symmetry being the extension of the latter's cyclic permutation symmetry.

Their stabilizer generators for semi-open boundary conditions are
\begin{align}
  \begin{array}{cccccccc}
  X & Z & I & I & I & I & I & \cdots\\
  Z & X & X & Z & I & I & I & \cdots\\
  I & Z & X & X & Z & I & I & \cdots\\
  I & I & Z & X & X & Z & I & \cdots\\
  \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \vdots & \ddots
  \end{array}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/quantum-convolutional]]
