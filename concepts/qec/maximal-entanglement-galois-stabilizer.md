---
type: concept
name: Maximal-entanglement EA Galois-qudit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ea-galois-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/maximal_entanglement_galois_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: maximal_entanglement_galois_stabilizer
---

# Maximal-entanglement EA Galois-qudit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/maximal_entanglement_galois_stabilizer) (`code_id: maximal_entanglement_galois_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦n,k,d;e⟧_q$ EA Galois-qudit stabilizer code for which $e = n-k$, i.e., the number of required pre-shared maximally entangled Galois-qudit pairs saturates the defining maximal-entanglement condition.

(source: raw/error-correction-zoo.md)

## Rate

Maximal entanglement is required to achieve the EA hashing bound for the depolarizing channel using the father protocol from Refs.  ([arXiv:quant-ph/0308044](https://arxiv.org/abs/quant-ph/0308044), [arXiv:quant-ph/0512015](https://arxiv.org/abs/quant-ph/0512015)); see  ([arXiv:1302.4150](https://arxiv.org/abs/1302.4150)).

## Relations

- _parent_: [[concepts/qec/ea-galois-stabilizer]]
- _cousin_: [`lcd`](https://errorcorrectionzoo.org/c/lcd) — Asymptotically good maximal-entanglement EA Galois-qudit stabilizer codes can be constructed from LCD codes  ([arXiv:1606.00134](https://arxiv.org/abs/1606.00134)).
