---
type: concept
name: $⟦5,1,3⟧$ Five-qubit perfect code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Laflamme code
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_5_1_3
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_5_1_3
---

# $⟦5,1,3⟧$ Five-qubit perfect code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_5_1_3) (`code_id: stab_5_1_3`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Five-qubit cyclic stabilizer code that is the smallest qubit stabilizer code to correct a single-qubit error.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{ccccc}
  X & Z & Z & X & I \\
  I & X & Z & Z & X \\
  X & I & X & Z & Z \\
  Z & X & I & X & Z
\end{array}~.
\end{align}
A basis of codewords for the above stabilizer is 
\begin{align}
\begin{split}
|\overline{0}\rangle &= \tfrac{1}{4}(|00000\rangle + |10010\rangle + |01001\rangle - |11011\rangle \\
&\quad + |10100\rangle - |00110\rangle - |11101\rangle - |01111\rangle \\
&\quad + |01010\rangle - |11000\rangle - |00011\rangle - |10001\rangle \\
&\quad - |11110\rangle - |01100\rangle - |10111\rangle + |00101\rangle)\\
|\overline{1}\rangle &= \tfrac{1}{4}(|11111\rangle + |01101\rangle + |10110\rangle - |00100\rangle \\
&\quad + |01011\rangle - |11001\rangle - |00010\rangle - |10000\rangle \\
&\quad + |10101\rangle - |00111\rangle - |11100\rangle - |01110\rangle \\
&\quad - |00001\rangle - |10011\rangle - |01000\rangle + |11010\rangle)~.
\end{split}
\end{align}
Logical Pauli operators are $\bar{X} = XXXXX$ and $\bar{Z} = ZZZZZ$ .
The code's automorphism group is the dihedral group of order 10  ([arXiv:2109.12735](https://arxiv.org/abs/2109.12735)).
A graph-code realization of the code uses a pentagon graph with an additional central input node  ([arXiv:quant-ph/0012111](https://arxiv.org/abs/quant-ph/0012111)).
The encoder-respecting form can be taken to have this shape  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).

It is the unique code for its parameters, up to equivalence  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043)).
Any five-qubit $2T$-transversal stabilizer code with distance $d>1$ must be the five-qubit code  ([arXiv:2306.12526](https://arxiv.org/abs/2306.12526)).

This code is sometimes referred to as the DiVincenzo-Shor code after a paper that studied the code's syndrome extraction circuits  ([arXiv:quant-ph/9605031](https://arxiv.org/abs/quant-ph/9605031)).

(source: raw/error-correction-zoo.md)

## Protection

Smallest stabilizer code that protects against a single error on any one qubit. Detects two-qubit errors.
The five-qubit perfect code approximately corrects a single AD error  ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002)).

## Encoders

- Nine single- and two-qubit unitaries, six of which are CNOT gates  ([arXiv:quant-ph/0410004](https://arxiv.org/abs/quant-ph/0410004)).
- Four generalized control gates, four Hadamard, and one $Z$ gate  ([doi:10.1201/9781420012293](https://doi.org/10.1201/9781420012293)).
- Evolution under stabilizer Hamiltonian  ([arXiv:1301.4796](https://arxiv.org/abs/1301.4796)).
- Four CNOT and five CPHASE gates  ([arXiv:1509.01239](https://arxiv.org/abs/1509.01239)).
- Reinforcement-learning discovery of logical-state-preparation circuits  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).
- Fault-tolerant logical one and logical minus state preparation in all-to-all and 2D grid connectivity  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).

## Transversal gates

- A non-Pauli Hadamard-phase "facet" gate $SH$ and three-qubit Clifford operation $M_3$  ([arXiv:quant-ph/9702029](https://arxiv.org/abs/quant-ph/9702029), [arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)). These realize the $2T$ binary tetrahedral subgroup of $SU(2)$.
- The entire logical Clifford group can be realized using fold-transversal gates  ([arXiv:1603.03948](https://arxiv.org/abs/1603.03948), [arXiv:2409.18175](https://arxiv.org/abs/2409.18175)).
- The code does not admit any non-Clifford transversal gates  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043)); in particular, see  ([arXiv:2011.00197](https://arxiv.org/abs/2011.00197)) for the case of collective $Z$ rotations.
- Transversal gates can be interpreted as monodromies under a particular notion of parallel transport  ([arXiv:1309.7062](https://arxiv.org/abs/1309.7062)).

## General gates

- Magic-state distillation protocol  ([arXiv:quant-ph/0403025](https://arxiv.org/abs/quant-ph/0403025)). One protocol distills the state $\ket{R}=\cos\beta\ket{0}+e^{\mathrm{i}\pi/4}\sin\beta\ket{1}$, with $\cos(2\beta)=1/\sqrt{3}$, using the fact that a transversal Clifford gate $R$ is a gadget for the code; the protocol projects five noisy $\ket{R}$ states onto the code space and suppresses the output error to $O(p^2)$ for independent input error probability $p$ .
- Pieceable fault-tolerant CZ, CNOT, and $CCZ$ gates  ([arXiv:1603.03948](https://arxiv.org/abs/1603.03948)).

## Decoders

- Ideal transversal computational-basis measurement distinguishes logical basis states by the parity of the outcome string, but this is not a fault-tolerant measurement gadget because a single faulty measurement bit can flip the decoded logical outcome .
- Fault-tolerant syndrome extraction circuits  ([arXiv:quant-ph/9605031](https://arxiv.org/abs/quant-ph/9605031), [arXiv:quant-ph/9608028](https://arxiv.org/abs/quant-ph/9608028)).
- Syndrome extraction circuit optimized for a linear qubit architecture  ([arXiv:quant-ph/0311116](https://arxiv.org/abs/quant-ph/0311116)).
- Combined dynamical decoupling and error correction protocol on individually-controlled qubits with always-on Ising couplings  ([arXiv:1509.01239](https://arxiv.org/abs/1509.01239)).
- Syndrome extraction circuit using only CNOT-SWAP gates  ([arXiv:2207.13356](https://arxiv.org/abs/2207.13356)).
- Symmetric decoder correcting all weight-one Pauli errors. The resulting logical error channel after coherent noise has been explicitly derived  ([arXiv:2203.01706](https://arxiv.org/abs/2203.01706)).
- Inspired by the honeycomb Floquet code, various weight-two measurement schemes have been designed  ([arXiv:2409.13681](https://arxiv.org/abs/2409.13681)).

## Fault tolerance

- Pieceable fault-tolerant CZ, CNOT, and $CCZ$ gates  ([arXiv:1603.03948](https://arxiv.org/abs/1603.03948)).
- A fault-tolerant logical $T$ gate can be obtained by encoding the five-qubit code's five physical qubits into the five logical qubits of a $⟦31,5,3⟧$ outer quantum divisible CSS code preserved by transversal $T^\dagger$; this layered construction can be viewed as a factorization of a $⟦31,1,3⟧$ triorthogonal code and does not require magic-state distillation  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
- Syndrome measurement can be done with two ancillary flag qubits  ([arXiv:1705.02329](https://arxiv.org/abs/1705.02329)). The depth of syndrome extraction circuits can be lowered by using past syndrome values  ([arXiv:2305.00784](https://arxiv.org/abs/2305.00784)).
- Fault-tolerant logical one and logical minus state preparation in all-to-all and 2D grid connectivity  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).
- Inspired by the honeycomb Floquet code, various weight-two measurement schemes have been designed  ([arXiv:2409.13681](https://arxiv.org/abs/2409.13681)).

## Realizations

- NMR: Implementation of perfect error correcting code on 5 spin subsystem of labeled crotonic acid for quantum network benchmarking  ([arXiv:quant-ph/0101034](https://arxiv.org/abs/quant-ph/0101034)). Single-qubit logical gates  ([arXiv:1208.4797](https://arxiv.org/abs/1208.4797)). Magic-state distillation using 7-qubit device  ([arXiv:1103.2178](https://arxiv.org/abs/1103.2178)).
- Superconducting qubits  ([arXiv:1907.04507](https://arxiv.org/abs/1907.04507)).
- Trapped-ion qubits: non-transversal CNOT gate between two logical qubits, including rounds of correction and fault-tolerant primitives such as flag qubits and pieceable fault tolerance, on a 12-qubit device by Quantinuum  ([arXiv:2208.01863](https://arxiv.org/abs/2208.01863)). Real-time magic-state distillation  ([arXiv:2310.12106](https://arxiv.org/abs/2310.12106)).
- Nitrogen-vacancy centers in diamond: fault-tolerant single-qubit Clifford operations using two ancillas  ([arXiv:2108.01646](https://arxiv.org/abs/2108.01646)). The fault-tolerant circuit yields better fidelity than the non-fault-tolerant circuit.

## Relations

- _parent_: [`twisted_xzzx`](https://errorcorrectionzoo.org/c/twisted_xzzx) — Twisted XZZX codes are 2D lattice extensions of the five-qubit perfect code. The five-qubit code is a small twisted XZZX toric code  ([arXiv:1108.5490](https://arxiv.org/abs/1108.5490)) ([arXiv:1212.6703](https://arxiv.org/abs/1212.6703)) ([arXiv:2101.09349](https://arxiv.org/abs/2101.09349)). Its genus-one double cover is a $⟦10,2,3⟧$ toric code  ([arXiv:1212.6703](https://arxiv.org/abs/1212.6703)) ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)). The base code's transversal $SH$ gate lifts to a logical $CX \cdot SWAP$ gate on that double cover  ([arXiv:2406.09951](https://arxiv.org/abs/2406.09951)).
- _parent_: [`stab_5_1_2_convolutional`](https://errorcorrectionzoo.org/c/stab_5_1_2_convolutional) — The $(5,1,2)$-convolutional code is a 1D lattice extension of the five-qubit perfect code, with the former's lattice-translation symmetry being the extension of the latter's cyclic permutation symmetry. The $(5,1,2)$-convolutional code reduces to the five-qubit code for a five-qubit chain and periodic boundary conditions. See Ref.  ([arXiv:2211.03094](https://arxiv.org/abs/2211.03094)) for the first few codes in a different extension of the five-qubit perfect code.
- _parent_: [`happy`](https://errorcorrectionzoo.org/c/happy) — The five-qubit code is the smallest (i.e., radius-one) single-qubit HaPPY code. The five-qubit encoding isometry tiles various holographic codes because its corresponding encoding isometry tensor is a perfect tensor  ([arXiv:1503.06237](https://arxiv.org/abs/1503.06237)).
- _parent_: [`quantum_perfect`](https://errorcorrectionzoo.org/c/quantum_perfect) — The five-qubit code is the smallest perfect code and is a member of the perfect qubit code family $⟦(4^r-1)/3, (4^r-1)/3 - 2r, 3⟧$ for $r = 2$.
- _parent_: [`stabilizer_over_gf4`](https://errorcorrectionzoo.org/c/stabilizer_over_gf4) — The five-qubit code is Hermitian , and is derived from the $[5,3,3]_4$ shortened hexacode via the qubit Hermitian construction  ([arXiv:quant-ph/0310137](https://arxiv.org/abs/quant-ph/0310137)) ([arXiv:quant-ph/0511016](https://arxiv.org/abs/quant-ph/0511016)).
- _parent_: [`quantum_mds`](https://errorcorrectionzoo.org/c/quantum_mds) — The only nontrivial qubit MDS codes have parameters $⟦5,1,3⟧$, $⟦6,0,4⟧$, and $⟦2m,2m-2,2⟧$ .
- _parent_: [`frobenius`](https://errorcorrectionzoo.org/c/frobenius) — The $⟦5,1,3⟧$ code is the smallest qubit Frobenius code  ([arXiv:1011.5814](https://arxiv.org/abs/1011.5814)).
- _parent_: [`qudit_5_1_3`](https://errorcorrectionzoo.org/c/qudit_5_1_3) — The $⟦5,1,3⟧_{\mathbb{Z}_q}$ modular-qudit code for $q=2$ reduces to the five-qubit perfect code.
- _parent_: [`galois_5_1_3`](https://errorcorrectionzoo.org/c/galois_5_1_3) — The $⟦5,1,3⟧_q$ Galois-qudit code for $q=2$ reduces to the five-qubit perfect code.
- _parent_: [`small_distance_qubit_stabilizer`](https://errorcorrectionzoo.org/c/small_distance_qubit_stabilizer)
- _cousin_: [`group_representation`](https://errorcorrectionzoo.org/c/group_representation) — The five-qubit code is a group-representation code with $G$ being the $2T$ subgroup of $SU(2)$  ([arXiv:2306.11621](https://arxiv.org/abs/2306.11621)).
- _cousin_: [`majorana_stab`](https://errorcorrectionzoo.org/c/majorana_stab) — The five-qubit code Hamiltonian is local when expressed in terms of mutually commuting Majorana operators .
- _cousin_: [`qubits_into_qubits`](https://errorcorrectionzoo.org/c/qubits_into_qubits) — Every $((5,2,3))$ qubit code is single-qubit-Clifford-equivalent equivalent to the five-qubit code  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043)).
- _cousin_: [`qubit_concatenated`](https://errorcorrectionzoo.org/c/qubit_concatenated) — The recursively concatenated five-qubit code has a measurement threshold of one  ([arXiv:2402.00145](https://arxiv.org/abs/2402.00145)). Code performance against general Pauli channels has been worked out  ([arXiv:quant-ph/0111003](https://arxiv.org/abs/quant-ph/0111003), [arXiv:quant-ph/0206061](https://arxiv.org/abs/quant-ph/0206061)).
- _cousin_: [`cluster_state`](https://errorcorrectionzoo.org/c/cluster_state) — The five-qubit perfect code is equivalent via a single-qubit Clifford circuit to a cluster-state code defined from a five-cycle (a.k.a. pentagon) graph and a classical repetition code  ([arXiv:0708.1021](https://arxiv.org/abs/0708.1021), [arXiv:1511.05647](https://arxiv.org/abs/1511.05647)) ([arXiv:1108.5490](https://arxiv.org/abs/1108.5490)).
- _cousin_: [`floquet`](https://errorcorrectionzoo.org/c/floquet) — Inspired by the honeycomb Floquet code, various weight-two measurement schemes have been designed for the five-qubit code  ([arXiv:2409.13681](https://arxiv.org/abs/2409.13681)).
- _cousin_: [`ampdamp`](https://errorcorrectionzoo.org/c/ampdamp) — The five-qubit perfect code approximately corrects a single AD error  ([arXiv:quant-ph/9704002](https://arxiv.org/abs/quant-ph/9704002)).
- _cousin_: [`quantum_divisible`](https://errorcorrectionzoo.org/c/quantum_divisible) — A fault-tolerant logical $T$ gate can be obtained by encoding the five-qubit code's five physical qubits into the five logical qubits of a $⟦31,5,3⟧$ outer quantum divisible CSS code preserved by transversal $T^\dagger$; this layered construction can be viewed as a factorization of a $⟦31,1,3⟧$ triorthogonal code and does not require magic-state distillation  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
- _cousin_: [`quantum_triorthogonal`](https://errorcorrectionzoo.org/c/quantum_triorthogonal) — A fault-tolerant logical $T$ gate can be obtained by encoding the five-qubit code's five physical qubits into the five logical qubits of a $⟦31,5,3⟧$ outer quantum divisible CSS code preserved by transversal $T^\dagger$; this layered construction can be viewed as a factorization of a $⟦31,1,3⟧$ triorthogonal code and does not require magic-state distillation  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
