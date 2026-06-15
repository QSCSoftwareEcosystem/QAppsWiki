---
type: concept
name: Homological code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Generalized surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qubit-generalized-homological-product-css
- concepts/qec/translationally-invariant-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/higher_dimensional_surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: higher_dimensional_surface
---

# Homological code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/higher_dimensional_surface) (`code_id: higher_dimensional_surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A CSS extension of the Kitaev surface code to arbitrary manifolds.
The version on a Euclidean manifold of some fixed dimension is called the $D$*-dimensional "surface"* or $D$*-dimensional toric* code.

Given a cellulation of a manifold, qubits are put on $p$-dimensional faces, $X$-type stabilizers
are associated with $(p-1)$-faces, while $Z$-type stabilizers are associated with $(p+1)$-faces.
Here, $p$ ranges between $1$ and $D-1$.

Lattice surface codes in $D$ spatial dimensions can be partially classified by the dimension of their stabilizer generators (and corresponding excitations).
There are $(p,q)$ *surface codes* for $q = D-p$  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468)).
Applying this construction to the dual lattice of a $(p,q)$ surface code yields a $(q,p)$ surface code.
All lattice surface codes have bosonic $e$ and $m$ excitations of dimension $p-1$ and $q-1$, respectively. Their logical operators are also of dimension $p$ and $q$, respectively.

In 2D, there is only the $(1,1)$ surface code, which is equivalent to the Kitaev surface code and which admits point-like $e$ and $m$ excitations.
In 3D, there are the $(1,2)$ and $(2,1)$ 3D surface codes, which are equivalent by Hadamard gates. Both admit point-like excitations of one type and loop-like excitations of the other.
In 4D, there are the $(1,3)$, $(2,2)$, and $(3,1)$ 4D surface codes, with the first and last being equivalent by Hadamard gates. The $(1,3)$ code admits point-like $e$ excitations and 2D membrane $m$ excitations, while the $(2,2)$ loop toric code admits loop-like $e$ and $m$ excitations.

Open-boundary hypercubic realizations give a family of $(d_1,d_2)$-surface codes whose logical $\overline{X}$ and $\overline{Z}$ operators have dimensions $d_1$ and $d_2$, respectively; the ordinary surface code, the 3D cubic code, and the 4D tesseract code are examples  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).

(source: raw/error-correction-zoo.md)

## Protection

The 2D members of the family obey the Bravyi-Terhal no-go theorem: geometrically local stabilizer generators allow distance at most $O(L)$ and only an $O(1)$ energy barrier, ruling out self-correction in two dimensions  ([arXiv:0810.1983](https://arxiv.org/abs/0810.1983)).
By contrast, the 4D $(2,2)$ loop surface code serves as a self-correcting quantum memory, while surface codes in higher dimensions can have distances not possible in lower dimensions.

## Rate

Rate depends on the underlying cellulation and manifold  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:1606.07116](https://arxiv.org/abs/1606.07116)).
For general 2D
manifolds, $kd^2\leq c(\log k)^2 n$ for some constant $c$
 ([arXiv:1301.6588](https://arxiv.org/abs/1301.6588)), meaning that (1) 2D surface codes with bounded
geometry have distance scaling at most as $O(\sqrt{n})$
 ([arXiv:0909.5200](https://arxiv.org/abs/0909.5200), [doi:10.1063/1.4726034](https://doi.org/10.1063/1.4726034)), and (2) surface codes with
finite rate can only achieve an asymptotic minimum distance that is
logarithmic in $n$.
Higher-dimensional manifolds yield distances scaling more favorably.
Loewner's theorem
provides an upper bound for any bounded-geometry surface code
 ([doi:10.1201/9781420035377-13](https://doi.org/10.1201/9781420035377-13)).

## Transversal gates

- Locality preserving operations can be determined for stacks of homological codes in any dimension  ([arXiv:1709.00020](https://arxiv.org/abs/1709.00020)).

## Decoders

- Local automaton decoders based on Toom's rule and its generalization, the sweep rule  ([doi:10.7907/THD5-A335](https://doi.org/10.7907/THD5-A335), [arXiv:1809.10145](https://arxiv.org/abs/1809.10145), [doi:10.7907/059V-MG69](https://doi.org/10.7907/059V-MG69)).
- Improved BP-OSD decoder  ([arXiv:2206.03122](https://arxiv.org/abs/2206.03122)).
- Renormalization group (RG) decoder  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).

## Code capacity threshold

- $>0\%$ threshold with sweep decoder for lattice surface codes in various dimensions  ([doi:10.7907/059V-MG69](https://doi.org/10.7907/059V-MG69)).

## Relations

- _parent_: [[concepts/qec/qubit-generalized-homological-product-css]] — The generalized surface code is constructed from chain complexes arising from cell complexes of the underlying manifold. Such complexes are not necessarily products of two non-trivial complexes, but the manifolds are picked so that their homology ensures favorable code properties.
- _cousin_: [[concepts/qec/translationally-invariant-stabilizer]] — Lattice surface codes in $D$ spatial dimensions can be partially classified by the dimension of their stabilizer generators (and corresponding excitations).
There are $(p,q)$ *surface codes* for $p+q=D$ realized by $Z$-type stabilizer generators of dimension $p$ and $X$-type stabilizer generators of dimension $q$.
The two corresponding types of excitations are of dimension $p-1$ and $q-1$, respectively.

## Notes

- 2D and 3D surface code [visualization
tool](https://gui.quantumcodes.io/).
- on the role of homology in constructing surface codes by D. Browne.
