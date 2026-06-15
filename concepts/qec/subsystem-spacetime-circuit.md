---
type: concept
name: Subsystem spacetime circuit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-subsystem-stabilizer
- concepts/qec/spacetime-circuit
- concepts/qec/sparse-subsystem
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/subsystem_spacetime_circuit
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: subsystem_spacetime_circuit
---

# Subsystem spacetime circuit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/subsystem_spacetime_circuit) (`code_id: subsystem_spacetime_circuit`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Subsystem stabilizer code obtained from a spacetime circuit code by gauging out logical operators that correspond to circuit faults with trivial effect  ([arXiv:2304.05943](https://arxiv.org/abs/2304.05943)).
In the original circuit-to-code construction, each circuit element is replaced by low-weight gauge generators enforcing its input-output relations, yielding subsystem codes from restricted Clifford postselection circuits  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334)).

An $⟦n,k,d⟧$ stabilizer code can be mapped into a sparse subsystem code with the same $k$ and $d$ as follows.
One can take the fault-tolerant syndrome extraction circuit associated with the stabilizer code, construct its spacetime circuit code, and then gauge out qubits corresponding to trivial faults.
The subsystem code can be made geometrically local at the cost of more ancilla qubits  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334)).

(source: raw/error-correction-zoo.md)

## Protection

When derived from a fault-tolerant error-detecting circuit for an $⟦n,k,d⟧$ stabilizer code, the resulting subsystem spacetime circuit code has parameters $⟦O(|V|),k,d⟧$, so the base-code distance is preserved  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334)).

## Rate

The spacetime circuit code construction is used to show the existence of spatially local subsystem codes that nearly saturate the subsystem BT bound  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334)).

## Fault tolerance

- Fault-tolerant measurement gadget that is a modification based on the DiVincenzo-Shor cat-state method  ([arXiv:quant-ph/9605011](https://arxiv.org/abs/quant-ph/9605011), [arXiv:quant-ph/9605031](https://arxiv.org/abs/quant-ph/9605031)).
- The original construction uses $|+\rangle$-state vertex qubits together with expander-graph parity checks to obtain $O(w)$-size postselection gadgets for measuring weight-$w$ stabilizers, with gates acting on at most ten wires  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334)).

## Relations

- _parent_: [[concepts/qec/qubit-subsystem-stabilizer]]
- _parent_: [[concepts/qec/sparse-subsystem]]
- _cousin_: [[concepts/qec/spacetime-circuit]] — Spacetime circuit codes can yield subsystem spacetime circuit codes by gauging out a subgroup of the logical Pauli group which causes trivial faults in the corresponding Clifford circuit. This construction is used to show the existence of geometrically local subsystem codes that nearly saturate the subsystem BT bound  ([arXiv:1411.3334](https://arxiv.org/abs/1411.3334)).
