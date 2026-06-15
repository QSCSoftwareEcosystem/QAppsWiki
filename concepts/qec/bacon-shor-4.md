---
type: concept
name: $⟦4,1,1,2⟧$ Four-qubit subsystem code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bacon-shor
- concepts/qec/bravyi-bacon-shor-6
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stab-4-2-2
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bacon_shor_4
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bacon_shor_4
---

# $⟦4,1,1,2⟧$ Four-qubit subsystem code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bacon_shor_4) (`code_id: bacon_shor_4`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Error-detecting four-qubit subsystem stabilizer code encoding one logical qubit and one gauge qubit.

The $⟦4,1,1,2⟧$ code can be obtained by picking one of the logical qubits of the $⟦4,2,2⟧$ four-qubit code to be a gauge qubit; e.g., see Ref. .
One particular gauge configuration has gauge group $\mathsf{G}$ with gauge generators (excluding phases)
\begin{align}
\begin{array}{cccc}
  X & X & I & I \\
  I & I & X & X \\
  Z & I & Z & I \\
  I & Z & I & Z
\end{array}~.
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

The code detects arbitrary single-qubit errors.
An equal-weight sum of its gauge generators has energy separation $2(\sqrt{2}-1)$, so encoding into the corresponding ground subspace suppresses arbitrary single-qubit errors using non-commuting two-local Hamiltonian terms  ([arXiv:1511.01997](https://arxiv.org/abs/1511.01997)).

## Relations

- _parent_: [[concepts/qec/bacon-shor]] — The four-qubit subsystem code is the shortest error-detecting Bacon-Shor code.
- _cousin_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _cousin_: [[concepts/qec/stab-4-2-2]] — The $⟦4,1,1,2⟧$ code can be obtained by picking one of the logical qubits of the $⟦4,2,2⟧$ four-qubit code to be a gauge qubit; e.g., see Ref. . One particular gauge configuration has gauge operators $\{XXII,IIXX,ZIZI,IZIZ\}$.
- _cousin_: [[concepts/qec/bravyi-bacon-shor-6]] — Both the $⟦6,2,3,2⟧$ BBS code and the four-qubit subsystem code can be used to suppress errors in adiabatic quantum computation  ([arXiv:1511.01997](https://arxiv.org/abs/1511.01997)).
