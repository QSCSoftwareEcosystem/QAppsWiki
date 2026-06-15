---
type: concept
name: BB5 code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qcga
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bb5
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bb5
---

# BB5 code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bb5) (`code_id: bb5`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A BB code with weight-five stabilizer generators
(contrasting with the weight-six checks of standard BB codes), designed and
benchmarked for long chains of trapped ions  ([arXiv:2503.22071](https://arxiv.org/abs/2503.22071)).

Two highlighted instances are $⟦30,4,5⟧$ and $⟦48,4,7⟧$, which improve
the best-known BB6 distances at the same $⟦n,k⟧$: respectively
$⟦30,4,4⟧$ and $⟦48,4,6⟧$  ([arXiv:2503.22071](https://arxiv.org/abs/2503.22071)).

(source: raw/error-correction-zoo.md)

## Fault tolerance

- Circuit-level simulations in  ([arXiv:2503.22071](https://arxiv.org/abs/2503.22071)) use BP-OSD for BB5 and BB6 instances under an ion-chain noise model.
- For physical error rate $10^{-3}$, the $⟦48,4,7⟧$ BB5 instance achieves logical error rate per syndrome round and per logical qubit $\approx 5\times 10^{-5}$, about $4\times$ lower than the best BB6 baseline considered in  ([arXiv:2503.22071](https://arxiv.org/abs/2503.22071)). In that comparison, it also matches the logical error rate of a distance-7 surface code while using about $4\times$ fewer physical qubits per logical qubit.

## Relations

- _parent_: [[concepts/qec/qcga]]
