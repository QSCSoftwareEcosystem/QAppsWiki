---
type: concept
name: Barbell quantum code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/tile
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/barbell
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: barbell
---

# Barbell quantum code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/barbell) (`code_id: barbell`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of tile codes  ([arXiv:2504.08887](https://arxiv.org/abs/2504.08887), [arXiv:2504.09171](https://arxiv.org/abs/2504.09171)) whose $X$- and $Z$-type check qubits are paired, with each pair joined by one *near-local coupler* and read out by superdense syndrome extraction  ([arXiv:2312.08813](https://arxiv.org/abs/2312.08813)).
A Bell pair prepared across the coupler lets both check qubits collect syndrome information for both stabilizers of the pair, so a stabilizer need only lie within the union of the two check qubits' neighborhoods in the connectivity graph  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)).
Every two-qubit gate of the QEC cycle is thereby native to a fixed-connectivity layout whose complexity does not grow with the code distance.

The codes are built for the *six-qubit star lattice plus near-local coupler* (6QSL+NLC) architecture, also called the *Barbell architecture*, a superconducting chip layout with two connectivity layers  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)).
The first layer is a honeycomb of hexagonal cells whose six qubits share one multi-qubit coupler, so that any two qubits in a cell can interact.
The second layer holds the near-local couplers, each joining an $X$-check qubit to its partner $Z$-check qubit.
The six cells containing the two check qubits form a *barbell*, and the corresponding pair of $X$- and $Z$-type stabilizers is supported on its data qubits.
A barbell code is obtained from a tile code in three steps  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)).
Dummy stabilizers with empty support are added so that $X$- and $Z$-type stabilizers correspond one to one, and a check qubit is placed at each stabilizer.
Each qubit type is then translated by a fixed vector so that every data qubit in the support of either stabilizer of a pair is adjacent to one of its two check qubits.
Because the tile code is translation invariant, all near-local couplers are parallel and of equal, distance-independent length, and can be routed in a single additional connectivity layer without crossings.

The weight-8 family with $k=16$ has $n=2LM$ for an $L\times M$ data-qubit lattice with bulk-stabilizer boxes of size $(D+1)\times(D+1)$, e.g., the $⟦450,16,14⟧$ code  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)).
See Ref.  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)) for the weight-6, weight-8, and weight-10 families.

(source: raw/error-correction-zoo.md)

## Rate

High-rate QLDPC family. The weight-8 examples encode $k=16$ logical qubits using fewer than 30 data qubits per logical qubit. This is a reduction in physical-qubit overhead by up to a factor of 7.0 compared with the rotated surface code of the same distance  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)). The weight-10 family reaches the maximal factor of eight with the $⟦512,16,16⟧$ code  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)).

## General gates

- For stabilizer tiles not confined to a strip and giving rise to total topological order, derived automorphisms of the underlying tile codes implement products of logical CNOT gates  ([arXiv:2511.14589](https://arxiv.org/abs/2511.14589)). The automorphisms extend the lattice on one side and shrink it on the other  ([arXiv:2511.14589](https://arxiv.org/abs/2511.14589)).

## Decoders

- Relay-BP decoder  ([arXiv:2506.01779](https://arxiv.org/abs/2506.01779)) applied to detector error models constructed with Stim  ([arXiv:2103.02202](https://arxiv.org/abs/2103.02202)). The $X$- and $Z$-type errors are decoded separately.

## Fault tolerance

- Superdense syndrome-extraction circuit  ([arXiv:2312.08813](https://arxiv.org/abs/2312.08813)) of depth $w+4$, which is depth 12 for weight-8 stabilizer generators. One near-local coupler per barbell prepares and later measures a Bell pair on the paired $X$- and $Z$-check qubits. A Pauli-frame correction tracked in software relates the measurement outcomes to the stabilizer syndromes.
- Under uniform depolarizing circuit-level noise, a distance-14 weight-8 barbell code reaches the teraquop regime, meaning a logical error rate below $10^{-12}$ per round, at physical error rates above $10^{-4}$  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)). At a physical error rate of $10^{-3}$, one patch of the distance-11 $⟦392,16,11⟧$ barbell code encodes 16 logical qubits at a per-round logical error rate of $8.8\times 10^{-7}$  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)). Sixteen patches of the distance-5 rotated surface code use nearly the same number of data qubits, 400 versus 392, to encode the same 16 logical qubits. Their per-round logical error rate is $9.6\times 10^{-4}$  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)).
- The logical multi-qubit Pauli measurement protocol for tile codes  ([arXiv:2506.18061](https://arxiv.org/abs/2506.18061)) applies directly. The per-round logical error rate of a distance-8 logical $ZZ$ measurement is slightly higher than that of the same code used as a memory  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)).

## Relations

- _parent_: [[concepts/qec/tile]] — Barbell codes are tile codes that constrain the pairing of $X$- and $Z$-type check qubits. Each pair shares a single near-local coupler, and every data qubit in the support of either check is adjacent to one of the two paired check qubits. Constraining the pairing in this way gives a syndrome-extraction cycle of depth $w+4$ for stabilizer generators of weight $w$  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)). It also keeps all near-local couplers parallel, of equal length, and independent of the code distance  ([arXiv:2606.06062](https://arxiv.org/abs/2606.06062)). Barbell codes are obtained from tile codes by adding ancilla check qubits and translating the qubit positions. The qubits are then embedded in the connectivity graph of the six-qubit star lattice plus near-local coupler architecture.
- _cousin_: [[concepts/qec/2d-color]] — Barbell syndrome extraction adapts the superdense syndrome-extraction circuits originally developed to implement color codes on a square grid  ([arXiv:2312.08813](https://arxiv.org/abs/2312.08813)).
