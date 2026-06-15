---
type: concept
name: Square-lattice cluster-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-stabilizer
- concepts/qec/cluster-state
- concepts/qec/qldpc
- concepts/qec/spt
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/square_lattice_cluster
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: square_lattice_cluster
---

# Square-lattice cluster-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/square_lattice_cluster) (`code_id: square_lattice_cluster`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code based on the cluster state on a square lattice that was used in the first proposal for MBQC  ([arXiv:quant-ph/0108118](https://arxiv.org/abs/quant-ph/0108118), [doi:10.1103/PhysRevLett.86.5188](https://doi.org/10.1103/PhysRevLett.86.5188)).
In the one-way model, the pre-entangled square-lattice cluster is a universal resource, and the computation is carried out entirely by adaptive single-qubit measurements.

(source: raw/error-correction-zoo.md)

## Protection

Random measurement outcomes induce Pauli byproduct operators that are tracked classically and propagated to later measurements or the final readout  ([doi:10.1103/PhysRevLett.86.5188](https://doi.org/10.1103/PhysRevLett.86.5188)).
For computations longer than the available lattice extent, the original paper proposed splitting the computation into consecutive segments and stabilizing each segment using standard error-correction techniques  ([doi:10.1103/PhysRevLett.86.5188](https://doi.org/10.1103/PhysRevLett.86.5188)).

## Encoders

- Initialization of each qubit in the $|+\rangle$ state followed by nearest-neighbor Ising-type entangling evolution, equivalently controlled-phase gates on the edges of the square lattice, prepares the resource state  ([doi:10.1103/PhysRevLett.86.5188](https://doi.org/10.1103/PhysRevLett.86.5188)).

## General gates

- Measurements in the $Z$ basis remove qubits from the lattice to carve out the computation network. $X$-basis measurements propagate quantum information along a wire, adaptive equatorial-basis measurements on a five-qubit chain implement arbitrary single-qubit $SU(2)$ rotations, and a four-qubit pattern implements CNOT between neighboring wires. Later measurement bases can depend on earlier outcomes because of the tracked Pauli byproducts  ([doi:10.1103/PhysRevLett.86.5188](https://doi.org/10.1103/PhysRevLett.86.5188)).
- Universal MBQC remains possible on irregular occupied sublattices above the percolation threshold because wires and gates can be bent and stretched without changing circuit topology  ([doi:10.1103/PhysRevLett.86.5188](https://doi.org/10.1103/PhysRevLett.86.5188)).

## Realizations

- Encoding on 72 qubits of the Zuchongzhi 3.1 quantum processor  ([arXiv:2505.01978](https://arxiv.org/abs/2505.01978)).

## Relations

- _parent_: [[concepts/qec/cluster-state]]
- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/2d-stabilizer]]
- _cousin_: [[concepts/qec/spt]] — The square-lattice cluster state, which is the prototypical resource for universal MBQC  ([arXiv:quant-ph/0108118](https://arxiv.org/abs/quant-ph/0108118), [doi:10.1103/PhysRevLett.86.5188](https://doi.org/10.1103/PhysRevLett.86.5188)), and other 2D cluster states  ([arXiv:1806.08780](https://arxiv.org/abs/1806.08780), [arXiv:1806.04663](https://arxiv.org/abs/1806.04663), [arXiv:1907.13279](https://arxiv.org/abs/1907.13279)) have SPT order protected by subsystem symmetries  ([arXiv:1803.02369](https://arxiv.org/abs/1803.02369), [arXiv:1803.00095](https://arxiv.org/abs/1803.00095), [arXiv:1806.08780](https://arxiv.org/abs/1806.08780)).

## Notes

- The original proposal discussed implementations using neutral atoms in optical lattices with controlled collisions and capacitively coupled quantum dots  ([doi:10.1103/PhysRevLett.86.5188](https://doi.org/10.1103/PhysRevLett.86.5188)).
