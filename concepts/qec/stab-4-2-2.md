---
type: concept
name: $⟦4,2,2⟧$ Four-qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- $C_4$ code
- Little Shor code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/4612-color
- concepts/qec/488-color
- concepts/qec/brickwork
- concepts/qec/cpc
- concepts/qec/group-4-2-2
- concepts/qec/hypercube-quantum
- concepts/qec/iceberg
- concepts/qec/jump
- concepts/qec/phantom
- concepts/qec/qubit-concatenated
- concepts/qec/rotated-surface
- concepts/qec/stab-5-1-3
- concepts/qec/stab-6-2-2
- concepts/qec/stab-6-4-2
- concepts/qec/steane
- concepts/qec/surface
- concepts/qec/toric
- concepts/qec/triangular-color
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/stab_4_2_2
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: stab_4_2_2
---

# $⟦4,2,2⟧$ Four-qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/stab_4_2_2) (`code_id: stab_4_2_2`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A four-qubit hyperbolic self-dual CSS stabilizer code that is the smallest two-logical-qubit stabilizer code to detect a single-qubit error.
It is unique for its parameters  ([arXiv:quant-ph/9704043](https://arxiv.org/abs/quant-ph/9704043)).

A stabilizer tableau for the code is given by 
\begin{align}
\begin{array}{cccc}
  Z & Z & Z & Z \\
  X & X & X & X
\end{array}~.
\end{align}
Its stabilizer generator matrix blocks, $H_{X}=H_{Z}=(1,1,1,1)$, are both the parity-check matrix of the $[4,3,2]$ SPC code.
A basis of codewords is
\begin{align}
  \begin{split}
    |\overline{00}\rangle = (|0000\rangle + |1111\rangle)/\sqrt{2}~{\phantom{.}}\\
    |\overline{01}\rangle = (|0011\rangle + |1100\rangle)/\sqrt{2}~{\phantom{.}}\\
    |\overline{10}\rangle = (|0101\rangle + |1010\rangle)/\sqrt{2}~{\phantom{.}}\\
    |\overline{11}\rangle = (|0110\rangle + |1001\rangle)/\sqrt{2}~.
  \end{split}
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

Detects a single-qubit error  ([arXiv:quant-ph/9603031](https://arxiv.org/abs/quant-ph/9603031)) or single erasure  ([arXiv:quant-ph/9610042](https://arxiv.org/abs/quant-ph/9610042)).
It cannot correct arbitrary single-qubit errors because $ \lfloor \frac{d-1}{2} \rfloor =0 $.
An equivalent version of this code can suppress errors in adiabatic quantum computation by being used as an excited-state space of a particular Hamiltonian  ([arXiv:2412.07764](https://arxiv.org/abs/2412.07764)).

## Magic scaling exponent

Various magic-state distillation protocols exist for the $⟦4,2,2⟧$ qubit code and the $C_6$ code in what are known as Meier-Eastin-Knill (MEK) protocols  ([arXiv:1204.4221](https://arxiv.org/abs/1204.4221), [arXiv:1703.07847](https://arxiv.org/abs/1703.07847)). In the inner/outer-code formulation of Ref.  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)), the $⟦4,2,2⟧$ code is a hyperbolic self-dual inner code for quadratic distillation. For example, the magic-state yield parameter is $\gamma = \log_2 5 \approx 2.322$ for a protocol using the $⟦10,2,2⟧$ code  ([arXiv:1612.07330](https://arxiv.org/abs/1612.07330)); see also  ([arXiv:1709.02789](https://arxiv.org/abs/1709.02789)).

## Transversal gates

- A tensor product of Hadamard gates applies a Hadamard gate to both logical qubits, and a tensor product of $S=\sqrt{Z}$ gates applies a $CZ$ gate followed by a logical $Z$ on both qubits  ([arXiv:1610.03507](https://arxiv.org/abs/1610.03507)) (see also  ([arXiv:1912.10063](https://arxiv.org/abs/1912.10063))). A logical $CZ$ gate is then realized by $\sqrt{Z}\otimes\sqrt{Z}^{\dagger}\otimes\sqrt{Z}^{\dagger}\otimes\sqrt{Z}$. With a different logical basis, transversal Hadamard swaps the two logical qubits, enabling control-SWAP and $H^{\otimes 2}$-measurement routines for quadratic magic-state distillation  ([arXiv:1703.07847](https://arxiv.org/abs/1703.07847)).
- This code is the only four-qubit subspace to house a transversal representation of the single-qubit Clifford group but not of the single-qubit unitary group  ([arXiv:1609.08172](https://arxiv.org/abs/1609.08172)). Equivalently, its projector is the only extra generator of the fourth tensor-power Clifford commutant beyond qubit permutations  ([arXiv:1609.08172](https://arxiv.org/abs/1609.08172)). Its $n$-block version is a $⟦4n,2n,2⟧$ code, which houses a signed permutation representation of the $n$-qubit Clifford group  ([arXiv:1609.08172](https://arxiv.org/abs/1609.08172)).

## General gates

- Some inter-block gates can be weight-two (two-body) with the help of perturbative gadgets, making it possible to suppress errors in adiabatic quantum computation  ([arXiv:2412.07764](https://arxiv.org/abs/2412.07764)).
- Logical Clifford circuits for various qubit connectivities  ([arXiv:2505.20261](https://arxiv.org/abs/2505.20261)).

## Decoders

- Erasure decoder  ([arXiv:quant-ph/0306098](https://arxiv.org/abs/quant-ph/0306098)).

## Fault tolerance

- Preparation of certain states, both magic and non-magic, along with transversal gates can be performed fault-tolerantly, but requires post-selection because the code cannot correct errors  ([arXiv:1610.03507](https://arxiv.org/abs/1610.03507)). Magic states can be injected into surface and color codes since the code is a small instance of both  ([arXiv:2305.13581](https://arxiv.org/abs/2305.13581)).
- Knill's $C_4/C_6$ architecture uses the $⟦4,2,2⟧$ code at the first level and the $C_6$ code at higher levels, together with error-correcting teleportation  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199)). Later work refined the postselected-threshold analysis  ([arXiv:quant-ph/0608018](https://arxiv.org/abs/quant-ph/0608018), [arXiv:quant-ph/0703264](https://arxiv.org/abs/quant-ph/0703264)) (see also Ref.  ([arXiv:quant-ph/0612073](https://arxiv.org/abs/quant-ph/0612073))).
- Concatenating quantum Hamming codes on top of the $⟦4,2,2⟧$ and $C_6$ codes yields fault-tolerant quantum computation with constant space and quasi-polylogarithmic time overheads  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)). In the optimized protocol of Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), a level-five $C_4/C_6$ code underlies concatenated quantum Hamming codes $\mathcal{Q}_5,\mathcal{Q}_6,\mathcal{Q}_7,\mathcal{Q}_7$, yielding a $2.5\%$ threshold and space overheads $162$ and $373$ physical qubits per logical qubit at physical error rate $0.1\%$ for logical CNOT error rates $10^{-10}$ and $10^{-24}$, respectively.
- Fault-tolerant implementation of the Deutsch-Jozsa algorithm  ([arXiv:2412.04791](https://arxiv.org/abs/2412.04791)).

## Realizations

- See also  ([arXiv:2412.07670](https://arxiv.org/abs/2412.07670)) for more details on each experimental realization.
- Trapped-ion device by IonQ  ([arXiv:1611.06946](https://arxiv.org/abs/1611.06946)).
- Logical state preparation and flag-qubit error correction realized in superconducting-circuit devices by IBM  ([arXiv:1705.09259](https://arxiv.org/abs/1705.09259), [arXiv:1705.08957](https://arxiv.org/abs/1705.08957), [arXiv:1806.02359](https://arxiv.org/abs/1806.02359), [arXiv:2110.04285](https://arxiv.org/abs/2110.04285)).
- The CZ magic state has been realized on an IBM heavy-hex superconducting circuit device  ([arXiv:2305.13581](https://arxiv.org/abs/2305.13581)).
- CPC gadgets for the $⟦4,2,2⟧$ code have been implemented on the IBM 5Q superconducting device  ([arXiv:1709.01866](https://arxiv.org/abs/1709.01866)).
- An FPGA implementation of the collision clustering decoder  ([arXiv:2309.05558](https://arxiv.org/abs/2309.05558)) realized on a Rigetti superconducting device  ([arXiv:2410.05202](https://arxiv.org/abs/2410.05202)).
- Neutral atom arrays: error detection, erasure correction, and post-selected fault-tolerant circuits demonstrated on 24 logical qubits on a 256-qubit device by Atom Computing, with each qubit encoded in the $⟦4,2,2⟧$ code  ([arXiv:2411.11822](https://arxiv.org/abs/2411.11822)). 
Post-selected fault-tolerant realization of a benchmarking protocol  ([arXiv:1610.03507](https://arxiv.org/abs/1610.03507)), preparation of the ground state of the single-impurity Anderson impurity model, and post-selected fault-tolerant logical Bell-state preparation demonstrated on one copy of the $⟦4,2,2⟧$ code on a device by Infleqtion  ([arXiv:2412.07670](https://arxiv.org/abs/2412.07670)).
Error correction with mid-circuit erasure measurements and logical teleportation demonstrated by the Thompson group  ([arXiv:2506.13724](https://arxiv.org/abs/2506.13724)). Logical implementation of Shor's algorithm on a device by Infleqtion  ([arXiv:2509.13247](https://arxiv.org/abs/2509.13247)).
- The $⟦4,2,2⟧$ code has been implemented on a star topology using superconducting devices and microwave cavities  ([arXiv:2503.12869](https://arxiv.org/abs/2503.12869)).
- Trapped-ion processor by AQT: modular logical-state teleportation between two four-qubit error-detecting code blocks without mid-circuit measurements  ([arXiv:2506.22600](https://arxiv.org/abs/2506.22600)).

## Relations

- _parent_: [[concepts/qec/rotated-surface]] — The $⟦4,2,2⟧$ code is the smallest rotated toric code  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).
- _parent_: [[concepts/qec/488-color]] — The $⟦4,2,2⟧$ code can be interpreted as a 2D color code on a square of the 4.8.8 tiling  ([arXiv:2212.00042](https://arxiv.org/abs/2212.00042), [arXiv:2305.13581](https://arxiv.org/abs/2305.13581)). Removing $X$ checks from blue octagons and $Z$ checks from green octagons of the 4.8.8 color code yields a light 4.8.8 color code that is equivalent to concatenating the surface/toric code with the $⟦4,2,2⟧$ code  ([arXiv:1604.04062](https://arxiv.org/abs/1604.04062)).
- _parent_: [[concepts/qec/triangular-color]] — The $⟦4,2,2⟧$ code can be interpreted as a 2D color code on a trapezoidal patch that makes up two-thirds of a hexagon of the 6.6.6 tiling  ([arXiv:2212.00042](https://arxiv.org/abs/2212.00042), [arXiv:2305.13581](https://arxiv.org/abs/2305.13581)).
- _parent_: [[concepts/qec/4612-color]] — The $⟦4,2,2⟧$ code can be interpreted as a 2D color code on a square of the 4.6.12 tiling  ([arXiv:2212.00042](https://arxiv.org/abs/2212.00042), [arXiv:2305.13581](https://arxiv.org/abs/2305.13581)). Concatenating the $⟦4,2,2⟧$ code with two copies of the surface code on a hexagonal lattice yields the self-dual 4.6.12 color code  ([arXiv:1604.04062](https://arxiv.org/abs/1604.04062)).
- _parent_: [[concepts/qec/hypercube-quantum]] — The $⟦4,2,2⟧$ code is a hypercube code for $D=2$.
- _parent_: [[concepts/qec/iceberg]] — The $⟦2m,2m-2,2⟧$ error-detecting code for $m=2$ reduces to the $⟦4,2,2⟧$ code.
- _parent_: [[concepts/qec/brickwork]] — The $⟦4,2,2⟧$ code can be interpreted as a brickwork code on a square of the overlapping rectangular tilings  ([arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).
- _parent_: [[concepts/qec/group-4-2-2]] — The four group-qudit code reduces to the four-qubit code for $G=\mathbb{Z}_2$.
- _cousin_: [[concepts/qec/stab-5-1-3]] — The $⟦4,2,2⟧$ code can be derived from the five-qubit code using a protocol that converts an $⟦n,k,d⟧$ code into an $⟦n-1, k+1, d-1⟧$ code  ([arXiv:quant-ph/9705052](https://arxiv.org/abs/quant-ph/9705052)) ([arXiv:1907.11253](https://arxiv.org/abs/1907.11253)).
- _cousin_: [[concepts/qec/surface]] — Concatenating the $⟦4,2,2⟧$ code with the surface code is equivalent to removing stabilizer generators from the 4.8.8 color code  ([arXiv:1604.04062](https://arxiv.org/abs/1604.04062)).
- _cousin_: [[concepts/qec/toric]] — The toric code can be constructed by arranging $⟦4,2,2⟧$ tensors on a square lattice and recovering the star and plaquette operators by operator pushing  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
- _cousin_: [[concepts/qec/qubit-concatenated]] — Concatenations of $⟦4,2,2⟧$ and $C_6$ codes yield fault-tolerant quantum computation schemes  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199)) admitting a post-selected threshold  ([arXiv:quant-ph/0608018](https://arxiv.org/abs/quant-ph/0608018), [arXiv:quant-ph/0703264](https://arxiv.org/abs/quant-ph/0703264)) (see also Ref.  ([arXiv:quant-ph/0612073](https://arxiv.org/abs/quant-ph/0612073))).
Concatenating quantum Hamming codes on top of the $⟦4,2,2⟧$ and $C_6$ codes yields fault-tolerant quantum computation with constant space and quasi-polylogarithmic time overheads  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)). In the optimized protocol of Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), a level-five $C_4/C_6$ code underlies concatenated quantum Hamming codes $\mathcal{Q}_5,\mathcal{Q}_6,\mathcal{Q}_7,\mathcal{Q}_7$, yielding a $2.5\%$ threshold and space overheads $162$ and $373$ physical qubits per logical qubit at physical error rate $0.1\%$ for logical CNOT error rates $10^{-10}$ and $10^{-24}$, respectively.
Concatenating the $⟦4,2,2⟧$ code with the surface code is equivalent to removing stabilizer generators from the 4.8.8 color code  ([arXiv:1604.04062](https://arxiv.org/abs/1604.04062)).
The $⟦4,2,2⟧$ code can be concatenated with two copies of the surface code to yield the 4.6.12 color code  ([arXiv:1604.04062](https://arxiv.org/abs/1604.04062)).
- _cousin_: [[concepts/qec/stab-6-2-2]] — Concatenations of $⟦4,2,2⟧$ and $C_6$ codes yield fault-tolerant quantum computation schemes  ([arXiv:quant-ph/0410199](https://arxiv.org/abs/quant-ph/0410199)) admitting a post-selected threshold  ([arXiv:quant-ph/0608018](https://arxiv.org/abs/quant-ph/0608018), [arXiv:quant-ph/0703264](https://arxiv.org/abs/quant-ph/0703264)) (see also Ref.  ([arXiv:quant-ph/0612073](https://arxiv.org/abs/quant-ph/0612073))) and the Meier-Eastin-Knill (MEK) magic-state distillation protocols  ([arXiv:1204.4221](https://arxiv.org/abs/1204.4221)). Concatenating quantum Hamming codes on top of the $⟦4,2,2⟧$ and $C_6$ codes yields fault-tolerant quantum computation with constant space and quasi-polylogarithmic time overheads  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)). In the optimized protocol of Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), a level-five $C_4/C_6$ code underlies concatenated quantum Hamming codes $\mathcal{Q}_5,\mathcal{Q}_6,\mathcal{Q}_7,\mathcal{Q}_7$, yielding a $2.5\%$ threshold and space overheads $162$ and $373$ physical qubits per logical qubit at physical error rate $0.1\%$ for logical CNOT error rates $10^{-10}$ and $10^{-24}$, respectively.
- _cousin_: [[concepts/qec/steane]] — The Steane code can be built from two $⟦4,2,2⟧$ codes in the quantum Lego code framework  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)). Ref.  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)) also introduces a $C_4$/Steane concatenated code, obtained by concatenating the $⟦4,2,2⟧$ code with the Steane code, as an underlying code for further concatenation with quantum Hamming codes.
- _cousin_: [[concepts/qec/stab-6-4-2]] — The $⟦6,4,2⟧$ error-detecting code can be constructed out of two $⟦4,2,2⟧$ codes in the quantum Lego code framework  ([arXiv:2109.08158](https://arxiv.org/abs/2109.08158)).
- _cousin_: [[concepts/qec/cpc]] — CPC gadgets for the $⟦4,2,2⟧$ code have been implemented on the IBM 5Q superconducting device  ([arXiv:1709.01866](https://arxiv.org/abs/1709.01866)).
- _cousin_: [[concepts/qec/jump]] — A $((4,3,1))_2$ jump code is a subcode of the $⟦4,2,2⟧$ code and contains the $⟦4,1,2⟧$ LNCY code as a subcode  ([arXiv:quant-ph/0208140](https://arxiv.org/abs/quant-ph/0208140)).
- _cousin_: [[concepts/qec/phantom]] — The $⟦4,2,2⟧$ code is the smallest phantom code: logical CNOT gates between its two logical qubits can be implemented by physical-qubit permutations  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)). Gluing copies of the $⟦4,2,2⟧$ code with $X$-type stabilizers yields CSS phantom codes with parameters $⟦4m,2,(d_X=2,d_Z=2m)⟧$, and puncturing one qubit from this construction yields $⟦4m-1,2,(d_X=2,d_Z=2m-1)⟧$, for $m\geq1$  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).
