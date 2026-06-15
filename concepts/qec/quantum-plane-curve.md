---
type: concept
name: Quantum plane-curve code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/quantum-ag
- concepts/qec/small-distance-quantum
- concepts/qec/stabilizer-over-gfqsq
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_plane_curve
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_plane_curve
---

# Quantum plane-curve code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_plane_curve) (`code_id: quantum_plane_curve`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Quantum AG code constructed from plane-curve codes via the Galois-qudit Hermitian construction.
Code parameters are $⟦q^3,q^3+q^2-3q-2r,r+2q-q^2⟧_q$, where $r$ is an integer satisfying $q^2 - 2 \leq r \leq q^2 + q - 3$, and where the underlying plane curve is $y^q + y = x^{q-1}$.

(source: raw/error-correction-zoo.md)

## Relations

- _parent_: [[concepts/qec/stabilizer-over-gfqsq]]
- _parent_: [[concepts/qec/quantum-ag]]
- _cousin_: [`plane_curve`](https://errorcorrectionzoo.org/c/plane_curve) — Quantum plane-curve codes are quantum analogues of plane-curve evaluation codes.
- _cousin_: [[concepts/qec/small-distance-quantum]] — The quantum plane-curve code for the Hermitian curve $y^3 + y = x^4$ is a $⟦27,13,4⟧_3$ qutrit code.
