---
type: concept
name: Quantum repetition code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/1d-stabilizer
- concepts/qec/ame
- concepts/qec/fracton
- concepts/qec/gnu-permutation-invariant
- concepts/qec/group-quantum-repetition
- concepts/qec/qldpc
- concepts/qec/quantum-parity
- concepts/qec/small-distance-qubit-stabilizer
- concepts/qec/topological-abelian
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/quantum_repetition
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: quantum_repetition
---

# Quantum repetition code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/quantum_repetition) (`code_id: quantum_repetition`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes $1$ qubit into $n$ qubits according to $|0\rangle\to|\phi_0\rangle^{\otimes n}$ and $|1\rangle\to|\phi_1\rangle^{\otimes n}$. The code is called a *bit-flip* code when $|\phi_i\rangle = |i\rangle$, and a *phase-flip* code when $|\phi_0\rangle = |+\rangle$ and $|\phi_1\rangle = |-\rangle$.
This repetition-style encoding does not clone an arbitrary quantum state; instead, it extends the copying of computational-basis states linearly to entangled codewords  .

The $\pm$-basis codewords for the bit-flip code are *GHZ states*  ([doi:10.1119/1.16243](https://doi.org/10.1119/1.16243), [doi:10.1119/1.16503](https://doi.org/10.1119/1.16503), [arXiv:0712.0921](https://arxiv.org/abs/0712.0921)) (a.k.a. qubit cat states) $|0\rangle^{\otimes n}\pm|1\rangle^{\otimes n}$. These are ground states of the 1D *classical Ising model* Hamiltonian $H=\sum_{i} Z_{i}Z_{i+1}$.

The $\pm$-basis codewords for the phase-flip code are expanded in the computational basis as
\begin{align}
  \begin{split}
    |\overline{+}\rangle =\frac{1}{\sqrt{2^{n-1}}}\sum_{\sum_{i}v_{i}=0}|v_{1},\cdots,v_{n}\rangle~{\phantom{,}}\\
    |\overline{-}\rangle =\frac{1}{\sqrt{2^{n-1}}}\sum_{\sum_{i}v_{i}=1}|v_{1},\cdots,v_{n}\rangle~,
  \end{split}
\end{align}
showing that the phase-flip code stores information in the total parity of the qubits.
For example, an early code realized in devices is the 2-qubit phase-flip code  ([arXiv:quant-ph/0006088](https://arxiv.org/abs/quant-ph/0006088)), which encodes a logical qubit into Bell states $|00\rangle+|11\rangle$ and $|01\rangle+|10\rangle$.

(source: raw/error-correction-zoo.md)

## Protection

Bit-flip code corrects bit-flip errors $X$ on $\left\lfloor (n-1)/2\right\rfloor$ qubits and does not detect any phase-flip errors $Z$.
Phase-flip code corrects phase-flip errors $Z$ on $\left\lfloor (n-1)/2\right\rfloor$ qubits and does not detect any bit-flip errors $X$.

Because they protect against only one type of noise, both codes can be thought of as a classical $[n,1,n]$ repetition code embedded in a quantum system.
Nevertheless, the phase-flip code can offer some degree of protection in particular physical systems based on superconducting circuits  ([arXiv:1205.1836](https://arxiv.org/abs/1205.1836), [arXiv:2303.17810](https://arxiv.org/abs/2303.17810)).

## Encoders

- Non-deterministic encoders for various specific states of the 2-qubit phase-flip code  ([arXiv:quant-ph/0408064](https://arxiv.org/abs/quant-ph/0408064)).
- Fault-tolerant GHZ-state preparation with small qubit registers  ([arXiv:0709.4539](https://arxiv.org/abs/0709.4539)).
- Unitary circuit of depth logarithmic in $n$  ([arXiv:1807.05572](https://arxiv.org/abs/1807.05572)). Any circuit has to have range $n$ because Ghz states are locally indistinguishable  ([arXiv:1910.08980](https://arxiv.org/abs/1910.08980)).
- Adaptive constant-depth circuit with geometrically local gates and measurements throughout  ([arXiv:1906.08890](https://arxiv.org/abs/1906.08890), [arXiv:2112.03061](https://arxiv.org/abs/2112.03061)).
- Lindbladian-based dissipative encoding and autonomous QEC passively protecting against bit flips  ([arXiv:quant-ph/0110111](https://arxiv.org/abs/quant-ph/0110111), [arXiv:1702.08673](https://arxiv.org/abs/1702.08673)).
- Error-corrected GHZ state distillation for Steane error correction  ([arXiv:2210.14143](https://arxiv.org/abs/2210.14143)).
- Approximate Hamiltonian-based encoding of GHZ states  ([arXiv:2406.10336](https://arxiv.org/abs/2406.10336)).

## General gates

- Toffoli magic-state preparation protocol  ([arXiv:2012.04108](https://arxiv.org/abs/2012.04108)).

## Decoders

- Fault-tolerant syndrome detection  ([arXiv:quant-ph/0412168](https://arxiv.org/abs/quant-ph/0412168)).
- Autonomous QEC for the 3-qubit bit-flip code  ([arXiv:quant-ph/0501049](https://arxiv.org/abs/quant-ph/0501049)).
- Machine learning algorithm to implement autonomous QEC for the three-qubit quantum repetition code  ([arXiv:2110.10378](https://arxiv.org/abs/2110.10378)).
- Quantum cellular automata for majority voting and two-line voting  ([arXiv:2309.03608](https://arxiv.org/abs/2309.03608)).
- Quantum version of the Tsirelson local automaton decoder  ([arXiv:2412.19803](https://arxiv.org/abs/2412.19803)).
- Planar decoder designed to work under circuit-level noise  ([arXiv:2501.03582](https://arxiv.org/abs/2501.03582)).
- Single-rule and shearing-rule local automaton decoders  ([arXiv:2505.10162](https://arxiv.org/abs/2505.10162)).

## Fault tolerance

- Fault-tolerant syndrome detection  ([arXiv:quant-ph/0412168](https://arxiv.org/abs/quant-ph/0412168)).
- An $m$-qubit GHZ state, i.e., qubit cat state, can serve as an ancilla for fault-tolerant measurement of a weight-$m$ Pauli operator by coupling each ancilla qubit to one data qubit, applying Hadamards to the ancilla, and reading out the parity of the measurement outcomes .
- Toffoli magic-state preparation protocol  ([arXiv:2012.04108](https://arxiv.org/abs/2012.04108)).

## Code capacity threshold

- Independent $X$ noise: $50\%$ with RG decoder for quantum repetition code arranged on a 1D or 2D lattice  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).
- A nonzero threshold exists under the single-rule local automaton decoders  ([arXiv:2505.10162](https://arxiv.org/abs/2505.10162)).

## Threshold

- Phenomenological noise: $11\%$ and $17.2\%$ with RG decoder for quantum repetition code arranged on a 1D and 2D lattice, respectively  ([arXiv:1708.09286](https://arxiv.org/abs/1708.09286)).
- Threshold under real-time geometrically local decoder based on introducing an ancillary buffer and confining spacetime interactions between anyons   ([arXiv:2510.08056](https://arxiv.org/abs/2510.08056)).

## Realizations

- NMR: 2-qubit phase-flip code  ([arXiv:quant-ph/9811068](https://arxiv.org/abs/quant-ph/9811068), [arXiv:cs/0012017](https://arxiv.org/abs/cs/0012017)); 3-qubit bit-flip code  ([arXiv:quant-ph/0004030](https://arxiv.org/abs/quant-ph/0004030)); 3-qubit phase-flip code  ([arXiv:quant-ph/9802018](https://arxiv.org/abs/quant-ph/9802018), [arXiv:1108.4842](https://arxiv.org/abs/1108.4842)), with up to two rounds of error correction in liquid-state NMR  ([arXiv:1109.4821](https://arxiv.org/abs/1109.4821)). Such codes were used to characterize noise  ([arXiv:quant-ph/0610038](https://arxiv.org/abs/quant-ph/0610038)).
- Linear optics: 2-qubit phase-flip code  ([arXiv:quant-ph/0502042](https://arxiv.org/abs/quant-ph/0502042)).
- Trapped ions: 3-qubit bit-flip code by Wineland group  ([doi:10.1038/nature03074](https://doi.org/10.1038/nature03074)), and 3-qubit phase-flip algorithm implemented in 3 cycles on high fidelity gate operations  ([doi:10.1126/science.1203329](https://doi.org/10.1126/science.1203329)).
Both phase- and bit-flip codes for 31 qubits and their stabilizer measurements have been realized by Quantinuum  ([arXiv:2305.03828](https://arxiv.org/abs/2305.03828)).
Multiple rounds of Steane error correction  ([arXiv:2312.09745](https://arxiv.org/abs/2312.09745)).
- Superconducting circuits: 3-qubit phase-flip and bit-flip code by Schoelkopf group  ([arXiv:1004.4324](https://arxiv.org/abs/1004.4324), [arXiv:1109.4948](https://arxiv.org/abs/1109.4948)); 3-qubit bit-flip code  ([arXiv:1411.5542](https://arxiv.org/abs/1411.5542)); 3-qubit phase-flip code up to 3 cycles of error correction  ([arXiv:1508.01388](https://arxiv.org/abs/1508.01388)); IBM 15-qubit device  ([arXiv:1709.00990](https://arxiv.org/abs/1709.00990)); IBM Rochester device using 43-qubit code  ([arXiv:2004.11037](https://arxiv.org/abs/2004.11037)); Google system performing up to 8 error-correction cycles on 5 and 9 qubits  ([arXiv:1411.7403](https://arxiv.org/abs/1411.7403)); Google Quantum AI Sycamore utilizing up to 11 physical qubits and running 50 correction rounds  ([arXiv:2102.06132](https://arxiv.org/abs/2102.06132)); Google Quantum AI Sycamore utilizing up to 25 qubits for comparison of logical error scaling with a quantum code  ([arXiv:2207.06431](https://arxiv.org/abs/2207.06431)) (see also  ([arXiv:2211.04728](https://arxiv.org/abs/2211.04728))). 
Google Quantum AI follow-up experiment on codes up to (classical) distance 29, demonstrating exponential suppression to an error floor of $10^{-10}$  ([arXiv:2408.13687](https://arxiv.org/abs/2408.13687)). 
Ising-model Nishimori phase transition realized for GHZ states on 54 qubits on a 127 qubit IBM device  ([arXiv:2309.02863](https://arxiv.org/abs/2309.02863)). 
GHZ state on 75 qubits made on an IBM device  ([arXiv:2411.14638](https://arxiv.org/abs/2411.14638)). 
Implementation of planar decoder for codes with distances between 3 and 11 on 72-qubit superconducting device  ([arXiv:2501.03582](https://arxiv.org/abs/2501.03582)).
Lattice surgery on the surface-17 code has been realized by splitting the code into two repetition codes by the Wallraff group  ([arXiv:2501.04612](https://arxiv.org/abs/2501.04612)).
2-qubit phase-flip code error detection realized with one ancilla by the Simakov group  ([arXiv:2506.20529](https://arxiv.org/abs/2506.20529)). GHZ state of 120 qubits realized on IBM device  ([arXiv:2510.09520](https://arxiv.org/abs/2510.09520)).
- Autonomous QEC protocols have been implemented on a 3-qubit superconducting qubit device  ([arXiv:2107.11398](https://arxiv.org/abs/2107.11398)).
- Semiconductor spin-qubit devices: 3-qubit devices at RIKEN  ([arXiv:2201.08581](https://arxiv.org/abs/2201.08581)) and Delft  ([arXiv:2202.11530](https://arxiv.org/abs/2202.11530)).
- Nitrogen-vacancy centers in diamond: 3-qubit phase-flip code  ([arXiv:1309.6424](https://arxiv.org/abs/1309.6424), [doi:10.1038/s42005-022-00875-6](https://doi.org/10.1038/s42005-022-00875-6)) (see also Ref.  ([arXiv:1309.5452](https://arxiv.org/abs/1309.5452))).
- Repetition codes are used in quantum annealing protocols  ([arXiv:quant-ph/0512170](https://arxiv.org/abs/quant-ph/0512170), [arXiv:1307.8190](https://arxiv.org/abs/1307.8190), [arXiv:1408.4382](https://arxiv.org/abs/1408.4382)).
- Neutral atom arrays: 41 rounds of syndrome extraction and heralded logical Bell state preparation  ([arXiv:2506.09936](https://arxiv.org/abs/2506.09936)).

## Relations

- _parent_: [[concepts/qec/quantum-parity]] — A $⟦m_1 m_2,1,\min(m_1,m_2)⟧$ QPC reduces to a repetition code when $m_1$ or $m_2$ is one.
- _parent_: [[concepts/qec/1d-stabilizer]] — The codespace of the quantum repetition code is the ground-state space of a frustration-free 1D classical Ising model with nearest-neighbor interactions.
- _parent_: [[concepts/qec/qldpc]] — The codespace of the quantum repetition code is the ground-state space of a frustration-free 1D classical Ising model with nearest-neighbor interactions.
- _parent_: [[concepts/qec/small-distance-qubit-stabilizer]]
- _parent_: [[concepts/qec/gnu-permutation-invariant]] — GNU codewords for $g=1$ reduce to the phase-flip repetition code.
- _parent_: [[concepts/qec/group-quantum-repetition]] — Group-based quantum repetition codes reduce to quantum repetition codes for $G = \mathbb{Z}_2$.
- _cousin_: [[concepts/qec/fracton]] — Product constructions built from the one-dimensional Ising/repetition code yield several fracton phases  ([arXiv:2402.16831](https://arxiv.org/abs/2402.16831)).
- _cousin_: [[concepts/qec/topological-abelian]] — Product constructions built from the one-dimensional Ising/repetition code yield several topological phases  ([arXiv:2402.16831](https://arxiv.org/abs/2402.16831)).
- _cousin_: [[concepts/qec/ame]] — GHZ states are $1$-uniform for all $n$ and AME for $n=2,3$.

## Notes

- Repetition codes can be used to benchmark device performance  ([arXiv:2202.11045](https://arxiv.org/abs/2202.11045)).
