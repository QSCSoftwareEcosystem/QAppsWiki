---
type: concept
name: Finite-dimensional quantum error-correcting code
status: provisional
updated: '2026-06-15'
concept_kind: qec
aliases: []
domains:
- quantum-error-correction
related_concepts:
- concepts/qec/qecc
sources:
- raw/error-correction-zoo.md
- https://errorcorrectionzoo.org/c/qecc_finite
provenance_status: needs-verification
imported_from: error-correction-zoo
imported_id: qecc_finite
---

# Finite-dimensional quantum error-correcting code

> **Imported by `qappswiki import-zoo eczoo`** from the [Error Correction Zoo](https://errorcorrectionzoo.org/c/qecc_finite) (`code_id: qecc_finite`). Text is reused under **CC-BY-SA**; attribute the Error Correction Zoo (errorcorrectionzoo.org), CC-BY-SA. This is a `needs-verification` page — confirm the claims against the cited primary sources before relying on it.

## Description

Encodes quantum information in a $K$-dimensional (*logical*) subspace of an $N$-dimensional (*physical*) Hilbert space such that it is possible to recover said information from errors. The logical subspace is spanned by a basis comprised of *code basis states* or *codewords*.

(source: raw/error-correction-zoo.md)

## Protection

Denoting Hilbert spaces by the letter $\mathsf{H}$, a finite-dimensional quantum code $(U,\cal{E})$ is a partial isometry $U:\mathsf{H}_{K}\to\mathsf{H}_{N}$ and a set of correctable errors ${\cal{E}}:\mathsf{H}_N\to\mathsf{H}_M$ with the following property: there exists a quantum operation ${\cal{D}}:\mathsf{H}_M\to \mathsf{H}_K$ such that for all $E\in\cal{E}$ and states $|\psi\rangle\in\mathsf{H}_{K}$,
\begin{align}
{\cal D}(EU|\psi\rangle\langle\psi|U^{\dagger}E^{\dagger})=c(E,|\psi\rangle)|\psi\rangle\langle\psi|\end{align}
for some constant $c$ . A code is said to *protect against* or *correct* the errors $\mathcal{E}$.

\subsection{Knill-Laflamme error-correction conditions}

Equivalently, correction capability is determined by the quantum
error-correction conditions. A code that satisfies
these conditions approximately, i.e., up to some small quantifiable error, is
called an approximate code.

\begin{defterm}{Knill-Laflamme conditions}
The Knill-Laflamme error-correction conditions  ([doi:10.1103/PhysRevA.55.900](https://doi.org/10.1103/PhysRevA.55.900), [arXiv:quant-ph/9604024](https://arxiv.org/abs/quant-ph/9604024)) ([doi:10.1017/CBO9780511976667](https://doi.org/10.1017/CBO9780511976667)) are necessary and sufficient conditions for a code to successfully
correct a set of errors in a finite-dimensional Hilbert space.
A code (defined by a partial isometry $U$) with code space projector $\Pi = U U^\dagger$
can correct a set of errors $\{ E_j \}$ if and only if
\begin{align}
  \Pi E_i^\dagger E_j \Pi = c_{ij}\, \Pi\qquad\text{for all $i,j$,}
\end{align}
where the *QEC matrix* elements $c_{ij}$ are arbitrary complex numbers.  
The term $\Pi E_i^\dagger E_j \Pi$ can be split into two types of conditions, the *diagonal* (a.k.a. non-deformation or invariance) conditions $\langle \psi| E_i^\dagger E_j | \psi\rangle$ for a codeword $|\psi\rangle$, and the *off-diagonal* (a.k.a. orthogonality or distinguishability) conditions $\langle \psi| E_i^\dagger E_j | \phi\rangle$ for two orthogonal codewords $|\psi\rangle$ and $|\phi\rangle$.
By linearity of quantum error correction, if a code corrects a set of errors $\mathcal{E}$, then it also corrects $\operatorname{span}\mathcal{E}$.
\end{defterm}

For codewords whose basis states are chosen far enough apart (in some notion of distance) so that the off-diagonal conditions are automatically zero, the remaining diagonal conditions correspond to a system of non-linear constraints on the basis-expansion coefficients of the codewords.
In this setting, there exist finite QECCs with $K = \lceil N/D\rceil/(D+1)$ that protect against an error set with $D$ basis elements  ([arXiv:quant-ph/9908066](https://arxiv.org/abs/quant-ph/9908066)), a consequence of the *Tverberg theorem*  ([doi:10.1112/jlms/s1-41.1.123](https://doi.org/10.1112/jlms/s1-41.1.123), [doi:10.1007/978-1-4613-0039-7](https://doi.org/10.1007/978-1-4613-0039-7), [arXiv:1712.06119](https://arxiv.org/abs/1712.06119)). For $K = 2$ this theorem reduces to Radon's theorem  ([doi:10.1007/BF01464231](https://doi.org/10.1007/BF01464231), [doi:10.1007/978-1-4613-0039-7](https://doi.org/10.1007/978-1-4613-0039-7)).

The Knill-Laflamme conditions can alternatively be expressed in terms of the complementary channel, in an entropic information-theoretic way via a data processing inequality  ([arXiv:quant-ph/9604022](https://arxiv.org/abs/quant-ph/9604022), [arXiv:quant-ph/9604034](https://arxiv.org/abs/quant-ph/9604034), [arXiv:quant-ph/9702031](https://arxiv.org/abs/quant-ph/9702031), [arXiv:quant-ph/9707023](https://arxiv.org/abs/quant-ph/9707023), [arXiv:quant-ph/0304007](https://arxiv.org/abs/quant-ph/0304007)), or can be interpreted thermodynamically  ([arXiv:quant-ph/0202054](https://arxiv.org/abs/quant-ph/0202054)).
They motivate higher-rank numerical ranges, which are generalizations of the numerical range of an operator  ([arXiv:quant-ph/0511101](https://arxiv.org/abs/quant-ph/0511101), [arXiv:math/0511278](https://arxiv.org/abs/math/0511278), [arXiv:1407.1350](https://arxiv.org/abs/1407.1350)).
They have been extended to sequences of multiple errors and rounds of correction  ([arXiv:2405.17567](https://arxiv.org/abs/2405.17567)).

\begin{defterm}{Degeneracy}
\label{topic:degeneracy}
A code is degenerate with respect to a noise model if different errors map code states to the same error subspace.
For a linearly independent error set $\cal{E}$, degeneracy is equivalent to $\text{rank}(c_{ij}) < |\cal{E}|$ .
\end{defterm}

\subsection{Correctability of quantum channels}

From now on, we use $\mathcal{E}$ to denote a noise channel constructed out of the set of errors $E$ and let $\mathcal{U}(\cdot)=U(\cdot)U^\dagger$ be the superoperator corresponding to the partial encoding isometry $U$.
A noise channel is correctable if there exists a recovery channel $\mathcal{D}$ such that
\begin{align}
  \mathcal{D}\mathcal{E}\mathcal{U}(\rho)=\rho
\end{align}
for all logical states $\rho$.

The above is equivalent to the fidelity between $\rho$ and $\mathcal{D}\mathcal{E}\mathcal{U}(\rho)$ being one for any notion of distance between quantum states.
In particular, we can consider a scenario where we send only one part of an entangled state through a channel and determine whether the entanglement has been preserved during transmission.
Using the notion of entanglement fidelity, a quantum channel $\mathcal{E}$ is exactly correctable iff there exists a quantum channel $\mathcal{D}$ such that
\begin{align}
  (\mathcal{D}\mathcal{E}\mathcal{U}\otimes\mathrm{id})(\ket{\psi}\bra{\psi})=\ket{\psi}\bra{\psi}
\end{align}
for all states $\rho$ and their corresponding purifications $\ket{\psi}$ (i.e., states $\ket{\psi}$ such that $\text{Tr}_{2}(|\psi\rangle\langle\psi|)=\rho$).

The above entanglement fidelity condition can be alternatively expressed using complementary channels.

\begin{defterm}{Complementary channel}
\label{topic:complementary-channel}
A complementary channel $\mathcal{E}^C$ is obtained from a channel $\mathcal{E}$ that acts on a system by interpreting the channel as coming from a unitary operation acting on a larger system-environment tensor-product space (i.e., performing an isometric extension) with the environment necessarily in a pure state, and then tracing out the system factor (instead of the second environmental factor)  ([doi:10.1017/CBO9781139525343](https://doi.org/10.1017/CBO9781139525343)).
A noise channel ${\cal E}(\cdot)=\sum_{j}E_{j}(\cdot)E_{j}^{\dagger}$ admits a complementary channel of the form
\begin{align}
  {\cal E}^{C}(\cdot)=\sum_{j,k}\text{Tr}\{E_{j}(\cdot)E_{k}^{\dagger}\}|j\rangle\langle k|~.
\end{align}
\end{defterm}

A channel $\mathcal{E}$ is correctable if  $\mathcal{E}^C(\rho)=\rho_0\mathrm{Tr}(\rho)$ for some constant state $\rho_0$, which is equivalent to the \term{Knill-Laflamme conditions}  ([arXiv:0811.1621](https://arxiv.org/abs/0811.1621), [arXiv:0907.5391](https://arxiv.org/abs/0907.5391)).
The logical and physical dimensions are related to the channel rank for non-degenerate codes via the quantum packing bound  ([arXiv:1007.3655](https://arxiv.org/abs/1007.3655)). 

Exact correctability can also be expressed using the coherent information.

\begin{defterm}{Coherent information}
\label{topic:coherent-information}
Given a bipartite state $\rho_{RQ}$, the coherent information in subsystem $Q$ is
\begin{align}
  I_{c}(\rho_{RQ})=S(\rho_{Q})-S(\rho_{RQ})~.
\end{align}
For a channel $\mathcal{E}:L\to Q$ and a pure input state $\rho$ on $R\otimes L$, the coherent information of the channel is
\begin{align}
  I_{c}(\mathcal{E},\rho)=S(\mathcal{E}(\rho_{L}))-S((\mathrm{id}\otimes\mathcal{E})(\rho))~.
\end{align}
Coherent information cannot increase under further processing of the output, a statement known as the *quantum data processing inequality*  ([arXiv:quant-ph/9604022](https://arxiv.org/abs/quant-ph/9604022), [arXiv:quant-ph/9604034](https://arxiv.org/abs/quant-ph/9604034), [arXiv:quant-ph/9702031](https://arxiv.org/abs/quant-ph/9702031), [arXiv:quant-ph/9707023](https://arxiv.org/abs/quant-ph/9707023), [arXiv:quant-ph/0304007](https://arxiv.org/abs/quant-ph/0304007)).
\end{defterm}

Exact correctability is equivalent to preservation of coherent information: a channel $\mathcal{E}$ is exactly correctable on a code iff the coherent information after encoding and noise is the same as that of the logical input for every pure input state, and it is enough to check this on a maximally entangled state between the logical system and a reference  ([arXiv:quant-ph/9604022](https://arxiv.org/abs/quant-ph/9604022), [arXiv:quant-ph/9702031](https://arxiv.org/abs/quant-ph/9702031)).

## Rate

The quantum channel capacity, i.e., the regularized coherent information, is the highest rate of quantum information transmission through a quantum channel with arbitrarily small error rate  ([arXiv:quant-ph/9604015](https://arxiv.org/abs/quant-ph/9604015), [arXiv:quant-ph/0304127](https://arxiv.org/abs/quant-ph/0304127)). 
In other words, the capacity formula implies that one can achieve a transmission rate
$r$ over a quantum channel $\mathcal{E}$ iff, for sufficiently large $n$, $m=\lfloor r n \rfloor$,
and for all $\epsilon>0$,
\begin{align}
  \lVert\mathcal{D}\mathcal{E}\mathcal{U}-I^{\otimes m}\rVert_1\leq \epsilon
\end{align}
for some encoding channel $\mathcal{U}$ and some recovery channel $\mathcal{D}$.
The quantum capacity $Q$ of $\mathcal{E}$ is defined as the supremum over $n$ of achievable transmission rates  ([doi:10.1017/9781316848142](https://doi.org/10.1017/9781316848142)).
See  ([arXiv:1106.1445](https://arxiv.org/abs/1106.1445)) for definitions and a history.     

The fault-tolerant capacity is the capacity for the more general case where the encoding and decoding maps are also assumed to undergo noise  ([arXiv:2009.07161](https://arxiv.org/abs/2009.07161)).

Doeblin coefficients  for quantum channels have been studied  ([arXiv:2309.08475](https://arxiv.org/abs/2309.08475)).

## Decoders

- The operation $\cal{D}$ in the definition of this code is called the decoder. However, the term *decoder* can sometimes be used for the unencoder $\cal{U}$ (i.e., the inverse of the encoder), which does not correct errors.
- There are several recovery maps which work for noise that is not exactly correctable; see AQECC entry.
- QECCs are useful  ([arXiv:1507.07072](https://arxiv.org/abs/1507.07072)) for the mean king's measurement problem  ([doi:10.1103/PhysRevLett.58.1385](https://doi.org/10.1103/PhysRevLett.58.1385)).
- Protection can be implemented via *autonomous QEC* (a.k.a. continuous QEC or continuous-time QEC)  ([doi:10.1098/rspa.1998.0165](https://doi.org/10.1098/rspa.1998.0165), [arXiv:quant-ph/9912104](https://arxiv.org/abs/quant-ph/9912104), [arXiv:quant-ph/0110111](https://arxiv.org/abs/quant-ph/0110111), [arXiv:quant-ph/0501038](https://arxiv.org/abs/quant-ph/0501038), [arXiv:quant-ph/0511221](https://arxiv.org/abs/quant-ph/0511221)) via, e.g., reservoir engineering  ([doi:10.1103/PhysRevLett.77.4728](https://doi.org/10.1103/PhysRevLett.77.4728)); see review  ([arXiv:1311.2485](https://arxiv.org/abs/1311.2485)). There are analogues of the \term{Knill-Laflamme conditions} for autonomous QEC  ([arXiv:1711.02999](https://arxiv.org/abs/1711.02999), [arXiv:2103.05007](https://arxiv.org/abs/2103.05007)), and it has been adapted to non-Markovian noise  ([arXiv:0705.2342](https://arxiv.org/abs/0705.2342)). Information-theoretic bounds have been derived for open-loop control  ([arXiv:quant-ph/0409187](https://arxiv.org/abs/quant-ph/0409187)). Machine learning can be used to optimize autonomous QEC encoding and recovery  ([arXiv:2506.21707](https://arxiv.org/abs/2506.21707)).

## Code capacity threshold

- Coherent information of the state under the action of a noise channel can be used to estimate the optimal threshold  ([arXiv:2312.06664](https://arxiv.org/abs/2312.06664)).

## Relations

- _parent_: [[concepts/qec/qecc]] — Finite-dimensional QECCs are a special case of quantum error-correcting codes, which can also include infinite-dimensional codes such as bosonic codes. The Knill-Laflamme conditions and the notion of correctability can be extended to infinite-dimensional codes.
- _cousin_: [`ecc_finite`](https://errorcorrectionzoo.org/c/ecc_finite) — Finite-dimensional QECCs are quantum analogues of finite-dimensional classical ECCs.
