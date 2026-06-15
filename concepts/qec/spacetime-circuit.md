---
type: concept
name: Spacetime circuit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/dynamic-gen
- concepts/qec/qldpc
- concepts/qec/qubit-subsystem-stabilizer
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/spacetime_circuit
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: spacetime_circuit
---

# Spacetime circuit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/spacetime_circuit) (`code_id: spacetime_circuit`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit stabilizer code constructed from a Clifford circuit, i.e., a circuit made up of Clifford gates and Pauli measurements, in order to detect and correct circuit faults.
The code utilizes redundancy in the measurement outcomes of a circuit to correct circuit faults, which correspond to Pauli errors of the code.

The structure of the Clifford circuit yields correlations between the circuit's possible measurement outcomes.
The set of outcomes can be made into a classical binary linear code called the *outcome code*  ([arXiv:2304.05943](https://arxiv.org/abs/2304.05943)).
The spacetime circuit code is defined such that its error syndromes can be backpropagated to obtain the parity checks of the outcome code.
In other words, both codes have the same set of parity check outcomes.

More technically, given an $[m,k]$ outcome code associated with an $n$-qubit circuit of depth $\Delta$ with $m$ measurements and $2^k$ outcomes, the corresponding spacetime circuit code is an $⟦ n (\Delta + 1), n (\Delta + 1) - (m - k) ⟧$ code  ([arXiv:2304.05943](https://arxiv.org/abs/2304.05943)).

The spacetime circuit code is the stabilizer-code counterpart of earlier subsystem constructions  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334), [arXiv:2210.15844](https://arxiv.org/abs/2210.15844)), which dealt with restricted families of Clifford circuits.
A more general construction includes circuits with intermediate and multi-qubit measurements  ([arXiv:2304.05943](https://arxiv.org/abs/2304.05943)).

Many features of the spacetime circuit formalism can be understood through ZX calculus  ([arXiv:2407.08566](https://arxiv.org/abs/2407.08566)).
Two circuits are *fault-equivalent* if all undetectable faults on one circuit have a corresponding fault on the other  ([arXiv:2506.17181](https://arxiv.org/abs/2506.17181)).

(source: raw/error-correction-zoo.md)

## Decoders

- A most-likely error decoder for the spacetime code can be converted into a most-likely fault decoder for the underlying circuit  ([arXiv:2304.05943](https://arxiv.org/abs/2304.05943)).
- Efficient decoders can be constructed for some circuits, especially when the resulting outcome and spacetime codes are LDPC  ([arXiv:2304.05943](https://arxiv.org/abs/2304.05943)).

## Fault tolerance

- The outcome-code distance is a lower bound on the circuit-level distance, and the bound need not be tight because some undetectable fault configurations are logically trivial. The circuit-level distance corresponds to the minimum-weight outcome codeword that is not in the kernel of the logical effect matrix  ([arXiv:2401.12017](https://arxiv.org/abs/2401.12017)).

## Relations

- _parent_: [[concepts/qec/qldpc]] — Spacetime circuit codes are useful for constructing fault-tolerant syndrome extraction circuits for qubit QLDPC codes. General spacetime circuit codes can be sparsified to yield QLDPC spacetime circuit codes  ([arXiv:2304.05943](https://arxiv.org/abs/2304.05943)).
- _parent_: [[concepts/qec/dynamic-gen]]
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — The set of measurement outcomes of a Clifford circuit can be made into a classical binary linear code.
Error syndromes of the spacetime circuit code can be used to obtain the parity checks of the outcome code.
- _cousin_: [[concepts/qec/surface]] — Stabilizer generators of a spacetime code are called *detectors* in Refs.  ([arXiv:2103.02202](https://arxiv.org/abs/2103.02202), [arXiv:2304.05943](https://arxiv.org/abs/2304.05943)).
- _cousin_: [[concepts/qec/qubit-subsystem-stabilizer]] — Spacetime circuit codes can be upgraded to subsystem codes by gauging out a subgroup of the logical Pauli group which causes trivial faults in the corresponding Clifford circuit.
- _cousin_: [`ldpc`](https://errorcorrectionzoo.org/c/ldpc) — There is an equivalence between Clifford circuits and LDPC codes with bit-check symmetry  ([arXiv:2403.10268](https://arxiv.org/abs/2403.10268)).

## Notes

- See  ([arXiv:2502.16408](https://arxiv.org/abs/2502.16408)) for a brief overview of spacetime circuits.
