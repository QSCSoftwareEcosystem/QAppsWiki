---
type: concept
name: 3D color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-stabilizer
- concepts/qec/3d-surface
- concepts/qec/color
- concepts/qec/qubit-concatenated
- concepts/qec/qudit-color
- concepts/qec/spt
- concepts/qec/topological-abelian
- concepts/qec/xs-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/3d_color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: 3d_color
---

# 3D color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/3d_color) (`code_id: 3d_color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Color code defined on a four-valent, four-colorable 3-colex in a 3-manifold.
In the original colex realization, qubits sit on vertices, $X$-type stabilizers are attached to 3-cells, and $Z$-type stabilizers are attached to faces  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).

For a closed 3-manifold, the code encodes $k=3h_1$ logical qubits, where $h_1$ is the first Betti number  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).
Logical operators can be represented by colored strings and colored membranes.
Excitations consist of point-like color charges at cell defects and loop-like color fluxes at face defects; winding a $p$-charge around a $pq$-flux produces a $-1$ phase  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).

There are 101 different types of boundaries for any uniform tiling  ([arXiv:2404.05033](https://arxiv.org/abs/2404.05033)); this was shown for the great rhombated cubic honeycomb (a.k.a. cantitruncated cubic honeycomb) uniform tiling, but is valid for general uniform tilings.

(source: raw/error-correction-zoo.md)

## Protection

On a closed 3-manifold with first Betti number $h_1$, the 3D color code encodes $k=3h_1$ logical qubits  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).

## Transversal gates

- Transversal action of $T$ gates on color codes on general 3-manifolds realizes a $CCZ$ gate on three logical qubits and is related to a topological invariant that is called the triple intersection number; this gate is related to the fact that this code admits a cup product structure  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)).
- Transversal $S$ gate on color codes on general 3-manifolds corresponds to a higher-form symmetry  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)).
- Universal transversal gates can be achieved using lattice surgery or code deformation  ([arXiv:1006.5260](https://arxiv.org/abs/1006.5260), [arXiv:0806.4827](https://arxiv.org/abs/0806.4827)).
- Families of 3D color codes on quasi-hyperbolic, fibre-bundle, and Torelli mapping-torus 3-manifolds support collective logical $CCZ$ gates via transversal $T$ and individually addressable, parallelizable logical $CZ$ gates via transversal $S$ on codimension-1 submanifolds. Their rate-distance scalings are $O(1/\log n)$ with $d=O(\log n)$, $O(1/\log^2 n)$ with $d=\Omega(\log^2 n)$, and $O(1)$ with distance scaling unknown, respectively  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)).

## General gates

- Magic-state distillation protocols  ([doi:10.7907/059V-MG69](https://doi.org/10.7907/059V-MG69)).
- Non-clifford gates can be implemented via code switching  ([doi:10.7907/059V-MG69](https://doi.org/10.7907/059V-MG69)).

## Decoders

- Decoder that maps 3D color code to three copies of the 3D surface code  ([arXiv:1606.00960](https://arxiv.org/abs/1606.00960)).

## Relations

- _parent_: [[concepts/qec/color]]
- _parent_: [[concepts/qec/3d-stabilizer]]
- _parent_: [[concepts/qec/qudit-color]] — Modular-qudit 3D color codes reduce to 3D color codes for $q=2$.
- _parent_: [[concepts/qec/topological-abelian]]
- _cousin_: [[concepts/qec/3d-surface]] — On closed 3-manifolds, the 3D color code is equivalent to multiple decoupled copies of the 3D surface code via a local constant-depth Clifford circuit  ([arXiv:1007.4601](https://arxiv.org/abs/1007.4601), [arXiv:1503.02065](https://arxiv.org/abs/1503.02065), [arXiv:1804.00866](https://arxiv.org/abs/1804.00866)). This process can be viewed as an ungauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) of certain symmetries. This mapping can also be done via code concatenation  ([arXiv:1801.04255](https://arxiv.org/abs/1801.04255)). In contrast to the 3D surface/toric code, the original colex Hamiltonian can be viewed as both a string-net condensate and a membrane-net condensate  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — On closed 3-manifolds, the 3D color code is equivalent to multiple decoupled copies of the 3D surface code via a local constant-depth Clifford circuit  ([arXiv:1007.4601](https://arxiv.org/abs/1007.4601), [arXiv:1503.02065](https://arxiv.org/abs/1503.02065), [arXiv:1804.00866](https://arxiv.org/abs/1804.00866)). This process can be viewed as an ungauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) of certain symmetries. This mapping can also be done via code concatenation  ([arXiv:1801.04255](https://arxiv.org/abs/1801.04255)).
- _cousin_: [[concepts/qec/xs-stabilizer]] — The 3D color code on a particular lattice admits XS stabilizers; see [talk by M. Kesselring at the 2020 FTQC conference](https://www.youtube.com/watch?v=B8h5-ANc_-8).
- _cousin_: [[concepts/qec/spt]] — Transversal action of $T$ gates on color codes on general 3-manifolds realizes a $CCZ$ gate on three logical qubits and is related to a topological invariant that is called the triple intersection number  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)). Transversal $S$ gate on color codes on general 3-manifolds corresponds to a higher-form symmetry  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982)).
