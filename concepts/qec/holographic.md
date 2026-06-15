---
type: concept
name: Holographic code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/approximate-qecc
- concepts/qec/qecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/holographic
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: holographic
---

# Holographic code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/holographic) (`code_id: holographic`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Block quantum code whose features serve to model aspects of the AdS/CFT holographic duality and, more generally, quantum gravity.

In the original exactly solvable toy models, a network of perfect tensors defines an isometric encoding map from bulk logical degrees of freedom to boundary physical degrees of freedom  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).
For connected boundary regions of negatively curved planar holographic states, the discrete Ryu-Takayanagi formula is satisfied exactly, and bulk operators admit multiple boundary reconstructions via tensor pushing and greedy-geodesic methods  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qecc]]
- _cousin_: [[concepts/qec/approximate-qecc]] — Universal subspace approximate error correction is used to model black holes  ([arXiv:1807.06041](https://arxiv.org/abs/1807.06041)).
- _cousin_: [`approximate_oaecc`](https://errorcorrectionzoo.org/c/approximate_oaecc) — Properties of holographic codes are often quantified in the Heisenberg picture, i.e., in terms of operator algebras  ([arXiv:1411.7041](https://arxiv.org/abs/1411.7041), [arXiv:1612.00017](https://arxiv.org/abs/1612.00017), [arXiv:2012.14001](https://arxiv.org/abs/2012.14001), [arXiv:2203.01379](https://arxiv.org/abs/2203.01379)).

## Notes

- Reviews of holographic codes  ([arXiv:2102.02619](https://arxiv.org/abs/2102.02619), [arXiv:2110.14669](https://arxiv.org/abs/2110.14669)).
- The original paper also describes black-hole toy models by removing central tensors and interpreting the newly exposed bulk legs as black-hole microstate degrees of freedom  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).
