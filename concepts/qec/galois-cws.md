---
type: concept
name: Galois-qudit CWS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-non-stabilizer
- concepts/qec/graph-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_cws
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_cws
---

# Galois-qudit CWS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_cws) (`code_id: galois_cws`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CWS code for Galois qudits, defined using a Galois-qudit cluster state and a set of Galois-qudit $Z$-type Pauli strings defined by a $q$-ary classical code.

This entry has not yet been developed explicitly in the literature, so the formulation below is a conjectural Galois-qudit adaptation of the modular-qudit CWS constructions in Refs.  ([arXiv:0712.1979](https://arxiv.org/abs/0712.1979), [arXiv:0801.0831](https://arxiv.org/abs/0801.0831)).
The Galois-qudit CWS construction takes in $ \mathcal{Q} = (\mathcal{G},\mathcal{C}) $, where $\mathcal{G}$ is a graph, and where $\mathcal{C}$ is an $(n,K,d)_q$ $q$-ary code.
From the graph, we form the Galois-qudit cluster state $ |\mathcal{G} \rangle $.
From the $q$-ary code, we form Galois-qudit Pauli $Z$-type operators $ W_i = Z_{c_{i,1}} \otimes \cdots \otimes Z_{c_{i,n}} $, where $c_{i,j} $ is the $j$-th coordinate of the $i$-th classical codeword.
The codewords are then $ | i \rangle =  W_i | \mathcal{G} \rangle $.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/galois-non-stabilizer]] — Any Galois-qudit CWS code can be written as a USt whose ($K=1$) stabilizer code is the Galois-qudit cluster state and whose coset representatives are constructed from the $q$-ary classical code.
- _cousin_: [[concepts/qec/graph-quantum]] — A type of Galois-qudit cluster-state code can be built from a Galois-qudit cluster state by applying the conjectural Galois-qudit CWS construction using a linear $q$-ary code, in which codewords are obtained by applying Galois-qudit $Z$-type operators defined by the code to the Galois-qudit cluster state.
