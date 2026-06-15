---
type: concept
name: Raussendorf-Bravyi-Harrington (RBH) cluster-state code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Raussendorf-Harrington-Goyal (RHG) cluster-state code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-stabilizer
- concepts/qec/bacon-shor-4
- concepts/qec/cluster-state
- concepts/qec/qldpc
- concepts/qec/qubit-concatenated
- concepts/qec/spt
- concepts/qec/steane
- concepts/qec/surface
- concepts/qec/symmetry-protected-self-correct
- concepts/qec/walker-wang
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rbh
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rbh
---

# Raussendorf-Bravyi-Harrington (RBH) cluster-state code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rbh) (`code_id: rbh`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A three-dimensional cluster-state code defined on the bcc lattice (i.e., a cubic lattice with qubits on edges and faces).

The MBQC version of the code is defined as the unique ground state of a certain code Hamiltonian. This state is the resource state used in the first MBQC scheme  ([arXiv:quant-ph/0510135](https://arxiv.org/abs/quant-ph/0510135), [arXiv:quant-ph/0610082](https://arxiv.org/abs/quant-ph/0610082)).
It encodes the temporal gate operations on the surface code into a third spatial dimension.

Addition of certain boundary Hamiltonians yields a degenerate ground-state space that serves as an example of a symmetry-protected self-correcting memory  ([arXiv:1805.01474](https://arxiv.org/abs/1805.01474)).

(source: raw/error-correction-zoo.md)

## Protection

Exhibits symmetry-protected self-correction  ([arXiv:1805.01474](https://arxiv.org/abs/1805.01474)). The energy barrier for symmetry-preserving excitations outside of the code space grows linearly with the lattice width. When the system is coupled locally to a thermal bath respecting the symmetry and below a critical temperature, the memory time grows exponentially with the lattice width.

## General gates

- The computation is encoded in a pre-determined fashion via topological features of the lattice, such as boundaries, defects, or twists. For example, qubits may be encoded in 2D defects along slices of the surface code, and Clifford gates are encoded by spatially braiding the defects along the 3rd dimension. Non-Clifford gates are performed by inserting non-Clifford states into particular *singular* qubits.
To perform the computation, qubits along the extra dimension are measured, e.g., along one two-dimensional slice per time step. This effectively teleports the logical information into the remaining unmeasured portion of the cluster state.

## Decoders

- MBQC syndrome extraction consists of single-qubit measurements and classical post-processing. The six $X$-measurements of qubits on the faces of a cube of the bcc lattice multiply to the product of the six cluster-state stabilizers whose vertices are on the faces of the cube. Such measurements, if done on a 2D slice, also yield $Z$-type syndromes on the next slice.
- Minimum weight perfect-matching (MWPM)  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:1307.1740](https://arxiv.org/abs/1307.1740)) (based on work by Edmonds on finding a matching in a graph  ([doi:10.4153/CJM-1965-045-4](https://doi.org/10.4153/CJM-1965-045-4), [doi:10.6028/jres.069B.013](https://doi.org/10.6028/jres.069B.013))).

## Threshold

- For the topological 3D cluster-state scheme of Raussendorf-Harrington-Goyal, the reported threshold is $1.4\%$ for local depolarizing noise and $0.11\%$ per location in a circuit-level model with preparation, gate, storage, and measurement errors  ([arXiv:quant-ph/0510135](https://arxiv.org/abs/quant-ph/0510135)).
- Various thresholds for optical quantum computing schemes with RBH codes  ([arXiv:quant-ph/0509060](https://arxiv.org/abs/quant-ph/0509060), [arXiv:1005.2915](https://arxiv.org/abs/1005.2915)).
- $0.75\%$ for preparation, gate, storage, and measurement errors  ([arXiv:quant-ph/0610082](https://arxiv.org/abs/quant-ph/0610082)).
- $24.9\%$ under erasure noise  ([arXiv:1005.2456](https://arxiv.org/abs/1005.2456)).
- Concatenation of the RBH code with small codes such as the $⟦2,1⟧$ repetition code, $⟦4,1,1,2⟧$ subsystem code, or Steane code can improve thresholds  ([arXiv:2209.09390](https://arxiv.org/abs/2209.09390)).

## Relations

- _parent_: [[concepts/qec/cluster-state]]
- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/3d-stabilizer]]
- _parent_: [[concepts/qec/walker-wang]] — The Walker-Wang model code reduces to the RBH cluster-state code when the input category $\mathcal{C}$ is that of the surface code  ([arXiv:2011.04693](https://arxiv.org/abs/2011.04693)).
- _cousin_: [[concepts/qec/symmetry-protected-self-correct]] — The RBH code can exhibit self-correction protected by a certain symmetry.
- _cousin_: [[concepts/qec/spt]] — In 3D, cluster states belong to SPT phases protected by higher-form symmetries  ([arXiv:1611.05450](https://arxiv.org/abs/1611.05450)) and enable universal fault-tolerant MBQC  ([arXiv:quant-ph/0703143](https://arxiv.org/abs/quant-ph/0703143)).
- _cousin_: [[concepts/qec/surface]] — The RBH state encodes the temporal gate operations on the surface code into a third spatial dimension  ([arXiv:quant-ph/0510135](https://arxiv.org/abs/quant-ph/0510135), [arXiv:quant-ph/0610082](https://arxiv.org/abs/quant-ph/0610082)). In addition, one possible 2D boundary of the RBH code is effectively a 2D toric code.
- _cousin_: [`bcc`](https://errorcorrectionzoo.org/c/bcc) — The RBH code is defined on the bcc lattice.
- _cousin_: [[concepts/qec/qubit-concatenated]] — Concatenation of the RBH code with small codes such as the $⟦2,1⟧$ repetition code, $⟦4,1,1,2⟧$ subsystem code, or Steane code can improve thresholds  ([arXiv:2209.09390](https://arxiv.org/abs/2209.09390)).
- _cousin_: [[concepts/qec/bacon-shor-4]] — Concatenation of the RBH code with small codes such as the $⟦2,1⟧$ repetition code, $⟦4,1,1,2⟧$ subsystem code, or Steane code can improve thresholds  ([arXiv:2209.09390](https://arxiv.org/abs/2209.09390)).
- _cousin_: [[concepts/qec/steane]] — Concatenation of the RBH code with small codes such as the $⟦2,1⟧$ repetition code, $⟦4,1,1,2⟧$ subsystem code, or Steane code can improve thresholds  ([arXiv:2209.09390](https://arxiv.org/abs/2209.09390)).

## Notes

- Introduction to MBQC protocols with the RBH state  ([arXiv:1504.01444](https://arxiv.org/abs/1504.01444)).
- Blind quantum computation is possible with the RBH state  ([arXiv:1110.5460](https://arxiv.org/abs/1110.5460)).
