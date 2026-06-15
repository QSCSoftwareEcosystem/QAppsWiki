---
type: concept
name: Quantum synchronizable code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-stabilizer
- concepts/qec/qubit-stabilizer-oaqecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_synchronizable
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_synchronizable
---

# Quantum synchronizable code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_synchronizable) (`code_id: quantum_synchronizable`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit stabilizer code designed to protect against synchronization errors (a.k.a. misalignment), which are errors that misalign the code block in a larger block by one or more locations. 

In such a setting, the qubits are arranged in a line and embedded into a larger block that represents a stream of information coming into the receiver.
The receiver may not properly identify the first qubit in the desired code block, leading to a misalignment of the block.
A quantum synchronizable code is denoted by $(a_l,a_r)-⟦n+a_l+a_r,k⟧$, correcting misalignment by up to $a_l$ ($a_r$) qubits to the left (right).

The initial construction of quantum synchronizable codes was based on the CSS construction  ([arXiv:1206.0260](https://arxiv.org/abs/1206.0260)), but later work extended it to non-CSS stabilizer codes  ([arXiv:2409.11312](https://arxiv.org/abs/2409.11312)).

(source: raw/error-correction-zoo.md)

## Protection

In the original CSS construction based on cyclic codes $C \subset D$ with parameters $[n,k_1,d_1]$ and $[n,k_2,d_2]$, one obtains an $(a_l,a_r)-⟦n+a_l+a_r,2k_1-n⟧$ code whenever $a_l+a_r<k_2-k_1$, correcting at least $\lfloor (d_1-1)/2\rfloor$ phase errors and $\lfloor (d_2-1)/2\rfloor$ bit errors  ([arXiv:1206.0260](https://arxiv.org/abs/1206.0260)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]]
- _cousin_: [`binary_cyclic`](https://errorcorrectionzoo.org/c/binary_cyclic) — The original construction of quantum synchronizable codes is based on pairs of binary cyclic codes satisfying $C^\perp \subseteq C \subset D$  ([arXiv:1206.0260](https://arxiv.org/abs/1206.0260)).
- _cousin_: [`bch`](https://errorcorrectionzoo.org/c/bch) — BCH codes can be used to construct quantum synchronizable codes via the CSS construction  ([arXiv:1206.0260](https://arxiv.org/abs/1206.0260)).
- _cousin_: [`binary_quad_residue`](https://errorcorrectionzoo.org/c/binary_quad_residue) — Binary QR codes can be used to construct quantum synchronizable codes via the CSS construction  ([arXiv:1403.6192](https://arxiv.org/abs/1403.6192)).
- _cousin_: [[concepts/qec/qubit-stabilizer-oaqecc]] — Quantum synchronizable versions of qubit subsystem codes, hybrid codes, and OA qubit stabilizer codes have been constructed  ([arXiv:2409.11312](https://arxiv.org/abs/2409.11312)).
