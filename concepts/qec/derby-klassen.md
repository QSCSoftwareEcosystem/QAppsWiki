---
type: concept
name: Derby-Klassen (DK) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Compact encoding
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-bosonization
- concepts/qec/2d-color
- concepts/qec/qetc
- concepts/qec/xzzx
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/derby_klassen
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: derby_klassen
---

# Derby-Klassen (DK) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/derby_klassen) (`code_id: derby_klassen`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A fermion-into-qubit code defined on regular tilings with maximum degree 4 whose stabilizers are associated with loops in the tiling.
The code outperforms several other encodings in terms of encoding rate  ([arXiv:2003.06939](https://arxiv.org/abs/2003.06939)).
It has been extended for models with several modes per site  ([arXiv:2205.15256](https://arxiv.org/abs/2205.15256)).

(source: raw/error-correction-zoo.md)

## Protection

Some single-qubit errors are detectable, with the rest inducing low-weight fermionic dephasing noise  ([arXiv:2003.07125](https://arxiv.org/abs/2003.07125)).

## Relations

- _parent_: [[concepts/qec/2d-bosonization]] — On the square lattice, the DK code is the $r=1.5$ exact-bosonization construction after finite-depth generalized local unitaries and re-pairing of Majorana modes  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).
- _parent_: [[concepts/qec/qetc]] — The DK code transmutes all single-qubit errors  ([arXiv:2310.10278](https://arxiv.org/abs/2310.10278)).
- _cousin_: [[concepts/qec/xzzx]] — The DK code encodes fermions into excitations of the Wen plaquette model  ([arXiv:2009.11860](https://arxiv.org/abs/2009.11860)).
- _cousin_: [[concepts/qec/2d-color]] — The DK code on several tilings resembles the 2D color code with some vertex qubits removed .
