---
type: concept
name: $⟦11,1,5⟧_3$ qutrit Golay code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-quad-residue
- concepts/qec/qudit-cluster-state
- concepts/qec/qudit-css
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qutrit_golay
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qutrit_golay
---

# $⟦11,1,5⟧_3$ qutrit Golay code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qutrit_golay) (`code_id: qutrit_golay`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦11,1,5⟧_3$ code constructed from the ternary Golay code via the CSS construction.
The code's stabilizer generator matrix blocks $H_{X}$ and $H_{Z}$ are both the generator matrix of the ternary Golay code.

(source: raw/error-correction-zoo.md)

## Transversal gates

- All single-qutrit encoded Clifford gates  ([arXiv:2003.02717](https://arxiv.org/abs/2003.02717)).

## Magic scaling exponent

Magic-state distillation scaling exponent $\gamma=\log_3(1728\times 11) \approx 8.97$, where the $1728$ factor comes from the fact that one round of distillation succeeds with probability $\approx 1/1728$  ([arXiv:2003.02717](https://arxiv.org/abs/2003.02717)).

## General gates

- Magic-state distillation of the strange state $|S\rangle=\frac{1}{\sqrt{2}}(|1\rangle-|2\rangle)$ and the Norell state $|N\rangle=\frac{1}{\sqrt{2}}(|1\rangle+|2\rangle)$, with the former achieving a cubic error suppression  ([arXiv:2003.02717](https://arxiv.org/abs/2003.02717)).

## Relations

- _parent_: [[concepts/qec/qudit-css]]
- _parent_: [[concepts/qec/galois-quad-residue]] — The qutrit Golay code is a qutrit quantum QR code since the ternary Golay code is a QR code.
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [`ternary_golay`](https://errorcorrectionzoo.org/c/ternary_golay) — The qutrit Golay code is a CSS code constructed from the ternary Golay code.
- _cousin_: [[concepts/qec/qudit-cluster-state]] — The qutrit Golay code can be realized as a modular-qudit cluster-state code  ([arXiv:2003.02717](https://arxiv.org/abs/2003.02717)).
