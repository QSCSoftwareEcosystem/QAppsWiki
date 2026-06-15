---
type: concept
name: Qubit code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases:
- Qubit subspace code
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/galois-into-galois
- concepts/qec/oa-qubits-into-qubits
- concepts/qec/qubit-classical-into-quantum
- concepts/qec/qudits-into-qudits
- concepts/qec/spins-into-spins
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qubits_into_qubits
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qubits_into_qubits
---

# Qubit code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qubits_into_qubits) (`code_id: qubits_into_qubits`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes $K$-dimensional Hilbert space into a $2^n$-dimensional (i.e., $n$-qubit) Hilbert space.
Usually denoted as $((n,K))$ or $((n,K,d))$, where $d$ is the code's distance.

The qubit codes are *equivalent* if the codespace of one code can be mapped into that of the other under a tensor product of single-qubit unitary operations and a qubit permutation.
Equivalent qubit codes have the same logical dimension and distance, and their decoding problems have the same computational complexity up to the corresponding relabeling of errors .

(source: raw/error-correction-zoo.md)

## Protection

An $((n,K,d))$ code with distance $d$ detects errors acting on up to $d-1$ qubits, corrects erasure errors on up to $d-1$ qubits  ([arXiv:quant-ph/9610042](https://arxiv.org/abs/quant-ph/9610042)), or corrects errors acting on up to $\lfloor (d-1)/2 \rfloor$ qubits.
Combinations of errors and erasures can also be corrected  ([arXiv:2511.01080](https://arxiv.org/abs/2511.01080)).
The number of correctable errors is often called the *decoding radius*, and it is upper bounded by half of the code distance.
As a result, qubit codes cannot tolerate adversarial errors on more than $(1-R)/4$ registers, where $R = \log_2 K/n$ is the code rate.

\subsection{Pauli-string error basis}
\label{topic:pauli}

A convenient and often considered error set is the *Pauli error* or *Pauli string* basis.

\begin{defterm}{Pauli strings}
For a single qubit, this set consists of products of powers of the Pauli matrices
\begin{align}
  X=\begin{pmatrix}0 & 1\\
  1 & 0
  \end{pmatrix}~,
\end{align}
\begin{align}
  Y=iXZ=\begin{pmatrix}0 & -i\\
  i & 0
  \end{pmatrix}~,
\end{align}
\begin{align}
  Z=\begin{pmatrix}1 & 0\\
  0 & -1
  \end{pmatrix}~.
\end{align}
The operator $X$ is a bit flip, $Z$ is a phase flip, and $Y$ is a combined bit and phase flip up to an overall physically irrelevant phase .
For multiple qubits, error set elements are tensor products of elements of the single-qubit error set.
Tensor products of $X$ ($Z$) Paulis acting on different qubits are called $X$*-type* ($Z$*-type*) Pauli strings.
Combining the $X$-type and $Z$-type strings with $i$ forms a group called the *Pauli group* on $n$ qubits, while combining them with $-1$ forms the *real Pauli group*.
\end{defterm}

The Pauli error set is a unitary and Hermitian basis for linear operators on the multi-qubit Hilbert space that is orthonormal under the Hilbert-Schmidt inner product; it is a prototypical nice error basis.
The distance associated with this set is often the minimum weight of a Pauli string that implements a nontrivial logical operation in the code.

\subsection{Noise channels}

A quantum channel that admits a set of Pauli strings as its Kraus operators is called a *Pauli channel*, and such channels are typically more tractable than the more general, non-Pauli channels.
Relevant Pauli channels include dephasing noise and depolarizing noise (a.k.a. Werner-Holevo channel  ([arXiv:quant-ph/0203003](https://arxiv.org/abs/quant-ph/0203003))).
A single-qubit dephasing channel has Kraus operators proportional to $I$ and $Z$, while the single-qubit depolarizing channel has equal probabilities for the $X$, $Y$, and $Z$ errors; both are Pauli channels .
One can extract a binary memoryless symmetric channel from a Pauli channel that is a classical counterpart to the Pauli channel  ([arXiv:1904.04713](https://arxiv.org/abs/1904.04713)).

Relevant non-Pauli channels are AD noise, erasure (which maps all qubit states into a third state $|e\rangle$ outside of the qubit Hilbert space), and biased erasure  ([arXiv:2302.03063](https://arxiv.org/abs/2302.03063)) (in which case only the $|1\rangle$ qubit state is mapped to $|e\rangle$).
Erasure channels are easier to correct than general channels because one can, in principle, measure whether the state left the qubit Hilbert space and thereby learn which qubits were erased without measuring the stored qubit state .
Noise can be correlated in space or in time, with the latter being an example of a non-Markovian phenomenon  ([arXiv:quant-ph/0505153](https://arxiv.org/abs/quant-ph/0505153), [arXiv:2012.01894](https://arxiv.org/abs/2012.01894)).

\subsection{Quantum weight enumerators and pure distance}
\label{topic:quantum-weight-enumerator}

\begin{defterm}{Quantum weight enumerator}
Determining protection and bounds on code parameters can also be done using the code's Shor-Laflamme *quantum weight enumerator*  ([arXiv:quant-ph/9610040](https://arxiv.org/abs/quant-ph/9610040)) (cf. weight enumerators)
  \begin{align}
  \begin{split}
    A(x)&=\sum_{j=0}^{n}A_{j}x^{j}\\
    A_{j}&=\frac{1}{K^{2}}\sum_{\text{wt-}j\text{ Paulis }P}\left|\text{tr}(P\Pi)\right|^{2}~,
  \end{split}
  \end{align}
where $K=\mathrm{tr}(\Pi)$ is the dimension of the code subspace, $\Pi$ is the code projection, and where the sum is over the Pauli group modulo the subgroup of phases (hence, the dagger below is necessary in case the coset representative is not Hermitian).

The dual quantum weight enumerator is
  \begin{align}
  \begin{split}
    B(x)&=\sum_{j=0}^{n}B_{j}x^{j}\\
    B_{j}&=\frac{1}{K}\sum_{\text{wt-}j\text{ Paulis }P}\text{tr}(P\Pi P^{\dagger}\Pi)~,
  \end{split}
  \end{align}
and the two satisfy the *quantum MacWilliams identity*  ([arXiv:quant-ph/9610040](https://arxiv.org/abs/quant-ph/9610040)); see .
Their coefficients satisfy $A_0=B_0=1$ and $B_j\geq A_j\geq 0$ for all $j$  ([arXiv:quant-ph/9610040](https://arxiv.org/abs/quant-ph/9610040)).
This identity gives rise to quantum linear programming (LP) bounds  ([arXiv:quant-ph/9611001](https://arxiv.org/abs/quant-ph/9611001), [arXiv:quant-ph/9709049](https://arxiv.org/abs/quant-ph/9709049)); see the book .
Weight enumerators give rise to an analogue of Poisson summation for qubit and, more generally, modular-qudit stabilizer codes  ([arXiv:2405.19643](https://arxiv.org/abs/2405.19643)).
\end{defterm}

\begin{defterm}{Pure distance}
The distance $d$ of a qubit code is the smallest integer $0<j=d$ at which the quantum weight enumerator is not equal to its dual, $A_j \neq B_j$  ([arXiv:quant-ph/9906126](https://arxiv.org/abs/quant-ph/9906126)).
A code is called *pure* if $A_j = 0$ for all $0 < j < d$; otherwise, the code is called *impure*.
The *pure distance*  ([arXiv:1409.2559](https://arxiv.org/abs/1409.2559), [arXiv:2107.14252](https://arxiv.org/abs/2107.14252)) (a.k.a. diagonal distance  ([arXiv:0712.1979](https://arxiv.org/abs/0712.1979), [arXiv:2107.11286](https://arxiv.org/abs/2107.11286))) $d_{\textnormal{pure}}$ is the smallest integer $1 < j=d_{\textnormal{pure}}$ at which $A_j > 0$.
Codes for which $d_{\textnormal{pure}} < d$ are impure, otherwise they are pure.
For impure codes, there exists a Pauli error of weight less than the $d$ that has a nonzero expectation value with respect to a code state.

Degenerate qubit codes are impure, but impure codes may not be degenerate  ([arXiv:quant-ph/9608006](https://arxiv.org/abs/quant-ph/9608006)).
There are subtleties with defining degeneracy for non-stabilizer qubit codes with even distance .
\end{defterm}

Other types of quantum weight enumerators are the Rains unitary enumerators  ([arXiv:quant-ph/9612015](https://arxiv.org/abs/quant-ph/9612015)) and the *Rains shadow enumerators*  ([arXiv:quant-ph/9611001](https://arxiv.org/abs/quant-ph/9611001)) (see also  ([arXiv:quant-ph/0406063](https://arxiv.org/abs/quant-ph/0406063))), and *signed weight enumerators* taking into account the sign of the expectation value of a Pauli string  ([arXiv:1702.06990](https://arxiv.org/abs/1702.06990)).
For qubit codes, the shadow enumerator coefficients are nonnegative and are determined by the Shor-Laflamme enumerator  ([arXiv:quant-ph/9611001](https://arxiv.org/abs/quant-ph/9611001)) via
\begin{align}
  Sh(x)=\frac{K}{2^n}(1+3x)^n A\left(\frac{x-1}{1+3x}\right)~.
\end{align}
Rains shadow enumerators are related to Bell sampling  ([arXiv:2408.16914](https://arxiv.org/abs/2408.16914)).
These notions can be generalized to qudit codes and other error bases  ([arXiv:0810.2574](https://arxiv.org/abs/0810.2574), [doi:10.1016/j.aam.2020.102085](https://doi.org/10.1016/j.aam.2020.102085), [arXiv:2211.02756](https://arxiv.org/abs/2211.02756), [arXiv:2308.05152](https://arxiv.org/abs/2308.05152)).
There are techniques to compute them for general codes  ([arXiv:2308.05152](https://arxiv.org/abs/2308.05152)).
Semidefinite programming (SDP) hierarchies and a quantum Delsarte bound have been developed for qubit codes, with rational infeasibility certificates later yielding rigorous non-existence proofs and improved upper bounds for small code parameters  ([arXiv:2408.10323](https://arxiv.org/abs/2408.10323), [arXiv:2603.19901](https://arxiv.org/abs/2603.19901)).

## Rate

Exact two-way assisted capacities have been obtained for the erasure and dephasing channels  ([arXiv:1510.08863](https://arxiv.org/abs/1510.08863)). There are many bounds on the quantum capacity of the depolarizing channel (e.g.,  ([arXiv:quant-ph/0607039](https://arxiv.org/abs/quant-ph/0607039))); see review  ([arXiv:1801.02019](https://arxiv.org/abs/1801.02019)). The optimal asymptotic error exponent of entanglement distillation is given by the reverse relative entropy of entanglement, a single-letter quantity  ([arXiv:2408.07067](https://arxiv.org/abs/2408.07067)).

## Transversal gates

- A qubit code is $U$-*quasi-transversal* if it can realize the logical gate $U$ in the third level of the \term{Clifford hierarchy} using the physical gate $C T^{\otimes n}$, where $C$ is some Clifford gate  ([arXiv:1606.01904](https://arxiv.org/abs/1606.01904)).
- If a qubit code $Q$ of length $n$ has compact subgroups $N\triangleleft G\leq \mathrm{Aut}(Q)$ such that $G/N$ is finite, non-Abelian, simple, and not $A_5$, then $n$ is at least the minimal permutation degree $\mu(G/N)$  ([arXiv:2604.15111](https://arxiv.org/abs/2604.15111)).

## General gates

- Computing with Clifford gates, Pauli measurements, and classical feedforward acting on stabilizer states only can be efficiently simulated on a classical computer by tracking stabilizer and logical generators, according to the *Gottesman-Knill theorem*  ([arXiv:quant-ph/9807006](https://arxiv.org/abs/quant-ph/9807006)).
There is a canonical form for Clifford circuits  ([arXiv:2003.09412](https://arxiv.org/abs/2003.09412), [arXiv:2408.15202](https://arxiv.org/abs/2408.15202)) and many algorithms for simulating them  ([arXiv:quant-ph/0406196](https://arxiv.org/abs/quant-ph/0406196), [arXiv:1712.03554](https://arxiv.org/abs/1712.03554), [arXiv:2301.02356](https://arxiv.org/abs/2301.02356)).
Universal quantum computing can be achieved using Clifford gates and a single type of non-Clifford gate, such as the $T$ gate  ([arXiv:quant-ph/9503016](https://arxiv.org/abs/quant-ph/9503016)).
More generally, the *Solovay-Kitaev* theorem  ([doi:10.1070/RM1997v052n06ABEH002155](https://doi.org/10.1070/RM1997v052n06ABEH002155), [doi:10.1090/gsm/047](https://doi.org/10.1090/gsm/047)) states that any subset of gates that generates a dense subgroup of the full $n$-qubit gate group can be used to construct any gate to arbitrary accuracy (see  ([arXiv:quant-ph/0505030](https://arxiv.org/abs/quant-ph/0505030)) ([doi:10.1017/cbo9780511976667.019](https://doi.org/10.1017/cbo9780511976667.019))). The task of approximating a desired gate by Clifford gates and a fixed set of non-Clifford gates is called *gate compilation* or *circuit synthesis*.
- Non-Clifford gates are typically more difficult to implement than Clifford gates and so are treated as a resource. Gate errors in circuit synthesis can sometimes add up destructively  ([arXiv:1612.01011](https://arxiv.org/abs/1612.01011)). There is a threshold against depolarizing noise for any single-qubit gate that determines if the gate enables universal quantum computation  ([arXiv:0907.3189](https://arxiv.org/abs/0907.3189), [arXiv:1011.2497](https://arxiv.org/abs/1011.2497)).
- The most studied set of universal gates is generated by the Clifford+$T$ gate set. Exactly optimizing $T$-gate count in circuit synthesis is $NP$-hard  ([arXiv:2310.05958](https://arxiv.org/abs/2310.05958), [arXiv:2503.06045](https://arxiv.org/abs/2503.06045)). Gate compilation can be done using various heuristic procedures  ([arXiv:1303.2042](https://arxiv.org/abs/1303.2042), [arXiv:1308.4134](https://arxiv.org/abs/1308.4134), [arXiv:1601.07363](https://arxiv.org/abs/1601.07363), [arXiv:1601.07601](https://arxiv.org/abs/1601.07601), [arXiv:1710.07345](https://arxiv.org/abs/1710.07345), [arXiv:1712.01557](https://arxiv.org/abs/1712.01557), [arXiv:1808.00128](https://arxiv.org/abs/1808.00128), [arXiv:2101.12223](https://arxiv.org/abs/2101.12223), [arXiv:2110.10292](https://arxiv.org/abs/2110.10292), [arXiv:2506.15147](https://arxiv.org/abs/2506.15147)), e.g., *ZX calculus* (a.k.a. Penrose spin calculus)  ([arXiv:1903.10477](https://arxiv.org/abs/1903.10477), [arXiv:1911.09039](https://arxiv.org/abs/1911.09039), [arXiv:2004.05164](https://arxiv.org/abs/2004.05164), [arXiv:2109.01076](https://arxiv.org/abs/2109.01076)), reinforcement learning  ([arXiv:2105.15048](https://arxiv.org/abs/2105.15048), [arXiv:2103.07585](https://arxiv.org/abs/2103.07585), [arXiv:2212.04508](https://arxiv.org/abs/2212.04508), [arXiv:2402.14396](https://arxiv.org/abs/2402.14396), [arXiv:2404.14865](https://arxiv.org/abs/2404.14865), [arXiv:2511.09951](https://arxiv.org/abs/2511.09951)), genetic algorithms  ([arXiv:2504.09391](https://arxiv.org/abs/2504.09391)), or Hermitian lattices  ([arXiv:2405.19302](https://arxiv.org/abs/2405.19302)).
There is an optimal asymptotic scaling of the number of T gates needed to prepare an arbitrary state  ([arXiv:1812.00954](https://arxiv.org/abs/1812.00954), [arXiv:2411.04790](https://arxiv.org/abs/2411.04790)).
- Other gate sets for generating universal gates are Clifford + $\sqrt{T}$  ([arXiv:2203.10064](https://arxiv.org/abs/2203.10064)), Toffoli and Hadamard  ([arXiv:quant-ph/0205115](https://arxiv.org/abs/quant-ph/0205115), [arXiv:1212.5069](https://arxiv.org/abs/1212.5069)), cosine-sine  ([arXiv:quant-ph/0404089](https://arxiv.org/abs/quant-ph/0404089)), and icosahedral super-golden gates  ([arXiv:1704.02106](https://arxiv.org/abs/1704.02106), [arXiv:2205.03007](https://arxiv.org/abs/2205.03007), [arXiv:2509.09047](https://arxiv.org/abs/2509.09047)). The $n$-qubit Toffoli gates can be exactly realized using at least $nT$ gates  ([arXiv:1904.01124](https://arxiv.org/abs/1904.01124)), but this can be relaxed at the expense of some errors  ([arXiv:2510.07223](https://arxiv.org/abs/2510.07223)).
- \begin{defterm}{Clifford hierarchy} \label{topic:clifford-hierarchy} The Clifford hierarchy  ([arXiv:quant-ph/9908010](https://arxiv.org/abs/quant-ph/9908010), [arXiv:1608.06596](https://arxiv.org/abs/1608.06596), [arXiv:1902.04022](https://arxiv.org/abs/1902.04022), [arXiv:2212.05398](https://arxiv.org/abs/2212.05398), [arXiv:2410.11818](https://arxiv.org/abs/2410.11818)) is a tower of gate sets which includes Pauli and Clifford gates at its first two levels, and non-Clifford gates at higher levels. The $k$th level is defined recursively by \begin{align} C_k = \{ U | U P U^{\dagger} \in C_{k-1} \}~, \end{align} where $P$ is any Pauli matrix, where $C_1$ is the Pauli group, and where $C_2$ is the Clifford group. Gates for one qubit have been classified  ([arXiv:2501.07939](https://arxiv.org/abs/2501.07939)). \end{defterm}
- Arbitrary $n$-qubit circuits can be implemented fault-tolerantly in a 3D architecture using $O(n^{3/2}\log^3 n)$ qubits, and in a 2D architecture using only $O(n^2 \log^3 n)$ qubits  ([arXiv:2402.13863](https://arxiv.org/abs/2402.13863)).
- Fault-tolerant gates can be done for any code supporting a transversal implementation of Pauli gates using generalized gate teleportation  ([arXiv:2409.11616](https://arxiv.org/abs/2409.11616)).

## Decoders

- Syndrome measurements are assumed to be perfect in the *code-capacity model*. Incorporating faulty syndrome measurements can be done using the *phenomenological noise model*, which simulates errors during syndrome extraction by flipping some of the bits of the measured syndrome bitstring. In the more involved *circuit-level noise model*, every component of the syndrome extraction circuit can be faulty.
- The decoder determining the most likely error given a noise channel is called the *maximum probability error* (MPE) decoder. For few-qubit codes ($n$ is small), MPE decoding can be based on creating a lookup table. For infinite code families, the size of such a table scales exponentially with $n$, so approximate decoding algorithms scaling polynomially with $n$ have to be used.
- \begin{defterm}{Effective distance and hook errors} \label{topic:effective-distance} Decoders are characterized by an effective distance (a.k.a. *circuit-level distance* or fault distance), the minimum number of faulty operations during syndrome measurement that is required to make an undetectable error. A code is *distance-preserving* if it admits a decoder whose circuit-level distance is equal to the code distance. A particularly dangerous class of syndrome measurement circuit faults are *hook errors*, which are ancilla faults that cause more than one data-qubit error  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143)). Hook errors occur at specific places in a syndrome extraction circuit and can sometimes be removed by re-ordering the gates of the circuit. If not, the use of *flag qubits* (see ) to detect hook errors may be necessary to yield fault-tolerant decoders. \end{defterm}

## Fault tolerance

- There are lower bounds on the overhead of fault-tolerant QEC in terms of the capacity of the noise channel  ([arXiv:2202.00119](https://arxiv.org/abs/2202.00119)). A more stringent bound applies to geometrically local QEC due to the fact that locality constrains the growth of the entanglement that is needed for protection  ([arXiv:2302.04317](https://arxiv.org/abs/2302.04317)).
- Arbitrary $n$-qubit circuits can be implemented fault-tolerantly in a 3D architecture using $O(n^{3/2}\log^3 n)$ qubits, and in a 2D architecture using only $O(n^2 \log^3 n)$ qubits  ([arXiv:2402.13863](https://arxiv.org/abs/2402.13863)).
- Fault-tolerant gates can be done for any code supporting a transversal implementation of Pauli gates using generalized gate teleportation  ([arXiv:2409.11616](https://arxiv.org/abs/2409.11616)).

## Threshold

- \begin{defterm}{Computational threshold}
\label{topic:computational-threshold}
A fault-tolerant computational threshold is the maximum noise rate in a particular single-parameter noise model below which any logical computation of size $M$ can be executed on a physical-qubit architecture to arbitrary accuracy and with an overhead of order $O(M\text{polylog}M)$.
The first methods to achieve a computational threshold use recursively concatenated stabilizer code families  ([arXiv:quant-ph/9702058](https://arxiv.org/abs/quant-ph/9702058), [arXiv:quant-ph/9705031](https://arxiv.org/abs/quant-ph/9705031), [arXiv:quant-ph/9903099](https://arxiv.org/abs/quant-ph/9903099), [arXiv:quant-ph/9906129](https://arxiv.org/abs/quant-ph/9906129), [arXiv:quant-ph/0410047](https://arxiv.org/abs/quant-ph/0410047), [arXiv:quant-ph/0504218](https://arxiv.org/abs/quant-ph/0504218), [arXiv:quant-ph/0703230](https://arxiv.org/abs/quant-ph/0703230), [arXiv:quant-ph/0604090](https://arxiv.org/abs/quant-ph/0604090)); such a threshold is called a *concatenated threshold*.
Initially proven under local stochastic noise, the concatenated threshold theorem also holds for various types of non-Markovian noise  ([arXiv:quant-ph/0402104](https://arxiv.org/abs/quant-ph/0402104), [arXiv:quant-ph/0504218](https://arxiv.org/abs/quant-ph/0504218), [arXiv:quant-ph/0703230](https://arxiv.org/abs/quant-ph/0703230), [arXiv:quant-ph/0510231](https://arxiv.org/abs/quant-ph/0510231)) and leakage errors  ([arXiv:quant-ph/0511065](https://arxiv.org/abs/quant-ph/0511065)).
This theorem can be rephrased in terms of Bernoulli site percolation  ([arXiv:quant-ph/0307166](https://arxiv.org/abs/quant-ph/0307166)).
The resulting concatenated code is highly degenerate, with all but an exponentially small fraction of generators having small weights. 
Circuit and measurement designs have to take care of the few stabilizer generators with large weights in order to be fault tolerant, but measurement duration may not pose a threat to scalability  ([arXiv:quant-ph/0607047](https://arxiv.org/abs/quant-ph/0607047)).
While generic concatenated methods yield a computational threshold with overhead $O(M\text{polylog}M)$, concatenations using quantum Hamming codes can additionally attain constant space overhead with quasi-polylogarithmic time overhead  ([arXiv:2207.08826](https://arxiv.org/abs/2207.08826), [arXiv:2402.09606](https://arxiv.org/abs/2402.09606)), and concatenations of the Steane code and certain QLDPC codes further improve this time overhead to polylogarithmic while keeping constant space overhead  ([arXiv:2411.03683](https://arxiv.org/abs/2411.03683)).
Subsequently, thresholds were determined for infinite families of lattice stabilizer codes, starting with the toric code  ([arXiv:quant-ph/0110143](https://arxiv.org/abs/quant-ph/0110143)); such a threshold is colloquially called a *topological threshold*.
When different classes of circuit locations have different error rates, the single-number threshold generalizes to a *threshold surface* in the space of error-rate vectors. A one-level crossing where a particular logical location becomes more reliable is then not a full-fledged threshold for the entire circuit; deciding whether a protocol really improves may require following the coupled recurrence relations through additional concatenation levels .
Fault-tolerant computations with no notion of locality can be made local on a 2D or 3D geometry with minimal overhead  ([arXiv:2402.13863](https://arxiv.org/abs/2402.13863)).
\end{defterm}
- There is an upper bound on the threshold under local update recovery that is derived via quantum optimal transport  ([arXiv:quant-ph/0310136](https://arxiv.org/abs/quant-ph/0310136)) (see also Ref.  ([arXiv:2309.16241](https://arxiv.org/abs/2309.16241))).
- There is a threshold against depolarizing noise for any single-qubit gate that determines if the gate enables universal quantum computation  ([arXiv:0907.3189](https://arxiv.org/abs/0907.3189), [arXiv:1011.2497](https://arxiv.org/abs/1011.2497)).
- \begin{defterm}{Measurement threshold} \label{topic:measurement-threshold} One can derive conditions quantifying how many random single-qubit measurements can be made without destroying the logical information  ([arXiv:2402.00145](https://arxiv.org/abs/2402.00145)). The measurement threshold is the maximum total probability that a single qubit is measured in a random $X$, $Y$, or $Z$ basis at which the logical information is still recoverable. The measurement threshold is at least as large as the erasure threshold  ([arXiv:2402.00145](https://arxiv.org/abs/2402.00145)). \end{defterm}
- There is a dynamical phase transition between a bounded-error and an unbounded-error phase for a model of qubits weakly coupled to a refrigerator  ([arXiv:2411.12805](https://arxiv.org/abs/2411.12805)).

## Relations

- _parent_: [[concepts/qec/oa-qubits-into-qubits]] — An OA qubit code which has no gauge qubits and no block structure is a qubit code.
- _parent_: [[concepts/qec/qudits-into-qudits]] — Modular-qudit quantum codes for $q=2$ correspond to qubit codes. Modular-qudit codes  ([arXiv:2502.05992](https://arxiv.org/abs/2502.05992)), circuits  ([arXiv:1905.10481](https://arxiv.org/abs/1905.10481)), and magic-state distillation schemes  ([arXiv:1205.3104](https://arxiv.org/abs/1205.3104), [arXiv:1406.3055](https://arxiv.org/abs/1406.3055)) can have advantages over their qubit counterparts. Modular qudits are useful for simulating gauge theories  ([arXiv:2207.01731](https://arxiv.org/abs/2207.01731), [arXiv:2209.10781](https://arxiv.org/abs/2209.10781)). There are several ways to embed one or more qubits into a single modular qudit, yielding efficient qubit gate decompositions  ([arXiv:2311.12003](https://arxiv.org/abs/2311.12003)).
- _parent_: [[concepts/qec/galois-into-galois]] — Galois-qudit quantum codes for $q=2$ correspond to qubit codes.
- _parent_: [[concepts/qec/spins-into-spins]] — Spin codes with spin $\ell=1/2$ correspond to qubit codes since the single-qubit Pauli matrices generate the Lie algebra of $SU(2)$.
- _cousin_: [`clifford_group`](https://errorcorrectionzoo.org/c/clifford_group) — Computing with Clifford gates, Pauli measurements, and classical feedforward acting on stabilizer states only can be efficiently simulated on a classical computer by tracking stabilizer and logical generators, according to the *Gottesman-Knill theorem*  ([arXiv:quant-ph/9807006](https://arxiv.org/abs/quant-ph/9807006)).
There is a canonical form for Clifford circuits  ([arXiv:2003.09412](https://arxiv.org/abs/2003.09412), [arXiv:2408.15202](https://arxiv.org/abs/2408.15202)) and many algorithms for simulating them  ([arXiv:quant-ph/0406196](https://arxiv.org/abs/quant-ph/0406196), [arXiv:1712.03554](https://arxiv.org/abs/1712.03554), [arXiv:2301.02356](https://arxiv.org/abs/2301.02356)).
Universal quantum computing can be achieved using Clifford gates and a single type of non-Clifford gate, such as the $T$ gate  ([arXiv:quant-ph/9503016](https://arxiv.org/abs/quant-ph/9503016)).
More generally, the *Solovay-Kitaev* theorem  ([doi:10.1070/RM1997v052n06ABEH002155](https://doi.org/10.1070/RM1997v052n06ABEH002155), [doi:10.1090/gsm/047](https://doi.org/10.1090/gsm/047)) states that any subset of gates that generates a dense subgroup of the full $n$-qubit gate group can be used to construct any gate to arbitrary accuracy (see  ([arXiv:quant-ph/0505030](https://arxiv.org/abs/quant-ph/0505030)) ([doi:10.1017/cbo9780511976667.019](https://doi.org/10.1017/cbo9780511976667.019))). The task of approximating a desired gate by Clifford gates and a fixed set of non-Clifford gates is called *gate compilation* or *circuit synthesis*.
- _cousin_: [[concepts/qec/qubit-classical-into-quantum]] — Qubit c-q codes are qubit codes designed to transmit classical information.

## Notes

- There is a relation between one-way entanglement distillation protocols and QECCs  ([arXiv:quant-ph/9604024](https://arxiv.org/abs/quant-ph/9604024)).
- Qubit error correction is required for unconditionally secure quantum key distribution  ([arXiv:quant-ph/9803006](https://arxiv.org/abs/quant-ph/9803006)).
- See [Qiskit QEC framework](https://github.com/qiskit-community/qiskit-qec) for realizing protocols on IBM machines.
- Any logical state $\psi$ of an $((n,2^k,d))$ qubit code obeys $E_h(\psi) \geq \left(d/2^h-1\right)H^{-1}(k/n)$, giving a distance- and rate-dependent lower bound on geometric entanglement  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)).
- Expanding any logical state of a distance-$d$ qubit code in any computational basis requires at least $2^{d-1}$ basis states  ([arXiv:2405.01332](https://arxiv.org/abs/2405.01332)).
