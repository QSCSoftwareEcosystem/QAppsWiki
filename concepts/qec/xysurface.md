---
type: concept
name: XY surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Tailored surface code (TSC)
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/heavy-hex
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/xysurface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: xysurface
---

# XY surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/xysurface) (`code_id: xysurface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A variant of the surface code whose generators are $XXXX$  and $YYYY$, obtained by mapping $Z \to Y$ in the surface code.
While this code is equivalent to a CSS surface code with the same distance, other properties like noise-bias performance can differ significantly.

(source: raw/error-correction-zoo.md)

## Protection

As a stabilizer code, $⟦n=O(d^2), k=O(1), d⟧$.

## Threshold

- $6.32(3)\%$ for infinite $Z$ bias, and thresholds of $\approx 5\%$ for $Z$ bias around $\eta = 100$ using a variant of the minimum-weight perfect matching decoder  ([arXiv:1907.02554](https://arxiv.org/abs/1907.02554)).

## Code capacity threshold

- $50\%$ at infinite $Z$ bias with maximum-likelihood decoder  ([arXiv:1812.08186](https://arxiv.org/abs/1812.08186)).
- $18.7\%$ for standard depolarizing noise with maximum-likelihood decoder  ([arXiv:1812.08186](https://arxiv.org/abs/1812.08186)).

## Relations

- _parent_: [[concepts/qec/surface]] — The XY surface code is obtained from the surface code by applying $H\sqrt{Z}H$ to all qubits, thereby exchanging $Z\leftrightarrow Y$. While it is equivalent to a CSS surface code with the same distance, but other properties like noise-bias performance can differ significantly.
- _cousin_: [[concepts/qec/heavy-hex]] — XY surface code can be adapted for a heavy-hexagonal point set  ([arXiv:2211.14038](https://arxiv.org/abs/2211.14038)).
