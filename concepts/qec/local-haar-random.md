---
type: concept
name: Local Haar-random circuit qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/1d-stabilizer
- concepts/qec/qubits-into-qubits
- concepts/qec/random-circuit
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/local_haar_random
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: local_haar_random
---

# Local Haar-random circuit qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/local_haar_random) (`code_id: local_haar_random`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $n$-qubit code whose codewords are a pair of approximately locally indistinguishable states produced by starting with any two orthogonal $n$-qubit states and acting with a random unitary circuit of depth polynomial in $n$.
Two states are *locally indistinguishable* if they cannot be distinguished by local measurements. A single layer of the encoding circuit is composed of about $n/2$ two-qubit nearest-neighbor gates run in parallel, with each gate drawn randomly from the Haar distribution on two-qubit unitaries.

The above circuit elements act on nearest-neighbor qubits arranged in a line, i.e., a 1D geometry ($D=1$); codes for higher-dimensional geometries require $O(n^{1/D})$-depth circuits  ([arXiv:1208.0692](https://arxiv.org/abs/1208.0692)). Follow-up work  ([arXiv:2010.09775](https://arxiv.org/abs/2010.09775)) showed that, at the erasure threshold, 1D random circuits require $O(\sqrt{n})$ depth, whereas dimensions $D \geq 2$ retain $O(\log n)$-depth scaling.
This result has in turn been extended to other types of Pauli noise  ([arXiv:2212.05071](https://arxiv.org/abs/2212.05071)), while the previous result applies to erasure noise.

(source: raw/error-correction-zoo.md)

## Protection

In a 1D geometry, the local Haar-random circuit qubit code approximately detects any error with support on a segment of length $\leq n/4$, with deviations exponentially suppressed in $n$. 
There is a phase transition in error correction power vs error rate $p$, with a critical depth of order $O(1/p)$  ([arXiv:2510.07512](https://arxiv.org/abs/2510.07512)).

## Encoders

- Random local circuit of depth proportional to $n^{\alpha}$, with $\alpha$ depending on system geometry.

## Relations

- _parent_: [[concepts/qec/qubits-into-qubits]]
- _parent_: [[concepts/qec/random-circuit]]
- _cousin_: [[concepts/qec/topological]] — Local Haar-random codewords, like topological codewords, are locally indistinguishable  ([arXiv:1208.0692](https://arxiv.org/abs/1208.0692)).
- _cousin_: [`unitary_design`](https://errorcorrectionzoo.org/c/unitary_design) — Local Haar-random circuits of polynomial depth form approximate unitary designs  ([arXiv:1208.0692](https://arxiv.org/abs/1208.0692)).
- _cousin_: [[concepts/qec/1d-stabilizer]] — In a 1D geometry, the local Haar-random circuit qubit code approximately detects any error with support on a segment of length $\leq n/4$, with deviations exponentially suppressed in $n$. There is a phase transition in error correction power vs error rate $p$, with a critical depth of order $O(1/p)$  ([arXiv:2510.07512](https://arxiv.org/abs/2510.07512)).
