---
type: concept
name: Stellated color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/stellated-surface
- concepts/qec/triangle-surface
- concepts/qec/twist-defect-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stellated_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stellated_color
---

# Stellated color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stellated_color) (`code_id: stellated_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A non-CSS color-code family on a lattice patch with a single central puncture that hosts a twist defect connected to the boundary by a domain wall.

The family is parameterized by a rotational symmetry order $s$; for odd $s$, the code encodes $k=s-1$ logical qubits, while for even $s$, it encodes $k=s-2$ logical qubits  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).

(source: raw/error-correction-zoo.md)

## Rate

Code families yield the following values of the constant $c$ in the BPT bound, $k d^2 \leq c n$. On the 4.8.8 lattice, stellated color codes have $c=4-\frac{4}{s}$ for odd $s$ and $c=4-\frac{8}{s}$ for even $s$, approaching $4$ as $s$ grows. On the 6.6.6 lattice, they have $c=\frac{8}{3}-\frac{8}{3s}$ for odd $s$ and $c=\frac{8}{3}-\frac{16}{3s}$ for even $s$, approaching $\frac{8}{3}$  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).

## Relations

- _parent_: [[concepts/qec/twist-defect-color]]
- _cousin_: [[concepts/qec/triangle-surface]] — Stellated color codes are color-code analogues of triangle surface codes in that both encode logical information in lattices with a single twist defect. Instances of the former can be obtained by fattening  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)) the vertices of the latter  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).
- _cousin_: [[concepts/qec/stellated-surface]] — Stellated color codes are color-code analogues of stellated surface codes; the surface-code family has the same rotational parameter $s$, but half the asymptotic $c$-value of the 4.8.8 stellated color-code family  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).
