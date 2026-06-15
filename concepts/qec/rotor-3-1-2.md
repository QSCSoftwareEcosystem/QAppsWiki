---
type: concept
name: $⟦3,1,2⟧_{\mathbb{Z}}$ Three-rotor code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ame
- concepts/qec/covariant
- concepts/qec/homological-rotor
- concepts/qec/small-distance-quantum
- concepts/qec/stab-3-1-2
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rotor_3_1_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rotor_3_1_2
---

# $⟦3,1,2⟧_{\mathbb{Z}}$ Three-rotor code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rotor_3_1_2) (`code_id: rotor_3_1_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

$⟦3,1,2⟧_{\mathbb Z}$ rotor code that is an extension of the $⟦3,1,2⟧_3$ qutrit CSS code to the integer alphabet, i.e., the angular momentum states of a rotor.

The code is $U(1)$-covariant and its ideal codewords,
\begin{align}
  |\overline{x}\rangle = \sum_{y\in\mathbb{Z}} \left| -3y,y-x,2(y+x) \right\rangle~,
\end{align}
where $x\in\mathbb{Z}$, are not normalizable.

(source: raw/error-correction-zoo.md)

## Protection

Normalized codewords approximately protect against erasure while maintaining covariance  ([arXiv:1902.07714](https://arxiv.org/abs/1902.07714)).

## Relations

- _parent_: [[concepts/qec/homological-rotor]] — Taking $H_X=\begin{pmatrix}-3 & 1 & 2\end{pmatrix}$ and $H_Z=\begin{pmatrix}4&6&3\end{pmatrix}$ yields the three-rotor code.
- _parent_: [[concepts/qec/ame]] — Three-rotor codewords are CV AME states  ([arXiv:2503.15698](https://arxiv.org/abs/2503.15698)).
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/covariant]] — The three-rotor code is $U(1)$-covariant.
- _cousin_: [[concepts/qec/stab-3-1-2]] — The three-rotor code is a rotor analogue of the three-qutrit code.
