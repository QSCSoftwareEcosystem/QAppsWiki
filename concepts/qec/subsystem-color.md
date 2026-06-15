---
type: concept
name: Subsystem color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Gauge color code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/color
- concepts/qec/eaoa-stabilizer
- concepts/qec/qubit-subsystem-css
- concepts/qec/qudit-subsystem-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_color
---

# Subsystem color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_color) (`code_id: subsystem_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A subsystem version of the color code.

Subsystem color codes form a $(d,e)$ family on punctured $D$-colexes, or equivalently on suitably colored simplicial $D$-balls, encoding one logical qubit and interpolating between conventional and subsystem color codes via gauge fixing  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).
Examples include 2D subsystem color codes obtained by expanding the vertices of a two-colex embedded in a surface of genus $g$, where each vertex is split into a triangle and each edge into a pair of edges.

The stabilizer group may contain generators of unbounded weight, distinguishing these codes from stabilizer codes with bounded-weight generators for which some logical qubits were re-assigned to be gauge qubits.

Gauge fixing between subsystem color codes defined on the same lattice can be implemented using local measurements and classical processing analogous to error correction  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).

(source: raw/error-correction-zoo.md)

## Transversal gates

- For a $D$-dimensional $(d,e)$ gauge color code, $CNOT$ is transversal, Hadamard is transversal when $d=e$, and $R_n=\operatorname{diag}(1,e^{2\pi i/2^n})$ is transversal whenever $D \geq n(D-e)$  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).

## Decoders

- Clustering decoder  ([arXiv:1503.08217](https://arxiv.org/abs/1503.08217)).
- Erasure decoder  ([doi:10.1109/ITW46852.2021.9457583](https://doi.org/10.1109/ITW46852.2021.9457583)).
- Gauge-fixing decoders  ([arXiv:2111.14594](https://arxiv.org/abs/2111.14594), [doi:10.1109/ITW46852.2021.9457583](https://doi.org/10.1109/ITW46852.2021.9457583)).

## Relations

- _parent_: [[concepts/qec/qubit-subsystem-css]]
- _parent_: [[concepts/qec/qudit-subsystem-color]] — Modular-qudit subsystem color codes reduce to subsystem color codes for $q=2$.
- _cousin_: [[concepts/qec/color]] — Gauge fixing relates subsystem color codes to conventional color codes defined on the same lattice  ([arXiv:1311.0879](https://arxiv.org/abs/1311.0879)).
- _cousin_: [[concepts/qec/eaoa-stabilizer]] — The 15-qubit subsystem color code yields several EAOA qubit stabilizer constructions, including $⟦13,1,3;6,2,3⟧$, $⟦15,1,3;5,1,2⟧$, and $⟦15,1,3;4,1,4⟧$ examples obtained via clean-qubits and entanglement-assisted gauge-fixing constructions  ([arXiv:2411.14389](https://arxiv.org/abs/2411.14389)).
