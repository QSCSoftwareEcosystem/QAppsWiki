---
type: concept
name: Ball-Verstraete-Cirac (BVC) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Verstraete-Cirac code
- Auxiliary fermion code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-bosonization
- concepts/qec/qetc
- concepts/qec/rotated-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bvc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bvc
---

# Ball-Verstraete-Cirac (BVC) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bvc) (`code_id: bvc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A 2D fermion-into-qubit encoding that builds upon the JW transformation by eliminating the weight-$O(n)$ non-local $Z$-type string at the expense of introducing an auxiliary qubit per site and local gauge constraints.
See  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)) for details.

(source: raw/error-correction-zoo.md)

## Protection

Some single-qubit errors are detectable, with the rest inducing low-weight fermionic dephasing noise  ([arXiv:2003.07125](https://arxiv.org/abs/2003.07125)).

## Relations

- _parent_: [[concepts/qec/2d-bosonization]] — The BVC code can be obtained from exact 2D bosonization by finite-depth generalized local unitaries after regrouping Majorana modes  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)).
- _parent_: [[concepts/qec/qetc]] — The BVC code transmutes all single-qubit errors  ([arXiv:2310.10278](https://arxiv.org/abs/2310.10278)).
- _cousin_: [[concepts/qec/rotated-surface]] — An appropriately chosen stabilizer generator set for the BVC code contains the stabilizers of the rotated surface code .
