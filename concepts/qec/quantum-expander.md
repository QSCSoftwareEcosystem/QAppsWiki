---
type: concept
name: Quantum expander code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Quantum Sipser-Spielman code
- Expander HGP code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-expander
- concepts/qec/hypergraph-product
- concepts/qec/multisector-hypergraph
- concepts/qec/single-shot
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_expander
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_expander
---

# Quantum expander code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_expander) (`code_id: quantum_expander`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

CSS code constructed from a hypergraph product of bipartite expander graphs  ([doi:10.1090/S0273-0979-06-01126-8](https://doi.org/10.1090/S0273-0979-06-01126-8)) with bounded left and right vertex degrees. For every bipartite graph there is an associated matrix (the parity check matrix) with columns indexed by the left vertices, rows indexed by the right vertices, and 1 entries whenever a left and right vertex are connected. This matrix can serve as the parity check matrix of a classical code. Two bipartite expander graphs can be used to construct a quantum CSS code (the quantum expander code) via the hypergraph product of their parity check matrices.

(source: raw/error-correction-zoo.md)

## Protection

The code family has distance scaling as order $\Omega(n^{1/2})$, and the small-set-flip decoder corrects a constant fraction of that many adversarial Pauli errors  ([arXiv:1504.00822](https://arxiv.org/abs/1504.00822)).

## Rate

$⟦n,k=\Theta(n),d=O(\sqrt{n})⟧$ code with asymptotically constant rate.

## Encoders

- Single-shot state preparation with constant space-time overhead  ([arXiv:2510.06760](https://arxiv.org/abs/2510.06760)).

## General gates

- Dimensional jump protocols between various quantum expander codes  ([arXiv:2510.06760](https://arxiv.org/abs/2510.06760)).

## Decoders

- Small set-flip linear-time decoder, which corrects order $\Omega(n^{1/2})$ adversarial errors  ([arXiv:1504.00822](https://arxiv.org/abs/1504.00822)). The decoder has been generalized to hypergraph products of 3 or more expander codes  ([arXiv:2510.06760](https://arxiv.org/abs/2510.06760)).
- Log-time decoder  ([arXiv:1808.03821](https://arxiv.org/abs/1808.03821)).
- Constant-time decoder .
- 2D geometrically local syndrome extraction circuits acting on a patch of $N$ physical qubits must have depth of order $\Omega(n/\sqrt{N})$ or greater. More generally, there is a tradeoff between the depth $D$ and width $W$ of a syndrome extraction circuit, namely, $D \geq n/\sqrt{W}$  ([arXiv:2109.14599](https://arxiv.org/abs/2109.14599)).

## Fault tolerance

- Fault-tolerance with constant overhead can be achieved  ([arXiv:1808.03821](https://arxiv.org/abs/1808.03821)).

## Threshold

- Locally stochastic noise: $2.7 \cdot 10^{-16}$  ([arXiv:1711.08351](https://arxiv.org/abs/1711.08351)).
- Dimensional jump protocols between various quantum expander codes have a threshold under local stochastic noise  ([arXiv:2510.06760](https://arxiv.org/abs/2510.06760)).

## Relations

- _parent_: [[concepts/qec/hypergraph-product]]
- _parent_: [[concepts/qec/galois-expander]]
- _parent_: [[concepts/qec/single-shot]] — Quantum expander codes are single-shot  ([arXiv:1808.03821](https://arxiv.org/abs/1808.03821)).
- _cousin_: [`expander`](https://errorcorrectionzoo.org/c/expander) — Quantum expander codes are quantum analogues of expander codes.
- _cousin_: [[concepts/qec/topological]] — Quantum expander codes realize topological quantum spin glass order  ([arXiv:2412.13248](https://arxiv.org/abs/2412.13248)).
- _cousin_: [[concepts/qec/multisector-hypergraph]] — Quantum expander codes have been generalized to hypergraph products of 3 or more expander codes  ([arXiv:2510.06760](https://arxiv.org/abs/2510.06760)).
