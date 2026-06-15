---
type: concept
name: Hyperbolic surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/higher-dimensional-surface
- concepts/qec/holographic-tensor
- concepts/qec/single-shot
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/hyperbolic_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: hyperbolic_surface
---

# Hyperbolic surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/hyperbolic_surface) (`code_id: hyperbolic_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An extension of the Kitaev surface code construction to hyperbolic manifolds.
Given a cellulation of a hyperbolic manifold of arbitrary dimension, qubits are put on $i$-dimensional faces, $X$-type stabilizers are associated with $(i-1)$-faces, while $Z$-type stabilizers are associated with $i+1$-faces.

(source: raw/error-correction-zoo.md)

## Protection

Constructions (see code children below) have yielded distances scaling favorably with the number of qubits. The use of hyperbolic surfaces allows one to circumvent bounds on code parameters (such as the \term{BPT bound}) that are valid for lattice geometries.

## General gates

- $(1,D-1)$ surface codes on hyperbolic geometries admit a fault-tolerant implementation of $C^D Z$ gates  ([arXiv:2312.09111](https://arxiv.org/abs/2312.09111)).
- Higher-dimensional hyperbolic surface codes can admit a cup product structure and can thus have logical gates in the \term{Clifford hierarchy} implemented by constant-depth Clifford circuits  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).

## Decoders

- Hastings decoder  ([arXiv:1312.2546](https://arxiv.org/abs/1312.2546)).

## Relations

- _parent_: [[concepts/qec/higher-dimensional-surface]]
- _cousin_: [[concepts/qec/holographic-tensor]] — Both holographic tensor-network and hyperbolic surface codes utilize tessellations of hyperbolic surfaces. Encodings for the former are hyperbolically tiled tensor networks, while the latter is defined on hyperbolically tiled physical-qubit lattices.
- _cousin_: [[concepts/qec/single-shot]] — A 4D hyperbolic surface code can be decoded with the Hastings decoder  ([arXiv:1312.2546](https://arxiv.org/abs/1312.2546)) in time $O(n\log n)$ and with a logical error scaling inverse polynomially with $n$.
