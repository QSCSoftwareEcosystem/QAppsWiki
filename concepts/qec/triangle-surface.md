---
type: concept
name: Triangular surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Triangle surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-lego
- concepts/qec/stellated-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/triangle_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: triangle_surface
---

# Triangular surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/triangle_surface) (`code_id: triangle_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A member of a twist-defect surface code family with a single central twist whose planar layout fits within a triangle.
Triangle codes can be viewed as three conjoined surface-code patches projected into two dimensions, with weight-four plaquette stabilizers and weight-two edge stabilizers  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).
Symmetric distance-$d$ triangle codes use $3d^2/4+1/4$ data qubits, i.e., about $25\%$ fewer than the rotated surface code for a given odd distance.
Logical $\overline{X}$, $\overline{Y}$, and $\overline{Z}$ operators can be supported on the three sides of the triangle, enabling initialization and measurement in any Pauli basis.

The size of the triangular patches and which patch encodes data versus acts as ancillas for gates depends on the initialization and measurement procedures.
See Ref.  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)) for tables and figures.

(source: raw/error-correction-zoo.md)

## Rate

Symmetric distance-$d$ triangle codes use $3d^2/4+1/4$ data qubits per logical qubit. Including ancillas needed for planar Clifford computation, the CC, BC, and CS architectures use $3d^2+O(d)$, $9d^2/4+O(d)$, and $6d^2/4+O(d)$ physical qubits per logical qubit, respectively  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## Encoders

- Code conversion (CC) initialization and measurement method, in which the surface code is used to hold data between gates in patches.
- Basis-state conversion (BC) initialization and measurement method in which one initializes and then measures a logical Pauli eigenstate. To do this, triangle ancilla qubits are required outside of the triangle patches that hold the data. That is, the ancilla patches must be empty of data and be adjacent to the side that contains the logical Pauli that needs to be measured or initialized.
- The CAT states (CS) initialization and measurement method uses a row of $d$ ancilla qubits along some edge of a triangle code with distance $d$ to create and verify a GHZ state that is used to measure the logical operator along the same edge. Creating this GHZ state takes $O(d)$ time steps. To reliably measure the logical state, the GHZ state must be measured $O(d)$ times, resulting in $O(d^2)$ time for logical measurement. Initialization is a similar procedure that requires $O(d^2)$ time for logical-operator measurements that occur $O(d)$ times as well as $O(d^2)$ time to project the code onto a logical state  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## Transversal gates

- Triangle codes admit transversal order-three single-qubit gates in the Clifford group, e.g., $\bar{SH}$  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## General gates

- Triangle codes admit a distillation-free implementation of the full Clifford group using lattice surgery, 1-bit teleportation, and patch reorientation  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).
- Performing single-qubit gates in the Clifford group using the CC procedure requires surface code patches to be embedded in triangle patches. This procedure requires $O(d)$ Clifford gate times for $H,S,CNOT$  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).
- The BC procedure requires $O(1)$ time to perform $H,S$ gates and $O(d)$ time to perform $CNOT$. Sometimes reorientation of the sides is required, and that takes $O(d)$ to perform  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## Decoders

- The decoding uses a single decoding graph since the triangle code is not a CSS code. Nodes of the graph are located at each stabilizer (center of the triangle graph) and have red or blue edges, where red associates with $X$ errors and blue with $Z$ errors. To take into account any errors from measuring the error syndrome, a three-dimensional stack of decoding graphs is laid on top of the code with vertical edges connecting qubits between layers  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## Fault tolerance

- The symmetry of triangle codes allows for fault-tolerant measurement and encoding in any Pauli basis  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).
- A non-fault-tolerant circuit initializes the triangle code. To guarantee fault-tolerance, post-selection is performed on trivial measurements of the syndrome and of the logical Pauli, depending on the basis of the logical states  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).
- Making syndrome extraction fault tolerant requires a specific ordering of syndrome measurements so as to avoid hook errors  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## Code capacity threshold

- $10\%$ under either bit-flip or bit-phase noise for ideal syndrome measurements. The decoder used is a decoding graph with the same weight assigned to each edge, and Dijkstra's algorithm is used to compute the total weight of any path  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## Threshold

- $3.2\%$ bit-flip error-correction threshold for noisy syndrome measurements and $2.6\%$ for bit-phase flip noise. The decoder used is a decoding graph as described above  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).
- In general, the triangular surface code has a threshold of similar magnitude to the toric code for uncorrelated $X$ and $Z$ errors. For correlated errors, the triangle code has a lower threshold by a factor of about $36$  ([arXiv:1612.04795](https://arxiv.org/abs/1612.04795)).

## Relations

- _parent_: [[concepts/qec/stellated-surface]] — The triangular surface code is the $s=3$ member of the stellated surface-code family  ([arXiv:1806.02820](https://arxiv.org/abs/1806.02820)).
- _cousin_: [[concepts/qec/quantum-lego]] — Triangle surface codes can be reproduced by inserting a defect tensor and Hadamard-modified tensors into the surface-code tensor network  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
