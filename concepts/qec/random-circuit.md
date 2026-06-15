---
type: concept
name: Random-circuit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dynamic-gen
- concepts/qec/quantum-random
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/random_circuit
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: random_circuit
---

# Random-circuit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/random_circuit) (`code_id: random_circuit`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose encoding is naturally constructed by randomly sampling from a large set of quantum circuits. Examples include short random Clifford circuits that define good quantum error-correcting codes  ([arXiv:1312.7646](https://arxiv.org/abs/1312.7646)) and monitored random circuits whose mixed phase dynamically generates error-protected subspaces with nonzero channel-capacity density on polynomial timescales  ([arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).

(source: raw/error-correction-zoo.md)

## Protection

A useful proxy and upper bound to the code distance $d$ is the *contiguous code distance*: the contiguous length (with periodic boundary conditions) of the shortest logical operator  ([arXiv:0810.1983](https://arxiv.org/abs/0810.1983), [arXiv:1905.05195](https://arxiv.org/abs/1905.05195)).

## Relations

- _parent_: [[concepts/qec/dynamic-gen]]
- _parent_: [[concepts/qec/quantum-random]]

## Notes

- See Refs.  ([arXiv:2111.08018](https://arxiv.org/abs/2111.08018), [arXiv:2207.14280](https://arxiv.org/abs/2207.14280)) for reviews on random-circuit codes.
