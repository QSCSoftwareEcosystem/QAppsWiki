---
type: concept
name: Mixed oscillator code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- LCA code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/group-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hybrid_qudit_oscillator
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hybrid_qudit_oscillator
---

# Mixed oscillator code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hybrid_qudit_oscillator) (`code_id: hybrid_qudit_oscillator`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes a logical Hilbert space into some number of modular qudits, some number of rotors, and a nonzero number of oscillators, i.e., the Hilbert space of $L^2$-normalizable functions on a locally compact Abelian (LCA) group.
In photonic systems, photonic states of multiple degrees of freedom of a photon (e.g., frequency, amplitude, and polarization) are called *hyper-entangled states*  ([doi:10.1080/09500349708231877](https://doi.org/10.1080/09500349708231877)).

(source: raw/error-correction-zoo.md)

## General gates

- Symplectic transformations (i.e., transformations that preserve the qudit Pauli and oscillator displacement group structure) are tensor products of qudit Clifford and oscillator Gaussian operations, and there are no entangling symplectic operations  ([arXiv:0806.4064](https://arxiv.org/abs/0806.4064), [arXiv:1611.09274](https://arxiv.org/abs/1611.09274), [arXiv:2508.04819](https://arxiv.org/abs/2508.04819)).
- Adding a conditional oscillator-qudit displacement makes the symplectic gate set universal  ([arXiv:2509.18854](https://arxiv.org/abs/2509.18854)).

## Relations

- _parent_: [[concepts/qec/group-quantum]] — Group quantum codes whose physical spaces are constructed using some number of modular qudits, some number of rotors, and a nonzero number of oscillators, which together constitute a general locally compact Abelian (LCA) group, are mixed oscillator codes.
- _cousin_: [`mixed`](https://errorcorrectionzoo.org/c/mixed) — Mixed oscillator codes are examples of quantum analogues of mixed codes.

## Notes

- See reviews  ([arXiv:1409.3719](https://arxiv.org/abs/1409.3719), [doi:10.1002/9783527635283](https://doi.org/10.1002/9783527635283), [arXiv:2407.10381](https://arxiv.org/abs/2407.10381)) for introductions to mixed oscillator platforms.
