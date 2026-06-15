---
type: concept
name: Tree cluster-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cluster-state
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/tree_cluster
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: tree_cluster
---

# Tree cluster-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/tree_cluster) (`code_id: tree_cluster`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code obtained from a cluster state on a tree graph (e.g., a star graph  ([arXiv:1008.2048](https://arxiv.org/abs/1008.2048), [arXiv:1008.3752](https://arxiv.org/abs/1008.3752))) that has been proposed in the context of quantum repeater and MBQC architectures.

(source: raw/error-correction-zoo.md)

## Protection

Some tree cluster-state codes have shown good performance over the depolarizing channel  ([arXiv:1910.00471](https://arxiv.org/abs/1910.00471)).

## General gates

- Cluster states constructed from star clusters can be used to perform universal MBQC with probabilistic two-qubit gates  ([arXiv:1008.3752](https://arxiv.org/abs/1008.3752)).
- Three-tree cluster states can be fused into larger tree and hexagonal cluster states using postselected Bell measurements  ([arXiv:1712.00294](https://arxiv.org/abs/1712.00294)).

## Relations

- _parent_: [[concepts/qec/cluster-state]]
