---
type: concept
name: Walker-Wang model code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/enriched-walker-wang
- concepts/qec/string-net
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/walker_wang
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: walker_wang
---

# Walker-Wang model code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/walker_wang) (`code_id: walker_wang`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A non-stabilizer commuting-projector 3D topological code defined by a unitary braided fusion category $ \mathcal{C} $ (also known as a unitary premodular category).
The code is defined on a cubic lattice that is resolved to be trivalent, with a qudit of dimension $ |\mathcal{C}| $ located at each edge.
The codespace is the ground-state subspace of the Walker-Wang model Hamiltonian  ([arXiv:1104.2632](https://arxiv.org/abs/1104.2632)) and realizes the Crane-Yetter model  ([arXiv:hep-th/9301062](https://arxiv.org/abs/hep-th/9301062), [arXiv:hep-th/9309063](https://arxiv.org/abs/hep-th/9309063), [arXiv:hep-th/9409167](https://arxiv.org/abs/hep-th/9409167)).
A single-state version of the code provides a resource state for MBQC  ([arXiv:2011.04693](https://arxiv.org/abs/2011.04693)).

(source: raw/error-correction-zoo.md)

## Protection

Codespace dimensions (i.e., ground-state degeneracy) has been calculated for various boundary conditions  ([arXiv:1208.5128](https://arxiv.org/abs/1208.5128)).

## Encoders

- For modular chiral anyon theories, a unitary encoder is conjectured to not be implementable in constant depth because it is believed to be an example of a *quantum cellular automaton* (QCA) (i.e., causal or locality-preserving automorphism) that cannot be locally implemented  ([arXiv:1812.01625](https://arxiv.org/abs/1812.01625), [arXiv:2205.09141](https://arxiv.org/abs/2205.09141)). States of modular gapped theories can be initialized in constant depth  ([arXiv:2208.03397](https://arxiv.org/abs/2208.03397)).

## Relations

- _parent_: [[concepts/qec/enriched-walker-wang]] — $G$-enriched Walker-Wang models reduce to Walker-Wang models for trivial $G$  ([arXiv:1606.07144](https://arxiv.org/abs/1606.07144)).
- _cousin_: [[concepts/qec/string-net]] — The Walker-Wang model is a generalization of the 3D version of the Levin-Wen model  ([arXiv:cond-mat/0404617](https://arxiv.org/abs/cond-mat/0404617)), which realizes gauge theories coupled to bosons and fermions.
