---
type: concept
name: $⟦k+4,k,2⟧$ H code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/generalized-quantum-divisible
- concepts/qec/self-dual-css
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_h
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_h
---

# $⟦k+4,k,2⟧$ H code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_h) (`code_id: quantum_h`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Family of $⟦k+4,k,2⟧$ self-dual CSS codes (for even $k$) with transversal Hadamard gates that are relevant to magic state distillation.
The four stabilizer generators are $X_1X_2X_3X_4$, $Z_1Z_2Z_3Z_4$, $X_1X_2X_5X_6...X_{k+4}$, and $Z_1Z_2Z_5Z_6...Z_{k+4}$.

(source: raw/error-correction-zoo.md)

## Protection

Detects weight-one Pauli errors. The $r$-level concatenated H code detects Pauli errors up to weight $2^r-1$.

## Transversal gates

- Hadamard and $TXT^{\dagger}$ gates, with the latter Clifford-equivalent to Hadamard, and where $T=\exp(i\pi(I-Z)/8)$ is the $\pi/8$-rotation gate.

## Magic scaling exponent

A total of $r$ rounds of magic-state distillation yields a magic-state yield parameter $\gamma\to 1^{+}$ as $k,r\rightarrow \infty$; see  ([arXiv:1612.07330](https://arxiv.org/abs/1612.07330)). This matches the Bravyi-Haah conjectured lower bound $\gamma \geq 1$ for concatenated triorthogonal-matrix protocols  ([arXiv:1209.2426](https://arxiv.org/abs/1209.2426)).

## Rate

The H codes are dense, i.e., the rate $\frac{k}{k+4}\rightarrow 1$ as $k \rightarrow \infty$. The distance is 2. However an $r$-level concatenation of H codes gives a distance of $2^r$.

## General gates

- The H codes can be used for high-quality and high-efficiency magic-state distillation  ([arXiv:1210.3388](https://arxiv.org/abs/1210.3388)). Their associated multi-level magic-state protocols have an efficiency advantage over the 10-to-2 and 15-to-1 protocols for output error below $10^{-7}$.

## Relations

- _parent_: [[concepts/qec/generalized-quantum-divisible]] — H codes are level-two generalized divisible codes  ([arXiv:1709.08658](https://arxiv.org/abs/1709.08658)).
- _parent_: [[concepts/qec/self-dual-css]]
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
