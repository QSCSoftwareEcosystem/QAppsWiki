---
type: concept
name: Bravyi-Kitaev superfast (BKSF) code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Loop-stabilized fermion simulation (LSFS) code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/mlsc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/bksf
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: bksf
---

# Bravyi-Kitaev superfast (BKSF) code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/bksf) (`code_id: bksf`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A single-error-detecting fermion-into-qubit encoding defined on a 2D qubit lattice whose stabilizers are associated with loops in the lattice.
For the square-lattice edge ordering used in Ref.  ([arXiv:2201.05153](https://arxiv.org/abs/2201.05153)), the BKSF logical operators coincide with exact 2D bosonization on the dual lattice after relabeling $X$ and $Y$.
The code can be generalized to a single error-correcting code (i.e., with distance three) on graphs of degree $\geq 6$  ([arXiv:1810.05274](https://arxiv.org/abs/1810.05274)).

(source: raw/error-correction-zoo.md)

## Protection

The code can detect single-qubit errors  ([arXiv:1812.08190](https://arxiv.org/abs/1812.08190)).
A generalized BKSF code has distance 3 on a graph with degree $\geq 6$, while original BKSF code cannot correct single-qubit errors on graphs of degree $< 6$  ([arXiv:1810.05274](https://arxiv.org/abs/1810.05274)).

## Relations

- _parent_: [[concepts/qec/mlsc]] — The BKSF code can be thought of as a particular MLSC  ([arXiv:1812.08190](https://arxiv.org/abs/1812.08190)).
