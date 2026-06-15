---
type: concept
name: Kitaev surface code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/clifford-deformed-surface
- concepts/qec/galois-topological
- concepts/qec/hamiltonian
- concepts/qec/higher-dimensional-surface
- concepts/qec/hypergraph-product
- concepts/qec/lacross
- concepts/qec/layer
- concepts/qec/lcs
- concepts/qec/lresc
- concepts/qec/quantum-double
- concepts/qec/qudit-surface
- concepts/qec/twist-defect-surface
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/surface
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: surface
---

# Kitaev surface code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/surface) (`code_id: surface`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

A family of Abelian topological CSS stabilizer codes
whose generators are few-body $X$-type and $Z$-type Pauli strings
associated to the stars and plaquettes, respectively, of a cellulation of a
two-dimensional surface (with a qubit located at each edge of the
cellulation).
Codewords correspond to ground states of the surface code Hamiltonian, and error operators create or annihilate pairs of anyonic charges or vortices.

The construction on a torus is called the toric code, while the construction on a planar patch with boundaries is called the *planar code*  ([arXiv:quant-ph/9810055](https://arxiv.org/abs/quant-ph/9810055), [arXiv:quant-ph/9811052](https://arxiv.org/abs/quant-ph/9811052)).
Boundary segments come in two types, *open* (a.k.a. rough or primal) and *closed* (a.k.a. smooth or dual); logical operators on patches with boundary are naturally described by relative homology classes  ([arXiv:quant-ph/9811052](https://arxiv.org/abs/quant-ph/9811052)).
In the homological formulation, a cellulation of a closed surface $M$ encodes $k=2-\chi(M)$ qubits, while a cellulation of a surface with boundary encodes $k=1-\chi(M)$ qubits; cutting handles of closed surfaces yields planar patches with holes  ([arXiv:quant-ph/0605094](https://arxiv.org/abs/quant-ph/0605094)).
A *mixed boundary* consists of an interleaving of the two boundary types  ([arXiv:1606.07116](https://arxiv.org/abs/1606.07116)).

(source: raw/error-correction-zoo.md)

## Protection

The original planar code on a square-lattice patch with different boundary conditions on the vertical and horizontal edges is a $⟦L^2+(L-1)^2,1,L⟧$ CSS code  ([arXiv:quant-ph/9810055](https://arxiv.org/abs/quant-ph/9810055)).
On a closed orientable surface of genus $g$, the codespace has dimension $2^{2g}$, i.e., the code encodes $k=2g$ logical qubits; such higher-genus surfaces have been investigated  ([arXiv:quant-ph/9811052](https://arxiv.org/abs/quant-ph/9811052), [arXiv:2307.04418](https://arxiv.org/abs/2307.04418)).
Planar patches with holes or mixed boundaries can encode multiple logical qubits, and mixed-boundary layouts can reduce planar overhead by about a factor of three compared with punctured square-lattice constructions  ([arXiv:1606.07116](https://arxiv.org/abs/1606.07116)).
The surface code has also been shown to be resilient to burst errors  ([arXiv:2406.18897](https://arxiv.org/abs/2406.18897)).


\subsection{Topological order and gauge-theory analogy}
When treated as ground states of the code Hamiltonian, the code states realize $\mathbb{Z}_2$ topological order, a topological phase of matter that also exists in $\mathbb{Z}_2$ lattice gauge theory  ([doi:10.1063/1.1665530](https://doi.org/10.1063/1.1665530)).
For sufficiently weak local perturbations on closed surfaces, the splitting of this topological ground-state degeneracy is exponentially small in the shortest linear lattice size  ([arXiv:quant-ph/9707021](https://arxiv.org/abs/quant-ph/9707021)).
This order does not persist at nonzero temperature  ([arXiv:1106.6026](https://arxiv.org/abs/1106.6026), [arXiv:2310.08639](https://arxiv.org/abs/2310.08639)).

Pauli noise operators can be organized into anyonic strings of the gauge theory, which cause excitations of the ground-state subspace.
The inability of local errors to distinguish the codewords translates to the "topologically protected" degeneracy of the ground state, rigorously formulated by the TQO-1 condition.
The joint $+1$-eigenspace of the $Z$-type Paulis corresponds to the subspace that conserves $\mathbb{Z}_2$ flux, while the joint $+1$-eigenspace of $X$-type operators corresponds to the subspace that preserves $\mathbb{Z}_2$ gauge symmetry (a one-form symmetry).
Logical Pauli operators correspond to non-contractible Wilson loops in the case of closed boundaries, and to paths connecting different types of boundaries in the case of open boundaries.

Behavior under Hamiltonian $X$-type and $Z$-type perturbations is related to an anisotropic 3D gauge Higgs model  ([arXiv:cond-mat/0609048](https://arxiv.org/abs/cond-mat/0609048), [arXiv:0804.3175](https://arxiv.org/abs/0804.3175), [arXiv:0807.0487](https://arxiv.org/abs/0807.0487), [arXiv:1201.6409](https://arxiv.org/abs/1201.6409), [arXiv:1411.5815](https://arxiv.org/abs/1411.5815)).
In order to corrupt logical states, any local noise must bring the code state out of the topological order  ([arXiv:2310.08639](https://arxiv.org/abs/2310.08639)).  

Alternatively, there is a general correspondence between stabilizer codes and gauge theory, with the stabilizer group playing the role of the gauge group  ([arXiv:2412.15317](https://arxiv.org/abs/2412.15317)).
In this interpretation, both the $X$ and $Z$ stabilizers are gauge group elements.

## Rate

Both the planar and toric codes saturate the BPT bound, which states that $k d^2 = O(L^2)$ for codes on a 2D lattice of length $O(L)$.

## Encoders

- A depth-$L^2$ circuit that grows the code out of a small patch on an $L\times L$ square lattice using CNOT gates (i.e., "local moves")  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:0712.0348](https://arxiv.org/abs/0712.0348)).
- Teleportation-based state injection into the planar code  ([arXiv:1202.1016](https://arxiv.org/abs/1202.1016)).
- Graph-state based adaptive circuit  ([arXiv:quant-ph/0703143](https://arxiv.org/abs/quant-ph/0703143), [arXiv:1105.2111](https://arxiv.org/abs/1105.2111)).
- For an $L\times L$ lattice, deterministic state preparation can be done with a geometrically local unitary $O(L)$-depth circuit  ([arXiv:2002.00362](https://arxiv.org/abs/2002.00362), [arXiv:2110.02020](https://arxiv.org/abs/2110.02020)) or an $O(\log{L})$-depth unitary circuit with non-local two-qubit gates  ([arXiv:0712.0348](https://arxiv.org/abs/0712.0348), [arXiv:0806.4583](https://arxiv.org/abs/0806.4583), [arXiv:1207.0253](https://arxiv.org/abs/1207.0253)) (matching lower bounds  ([arXiv:quant-ph/0603121](https://arxiv.org/abs/quant-ph/0603121), [arXiv:quant-ph/0603114](https://arxiv.org/abs/quant-ph/0603114), [arXiv:1810.03912](https://arxiv.org/abs/1810.03912))). The geometric entanglement measure of a ground state of the surface code scales as order $\Omega(L^2)$  ([arXiv:2405.07970](https://arxiv.org/abs/2405.07970)).
- Stabilizer measurement-based circuit of linear depth  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:1404.2495](https://arxiv.org/abs/1404.2495)).
- Any geometrically local unitary circuit on a lattice $\Lambda$ that prepares a state whose energy density with respect to the surface code Hamiltonian is $\epsilon$ must have depth of order $\Omega( \min(\sqrt{|\Lambda|}, 1/\epsilon^{\frac{1-\alpha}{2}}) )$ for any $\alpha>0$  ([arXiv:2210.06796](https://arxiv.org/abs/2210.06796)).
- Single-shot state preparation  ([arXiv:1904.01502](https://arxiv.org/abs/1904.01502)), with MWPM decoding for such schemes  ([arXiv:2209.09774](https://arxiv.org/abs/2209.09774)).
- Various techniques to generate lattices useful for particular architectures  ([arXiv:2111.13729](https://arxiv.org/abs/2111.13729)) or removing lattice defects  ([arXiv:2211.08468](https://arxiv.org/abs/2211.08468), [arXiv:2405.06941](https://arxiv.org/abs/2405.06941)) exist.
- Fault-tolerant constant-depth encoder and unencoder using measurements  ([arXiv:2408.06299](https://arxiv.org/abs/2408.06299)).

## Transversal gates

- Folded surface codes, which are local-Clifford equivalent to triangular color codes with three differently colored boundaries, admit transversal Clifford gates  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065), [arXiv:1603.02286](https://arxiv.org/abs/1603.02286)).
- Fold-transversal initialization of the $|Y\rangle$ logical state  ([arXiv:1603.02286](https://arxiv.org/abs/1603.02286), [arXiv:2302.07395](https://arxiv.org/abs/2302.07395), [arXiv:2302.12292](https://arxiv.org/abs/2302.12292), [arXiv:2502.00957](https://arxiv.org/abs/2502.00957)).

## General gates

- Clifford gates can be implemented via lattice surgery
 ([arXiv:1111.4022](https://arxiv.org/abs/1111.4022), [arXiv:1709.02318](https://arxiv.org/abs/1709.02318), [arXiv:1808.02892](https://arxiv.org/abs/1808.02892), [arXiv:2109.02746](https://arxiv.org/abs/2109.02746)). Gauging logical operators directly generalizes lattice surgery and recovers conventional surface-code lattice surgery for suitable graph choices  ([arXiv:2410.02213](https://arxiv.org/abs/2410.02213)).
- Logical Hadamard gate  ([arXiv:1202.2639](https://arxiv.org/abs/1202.2639)).
- Non-Clifford gates can be implemented using magic-state distillation
 ([arXiv:1905.06903](https://arxiv.org/abs/1905.06903)), Dehn twists  ([arXiv:1703.00590](https://arxiv.org/abs/1703.00590), [arXiv:1806.06078](https://arxiv.org/abs/1806.06078)), or
just-in-time decoding  ([arXiv:1903.11634](https://arxiv.org/abs/1903.11634), [arXiv:2412.12529](https://arxiv.org/abs/2412.12529), [arXiv:2503.15751](https://arxiv.org/abs/2503.15751)).
- Non-stabilizer surface-code states can be prepared by augmenting the code with a quantum double model  ([arXiv:1811.06738](https://arxiv.org/abs/1811.06738), [arXiv:2505.18265](https://arxiv.org/abs/2505.18265)).
- ZX calculus  ([doi:10.1007/978-3-540-70583-3_25](https://doi.org/10.1007/978-3-540-70583-3_25), [arXiv:0906.4725](https://arxiv.org/abs/0906.4725)) can be used to reduce the complexity of surface-code lattice surgery diagrams  ([arXiv:1704.08670](https://arxiv.org/abs/1704.08670)) and
to reduce $T$-gate counts in magic-state distillation protocols  ([arXiv:1812.01238](https://arxiv.org/abs/1812.01238), [arXiv:1905.08916](https://arxiv.org/abs/1905.08916)).
- Transversal injection method to prepare non-stabilizer states  ([arXiv:2211.10046](https://arxiv.org/abs/2211.10046)).
- Logical CZ gate from physical CZ gates  ([arXiv:1508.03468](https://arxiv.org/abs/1508.03468), [arXiv:1610.03485](https://arxiv.org/abs/1610.03485), [arXiv:2208.07367](https://arxiv.org/abs/2208.07367)), related to the fact that the code admits a cup product structure  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).
- Certain gates can be performed adiabatically  ([arXiv:1406.2690](https://arxiv.org/abs/1406.2690), [arXiv:1411.4248](https://arxiv.org/abs/1411.4248), [arXiv:1708.02360](https://arxiv.org/abs/1708.02360)), yielding an instance of holonomic quantum computation  ([arXiv:quant-ph/9904011](https://arxiv.org/abs/quant-ph/9904011)).
Fault-tolerant gates should be interpretable as monodromies under a particular notion of parallel transport  ([arXiv:1309.7062](https://arxiv.org/abs/1309.7062)).
- A combination of fold-transversal gates, Dehn twists and single-shot logical Pauli measurements generates the logical Clifford group  ([arXiv:2411.18287](https://arxiv.org/abs/2411.18287)).
- Magic-state cultivation that avoids grafting  ([arXiv:2502.01743](https://arxiv.org/abs/2502.01743)).

## Fault tolerance

- Transversal (non-Clifford) $CCZ$ gate by bringing 2D surface codes together and using just-in-time decoding  ([arXiv:1903.11634](https://arxiv.org/abs/1903.11634), [arXiv:2412.12529](https://arxiv.org/abs/2412.12529)). Gate can be simulated by taking 2D slices out of 3D surface codes  ([arXiv:2012.08536](https://arxiv.org/abs/2012.08536)).
- Flag fault-tolerant syndrome extraction  ([arXiv:1708.02246](https://arxiv.org/abs/1708.02246)).
- Homomorphic measurement protocols for arbitrary surface codes  ([arXiv:2211.03625](https://arxiv.org/abs/2211.03625)).
- Non-geometrically local connectivity can reduce overhead cost  ([arXiv:2211.15465](https://arxiv.org/abs/2211.15465)).
- Magic-state distillation protocols  ([arXiv:1208.0928](https://arxiv.org/abs/1208.0928), [arXiv:1209.0510](https://arxiv.org/abs/1209.0510), [arXiv:2212.00813](https://arxiv.org/abs/2212.00813), [arXiv:2403.03991](https://arxiv.org/abs/2403.03991)) leading up to magic-state cultivation  ([arXiv:2409.17595](https://arxiv.org/abs/2409.17595)).
- Framework of fault tolerance utilizing ZX calculus  ([doi:10.1007/978-3-540-70583-3_25](https://doi.org/10.1007/978-3-540-70583-3_25), [arXiv:0906.4725](https://arxiv.org/abs/0906.4725)) that is applicable to MBQC, FBQC, and conventional computation versions of the surface code  ([arXiv:2303.08829](https://arxiv.org/abs/2303.08829)).
- Syndrome extraction circuits consisting of CNOT gates and ancillary measurements  ([arXiv:1208.0928](https://arxiv.org/abs/1208.0928)). Measurement schedules can be optimized using spacetime circuit codes to yield what is known as the *3CX surface code*  ([arXiv:2302.02192](https://arxiv.org/abs/2302.02192)). Schedules can also be optimized via ZX calculus  ([doi:10.1007/978-3-540-70583-3_25](https://doi.org/10.1007/978-3-540-70583-3_25), [arXiv:0906.4725](https://arxiv.org/abs/0906.4725)). Inspired by the honeycomb Floquet code, various weight-two measurement schemes have been designed  ([arXiv:2007.00307](https://arxiv.org/abs/2007.00307), [arXiv:2206.12780](https://arxiv.org/abs/2206.12780), [arXiv:2310.12981](https://arxiv.org/abs/2310.12981)), with the scheme in Ref.  ([arXiv:2206.12780](https://arxiv.org/abs/2206.12780)) being a special case of DWR.
- LUCI framework for syndrome extraction circuits  ([arXiv:2410.14891](https://arxiv.org/abs/2410.14891), [arXiv:2502.10355](https://arxiv.org/abs/2502.10355)).
- Fault-tolerant constant-depth encoder and unencoder using measurements  ([arXiv:2408.06299](https://arxiv.org/abs/2408.06299)).

## Decoders

- Using data from multiple syndrome measurements prior to decoding allows for correcting syndrome measurement errors. The surface code requires order $O(d)$ extraction rounds in order to gain a reliable estimate. Syndrome measurements are distance-preserving because syndrome extraction circuits can be designed to avoid hook errors  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143)).
- Syndrome extraction circuits consist of CNOT gates and ancillary measurements since this is a stabilizer code  ([arXiv:1208.0928](https://arxiv.org/abs/1208.0928)). Measurement schedules can be optimized using spacetime circuit codes to yield what is known as the *3CX surface code*  ([arXiv:2302.02192](https://arxiv.org/abs/2302.02192)). Schedules can also be optimized via ZX calculus  ([doi:10.1007/978-3-540-70583-3_25](https://doi.org/10.1007/978-3-540-70583-3_25), [arXiv:0906.4725](https://arxiv.org/abs/0906.4725)). Inspired by the honeycomb Floquet code, various weight-two measurement schemes have been designed  ([arXiv:2007.00307](https://arxiv.org/abs/2007.00307), [arXiv:2206.12780](https://arxiv.org/abs/2206.12780), [arXiv:2310.12981](https://arxiv.org/abs/2310.12981)), with the scheme in Ref.  ([arXiv:2206.12780](https://arxiv.org/abs/2206.12780)) being a special case of DWR.
- Fault-tolerant syndrome extraction circuits using three-qubit gates  ([arXiv:2506.09029](https://arxiv.org/abs/2506.09029), [arXiv:2506.09028](https://arxiv.org/abs/2506.09028)).
- Expanding diamonds decoder correcting errors of some maximum fractal dimension . The sub-threshold failure probability scales as $(p/p_{\text{th}})^{d^\beta}$, where $p_{\text{th}}$ is the threshold and $\beta = \log_3 2$.
- Minimum weight perfect-matching (MWPM)  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:1110.5133](https://arxiv.org/abs/1110.5133), [arXiv:1202.5602](https://arxiv.org/abs/1202.5602), [arXiv:1307.1740](https://arxiv.org/abs/1307.1740)) (based on work by Edmonds on finding a matching in a graph  ([doi:10.4153/CJM-1965-045-4](https://doi.org/10.4153/CJM-1965-045-4), [doi:10.6028/jres.069B.013](https://doi.org/10.6028/jres.069B.013))), which takes time up to polynomial in $n$ for the surface code. For the case of the surface code, minimum-weight decoding reduces to MWPM  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [doi:10.4153/CJM-1965-045-4](https://doi.org/10.4153/CJM-1965-045-4), [doi:10.1088/0305-4470/15/2/033](https://doi.org/10.1088/0305-4470/15/2/033)). MWPM solves the MPE decoding problem exactly for independent $X$ and $Z$ noise. Minimum-weight decoding is $NP$-hard for more general Pauli noise and for transversal-CNOT decoding with Pauli-$Z$ and measurement bit-flip errors  ([arXiv:2309.10331](https://arxiv.org/abs/2309.10331), [arXiv:2603.22064](https://arxiv.org/abs/2603.22064)). PyMatching is a Python software library for implementing MWPM  ([arXiv:2105.13082](https://arxiv.org/abs/2105.13082)).
- The Bravyi-Suchara-Vargo (BSV) tensor network decoder  ([arXiv:1405.4883](https://arxiv.org/abs/1405.4883)) exactly solves the ML decoding problem under independent $X,Z$ noise for the surface code and has complexity of order $O(n^2)$; the decoder provides an efficient tensor-network contraction for the partition function resulting from the statistical mechanical mapping, which is known to be solvable for an Ising model on a planar graph  ([doi:10.1103/PhysRev.88.1332](https://doi.org/10.1103/PhysRev.88.1332)). ML decoding  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143)) is $\#P$-hard in general for the surface code  ([arXiv:2309.10331](https://arxiv.org/abs/2309.10331)).
- Union-find decoder  ([arXiv:1709.06218](https://arxiv.org/abs/1709.06218)) uses the *union-find data structure*  ([doi:10.1145/364099.364331](https://doi.org/10.1145/364099.364331), [doi:10.1137/0202024](https://doi.org/10.1137/0202024), [doi:10.1145/62.2160](https://doi.org/10.1145/62.2160)), solving the MPE decoding problem exactly for low-weight errors under depolarizing noise. A subsequent modification utilizes the continuous signal obtained in the physical implementation of the stabilizer measurement (as opposed to discretizing the signal into a syndrome bit)  ([arXiv:2107.13589](https://arxiv.org/abs/2107.13589)). Belief union find is a combination of belief-propagation and union-find  ([arXiv:2203.04948](https://arxiv.org/abs/2203.04948)). Strictly local (as opposed to partially local) union find  ([arXiv:2305.18534](https://arxiv.org/abs/2305.18534)) has a worst-case runtime of order $O(d^3)$ in the distance $d$.
- Modified MWPM decoders: topological code Autotune  ([arXiv:1202.6111](https://arxiv.org/abs/1202.6111)); pipeline MWPM (accounting for correlations between events)  ([arXiv:1310.0863](https://arxiv.org/abs/1310.0863), [arXiv:2205.09828](https://arxiv.org/abs/2205.09828)); modification tailored to asymmetric noise  ([arXiv:1812.01505](https://arxiv.org/abs/1812.01505)); parity blossom MWPM and fusion blossom MWPM  ([arXiv:2305.08307](https://arxiv.org/abs/2305.08307)), a modification utilizing the continuous signal obtained in the physical implementation of the stabilizer measurement (as opposed to discretizing the signal into a syndrome bit)  ([arXiv:2107.13589](https://arxiv.org/abs/2107.13589)); belief perfect matching (a combination of belief-propagation and MWPM)  ([arXiv:2203.04948](https://arxiv.org/abs/2203.04948)); spanning tree matching (STM) and rapid-fire (RFire) decoders  ([arXiv:2405.01151](https://arxiv.org/abs/2405.01151)); ordered decoding based on MWPM  ([arXiv:2408.01393](https://arxiv.org/abs/2408.01393)); Micro Blossom adapted for a parallelized architecture  ([arXiv:2502.14787](https://arxiv.org/abs/2502.14787)); logical observable MWPM and a windowed version  ([arXiv:2505.13599](https://arxiv.org/abs/2505.13599)). Combining, or *harmonizing*, various decoders can improve performance  ([arXiv:2401.12434](https://arxiv.org/abs/2401.12434)). One such example is the Libra decoder  ([arXiv:2408.12135](https://arxiv.org/abs/2408.12135)), a combination of MWPM decoders and matching synthesis.
- Renormalization group (RG)  ([arXiv:0911.0581](https://arxiv.org/abs/0911.0581), [arXiv:1304.6100](https://arxiv.org/abs/1304.6100), [arXiv:1411.3028](https://arxiv.org/abs/1411.3028)); see Ref.  ([arXiv:1310.2393](https://arxiv.org/abs/1310.2393)) for the planar surface code.
- Linear-time ML erasure decoder  ([arXiv:1703.01517](https://arxiv.org/abs/1703.01517)).
- Linear-time decoder for general noise, including coherent noise and correlated noise  ([arXiv:1801.01879](https://arxiv.org/abs/1801.01879)).
- Markov-chain Monte Carlo  ([arXiv:1302.2669](https://arxiv.org/abs/1302.2669)).
- Cellular automaton decoders  ([doi:10.7907/AHMQ-EG82](https://doi.org/10.7907/AHMQ-EG82), [arXiv:1406.2338](https://arxiv.org/abs/1406.2338), [arXiv:1511.05579](https://arxiv.org/abs/1511.05579)); see also  ([arXiv:1512.04528](https://arxiv.org/abs/1512.04528)).
- Neural network  ([arXiv:1610.04238](https://arxiv.org/abs/1610.04238), [arXiv:1802.06441](https://arxiv.org/abs/1802.06441), [arXiv:2208.01178](https://arxiv.org/abs/2208.01178), [arXiv:2208.05758](https://arxiv.org/abs/2208.05758), [arXiv:2307.03280](https://arxiv.org/abs/2307.03280), [arXiv:2501.14525](https://arxiv.org/abs/2501.14525), [arXiv:2506.16113](https://arxiv.org/abs/2506.16113)), reinforcement learning  ([arXiv:1810.07207](https://arxiv.org/abs/1810.07207), [arXiv:1811.12338](https://arxiv.org/abs/1811.12338), [arXiv:2212.11890](https://arxiv.org/abs/2212.11890), [arXiv:2101.07285](https://arxiv.org/abs/2101.07285)), and transformer-based  ([arXiv:2311.16082](https://arxiv.org/abs/2311.16082), [arXiv:2506.02734](https://arxiv.org/abs/2506.02734)) decoders like the AlphaQubit series  ([arXiv:2310.05900](https://arxiv.org/abs/2310.05900), [arXiv:2512.07737](https://arxiv.org/abs/2512.07737)).
- Lightweight low-latency look-up table (LILLIPUT) decoder for small surface codes  ([arXiv:2108.06569](https://arxiv.org/abs/2108.06569)).
- Decoders can be augmented with a pre-decoder  ([arXiv:2001.11427](https://arxiv.org/abs/2001.11427), [arXiv:2208.04660](https://arxiv.org/abs/2208.04660)), which can allow for some processing to be done inside the cryogenic environment of the quantum system  ([arXiv:2208.08547](https://arxiv.org/abs/2208.08547)).
- Sliding-window  ([arXiv:2209.09219](https://arxiv.org/abs/2209.09219), [arXiv:2209.08552](https://arxiv.org/abs/2209.08552)), parallel-window  ([arXiv:2209.09219](https://arxiv.org/abs/2209.09219)), and predictive-window  ([arXiv:2412.05115](https://arxiv.org/abs/2412.05115)) parallelizable decoders, designed to overcome the backlog problem, can be combined with many inner decoders, such as MWPM or union-find.
- Modifications of BP: generalized belief propagation (GBP)  ([arXiv:2212.03214](https://arxiv.org/abs/2212.03214)), based on a classical version ; AMBP4, a quaternary version  ([arXiv:2202.06612](https://arxiv.org/abs/2202.06612)) of the MBP decoder  ([arXiv:2104.13659](https://arxiv.org/abs/2104.13659)) of complexity $O(n\log\log n)$; blockBP, a combination of BP and tensor-network decoders  ([arXiv:2402.04834](https://arxiv.org/abs/2402.04834)); machine-learning inspired modifications  ([arXiv:2407.11523](https://arxiv.org/abs/2407.11523)). See Ref.  ([doi:10.1109/MBITS.2023.3285848](https://doi.org/10.1109/MBITS.2023.3285848)) for a review of BP decoders. The min-sum decoder, a simple variant of BP, cannot be used to attain the benefits of codes with distance greater than 9  ([arXiv:2406.14968](https://arxiv.org/abs/2406.14968)).
- A color-code decoder can be used for the surface code  ([arXiv:2306.16476](https://arxiv.org/abs/2306.16476)).
- Progressive-Proximity Bit-Flipping (PPBF) decoder  ([arXiv:2402.15924](https://arxiv.org/abs/2402.15924)).
- Collision clustering decoder  ([arXiv:2309.05558](https://arxiv.org/abs/2309.05558)).
- Quasi-local Lindbladian decoder based on the approximate Petz theorem  ([arXiv:2404.07251](https://arxiv.org/abs/2404.07251)).
- Exclusive decoder family incorporating post-selection on decoding instances deemed not too difficult  ([arXiv:2405.03766](https://arxiv.org/abs/2405.03766)).
- Quantum version of the Tsirelson local automaton decoder  ([arXiv:2412.19803](https://arxiv.org/abs/2412.19803)).
- Bubble clustering decoder  ([arXiv:2504.01654](https://arxiv.org/abs/2504.01654)).
- Union-Intersection Union-Find (UIUF) decoder  ([arXiv:2506.14745](https://arxiv.org/abs/2506.14745)).

## Threshold

- Circuit-level noise: $1.8\%$ under correlated CNOT-gate errors and single-qubit depolarizing noise  ([arXiv:0905.0531](https://arxiv.org/abs/0905.0531)) with optimal decoder  ([arXiv:1609.06373](https://arxiv.org/abs/1609.06373)), and $0.35\%$ under independent $X,Z$ noise with optimal decoder  ([arXiv:1609.06373](https://arxiv.org/abs/1609.06373)). Also, $0.57\%$ for depolarizing noise on data and syndrome qubits as well as initialization, gate, and measurement errors under MWPM decoding  ([arXiv:1208.0928](https://arxiv.org/abs/1208.0928)). For this model, a logical qubit with a $10^{-14}$ logical error rate requires between $10^3$ to $10^4$ physical qubits and a target gate fidelity above $99.9\%$. Later work gave a rigorous threshold proof for arbitrarily reliable computation under local stochastic circuit noise with physical error rate $p < 7.4\times 10^{-4}$  ([arXiv:1206.0800](https://arxiv.org/abs/1206.0800)). Thresholds of $0.5-2.9\%$ have been observed for various noise models  ([arXiv:quant-ph/0207088](https://arxiv.org/abs/quant-ph/0207088), [arXiv:quant-ph/0610082](https://arxiv.org/abs/quant-ph/0610082), [arXiv:0803.0272](https://arxiv.org/abs/0803.0272), [arXiv:0811.0464](https://arxiv.org/abs/0811.0464), [arXiv:1009.3686](https://arxiv.org/abs/1009.3686), [arXiv:1311.5003](https://arxiv.org/abs/1311.5003), [arXiv:1609.06373](https://arxiv.org/abs/1609.06373)). A threshold of $0.41\%$ when concatenated with the $⟦4,2,2⟧$ code  ([arXiv:1604.04062](https://arxiv.org/abs/1604.04062)). The union-find decoder has a finite threshold under circuit-level local stochastic noise  ([arXiv:2602.20238](https://arxiv.org/abs/2602.20238)).
- Phenomenological noise: $3.3\%$ for square tiling  ([arXiv:quant-ph/0401101](https://arxiv.org/abs/quant-ph/0401101)), and $2.93(2)\%$ using several rounds of syndrome measurement  ([arXiv:quant-ph/0207088](https://arxiv.org/abs/quant-ph/0207088)).
- Fabrication errors  ([arXiv:1706.04912](https://arxiv.org/abs/1706.04912)).
- Quasistatic phase damping and readout noise: $2.85\%$  ([arXiv:2401.04530](https://arxiv.org/abs/2401.04530)).
- When used as the underlying code of a surface/Hamming concatenation and benchmarked by a logical CNOT implemented via lattice surgery under circuit-level depolarizing noise, the threshold is $0.31\%$, and achieving logical CNOT error rate $10^{-24}$ at physical error rate $0.1\%$ requires space overhead $4.5\times 10^3$  ([arXiv:2402.09606](https://arxiv.org/abs/2402.09606)).
- Thresholds for various measurement schedules, including that of the 3CX surface code, have been obtained  ([arXiv:2408.02082](https://arxiv.org/abs/2408.02082)).

## Realizations

- Signatures of the corresponding topological phase of matter detected in superconducting circuits  ([arXiv:2104.01180](https://arxiv.org/abs/2104.01180)) and two-dimensional neutral atom arrays  ([arXiv:2104.04119](https://arxiv.org/abs/2104.04119)).
- Measurement schedules associated with the 3CX surface code realized in superconducting qubits on the Willow device by Google Quantum AI  ([arXiv:2412.14360](https://arxiv.org/abs/2412.14360)).

## Relations

- _parent_: [[concepts/qec/higher-dimensional-surface]] — The surface-code CSS stabilizer generator prescription is extendable to higher-dimensional manifolds.
- _parent_: [[concepts/qec/twist-defect-surface]] — Twist-defect surface codes reduce to surface codes when there are no defects.
- _parent_: [[concepts/qec/clifford-deformed-surface]] — CDSC codes are deformations of the surface code via constant-depth Clifford circuits that may not be CSS.
- _parent_: [[concepts/qec/lcs]] — LCS codes consist of sparsely interconnected stacks of surface codes.
- _parent_: [[concepts/qec/qudit-surface]] — The modular-qudit surface code for $q=2$ reduces to the surface code.
- _parent_: [[concepts/qec/galois-topological]] — The Galois-qudit surface code for $q=2$ reduces to the surface code.
- _cousin_: [[concepts/qec/layer]] — Layer codes are combinations of constant-rate QLDPC codes with surface codes built using lattice surgery.
- _cousin_: [[concepts/qec/lresc]] — LRESCs reduce to planar surface codes when a trivial LDPC code is used in the hypergraph product.
- _cousin_: [[concepts/qec/lacross]] — La-cross codes with periodic (open) boundary conditions reduce to the toric (planar surface) code at $k=1$.
- _cousin_: [[concepts/qec/quantum-double]] — On closed surfaces, a quantum-double model with $G=\mathbb{Z}_2$ reduces to the surface code; on a torus, this is the toric code. Quantum doubles with open boundary conditions also reduce to surface codes on open surfaces  ([arXiv:1707.04564](https://arxiv.org/abs/1707.04564), [arXiv:1707.05490](https://arxiv.org/abs/1707.05490), [arXiv:1609.02037](https://arxiv.org/abs/1609.02037), [arXiv:2602.19558](https://arxiv.org/abs/2602.19558), [arXiv:2603.05502](https://arxiv.org/abs/2603.05502)). Non-stabilizer surface-code states can be prepared by augmenting the surface code with a quantum double model  ([arXiv:1811.06738](https://arxiv.org/abs/1811.06738), [arXiv:2505.18265](https://arxiv.org/abs/2505.18265), [arXiv:2510.20890](https://arxiv.org/abs/2510.20890)).
- _cousin_: [[concepts/qec/hamiltonian]] — While codewords of the surface code form ground states of the code's stabilizer Hamiltonian, they can also be ground states of other gapless Hamiltonians  ([arXiv:1111.5817](https://arxiv.org/abs/1111.5817)).
- _cousin_: [`unitary_design`](https://errorcorrectionzoo.org/c/unitary_design) — Unitary $t$-designs can be generated via coherent errors, syndrome extraction, and correction  ([arXiv:2412.04414](https://arxiv.org/abs/2412.04414)).
- _cousin_: [[concepts/qec/hypergraph-product]] — The planar surface code on a square lattice can be obtained from a hypergraph product of two repetition codes with appropriate boundary checks.
- _cousin_: [`repetition`](https://errorcorrectionzoo.org/c/repetition) — The planar surface code on a square lattice can be obtained from a hypergraph product of two repetition codes with appropriate boundary checks.

## Notes

- Introduction to computation with the surface code  ([doi:10.21468/SciPostPhysLectNotes.49](https://doi.org/10.21468/SciPostPhysLectNotes.49), [arXiv:1504.01444](https://arxiv.org/abs/1504.01444)).
- Tutorials from error-correction perspective by
[A. Kubica](https://boulderschool.yale.edu/2023/boulder-school-2023-lecture-notes) and [J. Haah](https://boulderschool.yale.edu/2018/boulder-school-2018-lecture-notes)
and condensed-matter perspective by
[M. Levin
and C. Nayak](https://boulderschool.yale.edu/2016/boulder-school-2016-lecture-notes).
- Review of surface code decoders  ([arXiv:2307.14989](https://arxiv.org/abs/2307.14989)).
- Hardware requirements for implementing surface code QEC can be reduced by utilizing structure in the time slices of the QEC circuits  ([arXiv:2302.02192](https://arxiv.org/abs/2302.02192)). Various optimization and calibration routines exist  ([arXiv:2412.02036](https://arxiv.org/abs/2412.02036)).
- A database of surface codes is available in QECDB .
