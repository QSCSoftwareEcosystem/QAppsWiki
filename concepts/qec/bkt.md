---
type: concept
name: Bravyi-Kitaev transformation (BKT) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/fermions-into-qubits
- concepts/qec/jw
- concepts/qec/ternary-tree-fermion
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bkt
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bkt
---

# Bravyi-Kitaev transformation (BKT) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bkt) (`code_id: bkt`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A fermion-into-qubit encoding that maps Majorana operators into Pauli strings of weight $\lceil \log_2(n+1) \rceil$.
The code can be reformulated in terms of Fenwick trees  ([doi:10.1002/spe.4380240306](https://doi.org/10.1002/spe.4380240306)), and the Pauli-string weight can be further optimized to yield the *segmented Bravyi-Kitaev (SBK) transformation code*  ([arXiv:1701.07072](https://arxiv.org/abs/1701.07072)) (see also Ref.  ([arXiv:1904.09912](https://arxiv.org/abs/1904.09912))).

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/fermions-into-qubits]]
- _cousin_: [[concepts/qec/jw]] — The weight of a Majorana operator in the BKT (JW transformation) code scales logarithmically (linearly) with $n$, with the former demonstrating an exponential improvement  ([arXiv:1910.10746](https://arxiv.org/abs/1910.10746)).
- _cousin_: [[concepts/qec/ternary-tree-fermion]] — The ternary-tree fermion-into-qubit code improves over the BKT code by a factor of $\approx 1.58$ in the weight of encoded fermionic operators  ([arXiv:1910.10746](https://arxiv.org/abs/1910.10746)).

## Notes

- Review on the BKT  ([doi:10.1002/qua.24969](https://doi.org/10.1002/qua.24969)).
