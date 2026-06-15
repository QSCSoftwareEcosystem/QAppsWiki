---
type: concept
name: Clifford-hierarchy stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubits-into-qubits
- concepts/qec/yetter-gauge-theory
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/clifford_hierarchy
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: clifford_hierarchy
---

# Clifford-hierarchy stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/clifford_hierarchy) (`code_id: clifford_hierarchy`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit code whose codespace is a joint eigenspace of a subset of operators in the Clifford hierarchy.
The stabilizing set, which need not be a group, contains Pauli strings and operators at any level $m$ of the Clifford hierarchy, generalizing qubit stabilizer codes ($m=1$) and *Clifford stabilizer codes* ($m=2$).

Clifford-hierarchy codes in $D$ spatial dimensions include $(D+1)$-dimensional Dijkgraaf-Witten gauge theories with non-Abelian topological order  ([arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).
A $D$-dimensional code can be constructed from a twisted $\mathbb{Z}_2^{D+1}$ gauge theory with Dijkgraaf-Witten twist $(-1)^{\int a_1 \cup a_2 \cup \cdots \cup a_{D+1}}$, where the stabilizers include gates at the $D$th level of the Clifford hierarchy in addition to Pauli $X$ operators.

(source: raw/error-correction-zoo.md)

## Transversal gates

- A transversal logical $\text{diag}(1, e^{i2\pi/2^D})$ gate at the $D$th level of the Clifford hierarchy in $(D-1)$ spatial dimensions  ([arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _cousin_: [`clifford_group`](https://errorcorrectionzoo.org/c/clifford_group) — Clifford-hierarchy codes are joint eigenspaces of subsets of the Clifford hierarchy, whose second level is the Clifford group.
- _cousin_: [[concepts/qec/yetter-gauge-theory]] — Clifford-hierarchy codes in $D$ spatial dimensions include $(D+1)$-dimensional Dijkgraaf-Witten gauge theories with non-Abelian topological order  ([arXiv:2511.02900](https://arxiv.org/abs/2511.02900)).
A $D$-dimensional code can be constructed from a twisted $\mathbb{Z}_2^{D+1}$ gauge theory with Dijkgraaf-Witten twist $(-1)^{\int a_1 \cup a_2 \cup \cdots \cup a_{D+1}}$, where the stabilizers include gates at the $D$th level of the Clifford hierarchy in addition to Pauli $X$ operators.
