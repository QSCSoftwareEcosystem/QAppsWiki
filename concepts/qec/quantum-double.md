---
type: concept
name: Quantum-double code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Non-Abelian surface code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/bacon-shor-4
- concepts/qec/hamiltonian
- concepts/qec/hopf-quantum-double
- concepts/qec/spt
- concepts/qec/subsystem-group-quantum
- concepts/qec/tqd
- concepts/qec/tqd-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_double
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_double
---

# Quantum-double code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_double) (`code_id: quantum_double`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Group-based code whose codewords realize 2D modular gapped topological order defined by a finite group $G$.
The code's generators are few-body operators associated to the stars and plaquettes, respectively, of a tessellation of a two-dimensional surface (with a qudit of dimension $ |G| $ located at each edge of the tessellation).
The original Hamiltonian can be re-expressed via group-based right- and left-multiplication $X$-type as well as $Z$-type error operators  ([arXiv:2111.12096](https://arxiv.org/abs/2111.12096)).

The physical Hilbert space has dimension $ |G|^E  $, where $ E $ is the number of  edges in the tessellation. The dimension of the code space is the number of orbits of the conjugation action of $ G $ on $ \text{Hom}(\pi_1(\Sigma),G) $, the set of group homomorphisms from the fundamental group of the surface $ \Sigma $ into the finite group $ G $  ([arXiv:1908.02829](https://arxiv.org/abs/1908.02829), [arXiv:2509.10876](https://arxiv.org/abs/2509.10876)) (see also Ref.  ([arXiv:0909.3305](https://arxiv.org/abs/0909.3305))). When $ G $ is Abelian, the formula for the dimension simplifies to $ |G|^{2g} $, where $ g $ is the genus of the surface $ \Sigma $.

The codespace is the ground-state subspace of the quantum double model Hamiltonian, while local excitations are characterized by anyons.
Different types of anyons are labeled by irreducible representations of the group's quantum double algebra, $D(G)$ (a.k.a. Drinfeld center)  ([arXiv:1006.5479](https://arxiv.org/abs/1006.5479), [arXiv:2310.19661](https://arxiv.org/abs/2310.19661)).
Ribbon operators create particle-antiparticle pairs at their endpoints, and braiding followed by fusion of the resulting anyons furnishes the fault-tolerant computational primitive of the original model  ([arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021)).
Not all isomorphic non-Abelian groups give rise to different quantum doubles  ([arXiv:math/0605530](https://arxiv.org/abs/math/0605530)).

For non-Abelian groups, alternative constructions are possible, encoding information in the fusion space of the low-energy anyonic quasiparticle excitations of the model  ([doi:10.1007/3-540-49208-9_31](https://doi.org/10.1007/3-540-49208-9_31), [arXiv:quant-ph/0306063](https://arxiv.org/abs/quant-ph/0306063), [doi:10.1017/CBO9780511792908](https://doi.org/10.1017/CBO9780511792908)).
The fusion space of such non-Abelian anyons has dimension greater than one, allowing for topological quantum computation of logical information stored in the fusion outcomes.

Gapped boundaries of the models are classified by a subgroup $K \subseteq G$ and a two-cocycle  ([arXiv:0712.0190](https://arxiv.org/abs/0712.0190), [arXiv:1006.5479](https://arxiv.org/abs/1006.5479), [arXiv:1706.03611](https://arxiv.org/abs/1706.03611), [arXiv:2204.05341](https://arxiv.org/abs/2204.05341)).

(source: raw/error-correction-zoo.md)

## Protection

Error-correcting properties established in Ref.  ([arXiv:1908.02829](https://arxiv.org/abs/1908.02829)).
The code distance is the number of edges in the shortest non-contractible cycle in the tessellation or dual tessellation  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143)).
These models realize local topological order (LTO)  ([arXiv:2309.13440](https://arxiv.org/abs/2309.13440)).

## Encoders

- A depth-$L^2$ circuit that grows the code out of a small patch on an $L\times L$ square lattice using CMULT gates (i.e., "local moves")  ([arXiv:0712.0348](https://arxiv.org/abs/0712.0348), [arXiv:1101.0527](https://arxiv.org/abs/1101.0527)).
- For an $L\times L$ lattice, deterministic state preparation can be done with a geometrically local unitary $O(L)$-depth circuit  ([arXiv:0901.1345](https://arxiv.org/abs/0901.1345), [arXiv:1101.0527](https://arxiv.org/abs/1101.0527)) or an $O(\log{L})$-depth unitary circuit with non-local two-qubit gates  ([arXiv:0712.0348](https://arxiv.org/abs/0712.0348), [arXiv:0806.4583](https://arxiv.org/abs/0806.4583)).
- For any group $G$ of nilpotency class two, states can be initialized with a single round of adaptive measurements  ([arXiv:2209.06202](https://arxiv.org/abs/2209.06202)).
- For any solvable group $G$, ground-state preparation and anyon-pair creation can be done with an adaptive constant-depth circuit with geometrically local gates and measurements throughout  ([arXiv:2112.01519](https://arxiv.org/abs/2112.01519), [arXiv:2205.01933](https://arxiv.org/abs/2205.01933)) (see Ref.  ([arXiv:2112.03061](https://arxiv.org/abs/2112.03061)) for specific dihedral groups). Anyon-pair creation requires an adaptive circuit for any non-Abelian $G$  ([arXiv:2205.01933](https://arxiv.org/abs/2205.01933)).
- For non-solvable groups, states may not be preparable with an adaptive constant-depth circuit with geometrically local gates and measurements throughout  ([arXiv:2209.06202](https://arxiv.org/abs/2209.06202)).

## General gates

- Universal topological quantum computation possible for certain groups  ([arXiv:quant-ph/0306063](https://arxiv.org/abs/quant-ph/0306063), [arXiv:0901.1345](https://arxiv.org/abs/0901.1345)).

## Decoders

- For any solvable group $G$, topological charge measurements can be done with an adaptive constant-depth circuit with geometrically local gates and measurements throughout  ([arXiv:2205.01933](https://arxiv.org/abs/2205.01933)).

## Code capacity threshold

- Behavior under particular $X$-type noise (namely, diffusion of an anyon that squares to the trivial anyon) is related to the phase diagram of a disordered $D_4$ rotor model  ([arXiv:2409.12230](https://arxiv.org/abs/2409.12230), [arXiv:2409.12948](https://arxiv.org/abs/2409.12948)).

## Relations

- _parent_: [[concepts/qec/tqd]] — The anyon theory corresponding to a quantum-double code is a TQD with trivial cocycle.
- _parent_: [[concepts/qec/hopf-quantum-double]] — Hopf-algebra quantum-double codes reduce to quantum-double codes when the Hopf algebra is a group algebra. Quantum-double codes for non-Abelian groups $G$ are dual to Hopf-algebra quantum-double codes for Hopf algebras based on $\text{Rep}(G)$ under the Tannaka-Krein duality  ([arXiv:0907.2670](https://arxiv.org/abs/0907.2670)) ([arXiv:1006.5823](https://arxiv.org/abs/1006.5823)).
- _cousin_: [[concepts/qec/hamiltonian]] — Quantum double code Hamiltonians can be simulated, with the help of perturbation theory and the $⟦4,1,1,2⟧$ subsystem code, by two-dimensional two-body Hamiltonians with non-commuting terms  ([arXiv:1011.1942](https://arxiv.org/abs/1011.1942)).
- _cousin_: [[concepts/qec/subsystem-group-quantum]] — Subsystem versions of quantum-double codes have been formulated  ([doi:10.5446/35287](https://doi.org/10.5446/35287)).
- _cousin_: [[concepts/qec/bacon-shor-4]] — Quantum double code Hamiltonians can be simulated, with the help of perturbation theory and the four-qubit subsystem code, by two-dimensional two-body Hamiltonians with non-commuting terms  ([arXiv:1011.1942](https://arxiv.org/abs/1011.1942)).
- _cousin_: [[concepts/qec/spt]] — The $Q$ quantum double model can be obtained by gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) symmetries of a Type I and Type III $\mathbb{Z}_2^3$ SPT  ([arXiv:hep-th/9511201](https://arxiv.org/abs/hep-th/9511201), [arXiv:2411.04181](https://arxiv.org/abs/2411.04181)).
- _cousin_: [[concepts/qec/tqd-abelian]] — A Type-III $\mathbb{Z}_2^3$ Abelian TQD realizes the same topological order as the $G=D_4$ quantum double model  ([arXiv:hep-th/9511195](https://arxiv.org/abs/hep-th/9511195), [arXiv:1508.03468](https://arxiv.org/abs/1508.03468)). There is a sufficient condition for when a Type-III TQD can be realized as a quantum double model  ([arXiv:2408.09353](https://arxiv.org/abs/2408.09353)).

## Notes

- See Ref.  ([doi:10.1103/RevModPhys.51.659](https://doi.org/10.1103/RevModPhys.51.659)) for a review of gauge theory, which admits quantum-double topological phases. See Ref.  for another review.
