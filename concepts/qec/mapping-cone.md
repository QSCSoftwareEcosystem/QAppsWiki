---
type: concept
name: Mapping cone code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases:
- Height-$n$ cone code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/distance-balanced
- concepts/qec/good-qldpc
- concepts/qec/higher-dimensional-surface
- concepts/qec/qldpc
- concepts/qec/qubit-concatenated
- concepts/qec/qubit-css
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/mapping_cone
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: mapping_cone
---

# Mapping cone code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/mapping_cone) (`code_id: mapping_cone`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CSS code obtained from an input CSS code, called the *embedded code*, by adding physical qubits and parity checks in a way that guarantees a natural isomorphism between the logical operators of the input and output codes.
The framework unifies various quantum code embedding procedures, including code concatenation, weight reduction, layer codes, geometrically local codes obtained by subdivision, and gauging-based fault-tolerant logical measurement  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).

Formally, a *height-$n$ cone* is a chain complex $C$ whose spaces decompose into direct sums, $C_i = C_i^n \oplus C_i^{n-1} \oplus \cdots \oplus C_i^0$, with a boundary operator that is lower triangular with respect to the decomposition.
The diagonal blocks $\partial^s$ define chain complexes $C^s$ called the *levels* of the cone, while the sub-diagonal blocks $g_s$, called *gluing maps*, induce maps on homology that assemble the level homologies into the embedded complex $H_n(\partial^n) \to H_{n-1}(\partial^{n-1}) \to \cdots \to H_0(\partial^0)$.
If the levels have trivial homology away from the appropriate degrees, a condition called *regularity*, then the logical operators of the cone are naturally isomorphic to those of the embedded code  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).
The construction is an iterated application of the mapping cone of homological algebra.

(source: raw/error-correction-zoo.md)

## Protection

A cleaning lemma bounds the $Z$-distance of a height-2 cone from below  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).
It applies when the top-level boundary operator and the gluing map $g_2$ satisfy an isoperimetric inequality with coefficient $\alpha$.
The $Z$-distance is then at least $\alpha$ times the minimum weight of a middle-level representative of a nontrivial logical operator of the embedded code.
The lemma yields distance bounds for subdivided square complexes  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).
For gauging-based logical measurement, the lemma shows that the $Z$-distance of the cone is at least $\min(h,1)$ times that of the input code  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).
Here, $h$ is the Cheeger constant of the connected graph used to build the cone.

## Relations

- _parent_: [[concepts/qec/qubit-css]] — A mapping cone code is a qubit CSS code equipped with a direct-sum decomposition of its chain complex into levels, with lower-triangular boundary operator, such that the associated embedded code has naturally isomorphic logical operators.
- _cousin_: [[concepts/qec/qubit-concatenated]] — The mapping cone framework can be regarded as a generalization of code concatenation for CSS codes  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).
- _cousin_: [[concepts/qec/distance-balanced]] — The coning step of the weight reduction procedure of Ref.  ([arXiv:2102.10030](https://arxiv.org/abs/2102.10030)) is a height-1 cone  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)). The triangulation and thickening steps used in this procedure are regular height-2 cones  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).
- _cousin_: [[concepts/qec/good-qldpc]] — Optimal embeddings of good QLDPC codes into $D$-dimensional Euclidean space use layer codes  ([arXiv:2309.16503](https://arxiv.org/abs/2309.16503)) or subdivided square complexes  ([arXiv:2309.16104](https://arxiv.org/abs/2309.16104)). Both constructions yield regular height-2 cones whose embedded code is the input code  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).
- _cousin_: [[concepts/qec/surface]] — Surface codes on honeycomb and triangular lattices, with periodic or alternating smooth and rough boundaries, are regular cones whose embedded code is the square-lattice surface code  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)). The planar surface code cannot be realized by any 2D CW complex  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).
- _cousin_: [[concepts/qec/higher-dimensional-surface]] — The barycentric subdivision of an $n$-dimensional simplicial complex is a regular height-$n$ cone whose embedded complex is the original complex  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)). The homological codes of the two complexes therefore have isomorphic logical operators.
- _cousin_: [[concepts/qec/qldpc]] — Gauging-based logical measurement for QLDPC codes  ([arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) is a regular height-1 cone built from a connected graph  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)). The $Z$-type logical operators of this cone are those of the input code modulo the measured one  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361)). Homological measurement is also formulated using height-1 cones  ([arXiv:2410.02753](https://arxiv.org/abs/2410.02753), [arXiv:2507.05361](https://arxiv.org/abs/2507.05361)).
