---
type: concept
name: Qubit QLDPC code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Sparse qubit stabilizer code
domains:
- quantum-error-correction
related_concepts: []
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qldpc
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qldpc
---

# Qubit QLDPC code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qldpc) (`code_id: qldpc`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Member of a family of $⟦n,k,d⟧$ qubit stabilizer codes for which the number of sites participating in each stabilizer generator and the number of stabilizer generators that each site participates in are both bounded by a constant $w$ as $n\to\infty$.
The code can be denoted by $⟦n,k,d,w⟧$.
Sometimes, the two parameters are explicitly stated: each site of an $(l,w)$*-regular qubit QLDPC code* is acted on by $\leq l$ generators of weight $\leq w$.

Qubit QLDPC codes can correct many stochastic errors far beyond the distance, which may not scale as favorably.
Together with more accurate, faster, and easier-to-parallelize measurements than those of general stabilizer codes, this property makes QLDPC codes interesting in practice.

A *geometrically local qubit stabilizer code* is a qubit QLDPC code where the sites involved in any syndrome value are contained in a fixed volume that does not scale with $n$.
As opposed to general stabilizer codes, syndrome extraction of the constant-weight check operators of a QLDPC code can be done using a constant-depth circuit.

(source: raw/error-correction-zoo.md)

## Protection

Detects errors on $d-1$ sites, corrects errors on $\left\lfloor (d-1)/2 \right\rfloor$ sites.
Code distance may not be a reliable marker of code performance.

Since qubit QLDPC codes are stabilizer QLRCs whose locality $r \leq w$, their relative distance is bounded by  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653))
\begin{align}
  \delta = \frac{d}{n} \leq \frac{1}{2} - \Omega\left(\frac{1}{r}\right)~.
\end{align}

## Rate

Asymptotic scaling of $k$ and $d$ with $n$ depends heavily on the code construction.
Bounds generalizing the BPT bound to qubit QLDPC codes depend on the separation profile of the code's underlying connectivity graph  ([arXiv:2106.00765](https://arxiv.org/abs/2106.00765), [arXiv:2307.03283](https://arxiv.org/abs/2307.03283)).
A constant relative minimum distance can be achieved only for graphs that contain expanders  ([arXiv:2106.00765](https://arxiv.org/abs/2106.00765)).
Conversely, a code with parameters $k$ and $d$ requires a graph with order $\Omega(d)$ edges of length of order $\Omega(d/n^{1/D})$  ([arXiv:2109.10982](https://arxiv.org/abs/2109.10982)).
Random qubit QLDPC codes found by solving certain constraint satisfaction problems (CSPs) practically achieve the capacity of the erasure channel  ([arXiv:2207.03562](https://arxiv.org/abs/2207.03562)).

Qubit QLDPC codes cannot attain the capacity of the erasure channel  ([arXiv:1205.7036](https://arxiv.org/abs/1205.7036)), but this capacity can be attained by code families with weight $w = O(\text{polylog}n)$  ([arXiv:1703.00382](https://arxiv.org/abs/1703.00382)).
There are bounds on their performance against erasure noise  ([arXiv:1205.7036](https://arxiv.org/abs/1205.7036)).

## Encoders

- Fault-tolerant encoders utilizing pre-shared entanglement for qubit QLDPC codes  ([arXiv:2405.07242](https://arxiv.org/abs/2405.07242)).
- Any logical state of an $s$-sparse qubit QLDPC code with $d > s^4 2^{5h}$ has depth-$h$ geometric entanglement $\Omega(d)$, equivalently exponentially small overlap with any depth-$h$ topologically trivial state, even allowing arbitrary ancillas  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)).
- For a qubit QLDPC code with parameters $(n,k,d)$, any logical state has depth-$h$ geometric entanglement $\Omega\!\left(n H^{-1}(k/n)/2^{4h}\right)$; in particular, constant-rate families require $\Omega(n/2^{4h})$ entanglement  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)). Here, $H^{-1}$ is the inverse of the binary entropy function $H(p) = -p\log_2 p - (1-p)\log_2(1-p)$.
- Fault-tolerant state preparation can be done in an overhead that is constant with the number of qubits $n$  ([arXiv:2602.16948](https://arxiv.org/abs/2602.16948)).

## Transversal gates

- There are recipes to determine transversal gates for asymmetric qubit QLDPC codes  ([arXiv:2506.15905](https://arxiv.org/abs/2506.15905)).

## General gates

- Fault-tolerant logical measurements by gauging logical operators have worst-case qubit overhead $O(W\log^{2}W)$ for a weight-$W$ Pauli and improve earlier QLDPC measurement schemes  ([arXiv:2410.02213](https://arxiv.org/abs/2410.02213)). This can be used for a generalization of lattice surgery for CSS QLDPC codes  ([arXiv:2503.05003](https://arxiv.org/abs/2503.05003)). There are conditions on when fault-tolerant surgery can be performed with constant-time overhead  ([arXiv:2510.14895](https://arxiv.org/abs/2510.14895)).
- Repetition-code adapter for logical Pauli measurements and logical CNOT gates via Dehn twists  ([arXiv:2410.03628](https://arxiv.org/abs/2410.03628)).
- Fault-tolerant logical measurements based on an extractor system and allowing for universal computation  ([arXiv:2503.10390](https://arxiv.org/abs/2503.10390)).
- Fault-tolerant batched gadgets for CSS QLDPC codes with constant spacetime overhead  ([arXiv:2510.06159](https://arxiv.org/abs/2510.06159)).

## Decoders

- Iterative error estimation based on the MIN-SUM and SUM-PRODUCT algorithms  ([arXiv:quant-ph/0502086](https://arxiv.org/abs/quant-ph/0502086)).
- Quantum belief propagation (BP) decoder  ([arXiv:0706.4094](https://arxiv.org/abs/0706.4094), [arXiv:0708.1337](https://arxiv.org/abs/0708.1337), [arXiv:0801.1241](https://arxiv.org/abs/0801.1241)) is a quantum version of the classical BP decoder, but performance suffers due to degeneracy  ([arXiv:2012.15297](https://arxiv.org/abs/2012.15297)). Various post-processing algorithms have been proposed (see below and also Refs.  ([doi:10.1109/MILCOM58377.2023.10356284](https://doi.org/10.1109/MILCOM58377.2023.10356284), [doi:10.1109/ICASSP48485.2024.10446153](https://doi.org/10.1109/ICASSP48485.2024.10446153))).
- BP-OSD decoder, scaling as $O(n^3)$, adds a post-processing step based on ordered statistics decoding (OSD) to the belief propagation (BP) decoder  ([arXiv:1904.02703](https://arxiv.org/abs/1904.02703)).
- Neural network BP decoders  ([arXiv:1811.07835](https://arxiv.org/abs/1811.07835), [arXiv:2212.10245](https://arxiv.org/abs/2212.10245)) and GNN decoders  ([arXiv:2307.01241](https://arxiv.org/abs/2307.01241), [arXiv:2310.17758](https://arxiv.org/abs/2310.17758)) for qubit codes.
- Partially and fully decoupled BP decoders, which use the decoupling representation, yield improvements against depolarizing noise  ([arXiv:2305.17505](https://arxiv.org/abs/2305.17505)).
- Message-passing decoder utilizing stabilizer inactivation (MP-SI a.k.a. BP-SI) for CSS-type QLDPC qubit codes  ([arXiv:2205.06125](https://arxiv.org/abs/2205.06125)).
- BP localized statistics decoding (BP-LSD) that exploits error clustering  ([arXiv:2406.18655](https://arxiv.org/abs/2406.18655)).
- Syndrome-based linear programming (SB-LP) algorithm can be applied as a post-processing step after syndrome-based min-sum (SM-MS) decoding  ([arXiv:2311.18488](https://arxiv.org/abs/2311.18488)).
- BP guided decimation (BPGD) decoder  ([arXiv:2312.10950](https://arxiv.org/abs/2312.10950)).
- SymBreak decoder, which adaptively modifies the decoding graph to break the degeneracy of the BP decoder  ([arXiv:2412.02885](https://arxiv.org/abs/2412.02885)).
- Ambiguity clustering (AC) decoder, in which measurement data is divided into clusters and decoded independently  ([arXiv:2406.14527](https://arxiv.org/abs/2406.14527)).
- 2D geometrically local syndrome extraction circuits with bounded depth using order $O(n^2)$ ancilla qubits  ([arXiv:2109.14599](https://arxiv.org/abs/2109.14599)). For CSS codes, syndrome extraction can be implemented in constant depth  ([arXiv:2109.14609](https://arxiv.org/abs/2109.14609)).
- Soft (i.e., analog) syndrome iterative BP for CSS-type QLDPC codes, utilizing the continuous signal obtained in the physical implementation of the stabilizer measurement (as opposed to discretizing the signal into a syndrome bit)  ([arXiv:2205.02341](https://arxiv.org/abs/2205.02341)).
- The MWPM decoder for surface codes may be generalizable to QLDPC codes  ([arXiv:2207.06428](https://arxiv.org/abs/2207.06428)).
- Extensions of the union-find decoder for qubit QLDPC codes  ([arXiv:2103.08049](https://arxiv.org/abs/2103.08049), [arXiv:2209.01180](https://arxiv.org/abs/2209.01180), [arXiv:2407.15988](https://arxiv.org/abs/2407.15988)).
- Sliding-window decoding  ([arXiv:2311.03307](https://arxiv.org/abs/2311.03307)).
- Closed-branch decoder  ([arXiv:2402.01532](https://arxiv.org/abs/2402.01532)).
- BP with guided decimation guessing (GDG) sliding-window decoder for CSS qubit codes  ([arXiv:2403.18901](https://arxiv.org/abs/2403.18901)).
- Performing $d$ syndrome extraction rounds obtains an effective distance of $d$ for a qubit QLDPC code  ([arXiv:1310.2984](https://arxiv.org/abs/1310.2984)).
- BP plus ordered Tanner forest (BP+OTF) almost-linear time decoder  ([arXiv:2409.01440](https://arxiv.org/abs/2409.01440)).
- Cluster decoder  ([arXiv:2412.08817](https://arxiv.org/abs/2412.08817)).
- BP approximate degenerate OSD (BP+ADOSD) decoder  ([arXiv:2412.21118](https://arxiv.org/abs/2412.21118)).
- Decision tree decoders (DTDs), one that provably finds the minimum-weight correction, and one that is heuristic  ([arXiv:2502.16408](https://arxiv.org/abs/2502.16408)).
- AutDEC decoder for codes with large automorphism groups  ([arXiv:2503.01738](https://arxiv.org/abs/2503.01738)).
- Tesseract ML decoder  ([arXiv:2503.10988](https://arxiv.org/abs/2503.10988)).
- Relay-BP decoder  ([arXiv:2506.01779](https://arxiv.org/abs/2506.01779)).
- HyperBlossom  ([arXiv:2508.04969](https://arxiv.org/abs/2508.04969)).
- Post-selection strategies for clustering based decoders  ([arXiv:2510.05795](https://arxiv.org/abs/2510.05795)).
- Decoder switching between soft-output and higher-accuracy decoders  ([arXiv:2510.25222](https://arxiv.org/abs/2510.25222)).
- Graph augmentation and rewiring for interference (GARI) framework for circuit-level noise  ([arXiv:2510.14060](https://arxiv.org/abs/2510.14060)).

## Fault tolerance

- Lattice surgery techniques with ancilla qubits  ([arXiv:2110.10794](https://arxiv.org/abs/2110.10794), [arXiv:2308.08648](https://arxiv.org/abs/2308.08648), [arXiv:2407.18393](https://arxiv.org/abs/2407.18393)). In one such technique, one first performs a logical measurement by code switching into a code whose stabilizer group includes the original stabilizers together with the logical Paulis that are to be measured. Then, one can reduce the weight of the output code using weight reduction.
- Fault-tolerance with constant overhead can be performed on certain qubit QLDPC codes  ([arXiv:1310.2984](https://arxiv.org/abs/1310.2984)), e.g., quantum expander codes  ([arXiv:1808.03821](https://arxiv.org/abs/1808.03821)).
- Error-corrected GHZ state distillation for Steane error correction  ([arXiv:2210.14143](https://arxiv.org/abs/2210.14143)).
- Fault-tolerant logical measurements by gauging logical operators have worst-case qubit overhead $O(W\log^{2}W)$ for a weight-$W$ Pauli and improve earlier QLDPC measurement schemes  ([arXiv:2410.02213](https://arxiv.org/abs/2410.02213)). This can be used for a generalization of lattice surgery for CSS QLDPC codes  ([arXiv:2503.05003](https://arxiv.org/abs/2503.05003)). There are conditions on when fault-tolerant surgery can be performed with constant-time overhead  ([arXiv:2510.14895](https://arxiv.org/abs/2510.14895)).
- Fault-tolerant logical measurements based on an extractor system and allowing for universal computation  ([arXiv:2503.10390](https://arxiv.org/abs/2503.10390)).
- Fault-tolerant batched gadgets for CSS QLDPC codes with constant spacetime overhead  ([arXiv:2510.06159](https://arxiv.org/abs/2510.06159)).
- High-rate surgery, which yields parallelizable logical Pauli-product measurements  ([arXiv:2510.08523](https://arxiv.org/abs/2510.08523)).
- Fault-tolerant state preparation can be done in an overhead that is constant with the number of qubits $n$  ([arXiv:2602.16948](https://arxiv.org/abs/2602.16948)).

## Code capacity threshold

- Bounds on code capacity thresholds using ML decoding can be obtained by mapping the effect of noise on the code to a statistical mechanical model  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:1208.2317](https://arxiv.org/abs/1208.2317), [arXiv:1311.7688](https://arxiv.org/abs/1311.7688)). In particular, any family of qubit QLDPC codes with superlogarithmic distance achieves a threshold  ([arXiv:1208.2317](https://arxiv.org/abs/1208.2317)).
- Bounds on code capacity thresholds for various noise models exist in terms of stabilizer generator weights  ([arXiv:1412.6172](https://arxiv.org/abs/1412.6172)).

## Threshold

- Qubit QLDPC codes with a constant encoding rate can reduce the overhead of fault-tolerant quantum computation to be constant  ([arXiv:1310.2984](https://arxiv.org/abs/1310.2984)).

## Relations

- _parent_: [`qubit_stabilizer`](https://errorcorrectionzoo.org/c/qubit_stabilizer)
- _parent_: [`quantum_locally_recoverable`](https://errorcorrectionzoo.org/c/quantum_locally_recoverable) — Qubit QLDPC codes are stabilizer QLRCs whose locality $r \leq w$, where $w$ is the maximum stabilizer-generator weight  ([arXiv:2311.08653](https://arxiv.org/abs/2311.08653)).
- _parent_: [`general_qldpc`](https://errorcorrectionzoo.org/c/general_qldpc)
- _cousin_: [`ldpc`](https://errorcorrectionzoo.org/c/ldpc) — Qubit QLDPC codes are quantum analogues of binary LDPC codes.
- _cousin_: [`commuting_projector`](https://errorcorrectionzoo.org/c/commuting_projector) — Qubit QLDPC codes with check soundness, meaning that every weight-$m$ stabilizer can be written as a product of order $O(m)$ stabilizer generators, are robust against few-body perturbations. This means that phases of matter can be defined from certain non-geometrically local QLDPC code Hamiltonians  ([arXiv:2411.01002](https://arxiv.org/abs/2411.01002)).
- _cousin_: [`single_shot`](https://errorcorrectionzoo.org/c/single_shot) — Qubit QLDPC codes satisfying linear confinement are single shot  ([arXiv:2009.11790](https://arxiv.org/abs/2009.11790)). Any code that admits a local greedy decoder also satisfies linear confinement, and so is single shot  ([arXiv:2308.08648](https://arxiv.org/abs/2308.08648)).
- _cousin_: [`ldgm`](https://errorcorrectionzoo.org/c/ldgm) — LDGM codes can yield CSS  ([doi:10.1109/SPAWC.2005.1506298](https://doi.org/10.1109/SPAWC.2005.1506298), [doi:10.1109/CISS.2008.4558588](https://doi.org/10.1109/CISS.2008.4558588), [doi:10.1103/PhysRevA.103.022617](https://doi.org/10.1103/PhysRevA.103.022617)) and non-CSS  ([doi:10.1103/PhysRevA.102.012423](https://doi.org/10.1103/PhysRevA.102.012423), [doi:10.1109/QCE49297.2020.00022](https://doi.org/10.1109/QCE49297.2020.00022)) qubit QLDPC codes. Some of the LDGM-based CSS codes have $n$-independent minimum distance and no code capacity threshold  ([arXiv:0903.0566](https://arxiv.org/abs/0903.0566)).
- _cousin_: [`random_stabilizer`](https://errorcorrectionzoo.org/c/random_stabilizer) — Random qubit QLDPC codes found by solving certain constraint satisfaction problems (CSPs) practically achieve the capacity of the erasure channel  ([arXiv:2207.03562](https://arxiv.org/abs/2207.03562)).
- _cousin_: [`algebraic_ldpc`](https://errorcorrectionzoo.org/c/algebraic_ldpc) — Algebraic LDPC codes made from Latin squares can be used to make qubit QLDPC codes  ([arXiv:0812.5104](https://arxiv.org/abs/0812.5104)).
- _cousin_: [`asymmetric_qecc`](https://errorcorrectionzoo.org/c/asymmetric_qecc) — There are recipes to determine transversal gates for asymmetric qubit QLDPC codes  ([arXiv:2506.15905](https://arxiv.org/abs/2506.15905)).

## Notes

- Links to code tables of notable QLDPC codes  ([arXiv:2103.06309](https://arxiv.org/abs/2103.06309)).
- Collection of QLDPC qubit codes based on hyperbolic tilings in the QEC-Pages software library }.
- High-rate QLDPC codes can be used for Bell-pair distillation  ([arXiv:2502.09542](https://arxiv.org/abs/2502.09542)).
- Qldpc code circUIT Simulator (QUITS) Python software library for simulating QLDPC code circuits  ([arXiv:2504.02673](https://arxiv.org/abs/2504.02673))}.
- See  ([arXiv:2605.29137](https://arxiv.org/abs/2605.29137)) for a pedagogical introduction to QLDPC codes.
