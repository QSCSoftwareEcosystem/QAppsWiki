---
type: concept
name: Heavy-hexagon code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bacon-shor
- concepts/qec/compass-model
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/heavy_hex
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: heavy_hex
---

# Heavy-hexagon code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/heavy_hex) (`code_id: heavy_hex`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Subsystem stabilizer code on the heavy-hexagonal point set that combines Bacon-Shor and surface-code stabilizers.
Encodes one logical qubit into $n=(5d^2-2d-1)/2$ physical qubits with distance $d$.
The heavy-hexagonal point set allows for low degree (at most 3) connectivity between all the data and ancilla qubits, which is suitable for fixed-frequency transmon qubits subject to frequency collision errors.
The code can be split into a surface and a Bacon-Shor code, with the idling qubits of one code serving as the physical qubits of the other  ([arXiv:2404.15989](https://arxiv.org/abs/2404.15989)).

Data qubits and ancillas of the code are placed on a heavy-hexagonal point set, i.e., the vertices and edges of a tiling of hexagons. A subset of the ancilla qubits are flag qubits used for detecting high-weight errors arising from fewer faults. The code stabilizers for detecting $X$-type errors are measured by measuring weight-two $Z$-type gauge operators whose product produces stabilizers of the surface code. $X$-type stabilizers are column operators corresponding to stabilizers of the Bacon-Shor code, which are measured by taking products of weight-four and weight-two $X$-type gauge operators.

(source: raw/error-correction-zoo.md)

## Protection

Protects against Pauli noise. The code has no threshold for $Z$-type Pauli errors since they are detected by Bacon-Shor-type stabilizers.

## Rate

$1/n$ for a distance-$d$ heavy-hexagon code on $n = (5d^2-2d-1)/2$ qubits.

## Encoders

- For a logical-zero state, prepare all data qubits in the physical-zero state and then measure the $X$-type Bacon-Shor stabilizers. For logical-plus state, prepare all data qubits in the physical-plus state and then measure $Z$-type surface code stabilizers.
- Stabilizer measurement encoding circuits have a constant depth of 10 time steps (excluding ancilla state preparation and measurement).

## Transversal gates

- CNOT gates are transversal for this code. However, for most architectures, all logical gates would be implemented using lattice surgery methods.

## General gates

- Universal gate set achieved with magic state injection and lattice surgery.
- Magic-state injection with and without flag qubits  ([arXiv:2412.15751](https://arxiv.org/abs/2412.15751)).

## Decoders

- Any graph-based decoder can be used, such as MWPM and Union Find. However, edge weights must be dynamically renormalized using flag-qubit measurement outcomes after each syndrome measurement round.
- Machine-learning  ([arXiv:2210.09730](https://arxiv.org/abs/2210.09730)) and neural-network  ([arXiv:2311.15146](https://arxiv.org/abs/2311.15146)) decoders.

## Fault tolerance

- All logical gates can be fault-tolerantly implemented using lattice surgery and magic state injection.
- Stabilizer measurements are measured fault-tolerantly using one-flag circuits since some single-fault events can result in weight-two data qubit errors which are parallel to the code's logical operators. Hence, using information from the flag-qubit measurements is crucial to fault-tolerantly measure the code stabilizers.

## Threshold

- $0.45\%$ for $X$ errors under a full circuit-level depolarizing noise model (obtained from Monte Carlo simulations).
- $Z$-errors have no threshold given the $X$-type Bacon-Shor stabilizers.

## Realizations

- Superconducting qubits: Logical state preparation and flag-qubit error correction realized in superconducting-circuit devices (specifically, fixed-frequency transmon qubit architectures) by IBM for $d=2$  ([arXiv:1705.09259](https://arxiv.org/abs/1705.09259), [arXiv:2110.04285](https://arxiv.org/abs/2110.04285)) and $d=3$  ([arXiv:2203.07205](https://arxiv.org/abs/2203.07205)). Simultaneous syndrome extraction and logical Bell-state preparation for both the embedded surface and Bacon-Shor codes of distance $\leq 4$ on an IBM 133-qubit device  ([arXiv:2404.15989](https://arxiv.org/abs/2404.15989)). Embedded rotated surface code magic-state injection implemented on IBM fez device  ([arXiv:2412.01446](https://arxiv.org/abs/2412.01446)).

## Relations

- _parent_: [[concepts/qec/compass-model]] — The heavy-hex code is a compass code on a heavy-hexagonal lattice, combining weight-two $XX$ and $ZZ$ gauge operators that are partially gauge-fixed to yield surface-code $Z$-type stabilizers and Bacon-Shor $X$-type stabilizers  ([arXiv:1907.09528](https://arxiv.org/abs/1907.09528)).
- _cousin_: [[concepts/qec/surface]] — Surface code stabilizers are used to measure the Z-type stabilizers of the code. There are various ways to embed the surface code into the heavy-hex lattice  ([arXiv:2402.02185](https://arxiv.org/abs/2402.02185)).
- _cousin_: [[concepts/qec/bacon-shor]] — Bacon-Shor stabilizers are used to measure the X-type stabilizers of the code.
