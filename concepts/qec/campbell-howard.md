---
type: concept
name: $⟦6k+2,3k,2⟧$ Campbell-Howard code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-triorthogonal
- concepts/qec/small-distance-qubit-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/campbell_howard
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: campbell_howard
---

# $⟦6k+2,3k,2⟧$ Campbell-Howard code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/campbell_howard) (`code_id: campbell_howard`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Family of $⟦6k+2,3k,2⟧$ qubit stabilizer codes with quasi-transversal $CCZ^{\otimes k}$ gates that are relevant to magic-state distillation.
In the synthillation framework, these distance-two codes realize batches of logical $CCZ$ gates using physical $T$ gates followed by a Clifford correction.

(source: raw/error-correction-zoo.md)

## Protection

Detects single-qubit errors.

## Rate

Encoding rate is $3k/(6k+2)$, approaching $1/2$ as $k\to\infty$.

## Magic scaling exponent

A total of $r$ rounds of magic-state distillation yields a magic-state yield parameter $\gamma\to 1^{+}$ as $k,r\rightarrow \infty$. This matches the Bravyi-Haah conjectured lower bound $\gamma \geq 1$ for concatenated triorthogonal-matrix protocols  ([arXiv:1209.2426](https://arxiv.org/abs/1209.2426)).

## Transversal gates

- Quasi-transversal $CCZ^{\otimes k}$ gates  ([arXiv:1606.01904](https://arxiv.org/abs/1606.01904)).

## Relations

- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]] — The family has distance $2$.
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — Campbell-Howard codes arise from the generalized-triorthogonal/quasitransversal $G$-matrix framework, which extends Bravyi-Haah triorthogonal matrices by allowing odd pair and triple overlaps entirely within the logical-row block $K$  ([arXiv:1606.01904](https://arxiv.org/abs/1606.01904)).
