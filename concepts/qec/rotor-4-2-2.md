---
type: concept
name: Four-rotor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-4-2-2
- concepts/qec/homological-number-phase
- concepts/qec/homological-rotor
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rotor_4_2_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rotor_4_2_2
---

# Four-rotor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rotor_4_2_2) (`code_id: rotor_4_2_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

$⟦4,2,2⟧_{\mathbb Z}$ CSS rotor code that is an extension of the four-qubit code to the integer alphabet, i.e., the angular momentum states of a rotor.

The code is $U(1)$-covariant and its ideal logical-rotor codewords,
\begin{align}
  |\overline{a,b}\rangle = \sum_{j,k,l\in\mathbb{Z}} \delta_{a,j+k}\delta_{b,l} \left| j,k,j+l,k+l \right\rangle~,
\end{align}
where $a,b\in\mathbb{Z}$, are not normalizable.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/homological-rotor]]
- _parent_: [[concepts/qec/group-4-2-2]] — The four group-qudit code reduces to the four-rotor code for $G= \mathbb{Z}$.
- _cousin_: [[concepts/qec/homological-number-phase]] — After suitable rotor-parity flips and projection onto the non-negative angular-momentum orthant, the four-rotor current-mirror code yields a homological number-phase code  ([arXiv:2311.07679](https://arxiv.org/abs/2311.07679)).
