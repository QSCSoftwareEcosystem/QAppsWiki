---
type: concept
name: Color code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/higher-dimensional-surface
- concepts/qec/qldpc
- concepts/qec/quantum-pin
- concepts/qec/self-dual-css
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/color
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: color
---

# Color code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/color) (`code_id: color`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of qubit CSS codes defined on particular $D$-dimensional graphs.

In the colex realization introduced in  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)), qubits are placed on vertices of a $D$-colex, and for any integers $p,q\in\{1,\dots,D-1\}$ with $p+q=D$, $Z$-type stabilizers are attached to $(p+1)$-cells while $X$-type stabilizers are attached to $(q+1)$-cells. On a closed $D$-manifold, the resulting commuting-projector Hamiltonian encodes $k=\binom{D}{p} h_p$ logical qubits, where $h_p$ is the $p$th Betti number  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).

One family is defined on a $D$-dimensional graph which satisfies two properties: (1) the graph is a homogeneous simplicial $D$-complex obtained as a triangulation of the interior of a $D$-simplex, and (2) the graph is $D+1$-colorable.
Qubits are placed on the $D$-simplices and generators are supported on suitable simplices  ([arXiv:1311.0277](https://arxiv.org/abs/1311.0277), [arXiv:1410.0069](https://arxiv.org/abs/1410.0069), [doi:10.7907/059V-MG69](https://doi.org/10.7907/059V-MG69)).
Admissible graphs can be obtained via a fattening procedure  ([arXiv:cond-mat/0607736](https://arxiv.org/abs/cond-mat/0607736)).
See also a construction based on the more general quantum pin codes  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394)).

(source: raw/error-correction-zoo.md)

## Protection

As with the surface code, the code distance depends on the specific kind of lattice used to define the code. More precisely, the distance depends on the homology of logical string operators  ([arXiv:1311.0277](https://arxiv.org/abs/1311.0277)).

## Transversal gates

- Some color codes on $D$-dimensional lattices can transversally implement a gate at the $D$th level of the \term{Clifford hierarchy} in the form of a $Z$-rotation by angle $\pi/2^{D-1}$  ([arXiv:1410.0069](https://arxiv.org/abs/1410.0069)).

## Decoders

- In contrast to the surface code, the color code can suffer from unremovable hook errors due to the specifics of its syndrome extraction circuits. Fault-tolerant decoders thus have to utilize additional flag qubits.

## Fault tolerance

- The 6D color code is a self-correcting quantum memory and admits fault-tolerant universal gate set in 7D  ([arXiv:0907.5228](https://arxiv.org/abs/0907.5228)).

## Relations

- _parent_: [[concepts/qec/qldpc]]
- _parent_: [[concepts/qec/quantum-pin]] — Color codes are special cases of quantum pin codes  ([arXiv:1906.11394](https://arxiv.org/abs/1906.11394))
- _cousin_: [[concepts/qec/self-dual-css]] — Color codes often have self-dual $X$- and $Z$-type bulk stabilizer structure, but boundary choices can prevent the full code from being self-dual. Thus, only color-code geometries for which transversal Hadamard is a logical operation are self-dual CSS codes.
- _cousin_: [[concepts/qec/higher-dimensional-surface]] — For the common realization with point-like electric excitations, the color code on a $D$-dimensional closed manifold is equivalent to $D$ decoupled copies of the $D$-dimensional toric/surface code via a local constant-depth Clifford circuit  ([arXiv:1007.4601](https://arxiv.org/abs/1007.4601), [arXiv:1503.02065](https://arxiv.org/abs/1503.02065), [arXiv:1804.00866](https://arxiv.org/abs/1804.00866)) (see also  ([arXiv:2507.16797](https://arxiv.org/abs/2507.16797))).
On a $D$-simplex-like lattice with $D+1$ differently colored boundaries, the corresponding toric-code copies are attached along a common $(D-1)$-dimensional boundary rather than fully decoupled  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065)).
The reverse of this process can be viewed as gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) certain symmetries.
Morphing subsets of colorable $D$-balls produces hybrid color-toric codes that interpolate between the color code and $D$ copies of the toric code (up to ancillas when all balls of one color are morphed), while inheriting the parent color code's fault-tolerant gates  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446)).
Several hybrid color-surface codes exist  ([arXiv:2112.01446](https://arxiv.org/abs/2112.01446), [arXiv:2201.12450](https://arxiv.org/abs/2201.12450)).

## Notes

- See Ref.  ([arXiv:1311.0277](https://arxiv.org/abs/1311.0277)) for an overview of color codes.
