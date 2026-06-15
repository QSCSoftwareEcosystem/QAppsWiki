---
type: concept
name: Majorana color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/2d-color
- concepts/qec/2d-stabilizer
- concepts/qec/majorana-stab
- concepts/qec/majorana-surface
- concepts/qec/qldpc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/majorana_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: majorana_color
---

# Majorana color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/majorana_color) (`code_id: majorana_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A fermionic analogue of a 2D color code.

In the original construction  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)), Majorana modes occupy the vertices of a trivalent graph embedded on a cylinder, each face operator is the product of the Majoranas around an even-length face, and the graph is only locally $3$-colorable.
The code encodes one qubit whose two odd logical operators live on the opposite cylinder boundaries, while an even logical operator is supported on a string connecting the boundaries.

Later hardware-oriented Majorana color-code constructions realize related codes by concatenating Majorana surface codes with small Majorana fermion codes  ([arXiv:1703.00612](https://arxiv.org/abs/1703.00612), [arXiv:1704.01589](https://arxiv.org/abs/1704.01589), [arXiv:1708.05012](https://arxiv.org/abs/1708.05012), [arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
Equivalently, they are multiple Majorana-surface-code layers whose stacked building blocks are replaced by an outer $⟦n_f,k,d_m⟧_{f}$ Majorana code; hexon, octon, $⟦8,3,4⟧_{f}$, and $⟦10,4,4⟧_{f}$ outer codes give concrete order-2, -3, and -4 examples  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

(source: raw/error-correction-zoo.md)

## Protection

For the original cylindrical family with circumference $R$ and length $L$, the code distance scales as $d=\Omega( \min(R,L) )$, while the minimum diameter of an even logical operator obeys $l_{\rm even}=\Omega(L)$  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)).
The code therefore interpolates between Kitaev-chain-like protection by fermion-parity superselection ($R=O(1)$, $L\gg 1$) and distance-based protection when both linear dimensions are macroscopic.

## Rate

Concatenating a 4.8.8 Majorana surface code with an outer $⟦n_f,k,d_m⟧_{f}$ code yields a fermionic mode overhead of $\frac{2n_f}{k d_m^2} d^2$ per logical qubit of distance $d$  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

## General gates

- Color-to-surface-code lattice surgery  ([arXiv:1708.05012](https://arxiv.org/abs/1708.05012)).
- Logical tetrons and hexons can be encoded in Majorana color codes and manipulated by ordinary, twist-based, or surface-to-color-code lattice surgery  ([arXiv:1708.05012](https://arxiv.org/abs/1708.05012), [arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).

## Fault tolerance

- Ordinary and twist-based lattice surgery can be made fault tolerant, and surface-to-color-code surgery reduces ancilla-measurement weight for the 16-Majorana-stabilizer families  ([arXiv:1801.08143](https://arxiv.org/abs/1801.08143)) (see also  ([arXiv:2211.11777](https://arxiv.org/abs/2211.11777))).

## Relations

- _parent_: [[concepts/qec/majorana-stab]]
- _parent_: [[concepts/qec/qldpc]] — The Majorana color code is a 2D qubit stabilizer code with respect to the Majorana operator basis.
- _parent_: [[concepts/qec/2d-stabilizer]] — The Majorana color code is a 2D qubit stabilizer code with respect to the Majorana operator basis.
- _cousin_: [[concepts/qec/2d-color]] — The original Majorana color code is a fermionic analogue of a 2D color code in which one Majorana face operator doubles to matching $X$- and $Z$-type face checks, but the underlying cylinder graph need only be locally $3$-colorable and can support odd boundary logical operators  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)). Later realizations stack Majorana surface-code layers and replace stacked building blocks with small Majorana fermion codes  ([arXiv:1703.00612](https://arxiv.org/abs/1703.00612), [arXiv:1704.01589](https://arxiv.org/abs/1704.01589), [arXiv:1708.05012](https://arxiv.org/abs/1708.05012), [arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
- _cousin_: [[concepts/qec/majorana-surface]] — The original Majorana color code is a fermionic analogue of a 2D color code in which one Majorana face operator doubles to matching $X$- and $Z$-type face checks, but the underlying cylinder graph need only be locally $3$-colorable and can support odd boundary logical operators  ([arXiv:1004.3791](https://arxiv.org/abs/1004.3791)). Later realizations stack Majorana surface-code layers and replace stacked building blocks with small Majorana fermion codes  ([arXiv:1703.00612](https://arxiv.org/abs/1703.00612), [arXiv:1704.01589](https://arxiv.org/abs/1704.01589), [arXiv:1708.05012](https://arxiv.org/abs/1708.05012), [arXiv:1801.08143](https://arxiv.org/abs/1801.08143)).
