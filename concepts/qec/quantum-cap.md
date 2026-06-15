---
type: concept
name: $⟦n,n-2k,4⟧$ Quantum cap code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/stabilizer-over-gf4
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_cap
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_cap
---

# $⟦n,n-2k,4⟧$ Quantum cap code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_cap) (`code_id: quantum_cap`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A distance-four pure Hermitian qubit code constructed from a Hermitian self-orthogonal $[n,k]_4$ code associated with an $n$-cap in $PG(k-1,4)$.

(source: raw/error-correction-zoo.md)

## Rate

Quantum cap codes can have a high rate and include codes with parameters $⟦6,0,4⟧$ (from the hyperoval in $PG(2,4)$), $⟦12,4,4⟧$ (from the union of two hyperovals in $PG(3,4)$ on two planes meeting in an exterior line), $⟦40,30,4⟧$ (from the 40-cap in $AG(4,4)$), $⟦41,31,4⟧$ (from a 41-cap in $PG(4,4)$), $⟦126,114,4⟧$ (from the Glynn 126-cap in $PG(5,4)$), $⟦756,740,4⟧$ (from a 756-cap in $PG(7,4)$), and $⟦5040,5020,4⟧$ (from a 5040-cap in $PG(9,4)$)  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)), as well as $⟦12,2,4⟧$, $⟦20,10,4⟧$, or $⟦29,19,4⟧$  ([arXiv:0905.1059](https://arxiv.org/abs/0905.1059)).

## Relations

- _parent_: [[concepts/qec/stabilizer-over-gf4]] — A quantum cap code is a distance-four pure Hermitian qubit code constructed by identifying its underlying Hermitian self-orthogonal $[n,k]_4$ code with a particular projective cap in $PG(k-1,4)$.
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]] — Quantum cap codes can have a high rate and include codes with parameters $⟦6,0,4⟧$, $⟦12,4,4⟧$, $⟦40,30,4⟧$, $⟦41,31,4⟧$, $⟦126,114,4⟧$, $⟦756,740,4⟧$, and $⟦5040,5020,4⟧$  ([doi:10.2140/iig.2008.6.53](https://doi.org/10.2140/iig.2008.6.53)), as well as $⟦12,2,4⟧$, $⟦20,10,4⟧$, or $⟦29,19,4⟧$  ([arXiv:0905.1059](https://arxiv.org/abs/0905.1059)).
- _cousin_: [`projective`](https://errorcorrectionzoo.org/c/projective) — A quantum cap code is a distance-four pure Hermitian qubit code constructed by identifying its underlying Hermitian self-orthogonal $[n,k]_4$ code with a particular projective cap in $PG(k-1,4)$.
