---
type: concept
name: EA Galois-qudit stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/ea-galois-into-galois
- concepts/qec/galois-grs
- concepts/qec/galois-stabilizer
- concepts/qec/quantum-concatenated
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/ea_galois_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: ea_galois_stabilizer
---

# EA Galois-qudit stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/ea_galois_stabilizer) (`code_id: ea_galois_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A Galois-qudit stabilizer code constructed using a variation of the stabilizer formalism designed to utilize pre-shared entanglement between sender and receiver.
A code is typically denoted as $⟦n,k;e⟧_q$ or $⟦n,k,d;e⟧_q$, where $d$ is the distance of the EA code and $e$ is the number of required pre-shared maximally entangled Galois-qudit states.

(source: raw/error-correction-zoo.md)

## Decoders

- Syndrome extraction and computation based on classical additive codes  ([doi:10.1103/PhysRevA.103.042420](https://doi.org/10.1103/PhysRevA.103.042420)).

## Relations

- _parent_: [[concepts/qec/ea-galois-into-galois]]
- _cousin_: [[concepts/qec/galois-stabilizer]] — EA Galois-qudit stabilizer codes utilize additional ancillary Galois-qudits in a pre-shared entangled state, but reduce to Galois-qudit stabilizer codes when said qudits are interpreted as noiseless physical qudits. Pure Galois-qudit codes can be used to make EA Galois-qudit stabilizer codes  ([arXiv:1105.5872](https://arxiv.org/abs/1105.5872)) ([arXiv:2010.07902](https://arxiv.org/abs/2010.07902)).
- _cousin_: [[concepts/qec/galois-grs]] — Galois-qudit GRS codes can be used to construct EA Galois-qudit stabilizer codes  ([arXiv:1606.00134](https://arxiv.org/abs/1606.00134), [doi:10.1007/s11128-021-03028-w](https://doi.org/10.1007/s11128-021-03028-w)).
- _cousin_: [[concepts/qec/quantum-concatenated]] — Concatenated EA Galois-qudit stabilizer codes have been studied  ([arXiv:2202.08084](https://arxiv.org/abs/2202.08084), [arXiv:2202.00248](https://arxiv.org/abs/2202.00248)).
- _cousin_: [`ag`](https://errorcorrectionzoo.org/c/ag) — Certain AG codes can be used to construct EA Galois-qudit stabilizer codes  ([arXiv:2101.06461](https://arxiv.org/abs/2101.06461)).
