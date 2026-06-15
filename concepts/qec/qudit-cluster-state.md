---
type: concept
name: Modular-qudit cluster-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Modular-qudit graph-state code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/1d-stabilizer
- concepts/qec/graph-quantum
- concepts/qec/hopf-cluster-state
- concepts/qec/qudit-cws
- concepts/qec/qudit-stabilizer
- concepts/qec/spt
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qudit_cluster_state
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qudit_cluster_state
---

# Modular-qudit cluster-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qudit_cluster_state) (`code_id: qudit_cluster_state`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code based on a modular-qudit cluster state.

Modular-qudit cluster states are modular-qudit stabilizer states defined on a graph.
There is one modular-qudit stabilizer generator $S_v$ per graph vertex $v$ of the form  ([arXiv:quant-ph/0304054](https://arxiv.org/abs/quant-ph/0304054))
\begin{align}
  S_v = X^{\dagger}_{v} \prod_{w\in N(v)} Z_w~,
\end{align}
where the neighborhood $N(v)$ is the set of vertices which share an edge with $v$.

(source: raw/error-correction-zoo.md)

## Encoders

- Operators forming the information group can be used to track how logical information is encoded  ([arXiv:0912.2017](https://arxiv.org/abs/0912.2017)).

## General gates

- 1D modular-qudit cluster states  ([arXiv:quant-ph/0304054](https://arxiv.org/abs/quant-ph/0304054), [arXiv:quant-ph/0512155](https://arxiv.org/abs/quant-ph/0512155)) are resources for universal MBQC.

## Realizations

- Quantum computation with cluster states has been realized using photons in the time and frequency domains  ([doi:10.1038/s41567-018-0347-x](https://doi.org/10.1038/s41567-018-0347-x)).

## Relations

- _parent_: [[concepts/qec/qudit-stabilizer]] — Modular-qudit cluster-state codes are particular modular-qudit stabilizer codes. Any modular-qudit stabilizer code is equivalent to a graph quantum code for $G=\mathbb{Z}_q$ via a single-modular-qudit Clifford circuit  ([arXiv:quant-ph/0111080](https://arxiv.org/abs/quant-ph/0111080)) (see also  ([arXiv:quant-ph/0703112](https://arxiv.org/abs/quant-ph/0703112))).
- _parent_: [[concepts/qec/qudit-cws]] — A type of modular-qudit cluster-state code can be built from a modular-qudit cluster state by applying the modular-qudit CWS construction using a linear $q$-ary code, in which codewords are obtained by applying modular-qudit $Z$-type operators defined by the code to the modular-qudit cluster state; see, e.g., Ref.  ([arXiv:2304.08363](https://arxiv.org/abs/2304.08363)).
- _parent_: [[concepts/qec/graph-quantum]] — Graph quantum codes for $G=\mathbb{Z}_q$ reduce to modular-qudit cluster-state codes.
- _parent_: [[concepts/qec/hopf-cluster-state]] — Hopf-algebra cluster-state codes reduce to modular-qudit cluster-state codes when the Hopf algebra reduces to the group $\mathbb{Z}_q$.
- _cousin_: [[concepts/qec/spt]] — Qudit cluster states defined on 1D lattices are representatives of various SPT phases  ([arXiv:1503.06794](https://arxiv.org/abs/1503.06794)).
- _cousin_: [[concepts/qec/1d-stabilizer]] — Qudit cluster states defined on 1D lattices are representatives of various 1D SPT phases  ([arXiv:1503.06794](https://arxiv.org/abs/1503.06794)).
