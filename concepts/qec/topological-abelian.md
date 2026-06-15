---
type: concept
name: Abelian topological code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/3d-stabilizer
- concepts/qec/topological
- concepts/qec/walker-wang
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/topological_abelian
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: topological_abelian
---

# Abelian topological code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/topological_abelian) (`code_id: topological_abelian`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Code whose codewords realize topological order associated with an Abelian anyon theory.
In 2D, this is equivalent to a unitary braided fusion category which is also an Abelian group under fusion  ([arXiv:2004.12048](https://arxiv.org/abs/2004.12048)).
Unless otherwise noted, the phases discussed are bosonic.

\subsection{2D Abelian topological codes}

A theory is defined by an Abelian group $A$ of anyon types whose multiplication relations define the fusion rules, and a set of exchange statistics $\theta(a)\in U(1)$ obtained by exchanging two anyons of type $a\in A$.
The exchange statistics in turn define braiding relations,
\begin{align}
  B(a,b) = \frac{\theta(ab)}{\theta(a)\theta(b)}~,
\end{align}
between all anyon pairs $a,b$.

All 2D Abelian bosonic topological orders can be understood within the subsystem stabilizer formalism  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
As such, many of the operations one can perform on such codes have both a stabilizer and a topological-phase interpretation.
Stabilizer generators of 2D topological codes acting on 1D loops of qubits can be interpreted as one-form symmetries of the underlying phase realized by the code.
Identification of an anyon $a$ with the vacuum is equivalent to adding string excitation operators corresponding to $a$ to the stabilizer group and taking the center to get another stabilizer group.
Code states of this new stabilizer code correspond to a condensed phase of the parent topological phase.
A related subsystem-code operation is to gauge out anyon types by adjoining their short string operators to the gauge group; unlike condensation, the gauged-out anyons need not be bosons and are not identified with the vacuum  ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
The remaining unidentified parent-phase anyons behave differently with respect to the new condensed-phase state.
Some become *confined* while the remaining ones pick up new braiding relations.

A 2D Abelian anyon theory admits a gapped boundary iff it has a Lagrangian subgroup, i.e., a maximal subgroup of bosons with trivial mutual statistics whose order squares to that of the anyon group  ([arXiv:1008.0654](https://arxiv.org/abs/1008.0654), [arXiv:2107.13091](https://arxiv.org/abs/2107.13091), [arXiv:2112.11394](https://arxiv.org/abs/2112.11394)).
It is conjectured that the logical dimension of an Abelian topological code on a torus is always a square  ([arXiv:1008.0654](https://arxiv.org/abs/1008.0654)).

\subsection{3D Abelian topological codes}

While excitations are point-like in 2D topological codes, they can have higher dimension in 3D topological codes.
For example, there are three types of $\mathbb{Z}_2$ Abelian topological orders in 3D: one with bosonic charge and loop excitations (BcBl) and two with fermionic charge excitations and bosonic (FcBl) or fermionic (FcFl) loop excitations, respectively  ([arXiv:2011.11165](https://arxiv.org/abs/2011.11165), [arXiv:2110.14654](https://arxiv.org/abs/2110.14654)).
The first two correspond to the 3D surface code and 3D fermionic surface code, while the FcFl case is purported not to have a commuting projector Hamiltonian realization  ([arXiv:2110.14654](https://arxiv.org/abs/2110.14654)).
There exists an invariant that distinguishes these  ([arXiv:2110.14654](https://arxiv.org/abs/2110.14654)).

(source: raw/error-correction-zoo.md)

## Rate

$\mathbb{Z}_q$ topological order cannot exist on any fractal geometry that is embeddable in two Euclidean dimensions  ([arXiv:2108.00018](https://arxiv.org/abs/2108.00018)).

## Encoders

- Any local quantum circuit connecting ground states of topological orders with non-isomorphic Abelian groups must have depth that is at least linear in the diameter of the system  ([arXiv:1407.2926](https://arxiv.org/abs/1407.2926)).

## General gates

- Clifford gates can be implemented by braiding defects; for qubit-based stabilizer codes realizing Abelian topological phases, see Refs.  ([arXiv:1305.7203](https://arxiv.org/abs/1305.7203), [arXiv:2210.09282](https://arxiv.org/abs/2210.09282)). Most of such designs focus on the surface code  ([arXiv:1004.1838](https://arxiv.org/abs/1004.1838), [arXiv:1104.5047](https://arxiv.org/abs/1104.5047), [arXiv:1208.0928](https://arxiv.org/abs/1208.0928), [arXiv:1508.04166](https://arxiv.org/abs/1508.04166), [arXiv:1609.04673](https://arxiv.org/abs/1609.04673), [arXiv:2103.08381](https://arxiv.org/abs/2103.08381)).

## Fault tolerance

- Fault-tolerant logical operations can be interpreted as anyon condensation events  ([arXiv:2212.00042](https://arxiv.org/abs/2212.00042)).
- Modular decoding, designed to overcome the backlog problem, is applicable to fault-tolerant protocols based on topological qubit stabilizer codes  ([arXiv:2303.04846](https://arxiv.org/abs/2303.04846)).

## Relations

- _parent_: [[concepts/qec/topological]]
- _cousin_: [[concepts/qec/walker-wang]] — Any Abelian anyon theory $A$ can be realized at one of the surfaces of a 3D Walker-Wang model whose underlying theory is an Abelian TQD containing $A$ as a subtheory  ([arXiv:1907.02075](https://arxiv.org/abs/1907.02075), [arXiv:2202.05442](https://arxiv.org/abs/2202.05442)) ([arXiv:2211.03798](https://arxiv.org/abs/2211.03798)).
- _cousin_: [[concepts/qec/3d-stabilizer]] — Translation-invariant qubit 3D TQFT stabilizer models are conjectured to be equivalent, under a locality-preserving unitary, to multiple copies of the 3D surface code and/or the 3D fermionic surface code together with trivial ancillas  ([arXiv:1908.08049](https://arxiv.org/abs/1908.08049)).
