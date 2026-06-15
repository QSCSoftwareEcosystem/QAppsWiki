---
type: concept
name: $⟦2m,2m-2,2⟧$ error-detecting code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Iceberg code
- $⟦2m,2m-2,2⟧$ quantum parity code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/4612-color
- concepts/qec/ampdamp
- concepts/qec/ball-color
- concepts/qec/qmdpc
- concepts/qec/quantum-mds
- concepts/qec/self-complementary
- concepts/qec/self-dual-css
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/iceberg
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: iceberg
---

# $⟦2m,2m-2,2⟧$ error-detecting code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/iceberg) (`code_id: iceberg`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Self-complementary and self-dual CSS code for $m\geq 2$ with generators $\{XX\cdots X, ZZ\cdots Z\} $ acting on all $2m$ physical qubits.
The code is constructed via the CSS construction from an SPC code and a repetition code  ([arXiv:1803.06987](https://arxiv.org/abs/1803.06987)).
This is the highest-rate distance-two code when an even number of qubits is used  ([arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)).

Admits a basis such that each codeword is a superposition of a computational basis state labeled by an even-weight bitstring $b$ and a state labeled by the negation of $b$.
Its all-zero logical state is a conventional GHZ state.
Removing the $Z$-type generator expands the number of codewords to all combinations of bitstrings and their negations, yielding a code with $k=2m-1$  ([arXiv:quant-ph/0301105](https://arxiv.org/abs/quant-ph/0301105)).

All of its automorphisms lie in the Clifford group  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043)).

(source: raw/error-correction-zoo.md)

## Protection

Detects a single-qubit error.

## Encoders

- Adaptive constant-depth circuit with geometrically local gates and measurements throughout  ([arXiv:1906.08890](https://arxiv.org/abs/1906.08890), [arXiv:2112.03061](https://arxiv.org/abs/2112.03061)).

## Transversal gates

- Transveral CNOT gates can be performed by first teleporting qubits into different code blocks  ([arXiv:quant-ph/9702029](https://arxiv.org/abs/quant-ph/9702029)).
- For $2m$ being a multiple of four, this code houses a transversal representation of the single-qubit Clifford group  ([arXiv:1609.08172](https://arxiv.org/abs/1609.08172)). Its $n$-block version houses a transversal representation of the $n$-qubit Clifford group  ([arXiv:1609.08172](https://arxiv.org/abs/1609.08172)). The commutant of transversal representations of the Clifford group contains qubit permutations and projections onto the $⟦2m,2m-2,2⟧$ error-detecting code  ([arXiv:2504.12263](https://arxiv.org/abs/2504.12263)).

## General gates

- Logical SWAP gates can be performed fault tolerantly using an ancilla qubit  ([arXiv:quant-ph/9702029](https://arxiv.org/abs/quant-ph/9702029)).
- Universal set of gates, each of which is supported on two qubits  ([arXiv:2211.06703](https://arxiv.org/abs/2211.06703)).
- Fault-tolerant Clifford Trotter circuits that are linear in $k$ using flag qubits via a solve-and-stitch algorithm and application of a logical identity circuit  ([arXiv:2404.11953](https://arxiv.org/abs/2404.11953)).

## Decoders

- The $⟦2m,2m-2,2⟧$ error-detecting code  ([arXiv:quant-ph/0402067](https://arxiv.org/abs/quant-ph/0402067)) and its relative the code with single stabilizer $XX\cdots X$  ([arXiv:quant-ph/0302006](https://arxiv.org/abs/quant-ph/0302006)) admit autonomous QEC against single AD errors.

## Fault tolerance

- Logical SWAP gates can be performed fault tolerantly using an ancilla qubit  ([arXiv:quant-ph/9702029](https://arxiv.org/abs/quant-ph/9702029)).
- Two-qubit fault-tolerant state preparation, error detection and projective measurements  ([arXiv:1705.02329](https://arxiv.org/abs/1705.02329)) (see also  ([arXiv:2211.06703](https://arxiv.org/abs/2211.06703))).
- CNOT and Hadamard gates using only two extra qubits and four-qubit fault-tolerant $CCZ$ gate  ([arXiv:1705.05365](https://arxiv.org/abs/1705.05365)).
- Fault-tolerant Clifford Trotter circuits that are linear in $k$ using flag qubits via a solve-and-stitch algorithm and application of a logical identity circuit  ([arXiv:2404.11953](https://arxiv.org/abs/2404.11953)).
- Weak fault tolerance: any single gate error can be detected by measuring stabilizers and utilizing extra ancillas  ([arXiv:2408.14828](https://arxiv.org/abs/2408.14828)).

## Realizations

- Trapped-ion devices: the $m=5$ code has been realized on a 12-qubit device by Quantinuum  ([arXiv:2211.06703](https://arxiv.org/abs/2211.06703)). The QAOA algorithm has been realized on the $m=18$ code using 510 two-logical-qubit gates  ([arXiv:2504.21172](https://arxiv.org/abs/2504.21172)). State preparation, measurement, and a partially fault-tolerant simulation of the XY model demonstrated on a 98-qubit Quantinuum Helios device using the code and its concatenated version  ([arXiv:2602.22211](https://arxiv.org/abs/2602.22211)).

## Relations

- _parent_: [[concepts/qec/qmdpc]] — The $⟦2m,2m-2,2⟧$ error-detecting code is a 1D QMDPC.
- _parent_: [[concepts/qec/quantum-mds]] — The only nontrivial qubit MDS codes have parameters $⟦5,1,3⟧$, $⟦6,0,4⟧$, and $⟦2m,2m-2,2⟧$ .
- _parent_: [[concepts/qec/ball-color]] — The $⟦2m,2m-2,2⟧$ error-detecting code is a ball color code  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
- _parent_: [[concepts/qec/stabilizer-over-gf4]] — The $⟦2m,2m-2,2⟧$ error-detecting code is Hermitian  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
- _parent_: [[concepts/qec/self-dual-css]]
- _parent_: [[concepts/qec/self-complementary]]
- _cousin_: [`parity_check`](https://errorcorrectionzoo.org/c/parity_check) — The $⟦2m,2m-2,2⟧$ error-detecting code is constructed via the CSS construction from an SPC code and its dual repetition code  ([arXiv:1803.06987](https://arxiv.org/abs/1803.06987)).
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The $⟦2m,2m-2,2⟧$ error-detecting code is constructed via the CSS construction from an SPC code and its dual repetition code  ([arXiv:1803.06987](https://arxiv.org/abs/1803.06987)).
- _cousin_: [[concepts/qec/4612-color]] — The $⟦2m,2m-2,2⟧$ error-detecting code for $m=4$ is a color code defined on a single octagon of the 6.6.6 or 4.6.12 tilings.
- _cousin_: [[concepts/qec/ampdamp]] — The $⟦2m,2m-2,2⟧$ error-detecting code  ([arXiv:quant-ph/0402067](https://arxiv.org/abs/quant-ph/0402067)) and its relative the code with single stabilizer $XX\cdots X$  ([arXiv:quant-ph/0302006](https://arxiv.org/abs/quant-ph/0302006)) admit autonomous QEC against single AD errors.
- _cousin_: [`gauss_law`](https://errorcorrectionzoo.org/c/gauss_law) — The iceberg code can be used for robustly simulating $SU(2)$ gauge theories  ([arXiv:2511.13721](https://arxiv.org/abs/2511.13721)).

## Notes

- See description of the code in Ref. .
- The code solves  ([arXiv:1701.01828](https://arxiv.org/abs/1701.01828)) the mean king's measurement problem  ([doi:10.1103/PhysRevLett.58.1385](https://doi.org/10.1103/PhysRevLett.58.1385)).
- The code is useful for entanglement distillation  ([arXiv:2408.15936](https://arxiv.org/abs/2408.15936)).
- The code is used in a fault-tolerant implementation of the QAOA algorithm  ([arXiv:2409.12104](https://arxiv.org/abs/2409.12104)).
- The iceberg code can be used for robustly simulating $SU(2)$ gauge theories  ([arXiv:2511.13721](https://arxiv.org/abs/2511.13721)).
