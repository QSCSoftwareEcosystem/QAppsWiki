---
type: concept
name: $D$-dimensional twisted toric code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/higher-dimensional-surface
- concepts/qec/multisector-hypergraph
- concepts/qec/qldpc
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/higher_dimensional_toric
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: higher_dimensional_toric
---

# $D$-dimensional twisted toric code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/higher_dimensional_toric) (`code_id: higher_dimensional_toric`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Extension of the Kitaev toric code to higher-dimensional lattices with regular or shifted (a.k.a. twisted) boundary conditions.
Such boundary conditions yield qubit geometries that are tori $\mathbb{R}^D/\Lambda$, where $\Lambda$ is an arbitrary $D$-dimensional lattice.
Picking a hypercubic lattice yields the ordinary $D$-dimensional toric code.

It is conjectured that appropriate twisted boundary conditions yield multi-dimensional toric code families with sublinear distance scaling of $n^{1-\epsilon}$ for any $\epsilon>0$ and logarithmic-weight stabilizer generators  ([arXiv:1608.05089](https://arxiv.org/abs/1608.05089), [arXiv:2505.10403](https://arxiv.org/abs/2505.10403)).
At finite $n$, twisting boundary conditions can reduce qubit overhead for a fixed distance  ([arXiv:2505.10403](https://arxiv.org/abs/2505.10403)).

(source: raw/error-correction-zoo.md)

## Protection

In two dimensions, different choices for the periodic boundary conditions yield higher-rate codes with parameters $⟦L^2+1,2,L⟧$ for odd $L$  ([arXiv:quant-ph/0605094](https://arxiv.org/abs/quant-ph/0605094)), and $⟦L^2,2,L⟧$ for even $L$ .
Cyclic analogs of toric codes with parameters $⟦t^2+(t+1)^2,1,2t+1⟧$ are constructed in  ([arXiv:1108.5490](https://arxiv.org/abs/1108.5490)).
Some higher-dimensional toric codes protect against burst errors  ([arXiv:2205.13582](https://arxiv.org/abs/2205.13582)).

## Encoders

- Entangled logical states can be prepared by single-shot techniques  ([arXiv:2505.10403](https://arxiv.org/abs/2505.10403)) for twisted toric codes.

## General gates

- Higher-dimensional toric codes can admit a cup product structure and can thus have logical gates in the \term{Clifford hierarchy} implemented by constant-depth Clifford circuits  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).

## Relations

- _parent_: [[concepts/qec/higher-dimensional-surface]]
- _parent_: [[concepts/qec/translationally-invariant-stabilizer]]
- _cousin_: [[concepts/qec/qldpc]] — It is conjectured that appropriate twisted boundary conditions yield multi-dimensional toric code families with sublinear distance scaling of $N^{1-\epsilon}$ for any $\epsilon>0$ and logarithmic-weight stabilizer generators  ([arXiv:1608.05089](https://arxiv.org/abs/1608.05089)). Assuming this conjecture, Hastings' weight-reduction construction yields QLDPC families with distance $\Theta^*(N^{1-\epsilon})$ for any $\epsilon>0$  ([arXiv:1611.03790](https://arxiv.org/abs/1611.03790)).
- _cousin_: [[concepts/qec/multisector-hypergraph]] — The non-twisted $D$-dimensional planar and toric codes on a hypercubic lattice can be obtained from a hypergraph product of $D$ repetition codes  ([arXiv:1810.01519](https://arxiv.org/abs/1810.01519)).
