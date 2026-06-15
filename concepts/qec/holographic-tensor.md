---
type: concept
name: Holographic tensor-network code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-grs
- concepts/qec/hamiltonian
- concepts/qec/holographic
- concepts/qec/qecc
- concepts/qec/quantum-lego
- concepts/qec/random-stabilizer
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/holographic_tensor
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: holographic_tensor
---

# Holographic tensor-network code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/holographic_tensor) (`code_id: holographic_tensor`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Quantum Lego code whose encoding isometry forms a holographic tensor network, i.e., a tensor network associated with a tiling of hyperbolic space.
Physical qubits are associated with uncontracted tensor legs at the boundary of the tessellation, while logical qubits are associated with uncontracted legs in the bulk.
The number of layers emanating from the central point of the tiling is the *radius* of the code.

The encoding map models radial time evolution for a fixed time slice in Anti de Sitter (AdS) space, mapping operators in the bulk of AdS, represented by logical qudits, onto operators on the boundary of the corresponding conformal field theory (CFT), represented by physical qudits.
See  ([arXiv:2108.11402](https://arxiv.org/abs/2108.11402)) for a technical formulation.

(source: raw/error-correction-zoo.md)

## Protection

Protects against erasure errors on the boundary.
Error-correction properties are often stated in the Heisenberg picture, i.e., in terms of which logical operators can be *reconstructed* after erasures.
Specifically, bulk operators outside the entanglement wedges of the erased boundary operators can be reconstructed using the remaining boundary operators.
However, the protection can be nontrivial, and may only apply to a subalgebra of bulk operators  ([arXiv:1411.7041](https://arxiv.org/abs/1411.7041), [arXiv:1612.00017](https://arxiv.org/abs/1612.00017)).

Typically, the encoding isometry $U$ obeys the *entanglement-wedge reconstruction condition*, which states that for any boundary region $R$, any bulk operator $O$ localized to the entanglement wedge of $R$ must be implementable by some boundary operator $O^{\prime}$ localized to $R$. Formally, $UO = O^{\prime}U$ and $[O^{\prime},UU^\dagger] = 0$. The entanglement wedge is the space enclosed within the Ryu–Takayanagi surface in the bulk (minimal surface) with boundary $R$.

## Encoders

- Quantum encoding maps are isometries, but non-isometric encodings are relevant to describing mappings into the interior of a black hole  ([arXiv:2207.06536](https://arxiv.org/abs/2207.06536)) and de Sitter time evolution  ([arXiv:2201.11658](https://arxiv.org/abs/2201.11658)). Trace-norm preserving encodings have also been studied  ([arXiv:0912.0963](https://arxiv.org/abs/0912.0963)).

## Transversal gates

- There exist holographic approximate codes with arbitrary transversal gate sets for any compact Lie group  ([arXiv:2108.11402](https://arxiv.org/abs/2108.11402)). However, for sufficiently localized logical subsystems of holographic stabilizer codes, the set of transversally implementable logical operations is contained in the Clifford group  ([arXiv:2103.13404](https://arxiv.org/abs/2103.13404)).

## Code capacity threshold

- The ideal holographic tensor-network code (perfect representation of AdS/CFT) should be able to protect a central bulk operator against erasures of half of the physical qubits on the boundary, in line with AdS-Rindler reconstruction  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).
- Holographic tensor-network codes are argued to have a *algebraic threshold*, for which the error rate scales polynomially (as opposed to exponentially) in the thermodynamic limit  ([arXiv:2202.04710](https://arxiv.org/abs/2202.04710)). Such a threshold is governed by the underlying conformal field theory describing the boundary.

## Relations

- _parent_: [[concepts/qec/holographic]] — Holographic codes whose encoders are holographic tensor networks are holographic tensor-network codes.
- _parent_: [[concepts/qec/quantum-lego]] — Quantum Lego codes whose encoders are tensor networks discretizing hyperbolic space can be thought of as holographic codes. More generally, holographic tensor-network codes are types of quantum LEGO codes made from stabilizer codes where logical and physical legs are pre-assigned and logical legs are not contracted. In other words, logical legs resulting from the conversion of codes to tensors must remain logical in the final tensor network, and the same for physical. Contracting logical legs is another word for gluing two logical legs together.
- _cousin_: [[concepts/qec/random-stabilizer]] — Random holographic tensor-network codes reproduce many aspects of holography  ([arXiv:1601.01694](https://arxiv.org/abs/1601.01694), [arXiv:1801.05289](https://arxiv.org/abs/1801.05289), [arXiv:2105.12067](https://arxiv.org/abs/2105.12067)).
- _cousin_: [[concepts/qec/hamiltonian]] — Local Hamiltonians lying at the CFT boundary can be mapped into the AdS bulk using tools from Hamiltonian simulation theory  ([arXiv:1810.08992](https://arxiv.org/abs/1810.08992)).
- _cousin_: [[concepts/qec/galois-grs]] — Galois-qudit GRS codes can be used to construct holographic p-adic (i.e., tree-tensor-network) codes on Bruhat-Tits trees and buildings and on Drinfeld symmetric spaces  ([arXiv:1801.09623](https://arxiv.org/abs/1801.09623), [arXiv:1812.04057](https://arxiv.org/abs/1812.04057)).
- _cousin_: [[concepts/qec/qecc]] — Quantum encoding maps are isometries, but non-isometric encodings are relevant to describing mappings into the interior of a black hole  ([arXiv:2207.06536](https://arxiv.org/abs/2207.06536)) and de Sitter time evolution  ([arXiv:2201.11658](https://arxiv.org/abs/2201.11658)). Trace-norm preserving encodings have also been studied  ([arXiv:0912.0963](https://arxiv.org/abs/0912.0963)).

## Notes

- There is a link between position verification and holography  ([arXiv:1912.05649](https://arxiv.org/abs/1912.05649), [arXiv:2401.09058](https://arxiv.org/abs/2401.09058)).
