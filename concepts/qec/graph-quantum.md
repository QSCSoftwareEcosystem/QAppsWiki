---
type: concept
name: Graph quantum code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-stabilizer
- concepts/qec/group-cluster-state
- concepts/qec/stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/graph_quantum
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: graph_quantum
---

# Graph quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/graph_quantum) (`code_id: graph_quantum`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A stabilizer code on tensor products of $G$-valued qudits for Abelian $G$ whose encoding isometry is defined using a graph  ([arXiv:quant-ph/0012111](https://arxiv.org/abs/quant-ph/0012111)).
An analytical form of the codewords exists in terms of the adjacency matrix of the graph and bicharacters of the Abelian group  ([arXiv:quant-ph/0012111](https://arxiv.org/abs/quant-ph/0012111)); see  ([arXiv:quant-ph/0703112](https://arxiv.org/abs/quant-ph/0703112)).
A graph quantum code for $G=\mathbb{Z}_2$ contains a cluster state as one of its codewords and reduces to a cluster state when its logical dimension is one  ([arXiv:1511.05647](https://arxiv.org/abs/1511.05647)).

(source: raw/error-correction-zoo.md)

## Protection

The \term{Knill-Laflamme conditions} have a graph-based analogue  ([arXiv:quant-ph/0012111](https://arxiv.org/abs/quant-ph/0012111)); see Ref.  ([arXiv:1407.2777](https://arxiv.org/abs/1407.2777)).

## Relations

- _parent_: [[concepts/qec/stabilizer]] — Graph quantum codes are a subset of stabilizer codes over $G$-valued qudits for Abelian $G$  ([arXiv:quant-ph/0111080](https://arxiv.org/abs/quant-ph/0111080)). Any stabilizer code over Abelian $G$ is locally equivalent to a graph quantum code  ([arXiv:quant-ph/0111080](https://arxiv.org/abs/quant-ph/0111080)) (see also  ([arXiv:quant-ph/0308151](https://arxiv.org/abs/quant-ph/0308151), [arXiv:quant-ph/0703112](https://arxiv.org/abs/quant-ph/0703112))).
- _parent_: [[concepts/qec/group-cluster-state]] — Group-based cluster-state codes reduce to graph codes for Abelian $G$.
- _cousin_: [[concepts/qec/galois-stabilizer]] — Graph quantum codes for $G=\mathbb{F}_q$ are a subset of Galois-qudit stabilizer codes  ([arXiv:quant-ph/0111080](https://arxiv.org/abs/quant-ph/0111080)). Any Galois-qudit stabilizer code is equivalent to a graph quantum code for $G=\mathbb{F}_q$ via a single-Galois-qudit Clifford circuit  ([arXiv:quant-ph/0111080](https://arxiv.org/abs/quant-ph/0111080)) (see also  ([arXiv:quant-ph/0308151](https://arxiv.org/abs/quant-ph/0308151), [arXiv:quant-ph/0703112](https://arxiv.org/abs/quant-ph/0703112))).
