---
type: concept
name: Qubit CSS code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Qubit Euclidean code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/binary-quantum-goppa
- concepts/qec/cft
- concepts/qec/cpc
- concepts/qec/galois-css
- concepts/qec/movassagh-ouyang
- concepts/qec/qubit-stabilizer
- concepts/qec/qubit-subsystem-stabilizer
- concepts/qec/qudit-css
- concepts/qec/random-stabilizer
- concepts/qec/topological-abelian
- concepts/qec/translationally-invariant-stabilizer
- concepts/qec/two-block-quantum
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubit_css
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubit_css
---

# Qubit CSS code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubit_css) (`code_id: qubit_css`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

An $⟦n,k,d⟧$ stabilizer code admitting a set of stabilizer generators that are either $Z$-type or $X$-type Pauli strings.
Codes can be defined from two classical codes and/or chain complexes over $\mathbb{Z}_2$ per the qubit CSS-to-homology correspondence below.

The stabilizer generator matrix is of the form
\begin{align}
H=\begin{pmatrix}0 & H_{Z}\\
H_{X} & 0
\end{pmatrix}
\label{eq:parity}
\end{align}
such that the rows of the two blocks must be orthogonal
\begin{align}
H_X H_Z^T=0~.
\label{eq:comm}
\end{align}
The above condition guarantees that the $X$-stabilizer generators, defined in the symplectic representation as rows of $H_X$, commute with the $Z$-stabilizer generators associated with $H_Z$.
A qubit stabilizer code is a qubit CSS code if and only if $\text{rank}H_X + \text{rank} H_Z = n-k$  ([arXiv:2501.17447](https://arxiv.org/abs/2501.17447)).

Encoding is based on two related binary linear codes, an $[n,k_X,\delta_X]$ code $C_X$ and $[n,k_Z,\delta_Z]$ code $C_Z$, satisfying $C_X^\perp \subseteq C_Z$.
The resulting CSS code has $k=k_X+k_Z-n$ logical qubits.
The $H_X$ ($H_Z$) block of $H$ \eqref{eq:parity} is the parity-check matrix of the code $C_Z$ ($C_X$).
The requirement $C_X^\perp \subseteq C_Z$ guarantees \eqref{eq:comm} and also implies  $C_Z^\perp \subseteq C_X $.
Basis states for the code are, for coset representatives $\gamma \in C_X/C_Z^\perp$,
\begin{align}
|\gamma + C_Z^\perp \rangle = \frac{1}{\sqrt{|C_Z^\perp|}} \sum_{\eta \in C_Z^\perp} |\gamma + \eta\rangle.
\end{align}
After a Hadamard transform on every qubit, the same code can be described using superpositions over cosets of $C_X^\perp$ in $C_Z$, exchanging the roles of bit-flip and phase-flip protection.

Inequivalent CSS codes up to $n=14$ qubits have been classified  ([arXiv:2601.20927](https://arxiv.org/abs/2601.20927)).

\subsection{CSS-to-homology correspondence}

\begin{defterm}{Qubit CSS-to-homology correspondence}
\label{topic:CSS-to-homology-correspondence}
CSS codes and their properties can be formulated in terms of homology theory, yielding a powerful correspondence between codes and chain complexes, the primary homological structures.
There exists a many-to-one mapping from size three chain complexes to CSS codes  ([doi:10.1070/RM1997v052n06ABEH002155](https://doi.org/10.1070/RM1997v052n06ABEH002155), [arXiv:quant-ph/0605094](https://arxiv.org/abs/quant-ph/0605094), [arXiv:1311.0885](https://arxiv.org/abs/1311.0885), [arXiv:1802.01520](https://arxiv.org/abs/1802.01520), [arXiv:2505.06082](https://arxiv.org/abs/2505.06082)) that allows one to extract code properties from topological features of the complexes.
Codes constructed in this manner are sometimes called *homological CSS codes*, but they are equivalent to CSS codes.
This mapping of codes to manifolds allows the application of structures from topology to error correction, yielding various QLDPC codes with favorable properties.
\end{defterm}

A *chain complex* of size three is given by binary vector spaces $A_2$, $A_1$, $A_0$ and binary matrices $\partial_{i=1,2}$ (called *boundary operators*) from $A_i$ to $A_{i-1}$ that satisfy $\partial_1 \partial_2 = 0$. Such a complex is typically denoted as
\begin{align}
A_2 \xrightarrow{\partial_2} A_1 \xrightarrow{\partial_1} A_0~.
\label{eq:chain}
\end{align}
One constructs a CSS code by associating a physical qubit to every basis element of $A_1$, and defining parity-check matrices $H_X=\partial_1$ and $H_Z=\partial_2^T$. That way, the spaces $A_0$ and $A_2$ can be associated with $X$-type and $Z$-type Pauli operators, respectively, and boundary operators determine the Paulis making up the stabilizer generators. The requirement $\partial_1 \partial_2 = 0$ guarantees that the $X$-stabilizer generators associated with $H_X$ commute with the $Z$-stabilizer generators associated with $H_Z$.
The number of encoded logical qubits is equal to the dimension of the first $\mathbb{Z}_2$-homology of the chain complex, $H_1(\partial, \mathbb{Z}_2) = \frac{\text{Ker}(\partial_1)}{\text{Im}(\partial_2)}$.
See  ([arXiv:1504.01444](https://arxiv.org/abs/1504.01444)) for a Rosetta stone comparing statistical mechanical models, CSS codes, and chain complexes.

Usually, the chain complex \eqref{eq:chain} used in the construction comes from the chain complex associated with a cellulation of a manifold. When the manifold is a two-dimensional surface, its entire chain is used.
Higher-dimensional manifolds allow for longer chain complexes, and one can use the three largest non-trivial vector spaces in its chain.

CSS codes saturate a type of *error correction uncertainty relation*  ([doi:10.1103/PhysRevLett.77.793](https://doi.org/10.1103/PhysRevLett.77.793)), which is a special case of an entropic uncertainty relation between a pair of bases  ([doi:10.1007/BF01608825](https://doi.org/10.1007/BF01608825), [doi:10.1103/PhysRevLett.50.631](https://doi.org/10.1103/PhysRevLett.50.631), [doi:10.1103/PhysRevLett.60.1103](https://doi.org/10.1103/PhysRevLett.60.1103)).
The code state $\sum_{c\in C_{Z}}|c\rangle$ can be expressed in terms of either basis states labeled by the code $C_{Z}$ or its dual, satisfying, with equality, the relation
\begin{align}
  |C_{Z}||C_{Z}^{\perp}| \geq 2^{n}\,.
\end{align}

(source: raw/error-correction-zoo.md)

## Protection

The quantity $\min\{\delta_X,\delta_Z\}$ is the CSS code's pure distance  ([arXiv:2209.13474](https://arxiv.org/abs/2209.13474)), and it is equal to the code distance for a non-degenerate code.
To find the code distance of a degenerate CSS code, we have to first remove the codewords of the smaller codes as those codewords correspond to stabilizer generators instead of logical operators.
The general formulae are
\begin{align}
d_{X}&=\min\{ w_H(c) | c \in C_X \setminus C_Z^\perp \} \geq \delta_X \\
d_{Z}&=\min\{ w_H(c) | c \in C_Z \setminus C_X^\perp \} \geq \delta_Z \\
d&=\min\{d_X,d_Z\}~,
\end{align}
where $w_H$ is the Hamming weight of a codeword.
In the homology correspondence, the code distance is equal to the minimum of the combinatorial ($d-1$)-systole of the cellulated $d$-dimensional manifold and its dual.

A CSS code has *stabilizer weight* $w$ if the highest weight of any stabilizer generator is $w$, i.e., any row of $H_X$ and $H_Z$ has weight at most $w$.
*Strong CSS codes* are codes for which there exists a set of $X$ and $Z$ stabilizer generators of equal weight.
In the context of comparing weight as well as of determining distances for noise models biased toward $X$- or $Z$-type errors, an extended notation for asymmetric qubit CSS codes is $⟦n,k,(d_X,d_Z),w⟧$ or $⟦n,k,d_X/d_Z,w⟧$.

\begin{defterm}{Steane enlargement}
\label{topic:steane-enlargement}
An $⟦n,2k-n,d⟧$ CSS code can be converted to a $⟦n,k+k^{\prime}−n,\min(d,\left\lceil 3d^{\prime}/2\right\rceil )⟧$ code for particular $k^{\prime}$ and $d^{\prime}$ via the Steane enlargement construction  ([arXiv:quant-ph/9802061](https://arxiv.org/abs/quant-ph/9802061)).
\end{defterm}

## Rate

For a depolarizing channel with probability $p$, CSS codes allowing for arbitrarily accurate recovery exist with asymptotic rate $1-2h(p)$, where $h$ is the binary entropy function  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [doi:10.1109/ISIT.2013.6620358](https://doi.org/10.1109/ISIT.2013.6620358)).

## Encoders

- Steane Latin-rectangle encoder  ([arXiv:quant-ph/0202036](https://arxiv.org/abs/quant-ph/0202036), [arXiv:1410.5124](https://arxiv.org/abs/1410.5124)).
- Stabilizer measurement  ([arXiv:1404.2495](https://arxiv.org/abs/1404.2495)).
- Clusterization, i.e., measurement of a particular cluster state  ([arXiv:1607.02579](https://arxiv.org/abs/1607.02579)).
- Entanglement purification  ([arXiv:quant-ph/0210069](https://arxiv.org/abs/quant-ph/0210069)).
- Reinforcement-learning discovery of logical-state-preparation circuits  ([arXiv:2402.17761](https://arxiv.org/abs/2402.17761)).
- There is a correspondence between qubit CSS codes and phase-free ZX calculus diagrams  ([arXiv:2204.14038](https://arxiv.org/abs/2204.14038)). ZX calculus provides a canonical form for the encoding circuit  ([arXiv:2406.12083](https://arxiv.org/abs/2406.12083)).
- Automated fault-tolerant encoding circuit synthesis  ([arXiv:2408.11894](https://arxiv.org/abs/2408.11894)).

## Transversal gates

- Transversal CNOT gates preserve the logical subspace, up to $X$-type Paulis, iff a qubit stabilizer code is CSS  ([arXiv:quant-ph/9605011](https://arxiv.org/abs/quant-ph/9605011)). The Paulis are necessary for when the code is stabilized by stabilizers with a minus in front of them, e.g., $-XXXX$ and $ZZZZ$.
- *Fold-transversal*  ([arXiv:1503.02065](https://arxiv.org/abs/1503.02065), [arXiv:1603.02286](https://arxiv.org/abs/1603.02286), [arXiv:2202.06647](https://arxiv.org/abs/2202.06647)) Clifford gates are transversal gates combined with qubit permutations. Some of these can be obtained from automorphism groups of the underlying classical codes  ([arXiv:1302.1035](https://arxiv.org/abs/1302.1035)).
- Necessary and sufficient conditions for diagonal physical gates on a CSS code to induce logical gates in the \term{Clifford hierarchy} have been formulated  ([arXiv:2109.13481](https://arxiv.org/abs/2109.13481)) ([arXiv:2204.13176](https://arxiv.org/abs/2204.13176)) ([arXiv:2406.00425](https://arxiv.org/abs/2406.00425)). There are routines that can determine what diagonal gates in the \term{Clifford hierarchy} are realized by a code  ([arXiv:2303.15615](https://arxiv.org/abs/2303.15615)).
- CSS code families with asymptotic rate $> 1/3$ and distance at $\geq 3$ do not admit logical qubit permutations from physical permutations  ([arXiv:2502.13889](https://arxiv.org/abs/2502.13889)).
- Diagonal transversal Clifford gates on $\ell$ codeblocks of a CSS code form $GL(\ell,\mathbb{F}_2)$ for non-self-dual CSS codes, $U(\ell,R_8)$ for *semi-self-dual CSS codes* (i.e., CSS codes whose $X$-type stabilizers are contained in the $Z$-type stabilizers), and $Sp(2\ell,\mathbb{F}_2)$ for self-dual CSS codes  ([arXiv:2507.10519](https://arxiv.org/abs/2507.10519)).
- Diagonal transversal gate groups can be defined using a set of equations  ([arXiv:2601.21514](https://arxiv.org/abs/2601.21514)).

## General gates

- LDPC CSS code symmetries called $XZ$-dualities allow for fold-transversal gates, i.e., transversal gates followed by qubit permutations  ([arXiv:2202.06647](https://arxiv.org/abs/2202.06647)).
- Generalized lattice surgery  ([arXiv:2301.13738](https://arxiv.org/abs/2301.13738)).
- Cohomology invariants give rise to logical gates implemented by constant-depth Clifford circuits for codes admitting a cup product structure  ([arXiv:2310.16982](https://arxiv.org/abs/2310.16982), [arXiv:2410.14631](https://arxiv.org/abs/2410.14631), [arXiv:2410.16250](https://arxiv.org/abs/2410.16250), [arXiv:2411.15848](https://arxiv.org/abs/2411.15848)). For example, a diagonal *copy-cup* gate in the $m$th level of the \term{Clifford hierarchy} can be implemented on a code admitting an $m$-fold cup product  ([arXiv:2410.16250](https://arxiv.org/abs/2410.16250)).
- Fault-tolerant CNOT gate using generalized lattice surgery  ([arXiv:2505.01370](https://arxiv.org/abs/2505.01370)).

## Fault tolerance

- Steane error correction  ([arXiv:quant-ph/9611027](https://arxiv.org/abs/quant-ph/9611027)), where fault-tolerance is ensured by preparing ancillary encoded states and extracting syndromes via $CNOT$ gates.
- Encoded $\ket{0}$ and $\ket{+}$ ancillas for Steane error correction can be prepared by hierarchical Steane-style verification; without code-specific optimizations, a two-level procedure uses at least $(t+1)^2$ noisy ancillas for a distance-$2t+1$ CSS code .
- Steane's method also yields non-destructive logical Pauli measurement for CSS codes by coupling the data block transversally to encoded $\ket{0}$ or $\ket{+}$ ancillas and classically decoding the ancilla measurement results .
- Transversal computational-basis measurement followed by classical decoding is a fault-tolerant gadget for logical measurement of all encoded qubits .
- Fault-tolerant error correction and logical measurements using flag qubits for distance-three cyclic CSS codes  ([arXiv:1803.09758](https://arxiv.org/abs/1803.09758)). Parallel syndrome extraction for distance-three codes can be done fault-tolerantly using one flag qubit  ([arXiv:2208.00581](https://arxiv.org/abs/2208.00581)). Distance-preserving flag fault-tolerant error correction can be done using lookup tables for small codes  ([arXiv:2306.12862](https://arxiv.org/abs/2306.12862)).
- Homomorphic gadgets fault-tolerant measurement unify Steane and Shor error correction  ([arXiv:2211.03625](https://arxiv.org/abs/2211.03625)).
- A fault-tolerant error-correction protocol using $O(d\log d)$ syndrome measurements can be applied to any CSS code with distance $d \geq \Omega(n^{\alpha})$ for any $\alpha > 0$  ([arXiv:2002.05180](https://arxiv.org/abs/2002.05180)).
- Fault-tolerant measurement-free scheme for low-distance CSS codes  ([arXiv:2307.13296](https://arxiv.org/abs/2307.13296)).
- Automated fault-tolerant encoding circuit synthesis  ([arXiv:2408.11894](https://arxiv.org/abs/2408.11894)).
- Fault-tolerant homological measurement of logical Pauli operators  ([arXiv:2410.02753](https://arxiv.org/abs/2410.02753)).
- Fault-tolerant CNOT gate using generalized lattice surgery  ([arXiv:2505.01370](https://arxiv.org/abs/2505.01370)).

## Code capacity threshold

- Bounds on code capacity thresholds for various noise models exist in terms of stabilizer generator weights  ([arXiv:1208.2317](https://arxiv.org/abs/1208.2317), [arXiv:1412.6172](https://arxiv.org/abs/1412.6172)).

## Decoders

- CSS syndrome decoding splits into two classical decoding problems: measuring the $Z$-type stabilizers yields the classical syndrome for bit-flip errors with respect to $C_X$, while measuring the $X$-type stabilizers yields the classical syndrome for phase errors with respect to $C_Z$. In the Hadamard basis, phase-error decoding is ordinary classical syndrome decoding.
- Coherent decoders allow for measurement-free error correction  ([arXiv:2109.00086](https://arxiv.org/abs/2109.00086)). One method is table/multi-control decoding  ([arXiv:1002.1536](https://arxiv.org/abs/1002.1536)), which scales exponentially with the number of ancillas used in syndrome measurement. A fault-tolerant measurement-free scheme for low-distance CSS codes is formulated in Ref.  ([arXiv:2307.13296](https://arxiv.org/abs/2307.13296)). Another method, the Ising-based decoder, utilizes the mapping of the effect of the noise to a statistical mechanical model  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143), [arXiv:2002.11733](https://arxiv.org/abs/2002.11733)) such that the decoding problem maps to preparation of the ground state of an Ising model. See  ([arXiv:1504.01444](https://arxiv.org/abs/1504.01444)) for a Rosetta stone comparing statistical mechanical models, CSS codes, and chain complexes. Models for bit- and phase-flip noise can be dual to one another  ([arXiv:2401.17359](https://arxiv.org/abs/2401.17359)).
- Transformer-based decoder  ([arXiv:2301.11930](https://arxiv.org/abs/2301.11930)).
- MaxSAT decoder  ([arXiv:2410.01673](https://arxiv.org/abs/2410.01673)).

## Realizations

- Fully homomorphic encryption  ([arXiv:1708.09156](https://arxiv.org/abs/1708.09156)).
- Cryptographic applications stemming from the monogamy of entanglement of CSS code and error words  ([arXiv:2107.05692](https://arxiv.org/abs/2107.05692)).

## Relations

- _parent_: [[concepts/qec/cpc]] — CSS codes are a subset of CPC codes  ([arXiv:1611.08012](https://arxiv.org/abs/1611.08012)), with the latter not requiring the two classical codes to be related.
- _parent_: [[concepts/qec/qudit-css]] — Modular-qudit CSS codes for $q=2$ are qubit CSS codes.
- _parent_: [[concepts/qec/galois-css]] — Galois-qudit CSS codes for $q=2$ are qubit CSS codes.
- _cousin_: [[concepts/qec/qubit-stabilizer]] — Qubit CSS codes are qubit stabilizer codes whose stabilizer groups admit a generating set of pure-$X$ and pure-$Z$ Pauli strings. 
Transversal CNOT gates preserve the logical subspace iff a qubit stabilizer code is CSS  ([arXiv:quant-ph/9605011](https://arxiv.org/abs/quant-ph/9605011)).
Any $⟦n,k,d⟧$ stabilizer code can be mapped onto a $⟦2n,2k,\geq d⟧$ two-block CSS code via symplectic doubling, which preserves geometric locality of a code up to a constant factor.
For any non-CSS qubit stabilizer code $\mathsf{C}$, there exists a CSS code $\mathsf{C}^{\prime}$ such that $\mathsf{C} = DQ\mathsf{C}^{\prime}$, where $D$ is a diagonal Clifford operator, and where $Q$ is an element of an XP stabilizer group .
There is a holographic relation between qubit CSS codes describing CFTs and qubit stabilizer codes describing path integrals over certain topologies  ([arXiv:2504.08724](https://arxiv.org/abs/2504.08724)).
- _cousin_: [[concepts/qec/movassagh-ouyang]] — Qubit CSS codes encoding one logical qubit are a subset of Movassagh-Ouyang codes.
- _cousin_: [[concepts/qec/two-block-quantum]] — Any $⟦n,k,d⟧$ stabilizer code can be mapped onto a $⟦2n,2k,\geq d⟧$ two-block CSS code via symplectic doubling, which preserves geometric locality of a code up to a constant factor.
- _cousin_: [`binary_linear`](https://errorcorrectionzoo.org/c/binary_linear) — The CSS construction uses two related binary linear codes, $C_X$ and $C_Z$.
- _cousin_: [`alternant`](https://errorcorrectionzoo.org/c/alternant) — Alternant codes used in the CSS construction yield quantum codes that asymptotically achieve the quantum GV bound  ([doi:10.1109/TIT.2022.3201239](https://doi.org/10.1109/TIT.2022.3201239)).
- _cousin_: [[concepts/qec/random-stabilizer]] — Random CSS codes asymptotically achieve linear distance with high probability, achieving the quantum GV bound  ([arXiv:quant-ph/9512032](https://arxiv.org/abs/quant-ph/9512032)).
- _cousin_: [[concepts/qec/binary-quantum-goppa]] — Quantum Goppa codes can exceed the quantum GV bound  ([doi:10.1007/s11128-006-0047-9](https://doi.org/10.1007/s11128-006-0047-9)).
- _cousin_: [[concepts/qec/qubit-subsystem-stabilizer]] — Qubit CSS "seed" codes can be used to produce subsystem qubit stabilizer codes  ([arXiv:2404.18302](https://arxiv.org/abs/2404.18302)).
- _cousin_: [[concepts/qec/translationally-invariant-stabilizer]] — The mapping of qubit CSS codes to chain complexes allows the application of structures from topology to error correction. Chain complexes describing some QLDPC codes  ([arXiv:2012.02249](https://arxiv.org/abs/2012.02249), [arXiv:2309.16104](https://arxiv.org/abs/2309.16104)), and, more generally, CSS codes  ([arXiv:2404.16736](https://arxiv.org/abs/2404.16736)) can be "lifted" into higher-dimensional manifolds admitting some notion of geometric locality. Qubit CSS codes admit several dualities  ([arXiv:1710.02646](https://arxiv.org/abs/1710.02646), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032)). In particular, a CSS code and two dual classical codes can be organized by the same 2-complex, and gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) either classical code yields the same CSS code up to Hadamard  ([arXiv:2310.16032](https://arxiv.org/abs/2310.16032)).
- _cousin_: [[concepts/qec/topological-abelian]] — The mapping of qubit CSS codes to chain complexes allows the application of structures from topology to error correction. Chain complexes describing some QLDPC codes  ([arXiv:2012.02249](https://arxiv.org/abs/2012.02249), [arXiv:2309.16104](https://arxiv.org/abs/2309.16104)), and, more generally, CSS codes  ([arXiv:2404.16736](https://arxiv.org/abs/2404.16736)) can be "lifted" into higher-dimensional manifolds admitting some notion of geometric locality. Qubit CSS codes admit several dualities  ([arXiv:1710.02646](https://arxiv.org/abs/1710.02646), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032)). In particular, a CSS code and two dual classical codes can be organized by the same 2-complex, and gauging  ([arXiv:1202.3120](https://arxiv.org/abs/1202.3120), [arXiv:1407.1025](https://arxiv.org/abs/1407.1025), [arXiv:1603.04442](https://arxiv.org/abs/1603.04442), [arXiv:1603.05182](https://arxiv.org/abs/1603.05182), [arXiv:1605.01640](https://arxiv.org/abs/1605.01640), [arXiv:1805.01836](https://arxiv.org/abs/1805.01836), [arXiv:1806.08679](https://arxiv.org/abs/1806.08679), [arXiv:2108.11402](https://arxiv.org/abs/2108.11402), [arXiv:2310.16032](https://arxiv.org/abs/2310.16032), [arXiv:2410.02213](https://arxiv.org/abs/2410.02213)) either classical code yields the same CSS code up to Hadamard  ([arXiv:2310.16032](https://arxiv.org/abs/2310.16032)).
- _cousin_: [[concepts/qec/cft]] — There is a holographic relation between qubit CSS codes describing CFTs and qubit stabilizer codes describing path integrals over certain topologies  ([arXiv:2504.08724](https://arxiv.org/abs/2504.08724)).

## Notes

- See Refs.  ([arXiv:quant-ph/9605021](https://arxiv.org/abs/quant-ph/9605021), [doi:10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667)) for simple examples of CSS codes.
- Introduction to \ref{topic:CSS-to-homology-correspondence} by [M. Hastings](https://www.youtube.com/watch?v=SeLpWg_8qlc); see also Refs.  ([arXiv:1310.5376](https://arxiv.org/abs/1310.5376), [arXiv:1504.01444](https://arxiv.org/abs/1504.01444)).
- Entanglement purification protocols with qubit CSS codes are related to quantum key distribution (QKD)  ([arXiv:quant-ph/0003004](https://arxiv.org/abs/quant-ph/0003004)).
- Qubit CSS codes can be used in quantum repeaters  ([arXiv:0809.3629](https://arxiv.org/abs/0809.3629)).
