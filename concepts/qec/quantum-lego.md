---
type: concept
name: Tensor-network code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Quantum Lego code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/asymmetric-qecc
- concepts/qec/block-quantum
- concepts/qec/reinforcement-learning
- concepts/qec/rotated-surface
- concepts/qec/stab-4-2-2
- concepts/qec/stab-6-4-2
- concepts/qec/steane
- concepts/qec/surface
- concepts/qec/triangular-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_lego
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_lego
---

# Tensor-network code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_lego) (`code_id: quantum_lego`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Block quantum code constructed using a tensor-network-based graphical framework from atomic tensors a.k.a. *quantum "Lego" blocks*  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)), which can serve as encoding isometries for smaller quantum codes.
The class of codes constructed using the framework depends on the choice of atomic "Lego" blocks.

The individual "Lego" blocks and resulting quantum Lego codes can be stabilizer  ([arXiv:2009.10329](https://arxiv.org/abs/2009.10329), [arXiv:2109.11996](https://arxiv.org/abs/2109.11996)) or non-stabilizer  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158), [arXiv:2308.05152](https://arxiv.org/abs/2308.05152)).
They need not be isometries, meaning that this class of codes generalizes planar-perfect tensor-network codes.
However, both the logical and physical degrees of freedom must have the same local dimension.

For example, any stabilizer code can be built out of atomic blocks like the 2-site repetition code, single-site trivial stabilizer codes, and tensor products of the $|0\rangle$ state.
Specifically, the HaPPY holographic code is a quantum Lego code whose atomic "Lego" block is the five-qubit perfect qubit code.

Many known codes can be created using this code's methods in order to further their understanding, including a 6-qubit implementation of the generalized Bacon-Shor code, the toric code, and the $⟦7,1,3⟧$ Steane code.
Finite patches of the toric-code tensor network, equipped with boundary stopper tensors or repetition-code boundary tensors, reproduce surface-code patches and subsystem variants.
Local Hadamard modifications of alternating tensors yield XZZX surface-code variants, while re-interpreting alternating rows of surface-code physical legs as logical legs yields 2D Bacon-Shor codes and makes their relation to the quantum compass model explicit  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
The same framework also yields flat-geometry perfect-tensor codes, holographic Reed-Muller codes with transversal non-Clifford gates, and a 3D subsystem code built from Steane tensors with localized cube-like stabilizers  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
For example, a simple $ ⟦4,2,2⟧ $ stabilizer code can be written as a rank 6 tensor.
Attaching two of these via gluing together one logical leg from each can produce a $⟦6,4,2⟧$ stabilizer code.
Code optimization in this framework can be done using reinforcement learning  ([arXiv:2305.06378](https://arxiv.org/abs/2305.06378), [arXiv:2305.11470](https://arxiv.org/abs/2305.11470)).

To construct a Lego code, the encoding map $V$ for each code that is to be used in the construction is converted to a tensor by decomposing it using the formula
\begin{align}
V = \sum_{i_j} V_{i_1 \ldots i_{n+k}} | i_{k+1} \ldots i_{k+n} \rangle \langle i_1 \ldots i_k |~.
\end{align}
We then look at the codes graphically, treating each $i_j$ as an edge dangling out of the tensor vertex $V_{i_1 \ldots i_{n+k}}$. These edges are either connected to another tensor vertex's edges or left dangling. If the block codes are stabilizer, then each local tensor has unitary product stabilizers (UPS). The goal is to push each UPS through the tensor network until each dangling edge has only trivial support. Otherwise, a matching value is pushed through the edge and the process is repeated on the next tensor. If a UPS can be pushed through the whole network, then a UPS for the larger network has been found. The dangling legs (edges) and UPS of the whole network can then be converted to physical/logical elements and stabilizers/logical operators for a new quantum code.

(source: raw/error-correction-zoo.md)

## Protection

Stabilizer code distance can be calculated by tensor contraction  ([arXiv:2109.11996](https://arxiv.org/abs/2109.11996)), which can be optimized  ([arXiv:2510.08210](https://arxiv.org/abs/2510.08210)).
Quantum weight enumerators are related to tensor-network structures like correlation tensor norms  ([arXiv:1106.5756](https://arxiv.org/abs/1106.5756), [arXiv:1110.4108](https://arxiv.org/abs/1110.4108)).

## Encoders

- Unitary-circuit encoding exists for a restricted class of tensor networks contractible via isometries  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).

## Transversal gates

- The quantum Lego framework yields an $⟦8,1,2⟧$ stabilizer code that admits a transversal logical $T$ gate that originates from that of a trivial (distance-one) $⟦7,1⟧$ code. This code, in turn, is obtained from the $⟦15,1,3⟧$ code  ([arXiv:2310.19538](https://arxiv.org/abs/2310.19538)).

## Decoders

- The decoder is created by creating a decoding quantum circuit with dangling legs replaced with input/output wires, and tensors converted to unitary gates. Maximum likelihood decoding can be used when the tensors are stabilizer codes.
- Tensor-network decoder when the tensor network is contractible via stabilizer isometries  ([arXiv:2009.10329](https://arxiv.org/abs/2009.10329)). Independent logical qubits can be decoded in parallel  ([arXiv:2012.07317](https://arxiv.org/abs/2012.07317)).
- Tensor-network-based decoder when the encoding unitary is known  ([arXiv:1312.4578](https://arxiv.org/abs/1312.4578)).

## Relations

- _parent_: [[concepts/qec/block-quantum]]
- _cousin_: [[concepts/qec/steane]] — The Steane code can be built from two $⟦4,2,2⟧$ codes in the quantum Lego code framework  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
- _cousin_: [[concepts/qec/stab-6-4-2]] — The $⟦6,4,2⟧$ error-detecting code can be constructed out of two $⟦4,2,2⟧$ codes in the quantum Lego code framework  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
- _cousin_: [[concepts/qec/stab-4-2-2]] — The Steane and $⟦6,4,2⟧$ error-detecting codes can be built from two $⟦4,2,2⟧$ codes in the quantum Lego code framework  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)). The toric code can be constructed by arranging $⟦4,2,2⟧$ tensors on a square lattice and recovering the star and plaquette operators by operator pushing  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
- _cousin_: [[concepts/qec/rotated-surface]] — A tensor-network based modification of the rotated surface code improves performance against depolarizing noise by $\approx 2\%$  ([arXiv:2109.11996](https://arxiv.org/abs/2109.11996)).
- _cousin_: [[concepts/qec/triangular-color]] — Larger 6.6.6 color codes can be constructed by contracting legs of tensors of smaller codes  ([arXiv:2109.11996](https://arxiv.org/abs/2109.11996)).
- _cousin_: [[concepts/qec/asymmetric-qecc]] — Quantum Lego and more general tensor-network code optimization for biased noise can be done using reinforcement learning  ([arXiv:2305.06378](https://arxiv.org/abs/2305.06378), [arXiv:2305.11470](https://arxiv.org/abs/2305.11470)).
- _cousin_: [[concepts/qec/reinforcement-learning]] — Quantum Lego and more general tensor-network code optimization for biased noise can be done using reinforcement learning  ([arXiv:2305.06378](https://arxiv.org/abs/2305.06378), [arXiv:2305.11470](https://arxiv.org/abs/2305.11470)).
- _cousin_: [[concepts/qec/surface]] — Planar surface codes arise from finite patches of the toric-code tensor network by contracting boundary legs with stopper tensors or repetition-code boundary tensors  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)). The 2D Bacon-Shor code can also be obtained from a surface-code tensor network by reassigning every other row of dangling physical legs to logical legs; in this quantum-Lego picture, the gauge generators remain weight-two $XX$ and $ZZ$ operators and the construction makes explicit a connection to the quantum compass model  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).

## Notes

- TensorNetworkCodes Julia software library  ([arXiv:2109.11996](https://arxiv.org/abs/2109.11996)).
- LEGO$\_$HQEC software tool  ([arXiv:2410.22861](https://arxiv.org/abs/2410.22861)).
