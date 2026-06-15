---
type: concept
name: $⟦7,1,3⟧$ Steane code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/triangular-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/steane
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: steane
---

# $⟦7,1,3⟧$ Steane code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/steane) (`code_id: steane`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A $⟦7,1,3⟧$ self-dual CSS code that is the smallest qubit CSS code to correct a single-qubit error  ([arXiv:0803.1495](https://arxiv.org/abs/0803.1495)).
The code is constructed using the classical binary $[7,4,3]$ Hamming code for protecting against both $X$ and $Z$ errors.

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{ccccccc}
  I & I & I & X & X & X & X \\
  I & X & X & I & I & X & X \\
  X & I & X & I & X & I & X \\
  I & I & I & Z & Z & Z & Z \\
  I & Z & Z & I & I & Z & Z \\
  Z & I & Z & I & Z & I & Z
\end{array}~.
\end{align}
The code's stabilizer generator matrix blocks $H_{X}$ and $H_{Z}$ are both the parity-check matrix of the $[7,4,3]$ Hamming code.
The checks can be thought of as lying on the three trapezoids of the following tiling of the triangle.


The Steane code can also be thought of as a code on all corners of a cube except one  ([doi:10.1098/rsta.2011.0494](https://doi.org/10.1098/rsta.2011.0494), [arXiv:1306.4532](https://arxiv.org/abs/1306.4532)), and the code's encoder-respecting form is the graph of the full cube  ([arXiv:2411.14448](https://arxiv.org/abs/2411.14448)).

A set of logical codewords is
\begin{align}
\begin{split}
  |\overline{0}\rangle&=\frac{1}{\sqrt{8}}\Big(|0000000\rangle+|1010101\rangle+|0110011\rangle+|1100110\rangle\\&\,\,\,\,\,\,\,\,+|0001111\rangle+|1011010\rangle+|0111100\rangle+|1101001\rangle\Big)\\|\overline{1}\rangle&=\frac{1}{\sqrt{8}}\Big(|1111111\rangle+|0101010\rangle+|1001100\rangle+|0011001\rangle\\&\,\,\,\,\,\,\,\,+|1110000\rangle+|0100101\rangle+|1000011\rangle+|0010110\rangle\Big)~.
\end{split}
\end{align}

The automorphism group of the code is $PGL(3,2)$  ([arXiv:2109.12735](https://arxiv.org/abs/2109.12735)).
It is one of sixteen distinct indecomposable $⟦7,1,3⟧$ codes  ([arXiv:0709.1780](https://arxiv.org/abs/0709.1780)).

(source: raw/error-correction-zoo.md)

## Protection

The Steane code is a distance 3 code. It detects errors on 2 qubits, corrects errors on 1 qubit.

## Encoders

- Nine CNOT and four Hadamard gates  ([doi:10.1201/9781420012293](https://doi.org/10.1201/9781420012293)).
- Evolution under stabilizer Hamiltonian  ([arXiv:1301.4796](https://arxiv.org/abs/1301.4796)).
- Fault-tolerant logical zero and logical plus state preparation on all-to-all and 2D grid qubit connectivity  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).
- Parity-check encoding with flag-bridge qubits on a square lattice connectivity  ([arXiv:2504.01083](https://arxiv.org/abs/2504.01083)).

## Transversal gates

- The single-qubit Clifford group  ([arXiv:quant-ph/9605011](https://arxiv.org/abs/quant-ph/9605011), [arXiv:0706.1382](https://arxiv.org/abs/0706.1382)). More generally, $k$ copies of the Steane code form a $⟦7k,k,3⟧$ code that admits a $k$-fold transversal implementation of the full Clifford group on all $k$ logical qubits, showing the tightness of a no-go theorem that requires at least $k$-fold transversal gadgets for the full Clifford group  ([arXiv:2602.13395](https://arxiv.org/abs/2602.13395)).

## General gates

- Fault-tolerant approximations of arbitrary single-qubit gates  ([arXiv:quant-ph/0411206](https://arxiv.org/abs/quant-ph/0411206), [arXiv:quant-ph/0506126](https://arxiv.org/abs/quant-ph/0506126)).
- Non-fault-tolerant $T$ gate  ([arXiv:1303.4291](https://arxiv.org/abs/1303.4291)).
- Fault-tolerant logical zero and magic state preparation  ([doi:10.1038/srep19578](https://doi.org/10.1038/srep19578)). Magic-state preparation converts unbiased noise into biased noise  ([arXiv:2401.10982](https://arxiv.org/abs/2401.10982)).
- Because transversal Hadamard acts logically on the code, the Steane code serves as a normal self-dual inner code for magic-state distillation. One routine uses 14 noisy $T$ gates and one noisy input magic state to produce one output with cubic error suppression, and it can be pipelined with the $⟦17,1,5⟧$ code to obtain fifth-order suppression  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)).
- Pieceable fault-tolerant $CCZ$ gate  ([arXiv:1603.03948](https://arxiv.org/abs/1603.03948)).

## Decoders

- Shor error correction fidelity calculation  ([arXiv:1101.1950](https://arxiv.org/abs/1101.1950), [arXiv:1109.1714](https://arxiv.org/abs/1109.1714), [arXiv:1111.3930](https://arxiv.org/abs/1111.3930)).
- A $[15,3]$ syndrome-measurement code yields a QDS extension that uses the same 15 measurements as five-fold repetition of the three syndrome bits while achieving lower syndrome-decoding error  ([arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
- Fault-tolerant measurement-free error-correction cycle  ([arXiv:2307.13296](https://arxiv.org/abs/2307.13296)).

## Fault tolerance

- A fault-tolerant universal gate set can be done via code switching between the Steane code and the $⟦15,1,3⟧$ code  ([arXiv:1509.03239](https://arxiv.org/abs/1509.03239), [arXiv:1304.3709](https://arxiv.org/abs/1304.3709), [arXiv:1403.2734](https://arxiv.org/abs/1403.2734), [arXiv:1703.03860](https://arxiv.org/abs/1703.03860), [arXiv:2210.14074](https://arxiv.org/abs/2210.14074)).
- A fault-tolerant universal gate set can be done via code switching between the Steane code and the $⟦10,1,2⟧$ code  ([arXiv:2403.13732](https://arxiv.org/abs/2403.13732)).
- A fault-tolerant logical $T$ gate can be obtained by encoding the Steane code's seven physical qubits into the seven logical qubits of a $⟦63,7,3⟧$ outer quantum divisible CSS code preserved by transversal $T^\dagger$  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).
- Fault-tolerant logical zero and magic state preparation  ([doi:10.1038/srep19578](https://doi.org/10.1038/srep19578)). Magic-state preparation converts unbiased noise into biased noise  ([arXiv:2401.10982](https://arxiv.org/abs/2401.10982)).
- Fault-tolerant logical zero and logical plus state preparation on all-to-all and 2D grid qubit connectivity  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).
- Pieceable fault-tolerant $CCZ$ gate  ([arXiv:1603.03948](https://arxiv.org/abs/1603.03948)).
- Syndrome measurement can be done with ancillary flag qubits  ([arXiv:1705.02329](https://arxiv.org/abs/1705.02329)) or with no extra qubits  ([doi:10.1088/2058-9565/abc6f4](https://doi.org/10.1088/2058-9565/abc6f4)). The depth of syndrome extraction circuits can be lowered by using past syndrome values  ([arXiv:2305.00784](https://arxiv.org/abs/2305.00784)).
- Computation of ground-state energy of the hydrogen molecule  ([arXiv:2505.09133](https://arxiv.org/abs/2505.09133)).
- Fault-tolerant measurement-free error-correction cycle  ([arXiv:2307.13296](https://arxiv.org/abs/2307.13296)).

## Realizations

- Trapped-ion devices: seven-qubit device in Blatt group  ([arXiv:1403.5426](https://arxiv.org/abs/1403.5426)).
Ten-qubit QCCD device by Quantinuum  ([arXiv:2107.07505](https://arxiv.org/abs/2107.07505)) realizing repeated syndrome extraction, real-time look-up-table decoding (yielding lower logical SPAM error rate than physical SPAM), and non-fault-tolerant magic-state distillation (see APS Physics Synopsis  ([doi:10.1103/Physics.14.184](https://doi.org/10.1103/Physics.14.184))).
Fault-tolerant universal two-qubit gate set using T injection by Monz group  ([arXiv:2111.12654](https://arxiv.org/abs/2111.12654)).
Logical CNOT gate and Bell-pair creation between two logical qubits (yielding a logical fidelity higher than physical), including rounds of correction and fault-tolerant primitives such as flag qubits and pieceable fault tolerance, on a 20-qubit device by Quantinuum  ([arXiv:2208.01863](https://arxiv.org/abs/2208.01863)); logical fidelity interval of the combined preparation-CNOT-measurement procedure was higher than that of the unencoded physical qubits.
Multiple rounds of Steane error correction  ([arXiv:2312.09745](https://arxiv.org/abs/2312.09745)).
Fault-tolerant universal gate set via code switching between the Steane code and the $⟦10,1,2⟧$ code  ([arXiv:2403.13732](https://arxiv.org/abs/2403.13732)).
Post-selected fault-tolerant logical Bell-state preparation with logical error rates at least 10 times lower than physical rate on a device by Quantinuum  ([arXiv:2404.02280](https://arxiv.org/abs/2404.02280)).
The quantum Fourier transform on three code blocks  ([arXiv:2404.08616](https://arxiv.org/abs/2404.08616)).
Fault-tolerant transversal and lattice-surgery state teleportation protocols as well as Knill error correction  ([arXiv:2404.16728](https://arxiv.org/abs/2404.16728)).
Rains shadow enumerators have been measured  ([arXiv:2408.16914](https://arxiv.org/abs/2408.16914)).
Inter-block CNOT gates have been characterized via cycle reconstruction  ([arXiv:2504.12099](https://arxiv.org/abs/2504.12099)).
Code switching between the Steane code and the $⟦15,1,3⟧$ code as well as magic-state preparation and logical Bell measurements on the Steane code realized on the 28-qubit H2-1 device by Quantinuum  ([arXiv:2506.14169](https://arxiv.org/abs/2506.14169)).
End-to-end fault-tolerant execution of QAOA and HHL circuits, including logical non-Clifford operations, with up to 12 logical qubits on Quantinuum systems  ([arXiv:2603.04584](https://arxiv.org/abs/2603.04584)).
- Neutral atom arrays: Lukin group. Ten logical qubits, transversal CNOT gate performed, logical ten-qubit GHZ state initialized with break-even fidelity, and fault-tolerant logical two-qubit GHZ state initialized  ([arXiv:2312.03982](https://arxiv.org/abs/2312.03982)). Deep-circuit protocols with dozens of logical qubits and hundreds of logical teleportations  ([arXiv:2506.20661](https://arxiv.org/abs/2506.20661)).

## Relations

- _parent_: [[concepts/qec/triangular-color]] — Steane code is a 2D color code defined on a seven-qubit patch of the 6.6.6 tiling.
- _parent_: [`diagonal_clifford`](https://errorcorrectionzoo.org/c/diagonal_clifford)
- _parent_: [`quantum_hamming_css`](https://errorcorrectionzoo.org/c/quantum_hamming_css)
- _parent_: [`single_qubit_clifford`](https://errorcorrectionzoo.org/c/single_qubit_clifford)
- _parent_: [`stabilizer_over_gf4`](https://errorcorrectionzoo.org/c/stabilizer_over_gf4) — The Steane code is Hermitian  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
- _parent_: [`quantum_cyclic`](https://errorcorrectionzoo.org/c/quantum_cyclic) — The Steane code is equivalent to a cyclic code via qubit permutations  ([arXiv:1108.5490](https://arxiv.org/abs/1108.5490)).
- _parent_: [`galois_quad_residue`](https://errorcorrectionzoo.org/c/galois_quad_residue) — The Steane code is a qubit quantum QR code  ([arXiv:0712.0103](https://arxiv.org/abs/0712.0103), [arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
- _parent_: [`data_syndrome`](https://errorcorrectionzoo.org/c/data_syndrome) — There exists a set of stabilizer generators for the Steane code that make it a QDS code; a $[15,3]$ syndrome-measurement code beats five-fold repeated syndrome extraction at the same measurement cost  ([arXiv:1409.2559](https://arxiv.org/abs/1409.2559), [arXiv:1907.01393](https://arxiv.org/abs/1907.01393)).
- _parent_: [`pg_qldpc`](https://errorcorrectionzoo.org/c/pg_qldpc) — The Steane code is the $m=1$ member of the $⟦2^{2m}+2^{m}+1,1,>2^{m}⟧$ PG-QLDPC code family that is constructed from codes corresponding to lines and affine charts in $PG(2,2^m)$ via the CSS construction  ([arXiv:1512.07081](https://arxiv.org/abs/1512.07081)).
- _parent_: [`concatenated_steane`](https://errorcorrectionzoo.org/c/concatenated_steane) — The concatenated Steane code at level $m=1$ is the Steane code.
- _parent_: [`block_perfect`](https://errorcorrectionzoo.org/c/block_perfect) — The Steane code is the smallest heptagon holographic code. The encoding of more general heptagon holographic codes is a holographic tensor network consisting of the encoding isometry for the Steane code, which is a planar-perfect tensor.
- _cousin_: [`group_representation`](https://errorcorrectionzoo.org/c/group_representation) — The Steane code is a group-representation code with $G$ being the $2O$ subgroup of $SU(2)$  ([arXiv:2306.11621](https://arxiv.org/abs/2306.11621)).
- _cousin_: [`cluster_state`](https://errorcorrectionzoo.org/c/cluster_state) — The Steane code is equivalent via a single-qubit Clifford unitary to a cluster-state code for a particular graph and classical code  ([arXiv:1108.5490](https://arxiv.org/abs/1108.5490)). Four non-isomorphic graphs yield graph quantum codes that are equivalent to the Steane code under a single-qubit-Clifford circuit  ([arXiv:quant-ph/0703112](https://arxiv.org/abs/quant-ph/0703112)).
- _cousin_: [`eastab`](https://errorcorrectionzoo.org/c/eastab) — The Steane code is globally equivalent to a $⟦6,1,3;1⟧$ EA CSS code, which the paper identifies as an example of the smallest one-ebit EA CSS code correcting an arbitrary single-qubit error on the sender's qubits  ([arXiv:0803.1495](https://arxiv.org/abs/0803.1495)).
- _cousin_: [`stab_6_2_2`](https://errorcorrectionzoo.org/c/stab_6_2_2) — In Knill's $C_4/C_6$ architecture, noisy $\ket{\pi/8}$ states are injected using $C_4/C_6$ logical Bell pairs and then purified by encoding them into the Steane code; Knill also proposed using the Steane code as a final concatenation level for the $C_4/C_6$ scheme  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199)).
- _cousin_: [`quantum_divisible`](https://errorcorrectionzoo.org/c/quantum_divisible) — A fault-tolerant logical $T$ gate can be obtained by encoding the Steane code's seven physical qubits into the seven logical qubits of a $⟦63,7,3⟧$ outer quantum divisible CSS code preserved by transversal $T^\dagger$  ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)).

## Notes

- Pedagogical explanation of QEC using the Steane code  ([arXiv:quant-ph/9705031](https://arxiv.org/abs/quant-ph/9705031)).
- The Steane code can be used for entanglement purification  ([arXiv:0811.2639](https://arxiv.org/abs/0811.2639)).
