---
type: concept
name: Three-fermion (3F) subsystem code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/qubit-subsystem-stabilizer
- concepts/qec/surface
- concepts/qec/three-fermion
- concepts/qec/topological-abelian
- concepts/qec/translationally-invariant-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_three_fermion
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_three_fermion
---

# Three-fermion (3F) subsystem code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_three_fermion) (`code_id: subsystem_three_fermion`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

2D subsystem stabilizer code whose low-energy excitations realize the three-fermion anyon theory  ([arXiv:0712.1377](https://arxiv.org/abs/0712.1377), [arXiv:0811.0911](https://arxiv.org/abs/0811.0911), [arXiv:1103.4606](https://arxiv.org/abs/1103.4606)).
One version uses two qubits at each site  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)), while other manifestations utilize a single qubit per site and only weight-two (two-body) interactions  ([arXiv:0811.0911](https://arxiv.org/abs/0811.0911), [arXiv:0908.4246](https://arxiv.org/abs/0908.4246)).
All are expected to be equivalent to each other via a local constant-depth Clifford circuit.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/qubit-subsystem-stabilizer]]
- _parent_: [[concepts/qec/translationally-invariant-subsystem]]
- _parent_: [[concepts/qec/topological-abelian]] — The 3F code is a 2D subsystem code characterized by 3F topological order  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)), which is chiral and modular.
- _cousin_: [[concepts/qec/surface]] — One version of the 3F subsystem code can be obtained from two copies of the square-lattice surface code by gauging out the anyons $e_1m_1e_2$ and $e_2m_2$  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
- _cousin_: [[concepts/qec/three-fermion]] — The (three-dimensional) 3F Walker-Wang model cluster-like state encodes the temporal gate operations on the (two-dimensional) 3F subsystem code into a third spatial dimension  ([arXiv:2011.04693](https://arxiv.org/abs/2011.04693)).
- _cousin_: [[concepts/qec/2d-color]] — The 2D color code is equivalent to two decoupled copies of the 3F code in the sense that the same anyon theory describes the low-energy excitations of both codes  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).
