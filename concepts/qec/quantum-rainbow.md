---
type: concept
name: Quantum rainbow code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hypergraph-product
- concepts/qec/quantum-triorthogonal
- concepts/qec/quasi-hyperbolic-color
- concepts/qec/qubit-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_rainbow
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_rainbow
---

# Quantum rainbow code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_rainbow) (`code_id: quantum_rainbow`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CSS code whose qubits are associated with vertices of a simplex graph with $m+1$ colors.

(source: raw/error-correction-zoo.md)

## Magic scaling exponent

Hypergraph products of color codes yield quantum rainbow codes with growing distance and transversal gates in the \term{Clifford hierarchy}. In particular, utilizing this construction for quasi-hyperbolic color codes  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)) yields an $⟦n,O(n),O(\log n)⟧$ triorthogonal code family satisfying the necessary conditions for the magic-state yield parameter $\gamma$ to become arbitrarily small  ([arXiv:2408.13130](https://arxiv.org/abs/2408.13130)).

## Transversal gates

- Hypergraph products of color codes yield quantum rainbow codes with growing distance and transversal gates in the \term{Clifford hierarchy}  ([arXiv:2408.13130](https://arxiv.org/abs/2408.13130)).

## Relations

- _parent_: [[concepts/qec/qubit-css]]
- _cousin_: [[concepts/qec/hypergraph-product]] — Hypergraph products of color codes yield quantum rainbow codes with growing distance and transversal gates in the \term{Clifford hierarchy}. In particular, utilizing this construction for quasi-hyperbolic color codes yields an $⟦n,O(n),O(\log n)⟧$ triorthogonal code family satisfying the necessary conditions for the magic-state yield parameter $\gamma$ to become arbitrarily small  ([arXiv:2408.13130](https://arxiv.org/abs/2408.13130)).
- _cousin_: [[concepts/qec/quantum-triorthogonal]] — Hypergraph products of color codes yield quantum rainbow codes with growing distance and transversal gates in the \term{Clifford hierarchy}. In particular, utilizing this construction for quasi-hyperbolic color codes  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)) yields an $⟦n,O(n),O(\log n)⟧$ triorthogonal code family satisfying the necessary conditions for the magic-state yield parameter $\gamma$ to become arbitrarily small  ([arXiv:2408.13130](https://arxiv.org/abs/2408.13130)).
- _cousin_: [[concepts/qec/quasi-hyperbolic-color]] — Hypergraph products of color codes yield quantum rainbow codes with growing distance and transversal gates in the \term{Clifford hierarchy}. In particular, utilizing this construction for quasi-hyperbolic color codes yields an $⟦n,O(n),O(\log n)⟧$ triorthogonal code family satisfying the necessary conditions for the magic-state yield parameter $\gamma$ to become arbitrarily small  ([arXiv:2408.13130](https://arxiv.org/abs/2408.13130)).
