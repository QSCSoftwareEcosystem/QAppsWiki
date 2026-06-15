---
type: concept
name: Ruby Floquet code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Floquet color code
- Ruby Floquet color code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/floquet
- concepts/qec/quantum-repetition
- concepts/qec/subsystem-three-fermion
- concepts/qec/triangular-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/floquet_xyz_ruby
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: floquet_xyz_ruby
---

# Ruby Floquet code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/floquet_xyz_ruby) (`code_id: floquet_xyz_ruby`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

2D Floquet code whose qubits are placed on vertices of a ruby tiling, with weight-two Pauli check operators on $x$-, $y$-, and $z$-labeled edges  ([arXiv:2407.08566](https://arxiv.org/abs/2407.08566)).
The code admits two different measurement schedules, the XYZ ruby schedule and the color-code schedule.

One third of the time during the XYZ ruby measurement schedule, its ISG is that of the 6.6.6 color code concatenated with a three-qubit repetition code.
Together, all ISGs generate the gauge group of the 3F subsystem code.

A different three-round color-code schedule  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)) admits ISGs are FDLQC-equivalent to the 2D color code; in one round, the ISG is exactly the color code concatenated with a three-qubit repetition code.
The color-code schedule has a $\mathbb{Z}_3$ automorphism of the dynamically generated logical operators, while the rewinding schedule $012102$ and another six-round schedule both trivialize that automorphism.
A parent stabilizer code for this schedule is FDLQC-equivalent to two copies of the 2D color code  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

(source: raw/error-correction-zoo.md)

## Rate

On a torus, the color-code schedule encodes four logical qubits, two of which are dynamically generated relative to the underlying subsystem code  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

## General gates

- In the round whose ISG is the 2D color code concatenated with a three-qubit repetition code, the usual transversal logical Clifford gates of the color code remain available  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

## Threshold

- Circuit-level noise: $\approx 0.18\%$ using BP-OSD decoder  ([arXiv:2407.08566](https://arxiv.org/abs/2407.08566)).

## Fault tolerance

- Pairs of consecutive ISGs of the color-code schedule are locally reversible, and the paper argues that this suggests a non-zero fault-tolerant threshold  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).

## Relations

- _parent_: [[concepts/qec/floquet]]
- _cousin_: [[concepts/qec/triangular-color]] — One third of the time during the XYZ ruby measurement schedule, the ISG is that of the 6.6.6 color code concatenated with a three-qubit repetition code.
- _cousin_: [[concepts/qec/2d-color]] — Each ISG of the color-code schedule is FDLQC-equivalent to the 2D color code, and a parent stabilizer code is FDLQC-equivalent to two copies of the 2D color code  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [[concepts/qec/quantum-repetition]] — One third of the time during the XYZ ruby measurement schedule, the ISG is that of the 6.6.6 color code concatenated with a three-qubit repetition code. One round of the color-code schedule is exactly the 2D color code concatenated with a three-qubit repetition code  ([arXiv:2307.13668](https://arxiv.org/abs/2307.13668)).
- _cousin_: [`honeycomb`](https://errorcorrectionzoo.org/c/honeycomb) — The ruby Floquet code is defined on the ruby tiling.
- _cousin_: [[concepts/qec/subsystem-three-fermion]] — Together, all ISGs of the ruby Floquet code generate the gauge group of the 3F subsystem code.
