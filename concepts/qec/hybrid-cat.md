---
type: concept
name: Hybrid cat code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/cat
- concepts/qec/hybrid-qudit-oscillator
- concepts/qec/oscillators-concatenated
- concepts/qec/rbh
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hybrid_cat
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hybrid_cat
---

# Hybrid cat code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hybrid_cat) (`code_id: hybrid_cat`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A mixed oscillator code admitting codewords that are tensor products of a single-qubit (e.g., photon polarization) state with either a cat state or a coherent state.
 
Codewords of the coherent-state version  ([arXiv:1112.0825](https://arxiv.org/abs/1112.0825)) are $|\alpha\rangle|+\rangle$ and $|-\alpha\rangle|-\rangle$, i.e., hyper-entangled states of the occupation-number and polarization degrees of freedom of a photon.
Codewords of the cat-state version  ([arXiv:1712.10206](https://arxiv.org/abs/1712.10206), [arXiv:2401.00450](https://arxiv.org/abs/2401.00450)) are proportional to $(\left|\alpha\right\rangle +\left|-\alpha\right\rangle )|+\rangle$ and $(\left|i\alpha\right\rangle -\left|-i\alpha\right\rangle )|-\rangle$.

(source: raw/error-correction-zoo.md)

## Fault tolerance

- Photonic architecture based on concatenation with RBH codes  ([arXiv:2401.00450](https://arxiv.org/abs/2401.00450)).

## Relations

- _parent_: [[concepts/qec/hybrid-qudit-oscillator]]
- _cousin_: [[concepts/qec/cat]] — Hybrid cat codewords consist of a bosonic mode in either coherent or cat states.
- _cousin_: [[concepts/qec/rbh]] — Hybrid cat codes can be concatenated with RBH codes  ([arXiv:2401.00450](https://arxiv.org/abs/2401.00450)).
- _cousin_: [[concepts/qec/oscillators-concatenated]] — Hybrid cat codes can be concatenated with RBH codes  ([arXiv:2401.00450](https://arxiv.org/abs/2401.00450)).

## Notes

- See reviews  ([arXiv:1409.3719](https://arxiv.org/abs/1409.3719), [arXiv:2407.10381](https://arxiv.org/abs/2407.10381)) for introductions to mixed oscillator platforms.
