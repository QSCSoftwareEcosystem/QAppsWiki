---
type: concept
name: $⟦6,2,3⟧_{q}$ code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-true-stabilizer
- concepts/qec/graph-quantum
- concepts/qec/quantum-mds
- concepts/qec/small-distance-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_6_2_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_6_2_3
---

# $⟦6,2,3⟧_{q}$ code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_6_2_3) (`code_id: galois_6_2_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Six-qudit MDS error-correcting code defined for Galois-qudit dimension $q=3$  ([doi:10.1109/TIT.2002.800469](https://doi.org/10.1109/TIT.2002.800469)), $q=2^2$  ([arXiv:1205.4253](https://arxiv.org/abs/1205.4253)), and $q \geq 5$  ([doi:10.1109/TIT.2002.800469](https://doi.org/10.1109/TIT.2002.800469)) ([arXiv:quant-ph/0508070](https://arxiv.org/abs/quant-ph/0508070)).
This code cannot exist for qubits ($q=2$).

(source: raw/error-correction-zoo.md)

## Encoders

- Three different encoding circuits for $q=3$  ([doi:10.1007/978-3-642-20901-7_9](https://doi.org/10.1007/978-3-642-20901-7_9)).

## Relations

- _parent_: [[concepts/qec/galois-true-stabilizer]] — The code is a non-CSS stabilizer code in general  ([arXiv:1205.4253](https://arxiv.org/abs/1205.4253)).
- _parent_: [[concepts/qec/quantum-mds]]
- _parent_: [[concepts/qec/small-distance-quantum]]
- _cousin_: [[concepts/qec/graph-quantum]] — The $⟦6,2,3⟧_{q}$ code family contains examples of graph quantum codes  ([doi:10.1109/TIT.2002.800469](https://doi.org/10.1109/TIT.2002.800469)).
