---
type: concept
name: Galois-qudit GRS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-ag
- concepts/qec/quantum-concatenated
- concepts/qec/quantum-mds
- concepts/qec/random-stabilizer
- concepts/qec/stabilizer-over-gfqsq
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/galois_grs
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: galois_grs
---

# Galois-qudit GRS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/galois_grs) (`code_id: galois_grs`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A true $q$-Galois-qudit stabilizer code constructed from GRS codes via either the Hermitian construction  ([arXiv:1311.3009](https://arxiv.org/abs/1311.3009), [doi:10.1142/S0219749919500060](https://doi.org/10.1142/S0219749919500060), [doi:10.1109/TIT.2010.2054174](https://doi.org/10.1109/TIT.2010.2054174)) or the Galois-qudit CSS construction  ([arXiv:quant-ph/9906129](https://arxiv.org/abs/quant-ph/9906129), [arXiv:0812.4514](https://arxiv.org/abs/0812.4514)).

(source: raw/error-correction-zoo.md)

## Rate

Concatenations of quantum GRS codes and random stabilizer codes can achieve the quantum GV bound  ([arXiv:1004.1127](https://arxiv.org/abs/1004.1127)).

## Relations

- _parent_: [[concepts/qec/quantum-ag]] — Galois-qudit GRS codes can be constructed via the CSS construction or the Hermitian construction from GRS codes, which are evaluation AG codes.
- _cousin_: [`generalized_reed_solomon`](https://errorcorrectionzoo.org/c/generalized_reed_solomon) — Galois-qudit GRS codes are quantum analogues of generalized RS codes.
- _cousin_: [[concepts/qec/quantum-mds]] — Some Galois-qudit GRS codes are quantum MDS  ([arXiv:1311.3009](https://arxiv.org/abs/1311.3009)).
- _cousin_: [[concepts/qec/stabilizer-over-gfqsq]] — Galois-qudit GRS codes can be constructed via the CSS construction or the Hermitian construction.
- _cousin_: [[concepts/qec/quantum-concatenated]] — Concatenations of Galois-qudit GRS codes and random stabilizer codes can achieve the quantum GV bound  ([arXiv:1004.1127](https://arxiv.org/abs/1004.1127)).
- _cousin_: [[concepts/qec/random-stabilizer]] — Concatenations of Galois-qudit GRS codes and random stabilizer codes can achieve the quantum GV bound  ([arXiv:1004.1127](https://arxiv.org/abs/1004.1127)).
