---
type: concept
name: Fermion-into-qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-stabilizer
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/fermions_into_qubits
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: fermions_into_qubits
---

# Fermion-into-qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/fermions_into_qubits) (`code_id: fermions_into_qubits`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit stabilizer code encoding a logical fermionic Hilbert space into a physical space of $n$ qubits.
Such codes are primarily intended for simulating fermionic systems on quantum computers, and some of them have error-detecting, correcting, and transmuting properties.

The first fermion-into-qubit code is the Jordan-Wigner transformation code, a trivial $⟦n,n⟧$ stabilizer code encoding Majorana operators into Pauli strings of weight $O(n)$.
This is necessary to ensure that Majorana operators satisfy the proper anti-commutation relations.

Subsequent encodings consisted of stabilizer codes with $k < n$, ensuring anti-commutation through the long-range entanglement of the codestates.
This makes it possible to reduce the Pauli weight of a Majorana operator by multiplying by a stabilizer.
For example, for stabilizer constraints associated with loops of a 2D lattice, applying loop constraints to high-weight fermionic string-like operators yields operators of lower weight.

See  ([arXiv:2003.06939](https://arxiv.org/abs/2003.06939)) ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)) for comparisons of various fermion-into-qubit codes.
On the square lattice, explicit local 2D encodings with qubit-fermion ratios $2$, $1.5$, and $1.25$ are exhibited in Ref.  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).
In addition to the children of this entry, various custom encodings exist  ([arXiv:2009.11860](https://arxiv.org/abs/2009.11860), [arXiv:2212.09731](https://arxiv.org/abs/2212.09731), [arXiv:2311.07409](https://arxiv.org/abs/2311.07409), [arXiv:2302.01862](https://arxiv.org/abs/2302.01862), [doi:10.48550/arXiv.2403.17794](https://doi.org/10.48550/arXiv.2403.17794), [arXiv:2509.00147](https://arxiv.org/abs/2509.00147)) that can be tailored to the quantum simulation problem of interest.

(source: raw/error-correction-zoo.md)

## Encoders

- Any two locality-preserving fermion-into-qubit mappings in two spatial dimensions can be related by a finite-depth generalized local unitary transformation  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]] — Fermion-into-qubit codes are qubit stabilizer codes that encode a logical fermionic Hilbert space into a physical space of $n$ qubits.
- _cousin_: [[concepts/qec/twist-defect-surface]] — Treating a twist-defect surface codespace as a logical fermion encoding yields a fermion-into-qubit code  ([arXiv:2110.10280](https://arxiv.org/abs/2110.10280)).
