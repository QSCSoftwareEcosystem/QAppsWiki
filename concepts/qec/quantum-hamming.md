---
type: concept
name: $⟦2^r, 2^r-r-2, 3⟧$ Gottesman code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $⟦2^r, 2^r-r-2, 3⟧$ quantum Hamming code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-perfect
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_hamming
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_hamming
---

# $⟦2^r, 2^r-r-2, 3⟧$ Gottesman code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_hamming) (`code_id: quantum_hamming`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of pure  ([arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)) non-CSS stabilizer codes of distance $3$ that saturate the asymptotic quantum Hamming bound.

The family can be obtained from a modified CSS construction  ([arXiv:quant-ph/9604038](https://arxiv.org/abs/quant-ph/9604038), [arXiv:quant-ph/9605021](https://arxiv.org/abs/quant-ph/9605021)) with a $[2^r,r+1,2^{r-1}] = C_2^{\perp}$ first-order RM code and a $[2^r,2^r-1,2] = C_1$ even-weight code  ([arXiv:quant-ph/9604038](https://arxiv.org/abs/quant-ph/9604038), [arXiv:quant-ph/9605021](https://arxiv.org/abs/quant-ph/9605021)).
The modification introduces signs between the codewords.

(source: raw/error-correction-zoo.md)

## Protection

Protects against any single qubit error.

## Relations

- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/quantum-perfect]] — $⟦2^r, 2^r-r-2, 3⟧$ Gottesman codes saturate the asymptotic quantum Hamming bound.
- _cousin_: [`hamming`](https://errorcorrectionzoo.org/c/hamming) — $⟦2^r, 2^r-r-2, 3⟧$ Gottesman codes are analogues of Hamming codes in that they saturate the asymptotic Hamming bound.
- _cousin_: [`biorthogonal`](https://errorcorrectionzoo.org/c/biorthogonal) — Gottesman codes can be obtained from a modified CSS construction  ([arXiv:quant-ph/9604038](https://arxiv.org/abs/quant-ph/9604038), [arXiv:quant-ph/9605021](https://arxiv.org/abs/quant-ph/9605021)) with a $[2^r,r+1,2^{r-1}] = C_2^{\perp}$ first-order RM code and a $[2^r,2^r-1,2] = C_1$ even-weight code  ([arXiv:quant-ph/9604038](https://arxiv.org/abs/quant-ph/9604038), [arXiv:quant-ph/9605021](https://arxiv.org/abs/quant-ph/9605021)).
- _cousin_: [`projective`](https://errorcorrectionzoo.org/c/projective) — Gottesman codes are related to partial spreads in projective geometry  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)).

## Notes

- The code is useful for entanglement distillation  ([arXiv:2408.15936](https://arxiv.org/abs/2408.15936)).
