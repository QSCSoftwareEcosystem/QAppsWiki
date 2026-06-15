---
type: concept
name: Majorana surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/majorana-stab
- concepts/qec/qldpc
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/majorana_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: majorana_surface
---

# Majorana surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/majorana_surface) (`code_id: majorana_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Fermionic analogue of the surface code defined on a three-colorable 2D tiling whose face operators are non-overlapping even-Majorana stabilizers.
Open patches with four or six alternating colored boundaries encode logical tetrons or hexons.
The uniform 4.8.8, 6.6.6, and 4.6.12 tilings yield families with tetron, hexon, or dodecon building blocks and with twist-based lattice surgery supporting minimal-overhead logical Clifford gates  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

(source: raw/error-correction-zoo.md)

## Protection

Under quasiparticle-poisoning noise, single Majorana operators flip the syndromes of adjacent stabilizers and can be decoded with surface-code methods.
If the shortest logical operator has Majorana weight $d_m$, then the code corrects up to $d_m/2-1$ Majorana errors; the corresponding qubit distance is naturally labeled by $d=d_m/2$ because Pauli errors on tetron/hexon hardware involve pairs of Majoranas  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
Implementations that treat one color of stabilizers as parity-fixing constraints reduce measured stabilizer weight, at the cost that parity-violating single-Majorana events become leakage unless that color is also measured  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

## Rate

For code distance $d=d_m/2$, the 4.8.8, 6.6.6, and 4.6.12 families require $4d^2$, $6d^2+\mathcal{O}(d)$, and $12d^2+\mathcal{O}(d)$ Majoranas per logical qubit, respectively  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
Their maximum stabilizer weights for fault-tolerant lattice surgery can be reduced to $8$, $6$, and $6$ Majoranas, respectively, compared to $10$ Majoranas for bosonic twist-based surface-code surgery  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

## General gates

- All logical Clifford gates, including CNOT, can be implemented with zero time overhead by classically tracking them and measuring Pauli products via ordinary and twist-based lattice surgery  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
- Surface-code state injection of noisy magic states into logical tetrons  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

## Fault tolerance

- Repeated syndrome rounds make ordinary and twist-based lattice surgery fault tolerant against both data and measurement errors  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)) (see also  ([arXiv:2211.11777](https://arxiv.org/abs/2211.11777))).

## Relations

- _parent_: [[concepts/qec/majorana-stab]]
- _parent_: [[concepts/qec/qldpc]] — The Majorana surface code is a 2D qubit stabilizer code with respect to the Majorana operator basis.
- _parent_: [[concepts/qec/2d-stabilizer]] — The Majorana surface code is a 2D qubit stabilizer code with respect to the Majorana operator basis.
- _cousin_: [[concepts/qec/surface]] — Majorana surface codes map non-uniquely to bosonic surface codes: replacing each tetron in a 4.8.8 code by a qubit yields the square-lattice surface code, while 6.6.6 and 4.6.12 codes map to rotated-square and Kagome-lattice surface-code realizations, respectively  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
