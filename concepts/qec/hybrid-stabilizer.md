---
type: concept
name: Hybrid stabilizer code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/hybrid-qubits-into-qubits
- concepts/qec/iceberg
- concepts/qec/non-stabilizer
- concepts/qec/qubit-stabilizer
- concepts/qec/qubit-stabilizer-oaqecc
- concepts/qec/qubit-subsystem-stabilizer
- concepts/qec/shor-nine
- concepts/qec/stab-4-2-2
- concepts/qec/subsystem-quantum-parity
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hybrid_stabilizer
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hybrid_stabilizer
---

# Hybrid stabilizer code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hybrid_stabilizer) (`code_id: hybrid_stabilizer`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A qubit stabilizer code which stores both quantum and classical information.
Usually denoted as $⟦n,k:c⟧$ or $⟦n,k:c,d⟧$, where $k$ ($c$) is the number of encoded qubits (classical bits), and where $d$ is the distance.

The algebraic structure of a hybrid stabilizer code is the same as that of a USt code whose cosets are indexed by a linear binary code:
both codes utilize codewords of an inner $⟦n,k⟧$ qubit stabilizer code $\mathsf{C}$ and its cosets $t \mathsf{C}$, where the $2^c$ Pauli strings $t$ correspond to the outer $[n,c]$ linear binary code.
However, the hybrid stabilizer code does not utilize superpositions of codewords of $t \mathsf{C}$ and $t^{\prime} \mathsf{C}$ for $t \neq t^{\prime}$ since the different coset blocks correspond to classical codewords.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/hybrid-qubits-into-qubits]] — An $⟦n,k:c,d⟧$ hybrid stabilizer code is an $((n,2^k:2^c,d))$ hybrid qubit code.
- _parent_: [[concepts/qec/qubit-stabilizer-oaqecc]] — An OA stabilizer code which has no gauge qubits but has a block structure that corresponds to a linear binary code is a hybrid stabilizer code.
- _cousin_: [[concepts/qec/qubit-stabilizer]] — A hybrid stabilizer code storing no classical information reduces to a qubit stabilizer code.
Conversely, any qubit stabilizer code can be converted into a hybrid stabilizer code by using some of its qubits to store only classical information  ([arXiv:0802.2414](https://arxiv.org/abs/0802.2414)).
- _cousin_: [[concepts/qec/non-stabilizer]] — The algebraic structure of a hybrid stabilizer code is the same as that of a USt code whose cosets are indexed by a linear binary code  ([arXiv:0802.2414](https://arxiv.org/abs/0802.2414)).
- _cousin_: [[concepts/qec/shor-nine]] — The Shor code can be modified into a degenerate $⟦9,1:3,3⟧$ hybrid stabilizer code that still corrects arbitrary single-qubit errors  ([arXiv:0802.2414](https://arxiv.org/abs/0802.2414)).
- _cousin_: [[concepts/qec/iceberg]] — The $⟦2m+1,2m+2:1,2⟧$ hybrid stabilizer code  ([arXiv:1911.12260](https://arxiv.org/abs/1911.12260)) (extendable to modular qudits  ([arXiv:2002.11075](https://arxiv.org/abs/2002.11075))) is closely related to the $⟦2m,2m-2,2⟧$ error-detecting code.
- _cousin_: [[concepts/qec/stab-4-2-2]] — The $⟦4,2,2⟧$ codewords can be modified by signs to yield a $⟦4,1:1,2⟧$ hybrid stabilizer code  ([arXiv:1806.03702](https://arxiv.org/abs/1806.03702)).
- _cousin_: [[concepts/qec/qubit-subsystem-stabilizer]] — Hybrid stabilizer codes can be constructed from subsystem qubit stabilizer codes by using the gauge qubits of the latter to store classical information  ([arXiv:2012.05896](https://arxiv.org/abs/2012.05896)).
- _cousin_: [[concepts/qec/subsystem-quantum-parity]] — Hybrid stabilizer codes can be constructed from SHP codes by using the gauge qubits of the latter to store classical information  ([arXiv:2012.05896](https://arxiv.org/abs/2012.05896)).
