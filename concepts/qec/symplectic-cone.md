---
type: concept
name: Symplectic cone code
status: provisional
updated: '2026-09-29'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/distance-balanced
- concepts/qec/mapping-cone
- concepts/qec/qldpc
- concepts/qec/qubit-stabilizer
- concepts/qec/surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/symplectic_cone
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: symplectic_cone
---

# Symplectic cone code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/symplectic_cone) (`code_id: symplectic_cone`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Qubit stabilizer code obtained by attaching a CSS ancilla code to an input stabilizer code represented as a symplectic complex, with the output logical operators determined by an *embedded column complex*  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
*Gluing maps* extend the ancilla $X$-type checks onto the input qubits and the input checks onto the ancilla qubits.
A *defect map* then adds $Z$-type support on the ancilla's own qubits to the ancilla $X$-type checks so that all extended checks commute.
The construction generalizes the mapping cone framework of quantum code embedding from CSS codes to arbitrary stabilizer codes  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).

The generalization extends fault-tolerant logical measurement, geometrically local embedding, and weight reduction to codes and logical operators that admit no CSS structure  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
Formally, a symplectic cone is a height-two cone whose middle level is the input-code symplectic complex $D$.
Its top and bottom levels are the cochain complex and the chain complex of the ancilla code $A$, respectively.
Its stabilizer map is block lower triangular, with the level maps on the diagonal, the gluing maps below the diagonal, and the defect map in the corner  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
The gluing maps form a chain map compatible with the defect map, and this compatibility is what makes the cone a symplectic complex, i.e., keeps the extended checks commuting  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
If $H_1(A)=0$, the logical space $H_1(C)$ is naturally isomorphic to that of the embedded column complex $H^0(A)\to H_1(D)\to H_0(A)$  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
This column-complex homology need not equal the logical space of the input code $D$.
The Layer code and weight-reduction applications choose the column complex to preserve the input logical space.
For measurement of one logical operator $\ell^{\star}$, it instead gives $H_1(C)\cong[\ell^{\star}]^{\perp}/[\ell^{\star}]$, so the deformed code has one fewer logical qubit  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
The ancilla is CSS in isolation, but once glued its $X$-type checks are generically dressed with $Z$-type support by the defect map.
The output code is therefore generally non-CSS even when the input code is CSS  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).

(source: raw/error-correction-zoo.md)

## Protection

The distance of a symplectic cone code can be lower bounded in terms of the distance of its embedded code via the cleaning lemma of the mapping cone framework  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361), [arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).

## Fault tolerance

- A single weight-$W$ non-CSS logical operator of a QLDPC code can be measured fault-tolerantly using an $O(W\log W)$-qubit ancilla  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
When the measurement graph has constant expansion, the deformed code retains distance $\Omega(d)$.
A spacetime fault complex establishes a threshold for the procedure.
Native parallel measurement of general commuting non-CSS logical operators remains open  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
- The fast-surgery framework  ([arXiv:2510.04521](https://arxiv.org/abs/2510.04521)) extends conditionally to non-CSS logical measurement when a suitable CSS ancilla with meta-syndromes and relative expansion is available  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).

## Relations

- _parent_: [[concepts/qec/qubit-stabilizer]] — A symplectic cone code is a qubit stabilizer code whose symplectic complex has an ancillary cochain level, an input-code level, and an ancillary chain level.
Its stabilizer map is lower triangular, and a mixed symplectic form pairs the two ancillary sectors.
When $H_1(A)=0$, the output logical space is naturally isomorphic to the homology of the embedded column complex  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
- _cousin_: [[concepts/qec/mapping-cone]] — The symplectic cone framework generalizes height-two CSS mapping cones to arbitrary stabilizer codes. The full mapping-cone family also contains cones of other heights, so neither family contains the other  ([arXiv:2507.05361](https://arxiv.org/abs/2507.05361), [arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
- _cousin_: [[concepts/qec/qldpc]] — For a QLDPC input and a bounded-degree expanding measurement graph, the symplectic-cone construction remains QLDPC  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)). It measures a single non-CSS logical operator without first converting it to a CSS representative by a local Clifford circuit  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
- _cousin_: [[concepts/qec/surface]] — Measurement of a logical $Y$ operator of the surface code is an example of non-CSS surgery  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)). The defect map dresses the attached CSS ancilla such that the deformed code is non-CSS  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
- _cousin_: [[concepts/qec/distance-balanced]] — Symplectic cones extend weight reduction to non-CSS input codes  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
For an $n$-qubit input of check weight $w$ and total qubit degree $q$, the output has block length $O(w^4q^4)n$.
Its maximum stabilizer-generator weight is nine and its total qubit degree is at most eight  ([arXiv:2608.16995](https://arxiv.org/abs/2608.16995)).
