---
type: concept
name: Symmetry-protected topological (SPT) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/double-semion-string-net
- concepts/qec/surface
- concepts/qec/topological
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/spt
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: spt
---

# Symmetry-protected topological (SPT) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/spt) (`code_id: spt`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A code whose codewords form the ground-state or low-energy subspace of a code Hamiltonian realizing symmetry-protected topological (SPT) order.

(source: raw/error-correction-zoo.md)

## Protection

SPT codes typically do not offer protection against generic errors, but can protect against noise that respects the underlying symmetry.
One-form symmetries can be detected using tools from QEC  ([arXiv:2502.17572](https://arxiv.org/abs/2502.17572)).

## Encoders

- Conjectured QCA encoder for SPTs defined by Stiefel-Whitney classes in arbitrary dimensions  ([arXiv:2407.07951](https://arxiv.org/abs/2407.07951)).

## General gates

- There is a relation between the \term{Clifford hierarchy} and group cohomology  ([arXiv:1509.03626](https://arxiv.org/abs/1509.03626)) (with the latter being useful for classifying SPTs).

## Relations

- _parent_: [[concepts/qec/topological]] — SPT codes realize symmetry-protected topological phases.
- _cousin_: [`bits_into_bits`](https://errorcorrectionzoo.org/c/bits_into_bits) — SPT orders may be used for encoding classical information  ([arXiv:1407.3413](https://arxiv.org/abs/1407.3413)).
- _cousin_: [[concepts/qec/surface]] — Gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) the symmetry of a trivial 2D bosonic $\mathbb{Z}_2$ Ising SPT yields the surface-code phase  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120)).
- _cousin_: [[concepts/qec/double-semion-string-net]] — Gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) the symmetry of a nontrivial 2D bosonic $\mathbb{Z}_2$ Ising SPT yields the doubled-semion phase, with semionic $\pi$-flux excitations  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120)).

## Notes

- Review on generalized (i.e., non-tensor-product) symmetries  ([arXiv:2204.03045](https://arxiv.org/abs/2204.03045)).
