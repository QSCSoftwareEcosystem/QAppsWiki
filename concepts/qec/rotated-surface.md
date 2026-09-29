---
type: concept
name: Rotated surface code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Checkerboard code
- Medial surface code
- Rectified surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/heavy-hex
- concepts/qec/hierarchical
- concepts/qec/hypergraph-product
- concepts/qec/perm-self-dual-css
- concepts/qec/quantum-tanner
- concepts/qec/surface
- concepts/qec/yoked-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/rotated_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: rotated_surface
---

# Rotated surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/rotated_surface) (`code_id: rotated_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Variant of the surface code obtained by taking the medial graph of the surface code lattice (treated as a graph) and applying a procedure to construct the check operators  ([arXiv:quant-ph/0703272](https://arxiv.org/abs/quant-ph/0703272), [arXiv:1606.07116](https://arxiv.org/abs/1606.07116)) ([arXiv:2101.09349](https://arxiv.org/abs/2101.09349)).
On a square lattice, this amounts to a rotation by 45 degrees such that qubits are on vertices, and both $X$- and $Z$-type check operators occupy plaquettes in an alternating checkerboard pattern.

Stabilizer generators for this code on a square lattice are shown in \ref{figure:rotated-surface-operators}.

(source: raw/error-correction-zoo.md)

## Protection

The $⟦L^2,1,L⟧$ planar rotated surface code variant  ([arXiv:quant-ph/0703272](https://arxiv.org/abs/quant-ph/0703272)) includes the $⟦9,1,3⟧$ surface-17 code, named as such because 8 ancilla qubits are used for check operator measurements alongside the 9 physical qubits.
The $⟦L^2,2,L⟧$ periodic variant is a rotated toric code, whose smallest example is the $⟦4,2,2⟧$ code.
Non-bipartite rotated toric codes with odd distance include the family $⟦t^2+(t+1)^2,1,2t+1⟧$  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).

## Encoders

- Unitary encoder based on code conversion between rotated and regular surface codes  ([arXiv:2506.04084](https://arxiv.org/abs/2506.04084)).

## Transversal gates

- Fold-transversal $S$ gate  ([arXiv:2412.01391](https://arxiv.org/abs/2412.01391), [arXiv:2502.00957](https://arxiv.org/abs/2502.00957)).
- The logical Hadamard gate is transversal, but under the alternating six-layer gate sequence the detecting regions of the two boundary orientations do not align  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)). Alignment is restored either by one additional layer of boundary CNOT gates, needed only once every $6d$ layers and benchmarked to have negligible impact on the logical error rate, or by applying the transversal Hadamard at a square-shaped end cycle and reflecting the subsequent gate sequence, which takes six cycles and needs no CXSWAP gates.

## General gates

- Injection of the $|Y\rangle$ state  ([arXiv:2501.15566](https://arxiv.org/abs/2501.15566)).

## Decoders

- Only certain syndrome extraction schedules are distance-preserving  ([arXiv:1404.3747](https://arxiv.org/abs/1404.3747)).
- Local neural-network using 3D convolutions, combined with a separate global decoder  ([arXiv:2208.01178](https://arxiv.org/abs/2208.01178)).
- Iterative CNOT decoder  ([arXiv:2407.20976](https://arxiv.org/abs/2407.20976)).
- Fault-tolerant BP (FTBP) decoder  ([arXiv:2409.18689](https://arxiv.org/abs/2409.18689)).
- [Frontier decoder](https://github.com/aleverrier/frontier), a pruned dynamic-programming decoder  ([arXiv:2606.20513](https://arxiv.org/abs/2606.20513)).

## Code capacity threshold

- Depolarizing noise: close to the optimal value of $18.9\%$ under the Frontier decoder  ([arXiv:2606.20513](https://arxiv.org/abs/2606.20513)).

## Threshold

- Thresholds for various amounts of erasure, Pauli, correlated, and measurement noise are known  ([arXiv:2408.00829](https://arxiv.org/abs/2408.00829), [arXiv:2410.23779](https://arxiv.org/abs/2410.23779)).

## Fault tolerance

- A particular choice of CNOT gates during syndrome extraction is required to avoid hook errors and be fault-tolerant to syndrome qubit errors  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:1208.0928](https://arxiv.org/abs/1208.0928), [arXiv:1404.3747](https://arxiv.org/abs/1404.3747)).
- Memory, lattice surgery, and walking operations all fit within a bounding box of $2d^2$ physical qubits per distance-$d$ patch, rather than the $2(d+1)^2$ required by earlier schemes  ([arXiv:2605.30455](https://arxiv.org/abs/2605.30455)). The construction modifies the patch boundaries and uses an alternating six-layer gate sequence, namely one reset layer, four layers of two-qubit gates, and one measurement layer, in both the $X$-top and $Z$-top boundary configurations. Memory and lattice surgery need only a degree-three connectivity graph, and lattice surgery requires no padding region between patches. The walking operation instead needs a square grid together with CXSWAP gates on the boundary.
- Under circuit-level noise at $p=0.002$, the Frontier decoder yields an error-suppression factor $\Lambda\approx 8.6$, compared with $\Lambda\approx 7.9$ for correlated MWPM  ([arXiv:2606.20513](https://arxiv.org/abs/2606.20513)).

## Realizations

- Teleportation transition of distance-seven rotated surface-code states on a 125-qubit superconducting processor  ([arXiv:2602.21293](https://arxiv.org/abs/2602.21293)).

## Relations

- _parent_: [[concepts/qec/surface]] — The lattice of the rotated surface code can be obtained by taking the medial graph of the surface code lattice (treated as a graph) and applying a procedure to construct the check operators  ([arXiv:quant-ph/0703272](https://arxiv.org/abs/quant-ph/0703272), [arXiv:1606.07116](https://arxiv.org/abs/1606.07116)) ([arXiv:2101.09349](https://arxiv.org/abs/2101.09349)). Applying the quantum Tanner transformation to the surface code yields the rotated surface code }. The rotated surface code presents certain savings over the original surface code  ([arXiv:2409.14765](https://arxiv.org/abs/2409.14765)).
- _parent_: [[concepts/qec/quantum-tanner]] — Applying the quantum Tanner transformation to the surface code yields the rotated surface code }.
- _cousin_: [[concepts/qec/perm-self-dual-css]] — The $⟦L^2,1,L⟧$ rotated surface code is permutationally self-dual for odd $L$, with an $XZ$-duality given by a $\pi/2$ rotation of the qubit grid  ([arXiv:2412.01391](https://arxiv.org/abs/2412.01391)). For even $L$, the numbers of independent $X$- and $Z$-type stabilizer generators differ because they sum to the odd number $L^2-1$. No permutation can then exchange the two stabilizer groups.
- _cousin_: [[concepts/qec/hypergraph-product]] — Periodic rotated toric codes on the same lattice can be obtained from hypergraph products of two cyclic linear binary codes with palindromic check polynomials  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).
- _cousin_: [`binary_cyclic`](https://errorcorrectionzoo.org/c/binary_cyclic) — Periodic rotated toric codes on the same lattice can be obtained from hypergraph products of two cyclic linear binary codes with palindromic check polynomials  ([arXiv:1202.0928](https://arxiv.org/abs/1202.0928)).
- _cousin_: [[concepts/qec/heavy-hex]] — A rotated surface code can be mapped onto a heavy square lattice, resulting in a code similar to the heavy-hexagon code  ([arXiv:1907.09528](https://arxiv.org/abs/1907.09528)).
- _cousin_: [[concepts/qec/hierarchical]] — Hierarchical codes are concatenations of constant-rate QLDPC codes with rotated surface codes.
- _cousin_: [[concepts/qec/yoked-surface]] — Yoked surface codes are concatenations of QMDPC codes with rotated surface codes.
