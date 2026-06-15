---
type: concept
name: Honeycomb Floquet code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/floquet
- concepts/qec/kitaev-honeycomb
- concepts/qec/majorana-stab
- concepts/qec/qldpc
- concepts/qec/qudit-honeycomb
- concepts/qec/qudit-znone
- concepts/qec/subsystem-color
- concepts/qec/surface
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/honeycomb_floquet
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: honeycomb_floquet
---

# Honeycomb Floquet code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/honeycomb_floquet) (`code_id: honeycomb_floquet`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

2D Floquet code based on the Kitaev honeycomb model  ([arXiv:cond-mat/0506438](https://arxiv.org/abs/cond-mat/0506438)) whose logical qubits are generated through a particular sequence of measurements.
A CSS version of the code has been proposed which loosens the restriction of which sequences to use  ([arXiv:2210.02468](https://arxiv.org/abs/2210.02468)).
The code has also been generalized to arbitrary non-chiral, Abelian topological order  ([arXiv:2303.17664](https://arxiv.org/abs/2303.17664)).

The code is defined on a honeycomb tiling with a physical qubit located at each vertex. Edges are labeled $x$, $y$, and $z$, such that one edge of each label meets at every vertex. Check operators are defined as $XX$ acting on any two qubits joined by an $x$ edge, and similarly for $y$ and $z$. The honeycomb tiling is 3-colorable, so the hexagons may be labeled 0, 1, 2 such that no two neighboring hexagons have the same label.

The code-generating measurement pattern consists of measuring the check operators located on all of the $r$-labeled edges in round $r$ mod 3. The code space is the $+1$ eigenspace of the instantaneous stabilizer group (ISG). The ISG specifies the state of the system as a Pauli stabilizer state at a particular round of measurement, and it evolves into a (potentially) different ISG depending on the check operators measured.
When the same check operators are instead regarded as a static subsystem code, there are no logical qubits; the logical qubits are created dynamically by the measurement ordering  ([arXiv:2107.02194](https://arxiv.org/abs/2107.02194)).

(source: raw/error-correction-zoo.md)

## Protection

Protective features similar to the surface code: on a torus geometry, the code protects two logical qubits with a code distance proportional to the linear size of the torus. After each complete measurement round in the steady state, a depth-one local Clifford circuit maps the ISG to that of a toric code on a hexagonal superlattice, making the logical content explicit  ([arXiv:2107.02194](https://arxiv.org/abs/2107.02194)). Properties of the code with open boundaries are discussed in Refs.  ([arXiv:2110.09545](https://arxiv.org/abs/2110.09545), [arXiv:2110.05348](https://arxiv.org/abs/2110.05348)), and various other generalizations have been proposed  ([arXiv:2203.11137](https://arxiv.org/abs/2203.11137)).

## Encoders

- Initialization can be performed by preparing each pair of qubits on an edge in some particular state independently specified by the effective-one-qubit operators (two-qubit Pauli strings centered on an edge) and then beginning the check measurement sequence. This is analogous to projecting a state into the code space by measuring stabilizers.

## General gates

- There are two types of logical operators, *inner* and *outer*. An inner logical operator is the product of check operators on a homologically nontrivial cycle. They belong to the stabilizer group as a subsystem code. Outer logical operators have an interpretation in terms of magnetic and electric operators of an embedded toric/surface code, and they do not belong to the stabilizer group of the associated subsystem code.
- Fermionic string excitations can be condensed along 1D paths, yielding twist defects  ([arXiv:2306.08027](https://arxiv.org/abs/2306.08027)). Such excitations are created by taking products of plaquette check operators (that are present in all ISGs) over some region, multiplying them to yield a Pauli string on the boundary of said region, and cutting this string. Information is processed by braiding and fusing defects, which are located at the boundaries of the strings.
- Certain gates  ([arXiv:2203.11137](https://arxiv.org/abs/2203.11137)) can be performed by considering adiabatic paths in the space of Hamiltonians  ([arXiv:1406.2690](https://arxiv.org/abs/1406.2690), [arXiv:1411.4248](https://arxiv.org/abs/1411.4248), [arXiv:2203.11137](https://arxiv.org/abs/2203.11137)), yielding an instance of holonomic quantum computation  ([arXiv:quant-ph/9904011](https://arxiv.org/abs/quant-ph/9904011)).
Fault-tolerant gates should be interpretable as monodromies under a particular notion of parallel transport  ([arXiv:1309.7062](https://arxiv.org/abs/1309.7062)).

## Decoders

- The ISG has a static subgroup for all time steps $r\geq 3$ – that is, a subgroup which remains a subgroup of the ISG for all future times – given by so-called *plaquette stabilizers*. These are stabilizers consisting of products of check operators around homologically trivial paths. The syndrome bits correspond to the eigenvalues of the plaquette stabilizers. Because of the structure of the check operators, only one-third of all plaquettes are measured each round. The syndrome bits must therefore be represented by a lattice in spacetime, to reflect when and where the outcome was obtained.

## Fault tolerance

- One can run a fault-tolerant decoding algorithm by (1) bipartitioning the syndrome lattice into two graphs which are congruent to the Cayley graph of the free Abelian group with three generators (up to boundary conditions) and (2) performing a matching algorithm to deduce errors.

## Threshold

- $0.2\%-0.3\%$ in a controlled-not circuit model with a correlated minimum-weight perfect-matching decoder  ([arXiv:2108.10457](https://arxiv.org/abs/2108.10457)).
- $1.5\%<p<2.0\%$ in a circuit model with native weight-two measurements and a correlated minimum-weight perfect-matching decoder  ([arXiv:2108.10457](https://arxiv.org/abs/2108.10457)). Here, $p$ is the collective error rate of the two-body measurement gate, including both measurement and correlated data depolarization error processes.
- Against circuit-level noise: within $0.2\% − 0.3\%$ for SD6 (standard depolarizing 6-step cycle), $0.1\% − 0.15\%$ for SI1000 (superconducting-inspired 1000 ns cycle), and $1.5\% − 2.0\%$ for EM3 (entangling-measurement 3-step cycle)  ([arXiv:2202.11845](https://arxiv.org/abs/2202.11845), [arXiv:2202.11829](https://arxiv.org/abs/2202.11829)).

## Realizations

- Plaquette stabilizer measurement realized on the IBM Falcon superconducting-qubit device  ([arXiv:2210.13154](https://arxiv.org/abs/2210.13154))

## Relations

- _parent_: [[concepts/qec/floquet]] — The honeycomb Floquet code is the first 2D Floquet code.
- _parent_: [[concepts/qec/qudit-honeycomb]] — The modular-qudit honeycomb Floquet code reduces to the Hastings-Haah Floquet code for $q=2$.
- _cousin_: [[concepts/qec/qudit-znone]] — The dynamically generated logical qubit of the honeycomb Floquet code is generated by appropriately scheduling measurements of the gauge generators of the $\mathbb{Z}_{q=2}^{(1)}$ subsystem stabilizer code corresponding to the Kitaev honeycomb model. However, since this subsystem code has zero logical qubits, the instantaneous stabilizer codes of the honeycomb code cannot be interpreted as gauge-fixed versions of this subsystem code.
- _cousin_: [[concepts/qec/surface]] — Measurement of each check operator of the honeycomb Floquet code involves two qubits and projects the state of the two qubits to a two-dimensional subspace, which we regard as an effective qubit. 
These effective qubits form a surface code on an enlarged honeycomb tiling  ([arXiv:2107.02194](https://arxiv.org/abs/2107.02194)).
Electric and magnetic operators on the embedded surface code correspond to outer logical operators of the Floquet code.
In fact, outer logical operators transition back and forth from magnetic to electric surface code operators under the measurement dynamics.
Inspired by the honeycomb Floquet code, various weight-two measurement schemes have been designed  ([arXiv:2007.00307](https://arxiv.org/abs/2007.00307), [arXiv:2206.12780](https://arxiv.org/abs/2206.12780), [arXiv:2310.12981](https://arxiv.org/abs/2310.12981)), with the scheme in Ref.  ([arXiv:2206.12780](https://arxiv.org/abs/2206.12780)) being a special case of DWR.
Numerical comparisons have been performed  ([arXiv:2410.07065](https://arxiv.org/abs/2410.07065)).
- _cousin_: [[concepts/qec/twist-defect-surface]] — Fermionic string excitations of the honeycomb Floquet code can be condensed along 1D paths, yielding twist defects  ([arXiv:2306.08027](https://arxiv.org/abs/2306.08027)).
- _cousin_: [[concepts/qec/subsystem-color]] — Both honeycomb and subsystem color codes are generated via periodic sequences of measurements. However, any measurement sequence can be performed on the color code without destroying the logical qubits, while honeycomb codes can be maintained only with specific sequences. Honeycomb codes require a shorter measurement cycle and use fewer qubits at the given code distance  ([arXiv:2107.02194](https://arxiv.org/abs/2107.02194)).
- _cousin_: [[concepts/qec/majorana-stab]] — The Honeycomb code admits a convenient representation in terms of Majorana fermions. This leads to a possible physical realization of the code in terms of tetrons  ([arXiv:1610.05289](https://arxiv.org/abs/1610.05289)), where each physical qubit is composed of four Majorana modes.
- _cousin_: [[concepts/qec/qldpc]] — The Floquet check operators are weight-two, and each qubit participates in one check each round.
- _cousin_: [[concepts/qec/kitaev-honeycomb]] — The Kitaev honeycomb model Hamiltonian is a sum of checks of the honeycomb Floquet code  ([arXiv:2107.02194](https://arxiv.org/abs/2107.02194)).
- _cousin_: [`honeycomb`](https://errorcorrectionzoo.org/c/honeycomb) — The honeycomb Floquet code is defined on the honeycomb tiling.
